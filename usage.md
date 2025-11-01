# Exemple d’utilisation du modèle System∩2050

### Calcul du coefficient d’équilibre (k)

```python
E = 0.75  # Énergie
C = 0.80  # Cognition
S = 0.70  # Sens
H = 0.75  # Harmonie

k = (E * C) / (S * H)
print("k =", round(k, 2))
