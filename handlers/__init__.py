from .menu import SetupMenu
from .answers import SetupAnswers
from .buy import SetupBuy

def SetupHandlers(dp):
    SetupMenu(dp)
    SetupAnswers(dp)
    SetupBuy(dp)