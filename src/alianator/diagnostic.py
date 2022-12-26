import platform
from pathlib import Path

import chevron
import discord

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
    }
}

print(chevron.render((here / "templates" / "diagnostic.mustache").open(), data))
