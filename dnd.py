import random, Creature,Player,Monster,Locations

#creates a new Player Lvl 1
def createPlayer(name,role,lvl=1):
    Player1=Player.Player(name,role,lvl)
    return Player1

#possible Actions for the Player, add more actions later
#implement change Location
def chooseAction(Player1,location):
    print("\n"+"*"*10+"\n")
    action=input(f"What would you like to do?\nyou are currently at the {location.name} Area\nLook(l) for a monster in the current Area, Rest(r), Change(c) Area, or Exit(e) to leave the Game:\n")
    if action=="Look" or action== "l":
        return lookForMonster(Player1,location.localMonsters),False,location
    elif action=="Rest" or action== "r":
        return Player1.heal(),False,location
    
    elif action=="Exit" or action=="e":
        print("See you, I hope you had fun while Playing!")
        return True,True,location
    elif action=="Choose" or action=="c":
        l=int(input("type the Location you want to go: lvl1(1),lvl2(2),lvl3(3),lvl4(4),lvl5(5)\n"))
        try:
            location=Locations.Area(f"lvl{l}",l,monsterBookList[l-1])
            return True,False,location
        except:
            print("This location is not aviable")
            return True,False,location
    else:
        print("wrong Input, choose again!")
        return chooseAction(Player1)

#Sekking a random monster, add different Difficulties later Returns if the Player is alive
def lookForMonster(Player1,monsterBook):
    monster=createMonster(monsterBook)
    return foundMonster(Player1,monster)
    #Display Monster Type only for testing Purpose, remove later.
    print(f"You found a lvl {monster.lvl} {monster.name} with the {monster.element} Type near you.\nIf you want to fight it type Fight or f. If you want to Run type Run or r.")
    action=input()
    if action=="Fight" or action== "f":
        return fight(Player1,monster)
    elif action=="Run" or action== "r":
        return True
    else:
        print("Wrong Input, try again:")
        return lookForMonster(Player1,monsterBook)
    

def foundMonster(Player1,monster):
    print(f"You found a lvl {monster.lvl} {monster.name} with the {monster.element} Type near you.\nIf you want to fight it type Fight or f. If you want to Run type Run or r.")
    action=input()
    if action=="Fight" or action== "f":
        return fight(Player1,monster)
    elif action=="Run" or action== "r":
        return True
    else:
        print("Wrong Input, try again:")
        return foundMonster(Player1,monster)


#fight against a defined monster, add more actions later
def fight(Player1, Monster1):
    #action=input("attak?")
    move=Player1.chooseMove()
    while Player1.hp>0 and Monster1.hp>0:
        dmg=Player1.attackMove(Monster1,move)
        Monster1.hp-=dmg
        if Monster1.hp<=0:
            Player1.fights+=1
            return win(Player1,Monster1), False
        else:
            dmg=Monster1.attackMove(Player1)
            Player1.currentHp-=dmg
            if Player1.currentHp<=0:
                Player1.fights+=1
                print("Combat lost")
                print("Game Over...")
                return False

#Everything that happens after a won Combat
def win(Player1,Monster1):
    print("\n*** Combat won ***\n")
    print(f"You have {Player1.currentHp} hp left")
    Player1.experience+=Monster1.awardetExp
    gold=Monster1.lvl*random.randint(1,6)
    print(f"You got {Monster1.awardetExp} Exp and {gold} Gold")
    Player1.money+=gold
    if not Player1.lvlUp():
        print(f"You have now {Player1.experience} Exp, you need {Player1.lvl*100-Player1.experience} Exp more for Level {Player1.lvl+1}")
        return True

#Monster related Stuff
#make a List or Dictionary with different monsters
monsterBookLvl1={"Zombie":["Zombie",1,0,4],"Squirrel":["Small Animal",1,1,2],"Turtle":["Small Animal",1,2,0],"Bug":["Insect",1,3,2],"Weak Thug":["Human",1,4,3]}
monsterBookLvl2={"Strong Zombie":["Zombie",2,0,4],"Strong Squirrel":["Small Animal",2,1,2],"Strong Turtle":["Small Animal",2,2,0],"Strong Bug":["Insect",2,3,2],"Thug":["Human",2,4,3]}
monsterBookLvl3={"Skeleton":["Zombie",3,0,4],"Hawk":["Bird",3,0,2],"Rockling":["Rock",3,2,2],"Fish":["Fish",3,3,0],"Strong Thug":["Human",3,4,3]}
monsterBookLvl4={"Strong Skeleton":["Zombie",4,0,4],"Strong Hawk":["Bird",4,0,2],"Strong Rockling":["Rock",4,2,2],"Strong Fish":["Fish",4,3,0],"Weak Goblin":["Goblin",4,4,1]}
monsterBookLvl5={"Undead":["Zombie",5,0,4],"Weak Ape":["Animal",5,1,2],"Hedgehog":["Small Animal",5,2,2],"Small Boy":["Human",5,3,4],"Goblin":["Goblin",5,4,1]}
#create new books with other Lvls, and new Monsters



#list of all the Books
monsterBookList=[monsterBookLvl1,monsterBookLvl2,monsterBookLvl3,monsterBookLvl4,monsterBookLvl5]

#here will be a Function to create a random Monster from am Monsterlist/or Dictionary
def createMonster(monsterBook, randomCreature=True):
    if randomCreature:
        keyList=list(monsterBook.keys())
        r=random.randint(0,len(keyList)-1)
        monsterKey=keyList[r]
        monster=Monster.Monster(monsterKey,monsterBook.get(monsterKey)[0],monsterBook.get(monsterKey)[1],monsterBook.get(monsterKey)[2],monsterBook.get(monsterKey)[3])
        return monster
        #create a Monster

#Game related Stuff

#make a function to print a start Screen.
def story(Player1):
    print("\n"+"*"*10+"\n")
    print(f"Welcome {Player1.name} to the Game.\nThe goal of the Game is to reach LvL 6.\n On the way you have to battle against a lot of monsters.\n Have fun on your Journey.")


#runs the Game
def runGame():
    print("\n")
    print("Domis Test Text Game v1.0\n")
    Player1=createPlayer(input("Tell me your name:\n"),"Adventurer")#Sadly no Roles Yet
    #Player1=createPlayer(input("Tell me your name:\n"),input("As what would you like to Play? Pick a role:\n You can be a Wizard(w), a Fighter(f) or a Monk(m)"))
    story(Player1)
    alive=True
    exit=False
    location=Locations.Area("Lvl 1 Area",1,monsterBookList[0])
    while alive and not exit:
        alive,exit,location=chooseAction(Player1,location)

#createMonster(monsterBookWeak, randomCreature=True)
runGame()