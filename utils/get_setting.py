import os
import sys
import yaml

DIR_NAME = os.path.dirname((os.path.dirname(os.path.abspath(__file__))))
sys.path.append(DIR_NAME)


def get_global_setting():
    confpath = os.path.join(DIR_NAME, 'configs/global.yaml')
    with open(confpath, "r", encoding="utf8") as f:
        Iterations = yaml.load(f, Loader=yaml.FullLoader)
    return Iterations
