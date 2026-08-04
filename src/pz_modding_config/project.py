from pathlib import Path

PROJECT_DIR = Path(__file__).parent.parent.parent
EXTERNAL_DIR = PROJECT_DIR / "external"
OUT_DIR = PROJECT_DIR / "out"


if __name__ == "__main__":
    print(EXTERNAL_DIR)