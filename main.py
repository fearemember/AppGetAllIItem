from requirements import ensure_package

ensure_package("colorama")

import colorama
from Menu import *


colorama.init()
welcome()
menu()