import json, shutil

from pz_modding_config.project import OUT_DIR, EXTERNAL_DIR, EMMYLUA_DIR, PROJECT_DIR
from pz_modding_config.utils import merge_settings

# configuration files
CONFIGURATION_FILES = [
    EXTERNAL_DIR / "pz-translation-data" / "out" / "settings.json",
    EXTERNAL_DIR / "pz-xml-data" / "out" / "settings.json",
    PROJECT_DIR / "log-file-highlighter" / "settings.json",
]
OUT_PATH = OUT_DIR / ".vscode" / "settings.json"

# emmylua stuff
EMMYLUA_IN = EMMYLUA_DIR / ".emmyrc.json"
EMMYLUA_OUT = OUT_DIR / ".emmyrc.json"

def main():
    out_config = {}

    # merge VSCode configuration files from datasets into singular file
    for config_file in CONFIGURATION_FILES:
        assert config_file.exists(), f"Config doesn't exist: {config_file}"
        print(config_file)
        with open(config_file, 'r') as f:
            config = json.load(f)
            out_config = merge_settings(out_config, config)

    # output settings.json
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_PATH, 'w') as f:
        json.dump(out_config, f, indent=4)

    print(f"Configuration merged and saved to {OUT_PATH}")

    # copy emmylua configuration file into out
    EMMYLUA_OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(EMMYLUA_IN, EMMYLUA_OUT)

    print(f"EmmyLua configuration copied to {EMMYLUA_OUT}")

if __name__ == "__main__":
    main()