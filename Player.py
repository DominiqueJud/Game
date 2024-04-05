import Creature,random,Moves

elements=["Water","Fire","Nature","Light","Shadow","no Element"]

class Player(Creature.Creature):
    def __init__(self,name,role,lvl,element="Light",type="Human"):
        super().__init__(name,type,lvl)
        self.role=role
        self.hp=lvl*10
        self.currentHp=self.hp
        self.attack=lvl*1
        self.defense=lvl*1
        self.experience=0
        self.element=element
        self.money=0
        self.moves=[Moves.Move("Basic hit"),Moves.Move("Light Bolt")]
        self.movesEmptyMessage=False
        self.fights=0
        self.rests=0
    #add more moves later
    def heal(self):
        self.currentHp=self.hp
        for m in self.moves:
            if m != self.moves[0]:
                m.uses=m.maxUses
        print(f"hp to {self.hp}(Max Hp) restored, all Moves were restored")
        self.rests+=1
        return True

    #function to learn a random new Move
    def learnMove(self):
        l=[]
        for move in self.moves:
            l.append(move.name)
        newMoves=[]
        for key in Moves.moveBook.keys():
            if key not in l:
                newMoves.append(key)
        newMove=newMoves[random.randint(0,len(newMoves)-1)]
        print(f"you have learnt a new Move:\n{newMove}")
        return Moves.Move(newMove)
        
    def wonGame(self):
        print(f"\nCongratulations, you have reached the end Of the Game.\nYou have killed ****{self.fights}**** Monsters\You have done ****{self.rests}****")

    #Function to Level Up the Char.
    def lvlUp(self):
        if self.experience>=self.lvl*100:
            if self.lvl==5:
                self.wonGame()
            self.lvl+=1
            self.hp=self.lvl*10
            self.currentHp=self.hp
            self.attack=self.lvl*1
            self.defense=self.lvl*0.5
            self.experience=0
            for m in self.moves:
                if m != self.moves[0]:
                    m.uses=m.maxUses
            print(f"Congratulations you have archieved lvl {self.lvl}, your Hp were restored to {self.currentHp}")
            self.moves.append(self.learnMove())
            return True
        else:
            return False

    #Special Player attackMove with different Moves
    def attackMove(self,creature,move):
        if move.uses==0:
            if not self.movesEmptyMessage:
                print(f"No Moves of the Type {move.name} left, using {self.moves[0].name} instead. Rest to refill restore all Moves")
                self.movesEmptyMessage=True
            move=self.moves[0]
        e=self.elementEffect(move,creature)
        dmg= self.attack*random.randint(1,3)*move.multiplier*e-creature.defense
        if dmg<=0:
            print(f"{self.name} has missed")
            dmg=0
        else:
            print(f"The {self.name} has dealt {dmg} Damage with a {move.name}")
        move.uses-=1
        return dmg

        #gets one of the moves, if none is specified use Basic Move, if a wrong input comes use the Basic move.
    """def attackMove(self,move=0):
        try:
            print(f"{self.name} is using {self.move[move]}")
            return self.move[move]
        except:
            print(f"No Move with this name, {move[0]} will be performed in the fight")
            return move[0]"""
    def chooseMove(self):
        txt="Choose one of the following Moves:\n"
        count=0
        for m in self.moves:
            txt+=f"{m.name}({count}), "
            count+=1
        print(txt)
        n=int(input())
        if n<len(self.moves):
            print(f"{self.name} is using {self.moves[n].name}")
            return self.moves[n]
        else:
            print(f"No Move with this name, {self.moves[0].name} will be performed in the fight")
            return self.moves[0]
    def elementEffect(self,move,enemy):
        #sehr effektive elementare Aktionen

        if move.element == elements[0] and enemy.element == elements[1]:
            print("Very Effective Move")
            return 2
        elif move.element == elements[1] and enemy.element == elements[2]:
            print("Very Effective Move")
            return 2
        elif move.element == elements[2] and enemy.element == elements[0]:
            print("Very Effective Move")
            return 2
        elif move.element == elements[3] and enemy.element == elements[4]:
            print("Very Effective Move")
            return 2
        elif move.element == elements[4] and enemy.element == elements[3]:
            print("Very Effective Move")
            return 2
        #nicht sehr effektive Elementare Aktionen
        elif move.element == elements[0] and enemy.element == elements[2]:
            print("Move not Effective")
            return 0.5
        elif move.element == elements[1] and enemy.element == elements[0]:
            print("Move not Effective")
            return 0.5
        elif move.element == elements[2] and enemy.element == elements[1]:
            print("Move not Effective")
            return 0.5
        elif move.element==enemy.element:
            print("Move not Effective")
            return 0.5
        #restliche normal Effektive Aktionen
        else:
            return 1