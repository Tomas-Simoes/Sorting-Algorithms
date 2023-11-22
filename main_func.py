from random import randint

#? - Sorted Status
successRate = 0
errorRate = 0

def getRandomArray(arrayInfo):
  randomArray = []

  for i in range(1, arrayInfo['arraySize']):
    randomArray.append(
                          randint(
                            arrayInfo['arrayMinNumber'], 
                            arrayInfo['arrayMaxNumber'])
                        )

  return randomArray

def startTestingLoop(testingCycles, algorithm, algorithmName, baseArray):
  global successRate, errorRate

  for testCycleNumber in range(0, testingCycles):
    testArray = getRandomArray(baseArray.info)

    sortedArray = algorithm(testArray)
    getTestLoopStatus(sortedArray, testArray)

  successRateInPercentage = (successRate * 100) / testingCycles 
  errorRateInPercentage = (errorRate * 100) / testingCycles

  print("Your algorithm ", algorithmName, " got this data: ")
  print(f"""
  Success Rate: {successRateInPercentage}%( {successRate}/{testingCycles})
  Error Rate: {errorRateInPercentage}% ({errorRate}/{testingCycles})
  """)

def getTestLoopStatus(algorithmSortedArray, originalArray):
  global successRate, errorRate

  originalArrayWithoutFirstAndLast = originalArray[1:len(originalArray)-1]
  originalArrayWithoutFirstAndLast.sort()

  sortedOriginalArray = [originalArray[0]]
  sortedOriginalArray.extend(originalArrayWithoutFirstAndLast)
  sortedOriginalArray.append(originalArray[len(originalArray) - 1])

  if algorithmSortedArray == sortedOriginalArray: successRate += 1
  else: errorRate += 1

  print(successRate)
  print(errorRate)
  return successRate, errorRate
