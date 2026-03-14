import sys
from pathlib import Path

# Agrega el directorio raiz al sys.path para importar app durante los tests.
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))
