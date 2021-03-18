from enum import Enum

db_file = "database.vdb"
class States(Enum):
    """
    """
    S_START = "0"  # Начало нового диалога
    S_Chose_MODE = "1"
    S_ACT = "2"