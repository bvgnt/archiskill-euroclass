
# EUROCLASS — Spécification technique (v0.7)

> Classification européenne pour le BIM, multilingue natif, conçue pour servir l'allotissement et l'économie de la construction. Document vivant — itération 1.


## 1. Thèse fondatrice

**Euroclass est un pivot sémantique multilingue pour la classification des ouvrages, aligné sur ISO 12006-2, dont le cas d'usage pilote est l'allotissement et le chiffrage (CCTP/DPGF) dans un contexte européen multi-pays.**

Les trois apports distincts vs. existants :

1. **Multilingue natif** — le code est un pivot sémantique ; chaque entrée porte des libellés officiels par langue (FR/EN/DE minimum) et des mappings vers les systèmes nationaux. Uniclass/OmniClass sont anglo-centrés ; les systèmes nationaux (UNTEC/MeTod, CoClass, TALO 2000, GUBIMClass, NL/SfB) sont monolingues.
2. **Cas d'usage allotissement** — première classification pensée pour la dévolution des marchés (lots, CCTP, DPGF, DQE), pas seulement pour la modélisation géométrique. L'UNTEC/MeTod l'a prouvé en France ; aucun équivalent paneuropéen n'existe.
3. **Correspondances comme citoyens de première classe** — chaque code Euroclass embarque ses mappings Uniclass 2015, OmniClass, UniFormat II, et lot UNTEC. La correspondance n'est pas un annexe, c'est le produit.

## 2. Architecture des tables (v0.1)

| Table | Code | Contenu | Priorité |
|---|---|---|---|
| Groupes fonctionnels | **EU-F** | Fonctions majeures du bâtiment (porter, séparer, distribuer…) | P2 |
| Éléments | **EU-E** | Éléments constructifs (murs, dalles, fondations…) | **P1 — pilote** |
| Systèmes | **EU-S** | Systèmes techniques (CVC, élec, plomberie…) | P2 |
| Lots / dévolution | **EU-L** | Lots de marché (allotissement) — mappings nationaux obligatoires | P1 (mapping) |
| Ouvrages immatériels | **EU-W** | Implantation, réservations, stocks/réemploi, zones de chantier (v0.6) | P1 |
| Ouvrages chiffrables | **EU-O** | Ouvrages quantifiables avec unité et mode de mesure — la ligne de DPGF (v0.7) | P1 |
| Espaces | **EU-X** | Espaces et locaux | P3 |
| Produits | **EU-P** | Produits fabricants / objets BIM | P3 |

