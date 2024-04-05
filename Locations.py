#import dnd
import Creature
import Monster
import Player
class Area():
    def __init__(self,name,lvl,localMonsters):
        self.name=name
        self.lvl=lvl
        self.localMonsters=localMonsters
    def enter(self,Player1):
        print(f"you came to {self.name}. Here are a lot of lvl {self.lvl} Monsters")
        return self.localMonsters

