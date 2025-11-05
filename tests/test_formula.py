# Minimal test: without forcing and with moderate friction, k(t) should hover near ~1 on average.
import numpy as np
import importlib.util, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
calc_path = ROOT / "examples" / "calculate_k.py"
spec = importlib.util.spec_from_file_location("calculate_k", str(calc_path))
mod = importlib.util.module_from_spec(spec)
sys.modules["calculate_k"] = mod
spec.loader.exec_module(mod)  # type: ignore

def test_stability_near_one():
    ks, phis = mod.simulate(steps=5000, dt=0.005, alphaK=0.9, beta=1.0, tau=2.0, K=0.25, alpha_nl=0.3, sigma=0.0, seed=42)
    k_mean = float(np.mean(ks[-2000:]))
    assert 0.9 < k_mean < 1.1, f"k_mean out of range: {k_mean}"
