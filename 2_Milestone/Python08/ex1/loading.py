import importlib


def check_import() -> bool:

    dependencies = {"pandas": "Data manipulation ready",
                    "numpy": "Numerical computation ready",
                    "matplotlib": "Visualization ready"}

    for dep, description in dependencies.items():
        try:
            module = importlib.import_module(dep)
            print(f"[OK] {dep} ({module.__version__}) - {description}")
        except ModuleNotFoundError:
            print(f"""\nMissing {dep}
\npip install -r requirements.txt
python3 loading.py
\npoetry install
poetry run python loading.py""")
            return False
    return True


try:
    import pandas as pd
except ModuleNotFoundError:
    pd = None
try:
    import numpy as np
except ModuleNotFoundError:
    np = None  # type: ignore
try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    plt = None     # type: ignore[assignment]
check_import()
if ((pd is None) or (np is None) or (plt is None)):
    exit(0)


def get_data() -> pd.DataFrame:
    data = np.random.randn(1000)
    df = pd.DataFrame(data)
    print("\nAnalyzing Matrix data...")
    print(f"Processing {len(df)} data points...")
    print("Generating visualization...")
    return df


def gen_visual(df: pd.DataFrame) -> None:
    plt.hist(df, bins=50)
    plt.savefig("matrix_analysis.png")
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")
    if check_import():
        df = get_data()
        gen_visual(df)
