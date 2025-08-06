import subprocess
import sys

def install_libraries():
    required_libraries = [
        "numpy",
        "pandas",
        "matplotlib",
        "seaborn",
        "plotly",
        "scikit-learn"
    ]

    for lib in required_libraries:
        try:
            __import__(lib)
            print(f"'{lib}' is already installed.")
        except ImportError:
            print(f"Installing '{lib}'...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

if __name__ == "__main__":
    install_libraries()
