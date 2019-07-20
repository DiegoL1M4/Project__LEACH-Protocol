
import numpy as np

class node:

    packets = []
    slotTDMA = 0

    CH = 0
    cluster = []

    def __init__(self, battery, area):
        self.battery = battery
        self.x = round(np.random.uniform(0, area), 2)
        self.y = round(np.random.uniform(0, area), 2)

    # Battery spending
    def spendTx(self):
        battery -= 0.11

    def spendRx(self):
        battery -= 0.11

    # Packets
    def createPacket(self,pack):
        packets.append(pack)

    def sendPacket(self):
        spendTx()

    def receivePacket(self):
        spendRx()

    # Cluster-Head
    def 
