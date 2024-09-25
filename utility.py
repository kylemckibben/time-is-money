import os


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

class_icons = generate_class_icon_byteobjs()

class_data = [
    ('death_knight', 'Death Knight', '#c41f3a', class_icons[0]),
    ('demon_hunter','Demon Hunter','#a330c9', class_icons[1]),
    ('druid','Druid','#ff7c0a', class_icons[2]),
    ('evoker','Evoker','#33937f', class_icons[3]),
    ('hunter','Hunter','#aad372', class_icons[4]),
    ('mage','Mage','#3fc7eb', class_icons[5]),
    ('monk','Monk','#00ff98', class_icons[6]),
    ('paladin','Paladin','#f48cba', class_icons[7]),
    ('priest','Priest','#ffffff', class_icons[8]),
    ('rogue','Rogue','#fff468', class_icons[9]),
    ('shaman','Shaman','#0070dd', class_icons[10]),
    ('warlock','Warlock','#8788ee', class_icons[11]),
    ('warrior','Warrior','#c69b6d', class_icons[12]),
]

num_classes = len(class_data)