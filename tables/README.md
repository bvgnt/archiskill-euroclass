# Tables Euroclass

| Table | Contenu | Règle de codification |
|---|---|---|
| EU-E | Éléments (décomposition fonctionnelle) | Racine de chapitre |
| EU-O | Ouvrages chiffrables (unités + règles de mesure) | Racine = chapitre parent EU-E (sauf 01, 02, 40) |
| EU-C | Composants = produits marchands | `EU-C FF NN`, FF = famille |
| EU-N | Nomenclatures : Quantité composant = Qté ouvrage x coefficient | Paire unique (ouvrage, composant) |
| EU-L | Lots pivots (dévolution) | Racine 90 |
| EU-W | Immatériel | Racine 95 |

## Avant chaque push

```bash
python3 scripts/validate_euroclass.py
```

Le script contrôle la syntaxe CSV, l'unicité des codes, les références
croisées EU-N -> EU-O/EU-C, la cohérence des unités et des coefficients.
**Un push ne doit jamais être effectué si la validation échoue (exit 1).**
Les avertissements (exit 2) sont à vérifier mais non bloquants.

C'est la ceinture de sécurité contre les régressions silencieuses
(lignes écrasées, lectures de cache périmé, unités incohérentes).
