# System2050 v3.0 — Modele Ondulatoire (Minimal)
This is the minimal, GitHub-ready public bundle to replace the old repository with the official System∩2050 v3.0 ("Model Ondulatoire").

Included files (3):
- README.md (this file)
- examples/calculate_k.py (runnable simulator for phi(t) and k(t) = exp(phi))
- tests/test_formula.py (very small stability test using pytest)

## Core equations (ASCII form)
We integrate:
  phi'' + lambda(phi) * phi' + (omega0)^2 * phi = u(t) + sigma * xi(t)

with:
  k(t) = exp(phi(t))
  lambda = alphaK * K * (1 + alpha_nl * phi^2)
  omega0 = beta / tau

Ignition window (informal):
  0.8 < k < 1.2,  Sigma > 0.65,  K < 0.4,  n*T*tau > K

## Quick run
Requires Python 3.9+ and numpy (matplotlib optional for plot).
```bash
python examples/calculate_k.py --steps 2000 --dt 0.01 --alphaK 0.9 --beta 1.0 --tau 2.0 --K 0.2 --alpha_nl 0.3 --sigma 0.0
```

## Tests
```bash
pytest -q
```

## License
(c) 2025 Patrick Grenier. All rights reserved.

