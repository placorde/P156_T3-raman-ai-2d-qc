"""
Explore the curated Materials Cloud 2024.148 sample in data/raw/materials_cloud_2024.148/.

For each material folder: parse POSCAR to count atoms and detect the number of distinct
atomic layers (via z-coordinate clustering), then load raman.dat, drop the near-zero
acoustic modes, and plot the Raman spectrum.

Usage: python src/explore_materials_cloud_sample.py
Outputs: data/processed/materials_cloud_2024.148_summary.csv and one PNG per material in
data/processed/materials_cloud_2024.148_plots/.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data" / "raw" / "materials_cloud_2024.148"
OUT_DIR = ROOT / "data" / "processed"
PLOTS_DIR = OUT_DIR / "materials_cloud_2024.148_plots"

ACOUSTIC_FREQ_CUTOFF = 5.0  # cm^-1, modes below this are acoustic/numerical noise, not real peaks


def parse_poscar(path):
    lines = path.read_text().splitlines()
    formula_comment = lines[0].strip()
    c_axis_length = float(lines[4].split()[2])
    species = lines[5].split()
    counts = [int(x) for x in lines[6].split()]
    n_atoms = sum(counts)
    coord_start = 8
    z_fracs = [float(lines[coord_start + i].split()[2]) for i in range(n_atoms)]

    z_sorted = sorted(z_fracs)
    layers = [z_sorted[0]]
    for z in z_sorted[1:]:
        if z - layers[-1] > 0.03:  # new layer if z-coordinate jumps by more than ~3% of cell
            layers.append(z)
    n_layers = len(layers)

    return {
        "formula_comment": formula_comment,
        "species": "+".join(species),
        "n_atoms": n_atoms,
        "c_axis_angstrom": c_axis_length,
        "n_distinct_z_layers": n_layers,
    }


def load_raman(path):
    data = np.loadtxt(path)
    freq, intensity = data[:, 0], data[:, 1]
    mask = freq > ACOUSTIC_FREQ_CUTOFF
    return freq[mask], intensity[mask]


def main():
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    rows = []

    folders = sorted(p for p in DATA_DIR.iterdir() if p.is_dir())
    for folder in folders:
        info = parse_poscar(folder / "POSCAR")
        info["folder"] = folder.name
        freq, intensity = load_raman(folder / "raman.dat")
        info["n_raman_modes_total"] = len(np.loadtxt(folder / "raman.dat"))
        info["n_raman_modes_optical"] = len(freq)
        info["strongest_peak_cm-1"] = round(float(freq[np.argmax(intensity)]), 1) if len(freq) else None
        rows.append(info)

        fig, ax = plt.subplots(figsize=(5, 3))
        ax.stem(freq, intensity, basefmt=" ")
        ax.set_xlabel("Raman shift (cm$^{-1}$)")
        ax.set_ylabel("Intensity (A$^4$/amu)")
        ax.set_title(f"{folder.name} — {info['n_atoms']} atoms, {info['n_distinct_z_layers']} layer(s)")
        fig.tight_layout()
        fig.savefig(PLOTS_DIR / f"{folder.name}.png", dpi=120)
        plt.close(fig)

    df = pd.DataFrame(rows).sort_values(["species", "n_atoms"])
    df.to_csv(OUT_DIR / "materials_cloud_2024.148_summary.csv", index=False)
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()
