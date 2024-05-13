# Complete your game here
# WRITE YOUR SOLUTION HERE:
import pygame
import random

class GameState:
    def __init__(self):
        self.window=pygame.display.set_mode((640,480))
        self.robotImg=pygame.image.load(r"src\robot.png")
        self.coinImg=pygame.image.load(r"src\coin.png")
        self.monsterImg=pygame.image.load(r"src\monster.png")
        self.player=Player(self.robotImg)
        self.monsters=[]
        self.coins=[]
        self.score=0
        self.gameFont=pygame.font.SysFont("Arial",24)
        self.clock=pygame.time.Clock()
        self.importantKeys={
            pygame.K_LEFT:False,
            pygame.K_RIGHT:False}
        


    def moveObjects(self):
    #robot movement
        self.window.fill((128, 229, 255))
        pygame.draw.rect(self.window,(0,255,0),(0,460,680,20))



        self.player.moveByKeys(self.importantKeys,self.window)

        #spawns Coins
        if random.randint(0,60)==0:
            coin=GameObject(self.coinImg)
            self.coins.append(coin)

        #spawns Monster
        if random.randint(0,120)==0:
            monster=GameObject(self.monsterImg, isMonster=True)
            self.monsters.append(monster)
        #moves all Coins, and cheks if they hit the ground or the player
        for index,element in enumerate(self.coins):
            if not element.moveDownwards(self.window):
                self.coins.pop(index)
            if element.contact(self.player):
                self.score+=1
                self.coins.pop(index)
        
        for index, monster in enumerate(self.monsters):
            if not monster.moveDownwards(self.window):
                self.monsters.pop(index)
            if monster.contact(self.player):
                self.score=0
                self.monsters.pop(index)

        #score
        showScore=self.gameFont.render(f"Score: {self.score}",True,(255,0,0))
        self.window.blit(showScore,(550,10))
        
        pygame.display.flip()

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()

            if event.type==pygame.KEYDOWN:
                for key, value in self.importantKeys.items():
                    if event.key==key:
                        self.importantKeys[key]=True

            if event.type==pygame.KEYUP:
                for key, value in self.importantKeys.items():
                    if event.key==key:
                        self.importantKeys[key]=False

    

class GameObject:
    def __init__(self,img:object,isMonster=False):
        self.height=img.get_height()
        self.width=img.get_width()
        self.img=img
        self.coordinates=((random.randint(0,480-self.width),0))
        self.speed=random.randint(2,4)
        self.monster=isMonster

    def showEdges(self,window):
        for edge in self.getHitbox():
            pygame.draw.circle(window,(225,0,0),edge,3)

    def moveDownwards(self, window):
        window.blit(self.img,(self.coordinates))
        self.coordinates=(self.coordinates[0],self.coordinates[1]+self.speed)
        return True if self.coordinates[1]<=480 else False
    
    def getHitbox(self):
        upperLeftEdge=(self.coordinates[0],self.coordinates[1])
        upperRightEdge=(self.coordinates[0]+self.width,self.coordinates[1])
        lowerLeftEdge=(self.coordinates[0],self.coordinates[1]+self.height)
        lowerRightEdge=(self.coordinates[0]+self.width,self.coordinates[1]+self.height)
        edges=[upperLeftEdge,upperRightEdge,lowerLeftEdge,lowerRightEdge]
        return edges
    
    def isMonster(self):
        return self.monster
        

    def contact(self,another: object)->bool:
        upperLeftEdge,upperRightEdge,lowerLeftEdge,lowerRightEdge=another.getHitbox()
        edges=self.getHitbox()
        for edge in edges:
            if edge[0]>upperLeftEdge[0] and edge[0]<upperRightEdge[0]:
                if edge[1]>upperLeftEdge[1] and edge[1]<lowerLeftEdge[1]:
                    return True
        return False
    

class Player(GameObject):
    def __init__(self, img: object):
        super().__init__(img)
        self.coordinates=(320,460-self.height)
        self.speed=2
    def moveByKeys(self,keys,window):
        window.blit(self.img,(self.coordinates))
        if keys[pygame.K_LEFT]:
            self.coordinates=(self.coordinates[0]-self.speed,self.coordinates[1])
        if keys[pygame.K_RIGHT]:
            self.coordinates=(self.coordinates[0]+self.speed,self.coordinates[1])

#actual GameApplication
pygame.init()
game=GameState()

while True:
    game.handleEvents()
    game.moveObjects()
    game.clock.tick(60)

