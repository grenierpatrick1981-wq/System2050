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
