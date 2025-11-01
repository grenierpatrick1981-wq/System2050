# 🧠 System∩2050 — Cadre pour l’Ignition Cognitive

Cadre conceptuel et mathématique pour analyser les transitions civilisationnelles via l’équilibre **Énergie (E)**, **Cognition (C)**, **Sens/Structure sociale (S)** et **Harmonie (H)** avec une friction **K**.

> **Formule centrale** : `k = (E × C) / (S × H)`

## 🎯 Objectif
Fournir une boussole quantitative et falsifiable pour :
- détecter les **convergences** (k → 1),
- distinguer **ignition harmonique** vs **déséquilibre**,
- guider des politiques qui **réduisent K** (friction) et maintiennent l’équilibre.

## 🔥 Triple condition d’ignition (v2.0)
1. **Équilibre dynamique** : `0.8 < k < 1.2`  
2. **Seuil de maturité** : `Σ = (E+C+S+H)/4 > 0.65`  
3. **Friction maîtrisée** : `K < 0.4`  
*(Condition dynamique complémentaire : `n·T·τ > K`)*

## 📁 Fichiers du dépôt
- [`system2050.json`](./system2050.json) – Schéma / format d’échange des variables  
- [`usage.md`](./usage.md) – Guide d’utilisation rapide (exemples)  
- [`wiki.md`](./wiki.md) – Notes, définitions et FAQ  
- `README.md` – Ce document

## ⚙️ Exemple d’usage (pseudo-JSON)
```json
{
  "E": 0.82,
  "C": 0.84,
  "S": 0.78,
  "H": 0.80,
  "K": 0.28,
  "k": "(E*C)/(S*H)",
  "sigma": "(E+C+S+H)/4",
  "thresholds": { "k_min": 0.8, "k_max": 1.2, "sigma_min": 0.65, "K_max": 0.4 }
}
📊 Validation historique (extraits 1000–2025)

Période	k	Σ	K	Lecture

1945–1970	1.07	0.74	0.25	✅ Ignition harmonique
1990–2000	0.99	0.82	0.20	✅ Ignition harmonique
2007–2015	1.64	0.77	0.35	⚠️ Surinvestissement
2020–2025	2.42	0.74	0.55	❌ Déséquilibre critique


📚 Référence (DOI)

Zenodo : 10.5281/zenodo.17501970
“System∩2050 v2.0 — Cadre pour l’Ignition Cognitive” (CC BY-SA 4.0).

🏷️ Mots-clés

system2050 · cognitive-ignition · complex-systems · civilizational-dynamics · risk-assessment

📜 Licence

Creative Commons BY-SA 4.0 – partage et adaptation avec attribution et partage à l’identique.
