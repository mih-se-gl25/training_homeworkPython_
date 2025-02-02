# Implement script that simulate ships battle. In game there are two teams.
# Each team can has one or more ships. Each ship has a power and armor.
# Power is integer number that indicate maximum hit. Hit is float number that
# can be from 25% to 100% of power. Armour is float number that need to be
# subtracted by hit after ship was hitted. If armour will decreased to 0 ship
# will began drowning. Drowning last 2 step. After drowning ship should be
# removed from team. During drowning ship can shot. Simulation consist of
# iterations, during each iteration each ship shot to random ship from enemy
# team, information about iteration should be printed. Simulation should last
# until one of that team will run out of ships. Number of ships in each team,
# armour and power of each ship should be stored in json file, designing
# format of this json is also a part of homework.

import json
import random

class Ship():
    def __init__(self, power:float, armor:float, shipName:str, inputDamage:float=0, stepToDie:int=0, isKilled:bool=False, isDrowning:bool =False) -> None:
        self.power = power
        self.armor = armor
        self.shipName = shipName
        self.inputDamage =inputDamage
        self.stepToDie = stepToDie
        self.isKilled = isKilled
        self.isDrowning = isDrowning

    def giveHit(self):
        return random.uniform(self.power/4, self.power)
    
    def getHit(self, inputDamage):

        result = self.armor - inputDamage
        if result < 0:
            self.isDrowning = True
            self.armor = 0
        else:
            self.armor = result
        return self.armor
    
    def stepCheckerAndDrowningController(self):
       
        if self.isDrowning == True:
            self.stepToDie += 1
            if self.stepToDie >= 2:
                self.isKilled = True
        else:
            pass
        return self.isKilled

@staticmethod
def import1team():
    with open('t3-1appsettings.json') as f:
        jsonRaw = json.load(f)
        team1 = (jsonRaw["red team"])
    return team1

@staticmethod
def import2team():
    with open('t3-1appsettings.json') as f:
        jsonRaw = json.load(f)
        team2 = (jsonRaw["blue team"])
    return team2
               

class Team:

    def __init__(self,setTeam):
        self.team = setTeam
        self._army= []

    def setShips(self): 
        
        for ship in self.team:
            self._army.append(Ship(shipName=ship["name"], armor=ship["armor"], power=ship["hit"]))
        return self._army
    
    def teamCheckByAliveAndDrowning(self):
        for ship in self._army:
            if ship.isDrowning == True:
                ship.stepToDie += 1
                if ship.stepToDie >= 2:
                    ship.isKilled = True
            if ship.isKilled == True:
                self._army.remove(ship)            
            else:
                pass

    def returnRandomTarget(self) -> object:
        return random.choice(self._army)

class BattleSimulation(Team):
    def __init__(self, oneTeam, twoTeam, moveIterator:int=0):
        self.oneTeam =oneTeam
        self.twoTeam =twoTeam
        self.moveIterator = moveIterator
    
    def checkForVictory(self) -> bool:
        if len(self.oneTeam._army) == 0 or len(self.twoTeam._army) == 0:
            return True,
        else:
            return False

    def returnWinnerTeam(self) -> object:
        if len(self.oneTeam._army) == 0:
            return "2 team is win"
        if len(self.twoTeam._army) ==0:
            return "1 team is win"
        else:
            pass

    def BattleStepBy1Team(self):
        for ship in self.oneTeam._army:
            hit = ship.giveHit()
            target = self.twoTeam.returnRandomTarget()
            target.getHit(hit)

            print(f"{ship.shipName} make {hit} hit for {target.shipName}, his armor set as = {target.armor}")
    
    def BattleStepBy2Team(self):
        for ship in self.twoTeam._army:
            hit = ship.giveHit()
            target = self.oneTeam.returnRandomTarget()
            target.getHit(hit)
   
            print(f"{ship.shipName} make {hit} hit for {target.shipName}, his armor set as = {target.armor}")

    def runSimulations(self):
        while self.checkForVictory() == False:
            self.BattleStepBy1Team()
            self.BattleStepBy2Team()
            self.oneTeam.teamCheckByAliveAndDrowning()
            self.twoTeam.teamCheckByAliveAndDrowning()
            print("-------------------------------------------------")
        print(f"fight is finished, {self.returnWinnerTeam()}")


team_one = Team(setTeam=import1team())
team_one.setShips()
team_two = Team(setTeam=import2team())
team_two.setShips()
o = BattleSimulation(team_one,team_two)
o.runSimulations()

