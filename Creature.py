import random
#Superclass for all creatures
elements=["Water","Fire","Nature","Light","Shadow","no Element"]
class Creature():
    def __init__(self,name,type,lvl):
        self.name=name
        self.type=type
        self.lvl=lvl
    
    def elementEffect(self,enemy):
        #sehr effektive elementare Aktionen
        if self.element == elements[0] and enemy.element == elements[1]:
            print("Very Effective Move")
            return 2
        elif self.element == elements[1] and enemy.element == elements[2]:
            print("Very Effective Move")
            return 2
        elif self.element == elements[2] and enemy.element == elements[0]:
            print("Very Effective Move")
            return 2
        elif self.element == elements[3] and enemy.element == elements[4]:
            print("Very Effective Move")
            return 2
        elif self.element == elements[4] and enemy.element == elements[3]:
            print("Very Effective Move")
            return 2
        #nicht sehr effektive Elementare Aktionen
        elif self.element == elements[0] and enemy.element == elements[2]:
            print("Move not Effective")
            return 0.5
        elif self.element == elements[1] and enemy.element == elements[0]:
            print("Move not Effective")
            return 0.5
        elif self.element == elements[2] and enemy.element == elements[1]:
            print("Move not Effective")
            return 0.5
        elif self.element==enemy.element:
            print("Move not Effective")
            return 0.5
        #restliche normal Effektive Aktionen
        else:
            return 1
    
    def attackMove(self,creature):
        e=self.elementEffect(creature)
        dmg= self.attack*random.randint(1,3)*e-creature.defense
        if dmg<=0:
            print(f"{self.name} has missed")
            dmg=0
        else:
            print(f"The {self.name} has dealt {dmg} Damage")
        return dmg
    