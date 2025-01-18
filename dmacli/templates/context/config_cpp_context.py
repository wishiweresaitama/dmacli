CONFIG_PATCHES_CONTEXT = """\
class CfgPatches
{
    class {{MODIFICATION_NAME_PLACEHOLDER}}
    {
        units[] = {};
        weapons[] = {};
        requiredVersion = 0.1;
        requiredAddons[] = {};
    };
};
"""

CONFIG_MODS_CONTEXT = """\
class CfgMods
{
    class {{MODIFICATION_NAME_PLACEHOLDER}}
    {
        name = "{{MODIFICATION_NAME_PLACEHOLDER}}";
        dir = "{{MODIFICATION_NAME_PLACEHOLDER}}";
        credits = "";
        author = "";
        creditsJson = "";
        versionPath = "";
        inputs = "";
        type = "mod";
        dependencies[] = {
            "Game",
            "World",
            "Mission",
        };
        class defs
        {
            class imageSets
            {
                files[] = {};
            };

            class gameScriptModule
            {
                value = "";
                files[] = 
                {
                    "{{MODIFICATION_PREFIX_PLACEHOLDER}}/Scripts/3_Game"
                };
            };

            class worldScriptModule
            {
                value = "";
                files[] = 
                {
                    "{{MODIFICATION_PREFIX_PLACEHOLDER}}/Scripts/4_World"
                };
            };

            class missionScriptModule
            {
                value = "";
                files[] = 
                {
                    "{{MODIFICATION_PREFIX_PLACEHOLDER}}/Scripts/5_Mission"
                };
            };
        };
    };
};
"""

SUBMODULE_CONFIG_CPP_CONTEXT = {
    'name': 'config.cpp',
    'context': CONFIG_PATCHES_CONTEXT,
}

MODULE_CONFIG_CPP_CONTEXT = {
    'name': 'config.cpp',
    'context': CONFIG_PATCHES_CONTEXT + '\n\n' + CONFIG_MODS_CONTEXT,
}