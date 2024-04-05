#Class for the diffferent Attack Moves
elements=["Water","Fire","Nature","Light","Shadow","no Element"]
moveBook={"Basic hit":[elements[5],0.5,-1],"Kick":[elements[5],1,10],"Light Bolt":[elements[3],1,15],"Spikey Thorns":[elements[2],1,15],"Water Ballon":[elements[0],1,15]}

class Move():
    #List for all the Moves, with key=name and list[element, multiplier,uses]
    #ToDo make it a class Object in the future
    elements=["Water","Fire","Nature","Light","Shadow","no Element"]
    moveBook={"Basic hit":[elements[5],0.5,-1],"Kick":[elements[5],1,10],"Light Bolt":[elements[3],1,15],"Spikey Thorns":[elements[2],1,15],"Water Ballon":[elements[0],1,15],"Weak Flames":[elements[1],1,15],"Shadow Fist":[elements[4],1,15],"Magic Bolt":[elements[5],1.25,5]}
    def __init__(self,name):
        self.name=name
        self.element=self.moveBook.get(name)[0]
        self.multiplier=self.moveBook.get(name)[1]
        self.maxUses=self.moveBook.get(name)[2]
        self.uses=self.maxUses
    def describe(self):
        print(self.name,self.element,self.multiplier,self.maxUses)
#ToDo implement Moves and change Player Attack move