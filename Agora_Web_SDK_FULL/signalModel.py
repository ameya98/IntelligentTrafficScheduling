import json


class TrafficJunction:
    def __init__(self):
        self.signal = {'1': {"numCars": 0, "signalStatus": "green", "countLastChange": 0},
                    '2': {"numCars": 0, "signalStatus": "red", "countLastChange": 0}}
        self.currGreen = '1'
        self.signalRatio = 0.8

    def updateSignals(self, trafficDict):
        for key in trafficDict:
            self.signal[key]["numCars"] = trafficDict[key]

    def getLightStatus(self, signalName):
        return self.signal[signalName]["signalStatus"]

    def refreshSignals(self):
        bestCandidate = None
        bestNum = 0
        for signal in self.signal:
            if signal != self.currGreen:
                currNum = self.signal[signal]['numCars']
                if currNum > 0.8 * self.signal[self.currGreen]["numCars"]\
                        and currNum > bestNum:
                    bestNum = currNum
                    bestCandidate = signal

        if bestCandidate is not None:
            self.signal[bestCandidate]["signalStatus"] = "green"
            self.signal[self.currGreen]["signalStatus"] = "red"
            self.currGreen = bestCandidate
