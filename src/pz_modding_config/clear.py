import shutil

from pz_modding_config.project import OUT_DIR

def main():
    # clear recursively output directory
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)

if __name__ == "__main__":
    main()