import os

class_names = [
    'death_knight', 
    'demon_hunter', 
    'druid', 
    'evoker', 
    'hunter', 
    'mage', 
    'monk', 
    'paladin', 
    'priest', 
    'rogue', 
    'shaman', 
    'warlock', 
    'warrior'
]

def generate_class_icon_paths() -> list:
    """
    Generates list of class icon paths.
    """
    class_icon_paths = []
    icons = os.listdir("icons/")
    for icon in icons:
        class_icon_paths.append("/wow-guild-bot/icons/" + icon)
    return class_icon_paths

def generate_class_icon_byteobjs() -> list:
    """
    Generate byte objects of class icons.
    """
    class_icon_byteobjs = []
    class_icon_paths = generate_class_icon_paths()
    root_path = os.path.abspath(os.path.dirname(__file__))
    for icon_path in class_icon_paths:
        path = os.path.join(root_path, icon_path)
        with open(path, "rb") as img:
            icon = img.read()
            class_icon_byteobjs.append(icon)
    return class_icon_byteobjs