
import subprocess
import sys

def ensure_package(package_name):
    try:
        __import__(package_name)
    except ImportError:
        print(f"{package_name} no está instalado. Instalando...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])