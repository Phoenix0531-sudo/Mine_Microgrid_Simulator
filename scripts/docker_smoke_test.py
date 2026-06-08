"""Docker build-time smoke test: verify all imports succeed."""
import sys
import importlib

packages = [
    "streamlit",
    "plotly",
    "pandas",
    "numpy",
    "pvlib",
    "windpowerlib",
    "requests",
    "psutil",
]

for pkg in packages:
    try:
        importlib.import_module(pkg)
        print(f"{pkg}: OK")
    except ImportError as e:
        print(f"{pkg}: FAILED ({e})")
        sys.exit(1)

print("All imports OK")
