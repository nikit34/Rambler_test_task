# На проекте я бы использовал environment,
# но на задание в один вечер (ьчон) - локальные файлы json

# import os
# import .settings.PATH_APP
# os.environ.setdefault('path_app', 'settings.')

######################
import json

from .settings import CONFIG_FILE, PATH_APP


context = {}


def setup_context():
    global context

    try:
        with open(CONFIG_FILE, 'r') as f:
            env_variables = json.load(f)

            # Можем добавлять префиксы-суффиксы для ключей
            # - поддержка различных конфигураций
            context.update({PATH_APP: env_variables[PATH_APP]})

    except EnvironmentError as e:
        print("[ERROR]\tINCORRECT FILE PATH ENVIRONMENT:\t", e)


if __name__ == "__main__":
    setup_context()