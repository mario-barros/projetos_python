import sqlite3 as sq
import os
import sys
from pathlib import Path

# Adicionar o diretório principal ao sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from func_tabelas import estudantes
from func_tabelas import professor
from func_tabelas import 

estudantes.tabela_estudantes()
