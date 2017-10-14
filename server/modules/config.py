import yaml
import os

with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".yaml"), 'r') as ymlfile:
    cfg = yaml.load(ymlfile)


class Config:
    cfg = cfg

    @staticmethod
    def get(section, param):
        return cfg.get(section, {}).get(param, "")
