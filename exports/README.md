# Exports Euroclass — testez dans votre logiciel CAO

Fichiers générés automatiquement depuis les tables CSV de la v0.9
(68 éléments EU-E, 140 ouvrages EU-O, 21 lots pivots EU-L, 7 ouvrages immatériels EU-W).

| Logiciel | Fichier | Comment l'utiliser |
|---|---|---|
| **Revit** | `revit/Euroclass_Keynotes.txt` | Gérer → Paramètres supplémentaires → Nomenclature de clés → charger le .txt. Le code se lit par niveau : 21 = murs, 21 10 = murs ext., 21 10 5 = murs ext. porteurs. |
| **Revit** | `revit/Euroclass_SharedParameters.txt` | Gérer → Paramètres partagés → charger le .txt, puis lier EuroclassCode, EuroclassOuvrage, EuroclassLotFR… aux catégories mur/dalle/porte. |
| **Archicad** | `archicad/Euroclass_EU-E.xml` | Options → Interopérabilité → Classifications → importer le XML (système « EUROCLASS EU-E »), puis affectation via le Gestionnaire de classifications. |
| **Archicad** | `archicad/Euroclass_EU-O.xml` | Idem, comme deuxième système : les ouvrages chiffrables (unité + règle de mesure) deviennent sélectionnables. |
| **Rhino / Bonsaï** | `ifc/Euroclass_demo.ifc` | Ouvrir directement dans Bonsaï. Le mur est classé `EU-E 21 10 05`, la dalle `EU-E 22 10`, avec le jeu de propriétés `Euroclass`. |
| **Rhino / Grasshopper** | `rhino_bonsai/euroclass_map.json` | Lookup table complète (éléments, ouvrages, lots pivots) pour scripts GH / CPython. |
| **Allplan** | `ifc/Euroclass_demo.ifc` + `allplan/Euroclass_attributs.csv` | Importer l'IFC : le classement EUROCLASS remonte dans les attributs BIM. Le CSV (séparateur ;) sert de référence pour les attributs utilisateur code/libellé/unité. |
| **Tout visualiseur IFC** | `ifc/Euroclass_demo.ifc` | Testable aussi dans BIMvision, Solibri Anywhere, usBIM, BIMcollab Zoom — le système « EUROCLASS » apparaît dans les classifications. |

## Convention des clés Revit (keynotes)

Revit n'accepte que des clés numériques (pas de zéro de tête) :

- **EU-E** : clés directes — `EU-E 21 10 05` → clé `21 10 5`.
- **EU-O** : premier composant décalé de **+50** pour éviter les collisions — `EU-O 10 10 01` → clé `60 10 1`. Le vrai code figure en tête de libellé.
- **EU-L** : racine **90** (`EU-L 03` → `90 3`) · **EU-W** : racine **95**.

## Ce que ça teste

1. La hiérarchie des codes est-elle lisible et assignable dans votre outil ?
2. Le couple élément (EU-E) × lot (EU-L) se retrouve-t-il dans les nomenclatures ?
3. L'IFC démo valide le chemin buildingSMART : classification `EUROCLASS` + propriétés — le flux cible « maquette IFC classée EU-E → profil EU-L → DPGF ».
## Convention de codification EU-O (v0.9)

La racine d'un code EU-O reflète le chapitre EU-E de son élément parent (21 = murs, 22 = planchers, 23 = toitures…), sauf pour les travaux sans chapitre EU-E : 01 démolition, 02 terrassement, 40 aménagements extérieurs. Le champ `lot_fr` relève de la dévolution (profil FR) et peut donc différer de la racine (ex. EU-O 32 10 04 chauffe-eau thermodynamique : racine 32 CVC, lot 16 Plomberie).
