import importlib, sys
from typing import Any


PACKAGES = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready",
}


def check_installation() -> bool:
    missing = []
    print("Checking dependencies:")
    for pack, msg in PACKAGES.items():
        try:
            module = importlib.import_module(pack)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {pack} ({version}) - {msg}")
        except ModuleNotFoundError:
            print(f"[ERROR] {pack} is not installed")
            missing.append(pack)
    if missing:
        print("\nInstall with pip:")
        print("pip install -r requirements.txt\n")
        print("Or install with Poetry:")
        print("poetry install")
        return False
    return True



def analyze_data(points: int = 1000) -> Any:
    import numpy as np
    import pandas as pd

    print()
    print("Analyzing Matrix data...")
    gen = np.random.default_rng(42)
    a = gen.normal(75, 12, points)
    df = pd.DataFrame({"a": a})
    print(f"Processing {len(df)} data points...")
    return df
 
 
def visualize_data(df: Any) -> None:
    import numpy as np
    import matplotlib.pyplot as plt

    print("Generating visualization...")
    data = df["a"]
 
    plt.figure(figsize=(8, 5))
    plt.hist(data, bins=30, color="green", edgecolor="black", alpha=0.7, density=True)
    mean = data.mean()
    std = data.std()
    x = np.linspace(data.min(), data.max(), 200)
    trend = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std) ** 2)
    plt.plot(x, trend, color="red", linewidth=2, label="Trend")
 
    plt.title("Data Distribution")
    plt.xlabel("Value")
    plt.ylabel("Density")
    plt.grid(True, alpha=0.3)
    plt.legend()
 
    plt.savefig("matrix_analysis.png")
    plt.close()


def main():
    print("LOADING STATUS: Loading programs...\n")

    if not check_installation():
        sys.exit(1)
    try: 
        dataframe = analyze_data()
        visualize_data(dataframe)
    except Exception as e:
        print(e)
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")

if __name__ == "__main__":
    main()