def create_global_dict():
    global global_dict
    global_dict = {}


def set_value(name, value):
    global_dict[name] = value


def get_value(name, def_value=None):
    try:
        return global_dict[name]
    except:
        return def_value
