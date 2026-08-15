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


def generate_data() -> Any:
    import numpy as np

    gen = np.random.default_rng(42)
    a = gen.normal(75,12,1000)
    b = gen.normal(50,10,1000)
    c = gen.uniform(0,100,1000)
    return np.column_stack((a, b, c))


def analyze_data(data: Any) -> Any:
    import pandas as pd

    df = pd.DataFrame(data, columns=["a", "b", "c"])
    print()
    print("Analyzing Matrix data...")
    print(f"Processing {len(df)} data points...")

    print()
    print("Matrix data statistics:")
    print(df.describe())

    print()
    print(
        f"Average system load: "
        f"{df['a'].mean():.2f}"
    )
    print(
        f"Average threat level: "
        f"{df['b'].mean():.2f}"
    )
    print(
        f"Average anomaly score: "
        f"{df['c'].mean():.2f}"
    )

    high_threat = df[df["b"] > 60]

    print(f"High-threat data points: {len(high_threat)}")

    return df

def visualize_data(df: Any) -> None:
    import matplotlib.pyplot as plt

    print("Generating visualization...")

    plt.figure(figsize=(10, 6))

    # plt.plot(
    #     df.index,
    #     df["a"],
    #     label="System Load",
    # )
    # plt.plot(
    #     df.index,
    #     df["b"],
    #     label="Threat Level",
    # )
    plt.plot(
        df.index,
        df["c"],
        label="Anomaly Score",
    )

    plt.title("Matrix Data Analysis")
    plt.xlabel("Data Point")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("matrix_analysis.png")
    plt.close()


def main():
    print("LOADING STATUS: Loading programs...\n")

    if not check_installation():
        sys.exit(1)
    try:
        matrix_data = generate_data()
        dataframe = analyze_data(matrix_data)
        visualize_data(dataframe)
    except Exception as e:
        print(e)
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")

if __name__ == "__main__":
    main()