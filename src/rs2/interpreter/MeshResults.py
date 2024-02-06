class MeshResults:
    results = None

    def __init__(self, results):
        self.results = results

    def getXCoordinate(self, index):
        return self.results[index][0]
    def getYCoordiante(self, index):
        return self.results[index][1]
    def getValue(self, index):
        return self.results[index][2]