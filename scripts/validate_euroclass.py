#!/usr/bin/env python3
"""Validation des tables Euroclass — à lancer avant chaque push.

Usage :
    python3 scripts/validate_euroclass.py

Contrôles effectués :
    1. Syntaxe CSV (champs quotés, nombre de colonnes constant par table)
    2. Unicité des codes (EU-E, EU-O, EU-C)
    3. Format des codes (EU-X NN NN [NN])
    4. Référentiel : parents EU-O -> EU-E/EU-L/EU-W existants
    5. Nomenclatures EU-N :
       - ouvrages et composants référencés existent
       - coefficients numériques > 0
       - unicité des paires (ouvrage, composant)
       - unité de la ligne EU-N = unité du composant EU-C
    6. Champs obligatoires non vides (libellés 5 langues, unité, lot_fr)

Exit code 0 = OK, 1 = erreurs (le push doit être refusé), 2 = avertissements seuls.
"""

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TABLES = ROOT / "tables"

CODE_RE = re.compile(r"^EU-(E|O|C|L|W) \d{2}( \d{2})?( \d{2})?$")
UNITS = {"m2", "m3", "ml", "u", "kg", "L", "l"}

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def load(name: str, ncols: int) -> list[dict]:
    path = TABLES / name
    if not path.exists():
        err(f"manquant : {name}")
        return []
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    if not rows:
        err(f"{name} : fichier vide")
        return []
    header = rows[0]
    if len(header) != ncols:
        err(f"{name} : {ncols} colonnes attendues, {len(header)} trouvées")
    out = []
    for i, r in enumerate(rows[1:], start=2):
        if not any(c.strip() for c in r):
            continue
        if len(r) != len(header):
            err(f"{name}:{i} : {len(r)} champs au lieu de {len(header)} -> {r[:2]}")
            continue
        out.append(dict(zip(header, r)))
    return out


def check_codes(table: str, rows: list[dict], key: str = "code") -> None:
    seen: set[str] = set()
    for i, r in enumerate(rows):
        code = r.get(key, "")
        if not CODE_RE.match(code):
            err(f"{table} : code mal formé '{code}'")
        if code in seen:
            err(f"{table} : code dupliqué '{code}'")
        seen.add(code)


def main() -> int:
    # ---- tables
    eu_e = load("EU-E_elements.csv", 12)
    eu_o = load("EU-O_ouvrages.csv", 11)
    eu_c = load("EU-C_composants.csv", 9)
    eu_n = load("EU-N_nomenclatures.csv", 5)

    check_codes("EU-E", eu_e)
    check_codes("EU-O", eu_o)
    check_codes("EU-C", eu_c)

    # ---- parents EU-O
    parents = {r["code"] for r in eu_e}
    for r in eu_o:
        p = r.get("eu_e_parent", "")
        if p and not p.startswith("EU-"):
            err(f"EU-O {r['code']} : parent invalide '{p}'")
        elif p and p not in parents:
            # les racines EU-L/EU-W sont admises pour 01/02/40
            warn(f"EU-O {r['code']} : parent '{p}' absent de EU-E (vérifier EU-L/EU-W)")

    # ---- champs obligatoires EU-O
    for r in eu_o:
        for col in ("fr", "en", "de", "es", "it", "unite", "lot_fr"):
            if not r.get(col, "").strip():
                err(f"EU-O {r['code']} : colonne '{col}' vide")
        if r.get("unite") not in UNITS:
            warn(f"EU-O {r['code']} : unité inhabituelle '{r.get('unite')}'")

    # ---- EU-C
    for r in eu_c:
        for col in ("fr", "en", "de", "es", "it", "unite", "famille"):
            if not r.get(col, "").strip():
                err(f"EU-C {r['code']} : colonne '{col}' vide")

    # ---- EU-N
    codes_o = {r["code"] for r in eu_o}
    by_c = {r["code"]: r for r in eu_c}
    pairs: set[tuple] = set()
    for i, r in enumerate(eu_n, start=2):
        o, c = r.get("ouvrage_code", ""), r.get("composant_code", "")
        if o not in codes_o:
            err(f"EU-N:{i} : ouvrage inconnu '{o}'")
        if c not in by_c:
            err(f"EU-N:{i} : composant inconnu '{c}'")
            continue
        try:
            coef = float(r.get("coefficient", "").replace(",", "."))
            if coef <= 0:
                err(f"EU-N:{i} : coefficient <= 0 ({coef})")
        except ValueError:
            err(f"EU-N:{i} : coefficient non numérique '{r.get('coefficient')}'")
        if (o, c) in pairs:
            err(f"EU-N:{i} : paire dupliquée ({o}, {c})")
        pairs.add((o, c))
        comp = by_c[c]
        if r.get("unite_composant") != comp.get("unite"):
            err(
                f"EU-N:{i} : unité '{r.get('unite_composant')}' != unité composant "
                f"'{comp.get('unite')}' ({c})"
            )

    # ---- rapport
    print(f"EU-E : {len(eu_e)} éléments")
    print(f"EU-O : {len(eu_o)} ouvrages")
    print(f"EU-C : {len(eu_c)} composants")
    print(f"EU-N : {len(eu_n)} lignes, "
          f"{len({r['ouvrage_code'] for r in eu_n})} ouvrages couverts")
    if warnings:
        print(f"\n{len(warnings)} avertissement(s) :")
        for w in warnings:
            print(f"  ! {w}")
    if errors:
        print(f"\n{len(errors)} erreur(s) :")
        for e in errors:
            print(f"  X {e}")
        print("\nVALIDATION ÉCHOUÉE — ne pas pousser.")
        return 1
    if warnings:
        print("\nVALIDATION OK avec avertissements.")
        return 2
    print("\nVALIDATION OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