**Principe clé : EU-E (ce que c'est) × EU-L (qui le pose) = ligne de DPGF.** L'allotissement n'est pas une table figée : c'est une *association* élément → lot, paramétrable par pays/marché, car les lots sont une construction juridico-commerciale locale (lots français ≠ Gewerke allemands ≠ trades UK).

## 3. Schéma de codification (proposition à débattre)

Format : `EU-E nn nn nn` — numérique hiérarchique ISO 12006-2, lisible et triable.

```
EU-E 21       Porteurs verticaux
EU-E 21 10    Murs porteurs
EU-E 21 10 05 Mur porteur béton armé
```

- Règle de l'octet libre : chaque niveau réserve 20 % de codes non assignés pour extension.
- **Identifiant pivot stable, libellés multilingues versionnés** : le code ne change jamais ; les libellés FR/EN/DE évoluent sans casser les projets.
- Chaque entrée : `{code, libellés{}, definition, mappings{}, statut, date}`.

## 4. Table pilote EU-E — structure (extrait v0.1)

### Table EU-E — extrait v0.2, mappings vérifiés (phase 2)

| Code Euroclass | FR | EN | DE | Uniclass 2015 | OmniClass T21 | UniFormat II | Lot UNTEC (indicatif) |
|---|---|---|---|---|---|---|---|
| EU-E 10 | Fondations | Foundations | Fundamente | EF_20_05_30 | 21-01 10 | A10 | 02 Terrassement / GO |
| EU-E 10 10 | Semelles filantes | Strip footings | Streifenfundamente | EF_20_05_30 (Ss_20_05_15) | 21-01 10 10 | A1010 | 02 GO |
| EU-E 10 20 | Pieux | Piles | Pfähle | EF_20_05_30 | 21-01 10 20 | A1020 | 02 GO |
| EU-E 10 30 | Radier général | Raft foundation | Bodenplatte | EF_20_05_30 | 21-01 10 90 | A1010 (cf. A1030 si dallage) | 02 GO |
| EU-E 10 40 | Murs de fondation | Foundation walls | Grundmauern | EF_20_05_30 | 21-01 10 10 10 | A1010 | 02 GO |
| EU-E 21 | Murs et porteurs verticaux | Walls & vertical structure | Wände / Tragwerke | EF_25_10 | 21-02 20 (ext.) | B2010 (ext.) / B1010 (int.) | 03 GO |
| EU-E 21 10 | Murs extérieurs (porteurs ou non) | Exterior walls | Außenwände | EF_25_10_25 | 21-02 20 10 | B2010 | 06 Façade / 03 GO selon cas |
| EU-E 21 20 | Voiles et murs porteurs intérieurs | Interior loadbearing walls | Tragende Innenwände | EF_25_10 | 21-02 10 (frame) / 21-03 | B1010 | 03 GO |
| EU-E 21 30 | Poteaux | Columns | Stützen | EF_20_10_30 | 21-02 10 | B1010 | 03 GO |
| EU-E 22 | Planchers | Floor construction | Decken | EF_30_20 | 21-02 10 10 | B1010 | 03 GO |
| EU-E 22 10 | Dalles pleines | Solid slabs | Massivdecken | EF_30_20 (Ss_30_12) | 21-02 10 10 10 | B1010 | 03 GO |
| EU-E 22 20 | Planchers poutrelles | Beam-and-block floors | Decken mit Balken | EF_30_20 | 21-02 10 10 | B1010 | 03 GO |
| EU-E 23 | Toitures | Roofs | Dächer | EF_30_10 | 21-02 30 | B30 (B1020) | 05 Étanchéité / 04 Couverture |
| EU-E 25 | Enveloppe / façades | Envelope | Fassaden | EF_40 | 21-02 (Shell) | B20 | 06 Façade / menuiseries |

✅ *Mappings vérifiés contre les tables officielles en phase 2 : Uniclass 2015 EF (NBS/Buildig), OmniClass Table 21 (édition May 2012), UniFormat II (ASTM E1557). Voir §4bis pour les constats.*

## 4bis. Constats de la phase 2 — vérification des mappings

Les mappings v0.1 étaient **partiellement faux** ; voici ce que la vérification a révélé, et ce que ça change pour Euroclass :

1. **Uniclass EF est fonctionnel, pas structurel.** Les fondations sont `EF_20_05_30` (Structural elements → Substructure → Foundations) — pas un code dédié par type. Les murs, portes, fenêtres et barrières sont regroupés en `EF_25 Walls` sans distinction porteur/non-porteur. Un classement par *fonction* (mur = séparer), pas par *rôle structurel*.
2. **OmniClass T21 suit UniFormat** : substructure = 21-01, Shell/enveloppe = 21-02, Interiors = 21-03. La structure verticale est noyée dans 21-02 10 (Superstructure framing).
3. **UniFormat II tranche explicitement le cas ambigu** : murs porteurs extérieurs classés sous B2010 Exterior Walls (jugement technique), pas sous Superstructure.
4. **Conséquence pour Euroclass — le vrai choix de conception :** Uniclass (fonctionnel, européen) et UniFormat/OmniClass (UniFormat, structurel) ne découpent pas l'ouvrage aux mêmes endroits. Euroclass doit choisir son axe principal :
   - **Option A — fonctionnel** (alignement Uniclass, cohérent avec la démarche ISO 12006-2 européenne) : le rôle porteur devient un attribut, pas une classe.
   - **Option B — structurel** (alignement UniFormat/OmniClass) : cohérent avec la culture "gros œuvre / second œuvre" des lots français.
   - **Recommandation v0.2 : Option A (fonctionnel) + attribut `rôle structurel`** sur chaque entrée. Raison : c'est l'axe d'Uniclass (le seul grand système européen aligné ISO 12006-2), et l'attribut permet de dériver les vues "structurelles" sans dupliquer la table. MAIS contre-argument fort : le cas d'usage allotissement (DPGF) raisonne en gros œuvre/second œuvre… À trancher par Julien.

## 4ter. Décision d'architecture (Julien, v0.3) — la couche allotissement comme interface métier

**Décision : architecture à deux couches, orientée usage architecte / dévolution.**

1. **EU-E reste l'axe fonctionnel** (aligné Uniclass / ISO 12006-2) + attribut `rôle structurel` par entrée. C'est la colonne vertébrale universelle : mappings inter-systèmes, interopérabilité IFC, et l'axe naturel du dessin (on dessine des murs, pas des « éléments de superstructure »).
2. **EU-L est la couche de dévolution — l'interface de travail de l'architecte.** Les lots ne sont pas une classification de l'ouvrage mais une vue métier paramétrable par profil national :
   - `EU-L profile:FR-v2026` — lots CCTP/DPGF, reprenant la pratique UNTEC (lots ~01→30) pour ne pas réinventer ce que les économistes français utilisent déjà (condition d'adoption locale)
   - `EU-L profile:DE-v2026` — Gewerke (logique VOB/Ausbau)
   - `EU-L profile:UK-v2026` — trades/packages (logique NRM)
3. **Flux de travail cible :** maquette IFC classée EU-E → application d'un profil EU-L → extraction DPGF/CCTP (FR) ou équivalent local, depuis la même maquette, sans re-classification.

**Conséquences :**
- L'association élément → lot est une **règle paramétrique** (`EU-E 21 10` + profil FR → lot 06 Façade ; + profil DE → Gewerk xxx), jamais un mapping figé dans la table.
- Les zones grises (étanchéité, menuiseries, second œuvre) acceptent des **règles conditionnelles** par profil — c'est le mécanisme qui absorbe les différences juridiques nationales sans mentir sur elles.
- L'attribut `rôle structurel` de EU-E alimente les vues GO/SO et les tris de DPGF sans dupliquer la table.



C'est le point le plus sensible du projet :

- En France, l'allotissement est **la règle** en marchés publics (art. L2113-1 et s.), avec un CCTP par lot. ~30 lots types.
- En Allemagne, les **Gewerke** suivent une logique VOB différente ; le "Ausbau" regroupe ce que la France éclate en 10 lots.
- Au Royaume-Uni, on raisonne en **trades/packages** avec des regroupements contractuels différents (SMM/NRM).
- Les mêmes composants changent de lot selon les pratiques locales (l'étanchéité : lot séparé en France, intégrée à la couverture ailleurs).

**Décision d'architecture proposée :** EU-L définit des *lots pivot normalisés* (~20), avec des profils nationaux de regroupement : `EU-L profile:FR-v2026`, `EU-L profile:DE-v2026`… Un même élément EU-E peut être affecté à des lots pivot différents selon le profil. C'est la seule façon de rester honnête avec la réalité juridique de chaque pays.

## 5bis. Phase 3 — Couche EU-L v0.1 : lots pivots + profil FR

### Table EU-L — lots pivots normalisés (pivot = dénominateur sémantique européen)

| Code pivot | Pivot (FR / EN / DE) | Domaine |
|---|---|---|
| EU-L 01 | Démolition / déconstruction · Demolition · Abbruch | Démolition |
| EU-L 02 | Terrassement / VRD · Earthworks & siteworks · Erdarbeiten | Extérieur |
| EU-L 03 | Fondations spéciales · Special foundations · Sondergründungen | Infrastructure |
| EU-L 10 | Structure / gros œuvre · Structure · Rohbau | Structure |
| EU-L 11 | Charpente · Framing/timber structure · Holzbau | Structure |
| EU-L 12 | Couverture · Roofing · Dachdeckung | Clos-couvert |
| EU-L 13 | Étanchéité · Waterproofing · Abdichtung | Clos-couvert |
| EU-L 14 | Façades / bardages · Facades · Fassaden | Clos-couvert |
| EU-L 15 | Menuiseries extérieures · External joinery · Fenster/Aussentüren | Clos-couvert |
| EU-L 20 | Menuiseries intérieures / agencement · Internal joinery · Innenausbau Möbel | Second œuvre |
| EU-L 21 | Plâtrerie / cloisons / doublages · Partitions & linings · Trockenbau | Second œuvre |
| EU-L 22 | Revêtements sols/murs · Floor & wall finishes · Boden-/Wandbeläge | Finition |
| EU-L 23 | Peinture · Painting · Malerarbeiten | Finition |
| EU-L 24 | Serrurerie / métallerie · Metalwork · Metallbau | Second œuvre |
| EU-L 30 | Plomberie / sanitaire · Plumbing · Sanitär | Technique |
| EU-L 31 | CVC / chauffage-ventilation · HVAC · Heizung/Lüftung | Technique |
| EU-L 32 | Électricité CFO/CFA · Electrical · Elektro | Technique |
| EU-L 33 | Ascenseurs / élévateurs · Vertical transport · Aufzüge | Technique |
| EU-L 34 | SSI / sécurité incendie · Fire safety · Brandschutz | Technique |
| EU-L 40 | Aménagements extérieurs / paysage · Landscaping · Aussenanlagen | Extérieur |

*Principe : les pivots sont plus fins que les lots réels de chaque pays. Un lot d'un profil national = un regroupement de pivots (jamais l'inverse). C'est ce qui rend la traduction juridique fidèle : l'allemand "Ausbau" = EU-L 20+21+22+23 ; le français "lot peinture" = EU-L 23 seul.*

### Profil FR v2026 — allotissement type (lecture DPGF/CCTP)

| Lot FR | Contenu (pivots) | Remarque pratique |
|---|---|---|
| 01 Démolition | EU-L 01 | — |
| 02 Terrassement / VRD | EU-L 02 (+03 si géotechnicien séparé) | fondations spéciales souvent lot séparé sur gros projets |
| 03 Gros œuvre | EU-L 03 + 10 (+11 si charpente béton) | le lot GO absorbe l'infrastructure — zone grise documentée |
| 04 Charpente | EU-L 11 | parfois intégré au GO ou à la couverture |
| 05 Couverture – étanchéité | EU-L 12 + 13 | fusion fréquente en France, séparés ailleurs |
| 06 Façades – menuiseries extérieures | EU-L 14 + 15 | ou lots séparés 06/07 selon taille |
| 07–13 Second œuvre | EU-L 20, 21, 24 | menuiseries int., plâtrerie, serrurerie… |
| 14–15 Finitions | EU-L 22 + 23 | revêtements, peinture |
| 16–21 Techniques | EU-L 30–34 | plomberie, CVC, élec CFO/CFA, ascenseurs, SSI |

### Règles d'association élément → lot (extrait EU-E × profil FR)

| Élément EU-E | Condition | Pivot | Lot FR |
|---|---|---|---|
| EU-E 10 Fondations | — | EU-L 03/10 | 02 ou 03 selon type |
| EU-E 10 20 Pieux | toujours | EU-L 03 | 03 GO (ou lot fondations spéciales) |
| EU-E 21 10 Murs extérieurs | rôle structurel = porteur | EU-L 10 | 03 GO |
| EU-E 21 10 Murs extérieurs | rôle structurel = non porteur | EU-L 14 | 06 Façades |
| EU-E 23 Toitures | fonction = couverture | EU-L 12/13 | 05 |
| EU-E 25 Enveloppe | — | EU-L 14/15 | 06 |

**C'est ici que l'attribut `rôle structurel` (§4ter) paie** : le même `EU-E 21 10` bascule entre lot GO et lot Façades selon sa valeur d'attribut — exactement l'arbitrage que UniFormat tranche à la main (mur porteur extérieur → enveloppe) et que les CCTP français négocient au cas par cas. La règle conditionnelle capture la pratique au lieu de la figer.

### Profil DE v2026 — Gewerke (lecture VOB)

Contexte : la VOB/A §3a classe les Gewerke en 6 groupes (Landschaftsbau, Tiefbau, Verkehrswegebau, Ingenieurbau, **Ausbau­gewerke**, **Rohbau**) ; la VOB/C décrit 65 Gewerke avec leurs DIN. Point crucial : la distinction Rohbau/Ausbau détermine les seuils de passation publics (50k€/100k€) mais **n'a pas de définition légale** — c'est une zone grise interprétative, comme GO/SO en France.

| Gewerk DE (VOB/C) | DIN | Pivots EU-L correspondants | Équivalent lot FR | Δ vs FR |
|---|---|---|---|---|
| Erdarbeiten | 18300 | 02 | 02 Terrassement/VRD | = |
| Abbruch-/Rückbauarbeiten | 18459 | 01 | 01 Démolition | = |
| Mauerarbeiten | 18330 | 10 | 03 GO | fusion DE : maçonnerie dans le Rohbau unique |
| Beton-/Stahlbetonarbeiten | 18331 | 10 (+03) | 03 GO | = |
| Zimmer-/Holzbauarbeiten | 18334 | 11 | 04 Charpente | **Δ** : en DE, la charpente bois fait partie du Rohbau (Bauhauptgewerk), pas un lot d'« enveloppe » |
| Dachdeckungsarbeiten | 18338 | 12 | 05 Couverture | **Δ** : DE sépare couverture (Dachdeckung) et zinguerie (Klempnerarbeiten) ; FR fusionne couverture-étanchéité |
| Dachabdichtung / Bauabdichtung | — | 13 | 05 Étanchéité | **Δ** : DE distingue l'étanchéité toiture (souvent avec Dachdecker) et l'étanchéité enterrée (avec Betonarbeiten) ; FR a un lot 05 unique |
| Klempnerarbeiten | 18339 | 13 (+14) | 05 / 06 | zinguerie : partie toiture en DE, partie façade/métallerie en FR |
| Trockenbauarbeiten | 18340 | 21 | 07 Plâtrerie | ≈ |
| Putz-/Stuckarbeiten | 18350 | 21 (+22) | 07 | **Δ** : enduits intérieurs = Ausbau en DE, mais souvent dans le lot GO français (enduits sur maçonnerie) |
| WDVS (isolation extérieure) | 18345 | 14 | 06 Façade / 05 | même zone grise ITE que FR, cadrée par DIN propre |
| VHF (façades ventilées) | 18351 | 14 | 06 | = |
| Fliesen-/Plattenarbeiten | 18352 | 22 | 14 Revêtements | carrelage : Ausbau DE / revêtements FR — ≈ |
| Estricharbeiten | 18353 | 22 | 14 | **Δ** : chapes = Gewerk séparé en DE, quasi jamais lot séparé en FR (dans GO ou revêtements) |
| Tischlerarbeiten | 18355 | 20 (+15) | 06/07 | **Δ** majeur : le menuisier allemand (Tischler) fait fenêtres ET agencement intérieur ; FR coupe en menuiseries ext. (06) / int. (07) |
| Maler-/Lackierarbeiten | 18363 | 23 | 15 Peinture | = |
| Naturwerksteinarbeiten | 18332 | 22/24 | 14 | pierre : à cheval Ausbau/Fassade |
| Gas-/Wasser-/Entwässerungsarb. | 18381 | 30 | 16 Plomberie | = |
| SHK (Sanitär-Heizung-Klima) | — | 30 + 31 | 16 + 17 | **Δ** : DE fusionne sanitaire+chauffage+Clim en un Gewerk SHK ; FR sépare plomberie (16) et CVC (17) |
| Elektroinstallationen | — | 32 | 18 Élec | = |
| Aufzugsarbeiten | — | 33 | Ascenseurs | = |

### Verdict du test de robustesse (analyse v0.3)

**Le modèle pivot tient — 3 cas de figure seulement, tous absorbables :**

1. **Fusions/découpes différentes** (majorité) : SHK = 30+31 ; Tischler = 20+15 ; couverture/étanchéité restructurée. → Mécanisme existant : le profil regroupe des pivots. ✅ Aucune modification du modèle.
2. **Frontières déplacées entre domaines** (minorité) : charpente bois = Rohbau en DE mais « clos-couvert » en FR ; chapes = Gewerk séparé en DE. → Absorbé par les **règles conditionnelles** sur attributs (`matériau structure`, `fonction`), déjà prévues pour les zones grises FR. ✅
3. **Cas limite structurel** : l'**enduit intérieur** (Putzarbeiten) — Ausbau en DE, souvent GO en FR, mais Uniclass le classerait en finition. → Révèle que le pivot 21 (plâtrerie) doit rester **du côté second œuvre** et que l'enduit sur maçonnerie porte un attribut `support` qui conditionne sa bascule GO/lot. ✅ Un attribut de plus, pas une refonte.

**Aucun pivot n'a dû être ajouté ni supprimé pour mapper les Gewerke.** Les 20 pivots couvrent les 65 Gewerke VOB/C — c'est le test de la granularité fine : un Gewerk (comme un lot FR) est toujours une *combinaison* de pivots, jamais un pivot à découvert.

**Fond juridique commun validé** : DE comme FR ont la même structure profonde — un domaine « œuvre principale » (Rohbau / GO) déterminant la responsabilité décennale et des seuils de passation, un domaine secondaire, un domaine technique. Le pivot n'est pas une abstraction artificielle : il capture une taxonomie métier réellement partagée par les deux pays. Le profil UK (trades/NRM) devrait suivre la même logique (dessin de NRM1/NRM2 proche d'UniFormat, vérification à faire).

### Zones grises assumées (mécanisme d'extension)

- Étanchéité : pivot séparé EU-L 13 → fusionné en France (05), séparé en Belgique/DE (Dachabdichtung vs Bauabdichtung)
- Isolation par l'extérieur : bascule FR entre lot façade et étanchéité selon technique → règle conditionnelle sur attribut `technique ITE`
- Fondations spéciales : lot séparé ou intégré GO → règle conditionnelle sur attribut `profondeur/type de fondation`



## 5ter. Confrontation paneuropéenne élargie (ES · IT · AT · PL · Nordiques · UK)

### Synthèse pays par pays

| Pays | Système national | Nature | Lien avec Euroclass |
|---|---|---|---|
| 🇪🇸 ES | **GuBIMClass** (buildingSMART Spain, déployé par l'admin publique espagnole et en Amérique latine hispanophone) ; + SCFClass/RCEclass/AEASBIMclass par domaine | Classification d'éléments BIM « per función » | Très bon alignement : l'axe fonctionnel d'EU-E est la même logique → mapping direct table-à-table. GuBIMClass est le partnat naturel pour le libellé ES |
| 🇮🇹 IT | **UNI 8290** (système technologique : classes d'unités technologiques → fondations directes/indirectes, élévation, …, 3+ niveaux) | Classification élémentaire/fonctionnelle | Confirme l'axe EU-E : les Italiens classifient par unité technologique, structurellement identique à notre couche éléments. L'allotissement italien (capitoli/elenco prezzi) se mappe sur EU-L comme les lots FR |
| 🇦🇹 AT | **ÖNORM B 1801-1 Baugliederung** (0 Grund, 0A Allgemein…) + Gewerke à l'allemande | Double couche : éléments (Baugliederung) + dévolution (Gewerke) | Validation directe de l'architecture à deux couches EU-E/EU-L — l'Autriche fait déjà les deux séparément. Profil AT ≈ profil DE + mapping Baugliederung sur EU-E |
| 🇵🇱 PL | **KNR** (katalogi nakładów rzeczowych) : roboty betonowe, ciesielskie, pokrywcze, **izolacyjne**, tynkarskie, stolarskie, zduńskie, szklarskie, malarskie… + CPV pour la passation | Catalogues de **travaux** (works-based) + nomenclature UE de passation | Les « roboty » sont des works sections (comme Gewerke/trades) → couche EU-L. **Point de friction identifié** : les roboty izolacyjne polonais isolent l'isolation comme domaine de travaux à part entière |
| 🇸🇪🇩🇰🇫🇮🇳🇴 Nordiques | **CoClass** (SE) et **CCS/Cuneco** (DK), tables alignées ISO 12006-2 + principes ISO 81346 ; TALO 2000 (FI), NS 3420 (NO) | Classifications BIM complètes, fonctionnement en facettes | Le plus proche d'Euroclass par la philosophie (pivot + facettes + cycle de vie). Mapping table-à-table aisé, mais l'octet de compétition : ils l'ont déjà fait |
| 🇬🇧 UK | **NRM2** (RICS, a remplacé SMM7 en 2013, work sections élémentaires) + CAWS + CESMM4 (civil) | Mesurement QS + work sections | NRM2 est à la fois élémentaire et par sections de travaux → profile UK = mapping NRM2 sur EU-L + UniFormat-like sur EU-E. CAWS est l'ancêtre direct du concept de work section |

### Les 4 résultats de la confrontation

**1. L'axe fonctionnel EU-E est validé 3 fois de plus.** GuBIMClass (« per función »), UNI 8290 (unités technologiques), ÖNORM Baugliederung : trois traditions indépendantes classifient les éléments par fonction. La confrontation DE/FR avait montré que la *dévolution* diverge ; celle-ci confirme que la *description* converge. La colonne vertébrale EU-E est le bon choix.

**2. L'architecture à deux couches existe déjà en Autriche, implicitement.** ÖNORM B 1801 (Baugliederung = ce que c'est) + Gewerke (qui le pose). Euroclass ne projette pas un modèle français sur l'Europe : elle formalise un pattern déjà présent partout.

**3. Point de friction réel : l'isolation.** La Pologne (roboty izolacyjne) et l'Allemagne (WDVS, DIN 18345) traitent l'isolation comme un domaine de travaux autonome ; en France elle est éclatée (ITE → façade, ITI → plâtrerie, toiture → couverture). **Décision v0.4 : création du pivot EU-L 16 « Isolation »** (Isolierungsarbeiten / insulation works), avec règles de fusion nationales — le profil FR le redistribue sur 05/06/07, le profil PL/DE le garde entier. Premier pivot ajouté suite à confrontation : le mécanisme d'extension fonctionne comme prévu.

**4. Découverte stratégique majeure : CCI existe déjà.** La collaboration **Construction Classification International** relie déjà CoClass, CCS, Uniclass et OmniClass (ateliers internationaux, pilotes dont le tunnel du Fehmarn). **Repositionnement recommandé : Euroclass ne doit pas se construire contre ni à côté de CCI, mais s'y ancrer** — en y apportant les deux choses qui lui manquent : la couche dévolution/allotissement (EU-L, absente des systèmes CCI, orientés description) et le multilingue pivot avec profils nationaux. Le pitch devient : « CCI décrit l'ouvrage, Euroclass le dévolue. »

## 5quater. Les ouvrages immatériels — table EU-W (décision v0.6, demande de Julien)

**Le problème.** Implantation, réservations, stocks de terre pour réemploi : rien de tout ça n'est un « élément ». Uniclass EF et OmniClass T21 classent des objets physiques ; OmniClass T22 (Work Results) capte l'installation de chantier côté américain mais aucune table européenne ne traite le sujet. Or ces ouvrages **chiffrent** : l'implantation est une ligne de DPGF, une réservation mal coordonnée est le litige classique GO/lot technique, un stock de terre réemployable est un actif (matériauthèque) et une économie.

**La solution : une table dédiée EU-W « ouvrages immatériels »** — qui s'appuie nativement sur l'IFC :

| Code | FR | EN | DE | ES | IT | Entité IFC | Mapping |
|---|---|---|---|---|---|---|---|
| EU-W 10 | Implantation et tracing | Setting out | Bauvermessung / Absteckung | Replanteo | Tracciamento | IfcVirtualElement | OmniClass 22-01/31 (site survey) |
| EU-W 20 | Réservations | Reservations / voids | Aussparungen | Resalados | Resine/fori passanti | IfcOpeningElement (+ IfcRelVoidsElement) | lié à l'élément hôte EU-E |
| EU-W 30 | Stocks et dépôts de matériaux | Material stockpiles | Materiallager | Acopios | Depositi materiali | IfcVirtualElement / IfcEarthworksElement (4.3) | OmniClass 22-31 (earthworks) |
| EU-W 30 10 | Stock de terre réemployable | Reusable soil stock | Bodenlager (Wiederverwendung) | Acopio de tierra reutilizable | Deposito terra riutilizzabile | IfcEarthworksElement | — |
| EU-W 40 | Zones de chantier (base vie, grues) | Site zones (welfare, cranes) | Baustelleneinrichtung | Instalaciones de obra | Cantieri/aree di cantiere | IfcVirtualElement / IfcSpace (site) | OmniClass 22-01 |
| EU-W 50 | Élément de démolition/repérage | Demolition markers | Abbruchkennzeichnung | Marcado de demolición | Marcature demolizione | IfcVirtualElement | OmniClass 22-02 |

**Trois décisions de conception importantes :**

1. **EU-W est une table de classification à part entière, pas un hack d'EU-E.** Ces objets ont un cycle de vie différent (provisoires), une matérialité différente (nulle ou négative), et un usage BIM différent (coordination, phasage, réemploi). Les mélanger aux murs casserait la sémantique des deux tables.

2. **La réservation est un objet *relationnel*.** Une réservation appartient à la fois à l'élément hôte (`EU-E 21 10` le mur qui est percé) et au lot demandeur (le lot CVC qui a besoin du passage). C'est précisément le mécanisme de bascule des profils EU-L qui s'applique : **le coût de la réservation est affecté au lot demandeur, la contrainte est portée par l'élément hôte**. Euroclass devient ainsi le premier système à modéliser proprement les *interfaces entre lots* — le nerf de la guerre des CCTP. Mapping IFC direct : IfcOpeningElement → VoidsElement (hôte) → FillsElement (demandeur).

3. **Le réemploi est un citoyen de première classe.** Le stock de terre (EU-W 30 10) n'est pas un déchet de terrassement mais un **produit du bâtiment** : il peut recevoir un code EU-P (produits) à sa réutilisation, avec traçabilité du cycle (extraction → stockage → remise en œuvre). C'est l'alignement direct avec l'agenda européen économie circulaire (Level(s), indicateur 2.3 réutilisation, future réglementation sobriété matière). **Argument de financement UE supplémentaire pour le projet.**

**Validation par confrontation :** l'installation de chantier existe chez OmniClass T22 (MasterFormat Div 01) et chez les Gewerke allemands (Baustelleneinrichtung, DIN 18299 « Allgemeine Regelungen » — travaux généraux) ; la France la noie dans les « généralités » des CCTP. Le pivot EU-W 40 est donc un point de convergence : chaque pays a l'objet, personne ne le classifie. L'Allemagne, avec sa DIN 18299 dédiée aux prestations transversales, est le modèle le plus abouti à mapper.




- **Modèle recommandé** : fondation/asbl à l'européenne, tables publiées sous licence ouverte (CC BY 4.0), processus de contribution type git (pull requests), comité technique par table.
- Point d'ancrage plausible : **CCI (Construction Classification International)** en priorité — collaboration déjà active entre CoClass, CCS, Uniclass, OmniClass (découverte phase 4ter) — avec buildingSMART France-Mediaconstruct, l'UNTEC (couche dévolution FR) et buildingSMART Spain (GuBIMClass, voie hispanophone). Euroclass y apporte la couche dévolution + le multilingue pivot, qui manquent à CCI.
- Versionnement sémantique : Euroclass v1.0 figée 24 mois minimum.

## 7. Feuille de route

1. **Phase 1 — Thèse & cadre** (ce document) ✅ v0.1
2. **Phase 2 — Analyse comparative** ✅ v0.2 — mappings structure vérifiés contre tables officielles (Uniclass EF NBS/Buildig, OmniClass T21, UniFormat II ASTM E1557) ; constat majeur : divergence axe fonctionnel vs structurel (§4bis)
3. **Phase 3 — Table EU-E** ✅ v0.5 — 52 entrées, 5 langues (FR/EN/DE/ES/IT), attribut rôle structurel, mappings Uniclass/OmniClass/UniFormat + lots FR + Gewerke DE — publiée dans la table dédiée « EUROCLASS — Table EU-E ». Prochaine extension : EU-S (systèmes techniques) et passage à ~200 entrées avec relecture des mappings par des contributeurs nationaux
4. **Phase 4 — Profils d'allotissement** ✅ v0.4 — profils FR + DE + confrontation élargie ES/IT/AT/PL/Nordiques/UK (§5ter) : axe fonctionnel validé ×3, pivot EU-L 16 Isolation créé, ancrage stratégique CCI identifié
5. **Phase 5 — Prototype** : export IFC avec codes Euroclass (IfcClassificationReference), test sur un projet réel
6. **Phase 6 — Gouvernance & publication** v1.0

## 8. Questions ouvertes (à trancher par Julien)

- [x] **Axe principal de EU-E : fonctionnel** ✅ décision v0.3 (§4ter) — axe fonctionnel + attribut rôle structurel ; EU-L en couche de dévolution avec profils nationaux
- [ ] Codes numériques (OmniClass-like) vs alphanumériques fonction/produit (ISO 81346-like) ?
- [ ] Combien de langues au lancement ? FR/EN/DE suffisent-ils ou ES/IT/NL dès v1 ?
- [ ] L'allemand "Ausbau" ne se superpose à aucun lot français : accepte-t-on des entrées EU-L sans équivalent dans certains profils ?
- [ ] Statut des mappings : normatif (certifié) ou informatif (indicatif) ?
- [ ] Modèle économique de la maintenance : subvention UE, adhésions, ou open source pur ?