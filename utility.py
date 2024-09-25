import os

num_classes = 13

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

class_colors = [
    "#c41f3a", # dk
    "#a330c9", # dh
    "#ff7c0a", # dr
    "#33937f", # ev
    "#aad372", # hu
    "#3fc7eb", # ma
    "#00ff98", # mo
    "#f48cba", # pa
    "#ffffff", # pr
    "#fff468", # ro
    "#0070dd", # sh
    "#8788ee", # wl
    "#c69b6d"  # wr
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


def generate_class_titles() -> list:
    """
    Generate list of title case class names.
    """
    class_titles = []
    for i in range(len(class_names)):
        current_name = class_names[i]
        if current_name.count("_") > 0:
            current_name = current_name.replace("_", " ")
        class_titles.append(current_name.title())
    return class_titles