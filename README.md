# PZ Modding Configuration
Provides default configurations for Visual Studio Code and EmmyLua, created by retrieving default settings from different datasets and schema providers to easily get started with modding.

## Usage
To use the distributed configurations, download the latest `configurations.zip` from the [Releases](https://github.com/PZ-Wiki-Modding/pz-modding-config/releases/latest) page and put its content into your project root directory. For example:
```
📁 your-mod-project-root
    📁 Contents
        📁 mods
            ...
    📁 .vscode
        📄 settings.json
    📄 .emmyrc.json
```

## Build
Create a virtual environment and install dependencies:
```
python3 -m venv .venv
source .venv/bin/activate
pip install .
```

## License
See [LICENSE](LICENSE) for license information.