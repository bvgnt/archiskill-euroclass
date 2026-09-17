# Niveau composants EU-C / nomenclatures EU-N

## Principe

Le niveau EU-C décrit des **produits marchands** (jamais de quincaillerie générique non
référencée). La table EU-N fait le lien quantitatif entre un ouvrage chiffrable (EU-O)
et ses composants :

```
Quantité composant = Quantité ouvrage (EU-O) x coefficient (EU-N)
```

Exemple — doublage `EU-O 26 20 02`, 100 m2 de parement :

| Composant | Coefficient | Quantité |
|---|---|---|
| Fourrure F47 (EU-C 01 02) | 2,5 ml/m2 | 250 ml |
| Plaque BA13 (EU-C 03 01) | 1,0 m2/m2 | 100 m2 |
| PSE Th31 100 (EU-C 04 03) | 1,0 m2/m2 | 100 m2 |
| Vis TTPC 25 (EU-C 05 01) | 13 u/m2 | 1 300 u |
| Enduit à joint (EU-C 07 02) | 0,5 kg/m2 | 50 kg |

## Tables

- `EU-C_composants.csv` — code, libellés fr/en/de/es/it, unité, famille, description.
  Codification : `EU-C FF NN` où FF = famille (01 ossature métal, 02 ossature bois,
  03 panneaux, 04 isolants, 05 fixations, 06 membranes, 07 finitions).
- `EU-N_nomenclatures.csv` — ouvrage_code, composant_code, coefficient, unité_composant,
  note. Un ouvrage peut avoir plusieurs nomenclatures (variante ossature bois / métal).

## Règles

1. Les coefficients sont **indicatifs** (DTU 13/21/25.41, fiches fabricants) et doivent
   être ajustés aux pratiques de l'entreprise.
2. Le coefficient s'exprime **par unité d'ouvrage** (l'unité EU-O du même code).
3. Seuls des produits marchands codifiables entrent en EU-C ; les fournitures noyées
   dans un prix global n'ont pas de ligne EU-N.
4. Les nomenclatures sont **optionnelles** : un ouvrage EU-O sans ligne EU-N reste
   parfaitement valide (chiffrage au prix unitaire tout compris).

## Usages visés

- Sous-détail quantitatif d'un devis (évolution DPGF -> avant-métré composants)
- Calculs environnementaux RE2020 / FDES (quantités par produit)
- Réapprovisionnement et remplacement en maintenance
