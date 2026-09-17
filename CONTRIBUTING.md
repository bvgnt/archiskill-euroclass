# Contribuer à Euroclass

## Principe

Les tables sont des CSV simples, un fichier par table. Chaque ligne : un code, ses libellés en 5 langues, ses mappings.

## Types de contributions acceptées

1. **Corrections de mappings** (Uniclass / OmniClass / UniFormat / guBIMClass / UNI 8290) — citer la source officielle dans la description du PR.
2. **Nouvelles entrées** — respecter la règle des 20 % de codes libres par niveau ; jamais de renumérotation d'un code existant.
3. **Nouvelles langues** — ajouter une colonne au CSV (libellés officiels, pas des traductions machine).
4. **Nouveaux profils nationaux** — un fichier `profiles/XX_rules.csv` ; le profil regroupe des pivots existants, il ne crée pas de pivots. Si un pivot manque, le PR doit d'abord le proposer côté `EU-L_lots_pivots.csv`.
5. **Corrections de libellés** — le code ne change jamais, le libellé peut être versionné.
6. **Nouveaux ouvrages EU-O** — chaque ouvrage doit référencer son élément parent (`eu_e_parent`), une unité et un mode de mesure non ambigu.

## Règles d'or

- **Jamais de changement de sens d'un code publié** — créer un nouveau code et déprécier l'ancien.
- **Un mapping douteux vaut mieux qu'un mapping inventé** — marquer `à vérifier` en commentaire si incertain.
- **Les zones grises se règlent par attribut + règle conditionnelle**, pas par duplication d'entrées.
- **Un mode de mesure est contractuel** : préciser les inclusions/exclusions (vides déduits, relevés, etc.) comme le font le CCTP et la VOB/C.

## Format

CSV UTF-8, virgules, pas de guillemets sauf nécessité. Header en anglais court.
