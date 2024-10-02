import os


def generate_class_icon_paths() -> list:
    """
    Generates list of class icon paths.
    """
    class_icon_paths = []
    icons = os.listdir("../icons/")
    for icon in icons:
        class_icon_paths.append("/time-is-money/icons/" + icon)
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

class_icons = generate_class_icon_byteobjs()

class_data = [
    ('wow_death_knight',class_icons[0],'Death Knight','#c41f3a'),
    ('wow_demon_hunter',class_icons[1],'Demon Hunter','#a330c9'),
    ('wow_druid',class_icons[2],'Druid','#ff7c0a'),
    ('wow_evoker',class_icons[3],'Evoker','#33937f'),
    ('wow_hunter',class_icons[4],'Hunter','#aad372'),
    ('wow_mage',class_icons[5],'Mage','#3fc7eb'),
    ('wow_monk',class_icons[6],'Monk','#00ff98'),
    ('wow_paladin',class_icons[7],'Paladin','#f48cba'),
    ('wow_priest',class_icons[8],'Priest','#ffffff'),
    ('wow_rogue',class_icons[9],'Rogue','#fff468'),
    ('wow_shaman',class_icons[10],'Shaman','#0070dd'),
    ('wow_warlock',class_icons[11],'Warlock','#8788ee'),
    ('wow_warrior',class_icons[12],'Warrior','#c69b6d'),
]

num_classes = len(class_data)