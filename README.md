# DMACLI

DMACLI is a command-line interface tool for managing DayZ mod projects. It provides easy commands to set up configurations, build modules, create resources, debug, and run servers/clients.

## Installation

1. Place the `dmacli` folder in your Python environment or install as a standalone executable.  
2. Configure your environment variables as needed.

## Usage

```bash
dmacli.exe [COMMAND] [OPTIONS]
```

For detailed help on any command, run:
```bash
dmacli.exe [COMMAND] --help
```

## Commands

- **apply**  
  - `dmacli.exe apply config -f <path>`  
    Applies a JSON configuration file to the local environment.
- **describe**  
  - `dmacli.exe describe config`  
    Prints the currently applied JSON configuration.
- **create**  
  - `dmacli.exe create module <path> -n <name>`  
    Creates a new module directory structure at the specified path.  
  - `dmacli.exe create submodule <path> -n <name>`  
    Creates a submodule directory structure.  
  - `dmacli.exe create resource <path> -n <name>`  
    Creates a data resource structure.
- **build**  
  - `dmacli.exe build -s <source> -d <destination>`  
    Builds the module in the specified `<source>` directory and places results in `<destination>`.
- **debug**  
  - `dmacli.exe debug -m <modFolder> -m <anotherModFolder> ...`  
    Launches the Workbench for debugging specified modifications.
- **run**  
  - `dmacli.exe run`  
    Validates build checksums and runs the DayZ server/client.

## Examples

1. Apply a configuration:

   ```bash
   dmacli.exe apply config -f D:\Configs\myConfig.json
   ```
2. Create a module:

   ```bash
   dmacli.exe create module D:\Mods -n MyNewMod
   ```
3. Build a mod:

   ```bash
   dmacli.exe build -s D:\Mods\MyNewMod -d D:\Mods\MyNewMod_build
   ```

## Important Details

- Ensure you have a valid `config.json` in your home directory (`~\.dmacli\config.json`) before running build or run commands.
- Modify the config file to point to correct tool paths (e.g., `AddonBuilder.exe` and `workbenchApp.exe`).
- Use the `debug` command with one or more mod paths for quick testing inside the DayZ Workbench.

For more help, run:
```bash
dmacli.exe --help
```
