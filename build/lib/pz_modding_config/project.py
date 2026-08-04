from pathlib import Path

# Get project root from environment variable, or use current working directory
PROJECT_DIR = Path.cwd()
EXTERNAL_DIR = PROJECT_DIR / "external"
EMMYLUA_DIR = PROJECT_DIR / "emmylua"
OUT_DIR = PROJECT_DIR / "out"


if __name__ == "__main__":
    print(EXTERNAL_DIR)