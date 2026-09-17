# Archiskill / Euroclass

**Une classification européenne du bâti, multilingue native, conçue pour l'allotissement et l'économie de la construction.**

[![Licence: CC0](https://img.shields.io/badge/data-CC0_1.0-brightgreen.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
[![Code: Unlicense](https://img.shields.io/badge/code-Unlicense-blue.svg)](https://unlicense.org)
[![Statut](https://img.shields.io/badge/version-0.7_beta-orange.svg)]()

> *« CCI décrit l'ouvrage, Euroclass le dévolue. »*

Euroclass est une classification BIM à quatre couches, pensée pour la chaîne complète **maquette → CCTP → DPGF** :

| Couche | Question | Contenu |
|---|---|---|
| **EU-E** (éléments) | *Qu'est-ce que c'est ?* | 74 entrées fonctionnelles (mur, dalle, toiture…), alignées ISO 12006-2, avec attribut `rôle structurel` |
| **EU-O** (ouvrages) | *Comment ça se chiffre ?* | Ouvrages quantifiables avec unité et mode de mesure — la ligne de DPGF |
| **EU-L** (dévolution) | *Qui le pose ?* | 21 lots pivots combinables en profils nationaux (FR, DE…) |
| **EU-W** (immatériel) | *Ce qui n'existe pas encore (ou plus)* | Implantation, réservations relationnelles, stocks et **réemploi**, zones de chantier |

Chaque entrée est publiée en **5 langues** (FR / EN / DE / ES / IT) avec mappings vers **Uniclass 2015, OmniClass, UniFormat II, guBIMClass, UNI 8290** et les **Gewerke VOB/C allemands**.

## Le principe en une image

```
            MAQUETTE IFC (classée EU-E + EU-W)
                        │
        ┌───────────────┴───────────────┐
        ▼ profil FR                      ▼ profil DE
  Lot 03 GO                          Mauer-/Betonarbeiten (Rohbau)
  Lot 06 Façades                     Metall-/Glasbau
  Lot 14 Revêtements                 Estricharbeiten (Gewerk séparé)
  Lot 17 CVC                         SHK
        │                               │
        ▼                               ▼
   DPGF française                  Gewerke-Vergabe
   (lignes EU-O, m2/ml/m3/u)       (Leistungsverzeichnis)
```

**Règle d'or :** un lot national est toujours un *regroupement de pivots*, jamais l'inverse. L'« Ausbau » allemand = pivots EU-L 20+21+22+23 ; le « lot peinture » français = le pivot EU-L 23 seul. Le même modèle se ventile en lots français ou en Gewerke allemands **sans re-classification**.

## Structure du dépôt

```
tables/
  EU-E_elements.csv      74 éléments × 5 langues + mappings + rôle structurel
  EU-O_ouvrages.csv      Ouvrages chiffrables : unité + mode de mesure + parent EU-E
  EU-W_immaterial.csv    Ouvrages immatériels (IFC entities, réemploi)
  EU-L_lots_pivots.csv   21 lots pivots + équivalents FR/DE
profiles/
  FR_rules.csv           Règles conditionnelles élément → lot (profil France)
  DE_rules.csv           Règles conditionnelles élément → Gewerk (profil Allemagne)
engine/
  euroclass_engine.js    Moteur : IFC → classification → ventilation par profil
docs/
  SPEC.md                Spécification complète (thèse, architecture, confrontation 8 pays)
```

## Démarrage rapide

```bash
git clone https://github.com/bvgnt/archiskill-euroclass.git
cd archiskill-euroclass
node engine/euroclass_engine.js FR    # ventilation en lots français
node engine/euroclass_engine.js DE    # …en Gewerke allemands, même maquette
```

Les tables sont des **CSV UTF-8** sans dépendance : exploitables directement dans Excel, Revit (Classification Manager), Archicad, ou n'importe quel pipeline IFC via `IfcClassificationReference`.

## Exemple : une ligne de DPGF complète

`EU-O 21 05 01` — **Mur porteur blocs béton 20 (hourdage compris)** / Loadbearing block wall 20 (incl. bond beam) / Tragende Wand Betonblöcke 20 (mit Ringanker) …

- **Unité :** m2 · **Mode de mesure :** surface en élévation hors vides > 0,50 m², armatures horizontales comprises
- **Élément parent :** EU-E 21 10 05 (murs extérieurs porteurs)
- **Profil FR :** Lot 03 Gros œuvre · **Profil DE :** Mauerarbeiten (DIN 18330)
- **Mappings :** Uniclass EF_25_10_25 · OmniClass 21-02 20 10 · UniFormat B2010 · guBIMClass ES.21.10 · UNI 8290 1.2

## Ce qui distingue Euroclass

1. **La dévolution comme citoyen de première classe** — aucune classification existante (Uniclass, OmniClass, CoClass) ne modélise l'allotissement ; c'est pourtant la réalité contractuelle quotidienne (CCTP/DPGF, Gewerke, trades).
2. **Les réservations relationnelles** (EU-W 20) — le coût affecté au lot demandeur, la contrainte portée par l'élément hôte : le nerf des litiges GO/lots techniques, enfin formalisé.
3. **Le réemploi comme actif** (EU-W 30) — un stock de terre réutilisable n'est pas un déchet mais un produit traçable (aligné Level(s), économie circulaire).
4. **Multilingue pivot** — un code, cinq libellés officiels, mappings nationaux : la même maquette parle toutes les langues du chantier européen.

## Confrontation nationale

Le modèle a été testé contre 8 traditions : 🇫🇷 lots UNTEC · 🇩🇪 Gewerke VOB/C (65, DIN 18299–18459) · 🇪🇸 guBIMClass · 🇮🇹 UNI 8290 · 🇦🇹 ÖNORM B 1801 Baugliederung · 🇵🇱 KNR (roboty) · 🇸🇪🇩🇰 CoClass/CCS · 🇬🇧 NRM2/CAWS. Verdict détaillé dans `docs/SPEC.md` §5ter : l'axe fonctionnel converge partout, seule la dévolution diverge — et les profils pivots l'absorbent.

## Feuille de route

- [x] v0.6 — couches EU-E / EU-L / EU-W, profils FR + DE, moteur, spec
- [x] v0.7 — couche EU-O (ouvrages chiffrables avec modes de mesure)
- [ ] Étendre EU-O (≥ 150 ouvrages courants) et EU-E (≥ 200 entrées)
- [ ] Profils UK (NRM2), ES (capítulos), IT (capitoli/elenco prezzi), PL (KNR)
- [ ] Moteur : vraie lecture IFC (IfcOpenShell), export DPGF Excel
- [ ] v1.0 — gel de 24 mois, gouvernance ouverte

## Licence

Tables, profils et documentation : **CC0 1.0** (domaine public — aucune obligation, même pas l'attribution). Code : **Unlicense**. Le combo le plus ouvert possible : n'importe qui, y compris un éditeur propriétaire, peut embarquer Euroclass sans contrainte juridique.

## Contribuer

Voir [CONTRIBUTING.md](CONTRIBUTING.md) — les PR de correction de mappings sont bienvenues (source officielle exigée). Les zones grises se règlent par attribut + règle conditionnelle, jamais par duplication d'entrées.

---

Un projet [Archiskill](https://github.com/bvgnt) — par Julien Bouvagnet, architecte.
