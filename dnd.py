import random


#Superclass for all creatures
class Creature():
    def __init__(self,name,type,lvl):
        self.name=name
        self.type=type
        self.lvl=lvl
    def attackMove(self,):
        dmg= self.attack*random.randint(1,3)
        print(f"The {self.name} has dealt {dmg} Damage")
        return dmg
    
#Player related Stuff

#Player subclass, add different roles later(perhaps as Subclasses)
#add some roles in the Future
class Player(Creature):
    def __init__(self,name,role,lvl,type="Human"):
        super().__init__(name,type,lvl)
        self.role=role
        self.hp=lvl*10
        self.currentHp=self.hp
        self.attack=lvl*1
        self.defense=lvl*1
        self.experience=0
    #add more moves later
    def heal(self):
        self.currentHp=self.hp
        print(f"hp to {self.hp}(Max Hp) restored")
        return True
    #Function to Level Up the Char.
    def lvlUp(self):
        if self.experience>=self.lvl*100:
            self.lvl+=1
            self.hp=self.lvl*10
            self.currentHp=self.hp
            self.attack=self.lvl*1
            self.defense=self.lvl*1
            self.experience=0
            return True
        else:
            return False

#creates a new Player Lvl 1
def createPlayer(name,role,lvl=1):
    Player1=Player(name,role,lvl)
    return Player1

#possible Actions for the Player, add more actions later
def chooseAction(Player1):
    action=input("What would you like to do?\nType Look/l if you want to look for a monster or Rest/r to heal or Exit/e to leave the Game:\n")
    if action=="Look" or action== "l":
        return lookForMonster(Player1),False
    elif action=="Rest" or action== "r":
        return Player1.heal(),False
    elif action=="Exit" or action=="e":
        print("See you, I hope you had fun while Playing!")
        return True,True
    else:
        print("wrong Input, choose again!")
        return chooseAction(Player1)

#Sekking a random monster, add different Difficulties later Returns if the Player is alive
def lookForMonster(Player1):
    monster=createMonster(monsterBookWeak)
    print(f"You found a lvl {monster.lvl} {monster.name} near you.\nIf you want to fight it type Fight or f. If you want to Run type Run or r.")
    action=input()
    if action=="Fight" or action== "f":
        return fight(Player1,monster)
    elif action=="Run" or action== "r":
        return True
    else:
        print("Wrong Input, try again:")
        return lookForMonster(Player1)
    

#fight against a defined monster, add more actions later
def fight(Player1, Monster1):
    #action=input("attak?")
    while Player1.hp>0 and Monster1.hp>0:
        Monster1.hp-=Player1.attackMove()
        if Monster1.hp<=0:
            print("combat won")
            print(f"You have {Player1.currentHp} hp left")
            Player1.experience+=Monster1.awardetExp
            print(f"You got {Monster1.awardetExp} Exp")
            if Player1.lvlUp():
                print(f"Congratulations you have archieved lvl {Player1.lvl}, your Hp were restored to {Player1.currentHp}")
            else:
                print(f"You have now {Player1.experience}, you need {Player1.lvl*100} Exp for Level {Player1.lvl+1}")
            return True
        Player1.currentHp-=Monster1.attackMove()
        if Player1.currentHp<=0:
            print("Combat lost")
            print("Game Over...")
            return False

#Monster related Stuff


#Monster SuperClass,#later add some subclasses
class Monster(Creature):
    def __init__(self,name,type,lvl,statType):
        super().__init__(name,type,lvl)
        #StatModifier Monster get [0] high HP [1] strong Attack, [2] strong Defence, [3] no strengt, [4] Elite Monster
        #
        statModifier=[[2,1,1],[1,2,1],[1,1,2],[1,1,1],[1.5,1.5,1.5]]
        self.hp=lvl*5*statModifier[statType][0]
        self.attack=lvl*0.5*statModifier[statType][1]
        self.defese=(lvl-1)*1*statModifier[statType][2]
        self.awardetExp=lvl*10+self.hp


#make a List or Dictionary with different monsters
monsterBookWeak={"Skeleton":["Zombie",1,0],"Squirrel":["Small Animal",1,1],"Turtle":["Small Animal",1,2],"Bug":["Insect",1,3],"Weak Thug":["Human",1,4]}


#here will be a Function to create a random Monster from am Monsterlist/or Dictionary
def createMonster(monsterBook, randomCreature=True):
    if randomCreature:
        keyList=list(monsterBook.keys())
        r=random.randint(0,len(keyList)-1)
        monsterKey=keyList[r]
        #print(monsterKey)
        #print(monsterKey,monsterBook.get(monsterKey)[0],monsterBook.get(monsterKey)[1],monsterBook.get(monsterKey)[2])
        monster=Monster(monsterKey,monsterBook.get(monsterKey)[0],monsterBook.get(monsterKey)[1],monsterBook.get(monsterKey)[2])
        return monster
        #create a Monster


#creates a Moster Class named Skeleton lvl 1
def createSkeleton(name="Skeleton",type="undead",lvl=1):
    Skeli=Monster(name,type,lvl)
    print(f"You see a {Skeli.name} lvl: {Skeli.lvl} near you")
    return Skeli     

#Game related Stuff

#make a function to print a start Screen.




#runs the Game
def runGame():
    print("Welcome to Domis DND Test Text Game v1.0\n")
    Player1=createPlayer("Domi","Wizard")#Hardcoded for Testing
    #Player1=createPlayer(input("Chose a name:\n"),input("Chose a role:\n"))
    alive=True
    exit=False
    while alive and not exit:
        alive,exit=chooseAction(Player1)


#createMonster(monsterBookWeak, randomCreature=True)
runGame()