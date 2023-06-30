from .menu import SetupMenu
from .answers import SetupAnswers

def SetupHandlers(dp):
    SetupMenu(dp)
    SetupAnswers(dp)