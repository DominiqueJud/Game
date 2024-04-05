import Creature

class Monster(Creature.Creature):
    def __init__(self,name,type,lvl,statType,elementType):
        super().__init__(name,type,lvl)
       
        #Different possible Elements: 2x DMG Effectiveness Water->Fire->Nature->Water, Shadow-> Light -> Shadow
        #Less effective 0.5 DMG Water->Nature->Fire->Water
        #ToDo add Element Damages to the Game
        #ToDo add more interactions and more elements in the future
        elements=["Water","Fire","Nature","Light","Shadow","no Element"]


         #StatModifier Monster get [0] high HP [1] strong Attack, [2] strong Defence, [3] no strengt, [4] Elite Monster
        statModifier=[[2,1,1],[1,2,1],[1,1,2],[1,1,1],[1.5,1.5,1.5]]
        self.hp=lvl*5*statModifier[statType][0]
        self.attack=lvl*0.75*statModifier[statType][1]
        self.defense=(lvl-1)*0.5*statModifier[statType][2]
        self.awardetExp=lvl*10+self.hp
        self.element=elements[elementType]