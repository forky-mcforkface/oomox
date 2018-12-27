from .config import USER_CONFIG_DIR
from .export_config import OomoxConfig
from .presets_list import PRESET_LIST_MIN_SIZE


class OomoxSettings(OomoxConfig):

    config_keys = []

    def __init__(self, config_name, default_config):
        self.config_keys = default_config.keys()
        super().__init__(
            config_dir=USER_CONFIG_DIR,
            config_name=config_name,
            default_config=default_config
        )

    def __getattr__(self, item):
        if item in self.config_keys:
            return self.config[item]
        return self.__getattribute__(item)

    def __setattr__(self, item, value):
        if item in self.config_keys:
            self.config[item] = value
        elif item not in dir(self):
            raise KeyError(item)
        else:
            super().__setattr__(item, value)


SETTINGS = OomoxSettings(
    config_name='app_config', default_config=dict(
        preset_list_width=PRESET_LIST_MIN_SIZE
    )
)