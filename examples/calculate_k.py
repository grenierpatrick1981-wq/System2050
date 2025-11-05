#!/usr/bin/env python3
# System2050 v3.0 — minimal simulator for phi(t) and k(t)=exp(phi)

import argparse, math, sys
import numpy as np

try:
    import matplotlib.pyplot as plt
    HAS_PLOT = True
except Exception:
    HAS_PLOT = False

def simulate(steps=3000, dt=0.01, alphaK=0.9, beta=1.0, tau=2.0, K=0.2, alpha_nl=0.3, sigma=0.0, seed=123):
    """
    Integrate:
      phi'' + lambda(phi)*phi' + (omega0)^2*phi = u(t) + sigma*xi(t)
    with:
      lambda = alphaK * K * (1 + alpha_nl * phi^2)
      omega0 = beta / tau
      k(t) = exp(phi)
    Returns (ks, phis).
    """
    rng = np.random.default_rng(seed)
    phi = 0.0     # phi
    phid = 0.0    # phi'
    omega0 = beta / max(tau, 1e-12)

    ks = np.empty(steps, dtype=float)
    phis = np.empty(steps, dtype=float)

    for i in range(steps):
        lam = alphaK * K * (1.0 + alpha_nl * (phi ** 2))
        noise = sigma * rng.normal(0.0, 1.0) / math.sqrt(dt) if sigma > 0 else 0.0
        # phi'' = u - lambda*phi' - omega0^2 * phi + noise; here u(t)=0 for the minimal demo
        phidd = 0.0 - lam * phid - (omega0 ** 2) * phi + noise
        # explicit integration
        phid = phid + dt * phidd
        phi = phi + dt * phid

        phis[i] = phi
        ks[i] = math.exp(phi)

    return ks, phis

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--steps", type=int, default=3000)
    p.add_argument("--dt", type=float, default=0.01)
    p.add_argument("--alphaK", type=float, default=0.9)
    p.add_argument("--beta", type=float, default=1.0)
    p.add_argument("--tau", type=float, default=2.0)
    p.add_argument("--K", type=float, default=0.2)
    p.add_argument("--alpha_nl", type=float, default=0.3)
    p.add_argument("--sigma", type=float, default=0.0)
    p.add_argument("--seed", type=int, default=123)
    p.add_argument("--no-plot", action="st_
