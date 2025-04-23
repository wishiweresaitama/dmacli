from dmacli.constants import ROOT_MODIFICATION_FILE


MOD_CPP_CONTEXT = {
    'name': ROOT_MODIFICATION_FILE,
    'context':
"""\
name = "{{MODIFICATION_NAME_PLACEHOLDER}}";
picture = "";
logo = "";
logoSmall = "";
logoOver = "";
tooltip = "{{MODIFICATION_NAME_PLACEHOLDER}}";
overview = "";
action = "";
author = "";
authorID = "";
version = "";
"""
}