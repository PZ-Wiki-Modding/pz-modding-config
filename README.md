# PZ Modding Configuration
Provides default configurations for Visual Studio Code and EmmyLua, created by retrieving default settings from different datasets and schema providers to easily get started with modding.

Currently the configurations are generated from the following sources:
- repository defined EmmyLua configuration file from the suggested default configuration [here](https://pzwiki.net/wiki/Umbrella_(modding)). (stored in the [emmylua](emmylua/) directory)
- [pz-translation-data](https://github.com/PZ-Wiki-Modding/pz-translation-data)
- [pz-xml-data](https://github.com/PZ-Wiki-Modding/pz-xml-data)
- Console files definitions using the Log File Highlighter extension to provide syntax highlighting for console logs. (stored in the [log-file-highlighter](log-file-highlighter/) directory)

## Usage
### Requirements
You need to install the following extensions in Visual Studio Code to get access to the full configurations capabilities:
- [EmmyLua](https://marketplace.visualstudio.com/items?itemName=tangzx.emmylua)
- [XML by RedHat](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-xml)
- [Log File Highlighter](https://marketplace.visualstudio.com/items?itemName=emilast.LogFileHighlighter)

You'll have to setup your system environment variable `$PZ_UMBRELLA` to point to the Umbrella library folder to get full IntelliSense support for the API. See the wiki page about Umbrella's [EmmyLua support](https://pzwiki.net/wiki/Umbrella_(modding)#EmmyLua) for more information.

### Using the configurations
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

Alternatively, you can find these latest files in the `out` directory of this repository. You can also add these configurations to your global Visual Studio Code settings.

## Build
Create a virtual environment and install dependencies:
```
python3 -m venv .venv
source .venv/bin/activate
pip install .
```

## License
See [LICENSE](LICENSE) for license information.