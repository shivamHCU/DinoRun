from .model import Model
from pprint import pprint
import random

model = Model()

class Agent:

    def __init__(self, dinoJumpAction = None, restartGameAction = None):
        self.dinoJumpAction = dinoJumpAction
        self.restartGameAction = restartGameAction
        self.counter = 8
        self.data = []
        self.lastAction = 0
        self.lastPerformance = 0

    def updateState(self, cod, coa, speed, isJumping):
        if isJumping :
            return

        self.counter = self.counter - 1
        if self.counter <=0 :
            self.counter = 35 / speed

            # if(self.lastAction == 0) :
            #     self.reward()

            self.lastCod = cod
            self.lastCoa = coa
            self.lastSpeed = speed
            print("cod: ", cod, ", coa: ", coa, ", speed: ", speed)
            action = model.predict(cod, coa, speed)
            self.lastAction = action
            if action == 1 and not self.dinoJumpAction == None :
                self.dinoJumpAction()

    def reward(self):
        try :
            self.data.append({
                'cod': self.lastCod,
                'coa': self.lastCoa,
                'speed': self.lastSpeed,
                'action': self.lastAction
            })
        except:
            print("")

    def died(self, isJumping, isFalling, dino_Performance):
        print(pprint(vars(self)))

        if dino_Performance > self.lastPerformance:
            self.lastPerformance = dino_Performance
            if self.lastAction == 0:
                self.data.append({
                    'cod': self.lastCod,
                    'coa': self.lastCoa,
                    'speed': self.lastSpeed,
                    'action': 1
                })

            elif isJumping and isFalling:
                self.data.append({
                    'cod': self.lastCod,
                    'coa': self.lastCoa,
                    'speed': self.lastSpeed,
                    'action': 0
                })

        # elif isJumping and not isFalling:
        #     self.data.append({
        #         'cod': self.lastCod - self.lastSpeed,
        #         'coa': self.lastCoa,
        #         'speed': self.lastSpeed,
        #         'action': 1
        #     })

        else :
            self.data.append({
                'cod': self.lastCod,
                'coa': self.lastCoa,
                'speed': self.lastSpeed,
                'action': 0
            })



        print("trained on data\n", self.data)
        model.train(self.data)

        self.counter = 8

        if not self.restartGameAction == None:
            self.restartGameAction()
