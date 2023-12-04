from main_func import *
import SA_Simoes_FirstTry

#? CONFIGURATIONS
#? - Array Configuration
arraySize = 18
arrayMinNumber = -100
arrayMaxNumber = 100

class BaseArray:
    def __init__(self, size, minNumber, maxNumber):
        self.info = {
            'arraySize': size,
            'arrayMinNumber': minNumber,
            'arrayMaxNumber': maxNumber
        }

#? - Testing Configuration
testingCycles = 200


def main():
  baseArray = BaseArray(arraySize, arrayMinNumber, arrayMaxNumber)
  startTestingLoop(testingCycles, SA_Simoes_FirstTry.runAlgorithm, "Simões - First Try", baseArray)

main()