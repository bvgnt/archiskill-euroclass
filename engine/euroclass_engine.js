/**
 * EUROCLASS engine v0.1 — démonstrateur
 * Flux : entités IFC → classification Euroclass → ventilation par profil national (DPGF / Gewerke)
 * Usage : node euroclass_engine.js [FR|DE]
 * Licence : Unlicense (domaine public)
 */

const fs = require("fs");
const path = require("path");

// ---- Chargement des tables CSV (naïf, sans dépendance) ----
function loadCSV(file) {
  const rows = fs.readFileSync(file, "utf8").trim().split("\n");
  const header = rows[0].split(",");
  return rows.slice(1).map(r => {
    const cells = r.split(",");
    return Object.fromEntries(header.map((h, i) => [h, cells[i]]));
  });
}

const TABLES = {
  "EU-E": loadCSV(path.join(__dirname, "..", "tables", "EU-E_elements.csv")),
  "EU-O": loadCSV(path.join(__dirname, "..", "tables", "EU-O_ouvrages.csv")),
  "EU-W": loadCSV(path.join(__dirname, "..", "tables", "EU-W_immaterial.csv")),
  "EU-L": loadCSV(path.join(__dirname, "..", "tables", "EU-L_lots_pivots.csv")),
};

// ---- Règles de profil (issues de profiles/*.csv) ----
function loadRules(file) {
  return loadCSV(file).map(r => ({
    code: r.euroclass_code,
    condition: r.condition, // "toujours" | "role=porteur" | "technique=ITE" | "selon attribut requester"
    target: r.lot_fr || r.gewerk_de,
  }));
}

// ---- Application des règles conditionnelles ----
function applyProfile(rules, entity) {
  for (const rule of rules) {
    if (rule.code !== entity.euroclass) continue;
    if (rule.condition === "toujours") return rule.target;
    if (rule.condition.startsWith("role=") && entity.attributes?.role === rule.condition.slice(5)) return rule.target;
    if (rule.condition.startsWith("technique=") && entity.attributes?.technique === rule.condition.slice(9)) return rule.target;
    if (rule.condition === "selon attribut requester" && entity.requester) return `${entity.requester} (coût) | hôte ${entity.voidsHost} (contrainte)`;
  }
  return "⚠ NON CLASSÉ — action requise";
}

// ---- Contrôle qualité : cohérence entités ↔ tables ↔ profils ↔ ouvrages ----
function validate(model, rules) {
  const codes = new Set([...TABLES["EU-E"], ...TABLES["EU-W"]].map(e => e.code));
  const ouvrages = new Set(TABLES["EU-O"].map(o => o.eu_e_parent));
  const issues = [];
  for (const e of model) {
    if (!codes.has(e.euroclass)) issues.push(`${e.id}: code ${e.euroclass} absent des tables`);
  }
  for (const rule of rules) {
    if (!codes.has(rule.code)) issues.push(`règle orpheline: ${rule.code}`);
  }
  for (const parent of ouvrages) {
    if (!codes.has(parent)) issues.push(`ouvrage EU-O orphelin: parent ${parent} absent de EU-E`);
  }
  return issues;
}

// ---- Démo ----
function main() {
  const profile = process.argv[2] || "FR";
  const rulesFile = profile === "DE" ? "DE_rules.csv" : "FR_rules.csv";
  const rules = loadRules(path.join(__dirname, "..", "profiles", rulesFile));

  // Maquette de démonstration (en production : lecture IFC via IfcOpenShell)
  const model = [
    { id: "#101", type: "IfcWall", name: "Mur Extérieur Nord", euroclass: "EU-E 21 10 05", attributes: { role: "porteur" }, quantity: 84, unit: "m2", ouvrage: "EU-O 21 05 01" },
    { id: "#103", type: "IfcWall", name: "Mur rideau Hall", euroclass: "EU-E 21 10 15", quantity: 46, unit: "m2" },
    { id: "#104", type: "IfcWall", name: "Cloison bureau", euroclass: "EU-E 21 10 25", quantity: 32, unit: "m2", ouvrage: "EU-O 21 25 01" },
    { id: "#105", type: "IfcSlab", name: "Plancher R+1", euroclass: "EU-E 22 20", quantity: 210, unit: "m2", ouvrage: "EU-O 22 10 01" },
    { id: "#106", type: "IfcCovering", name: "Chape SDB", euroclass: "EU-E 22 40", quantity: 24, unit: "m2", ouvrage: "EU-O 22 40 01" },
    { id: "#108", type: "IfcCovering", name: "Enduit ITE", euroclass: "EU-E 25 40", attributes: { technique: "ITE" }, quantity: 380, unit: "m2", ouvrage: "EU-O 25 40 01" },
    { id: "#109", type: "IfcVirtualElement", name: "Stock terre réutilisable", euroclass: "EU-W 30 10", volumeM3: 320 },
    { id: "#110", type: "IfcOpeningElement", name: "Réservation gaine CVC", euroclass: "EU-W 20", voidsHost: "#101", requester: "Lot 17 CVC" },
    { id: "#111", type: "IfcVirtualElement", name: "Zone base vie", euroclass: "EU-W 40" },
  ];

  const issues = validate(model, rules);
  if (issues.length) {
    console.error("⚠ INCOHÉRENCES DÉTECTÉES:\n" + issues.join("\n"));
    process.exit(1);
  }

  console.log(`\nEUROCLASS engine — profil ${profile}\n=====================================`);
  const ventilation = {};
  for (const e of model) {
    const lot = applyProfile(rules, e);
    (ventilation[lot] ??= []).push(e.quantity ? `${e.id} (${e.quantity} ${e.unit})` : e.id);
  }
  for (const [lot, ids] of Object.entries(ventilation).sort()) {
    console.log(`${lot.padEnd(55)} ${ids.join(" ")}`);
  }
  console.log(`\n${model.length} entités ventilées, ${Object.keys(ventilation).length} lignes — validation OK`);
}

main();
