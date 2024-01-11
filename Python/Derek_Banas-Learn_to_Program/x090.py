#!/usr/bin/python3

'''
Sam attacks Paul and deals 9 damage
Paul is down to 10 health
Paul attacks Sam and deals 7 damage
Sam is down to 7 health
Sam attacks Paul and deals 19 damage
Paul is down to -9 health
Paul has Died and Sam is Victorious
Game Over
'''

import random
import math


# Warrior & Battle Class
class Warrior:
    # Warriors will have names, health, and attack and block maximums
    def __init__(self, name="Warrior", health=0, attMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attMax = attMax
        self.blockMax = blockMax

    # They will have the capabilities to attack and block random amounts
    # Attack random() 0.0 to 1.0 * maxAttack + .5
    # Block random() 0.0 to  1.0 * maxBlock + .5
    def attack(self):
        attAmt = self.attMax * (random.random() + .5)

        return (attAmt)

    def block(self):
        blockAmt = self.blockMax * (random.random() + .5)

        return (blockAmt)


# Battle Class capability of looping until 1 warrior dies
class Battle:
    # Warriors will each get a turn to attack each other
    # Function gets 2 warriors
    # 1 warrior attacks the other
    def startFight(self, warrior1, warrior2):
        while (True):
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break

            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break

    @staticmethod
    def getAttackResult(warriorA, warriorB):
        warriorAAttAmt = warriorA.attack()
        warriorBBlockAmt = warriorB.block()

        damage2WarriorB = math.ceil(warriorAAttAmt - warriorBBlockAmt)
        warriorB.health = warriorB.health - damage2WarriorB

        print("{} attacks {} and deals {} damage".format(warriorA.name,
                                                         warriorB.name,
                                                         damage2WarriorB))
        print("{} is down to {} health".format(warriorB.name,
                                               warriorB.health))

        if (warriorB.health <= 0):
            print("{} has Died and {} is Victorious".format(warriorB.name,
                                                            warriorA.name))
            return ("Game Over")
        else:
            return ("Fight Again")


def main():
    maximus = Warrior("Maximus", 50, 20, 10)
    galaxon = Warrior("Galaxon", 50, 20, 10)

    battle = Battle()

    battle.startFight(maximus, galaxon)


main()
