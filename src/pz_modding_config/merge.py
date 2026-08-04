import json

from pz_modding_config.project import OUT_DIR, EXTERNAL_DIR
from pz_modding_config.utils import merge_settings

# configuration files
CONFIGURATION_FILES = [
    EXTERNAL_DIR / "pz-translation-data" / "out" / "settings.json",
    EXTERNAL_DIR / "pz-xml-data" / "out" / "settings.json",
]
OUT_PATH = OUT_DIR / ".vscode" / "settings.json"

def main():
    out_config = {}

    # merge
    for config_file in CONFIGURATION_FILES:
        assert config_file.exists(), f"Config doesn't exist: {config_file}"
        print(config_file)
        with open(config_file, 'r') as f:
            config = json.load(f)
            out_config = merge_settings(out_config, config)

    # output
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_PATH, 'w') as f:
        json.dump(out_config, f, indent=4)

    print(f"Configuration merged and saved to {OUT_PATH}")

if __name__ == "__main__":
    main()