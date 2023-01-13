import platform
from pathlib import Path

import discord
from jinja2 import Environment, FileSystemLoader

import alianator

here = Path(__file__).parent

uname = platform.uname()

data = {
    "alianator_version": alianator.__version__,
    "pycord_version": discord.__version__,
    "python_implementation": platform.python_implementation(),
    "python_version": platform.python_version(),
    "system_info": {
        "name": uname.system,
        "version": uname.release,
        "architecture": uname.machine,
    },
}

env = Environment(loader=FileSystemLoader(here / "templates"))

print(env.get_template("diagnostic.yml.jinja").render(data))
