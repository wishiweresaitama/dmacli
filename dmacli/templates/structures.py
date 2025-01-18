from dmacli.templates.context.config_cpp_context import MODULE_CONFIG_CPP_CONTEXT, SUBMODULE_CONFIG_CPP_CONTEXT
from dmacli.templates.context.mod_cpp_context import MOD_CPP_CONTEXT

CONFIGURATION_STRUCTURE = {
    'config.json': {
        'kind': 'file',
        'spec': SUBMODULE_CONFIG_CPP_CONTEXT
    }
}

MODIFICATION_STRUCTURE = {
    'Scripts': {
        'kind': 'folder',
        'spec': {
            '3_Game': {
                'kind': 'folder',
                'spec': {
                    ".gitkeep": {
                        'kind': 'file',
                        'spec': {
                            'name': '.gitkeep',
                            'context': ''
                        }
                    }
                }
            },
            '4_World': {
                'kind': 'folder',
                'spec': {
                    ".gitkeep": {
                        'kind': 'file',
                        'spec': {
                            'name': '.gitkeep',
                            'context': ''
                        }
                    }
                }
            },
            '5_Mission': {
                'kind': 'folder',
                'spec': {
                    ".gitkeep": {
                        'kind': 'file',
                        'spec': {
                            'name': '.gitkeep',
                            'context': ''
                        }
                    }
                }
            },
            'config': {
                'kind': 'file',
                'spec': MODULE_CONFIG_CPP_CONTEXT
            }
        }
    },
    'mod': {
        'kind': 'file',
        'spec': MOD_CPP_CONTEXT
    },
    'prefix': {
        'kind': 'file',
        'spec': {
            'name': '.prefix',
            'context': ''
        }
    }
}