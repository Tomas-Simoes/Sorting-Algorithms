def runAlgorithm(vector):
    newVector = []
    newVector.append(vector[0])
    vectorLen = len(vector)
    print("Previous vector:", vector);

    ##
    #[1, 2, 3, 4, 6, 9]
    #[1, 5, 3, 2, 1, 9] -> new vector [1, 3, 2, 5]
    #[6, 6, 3, 1]
    ##

    vectorCropped = vector[1:vectorLen-1]
    nextIndex = 2
    currentIndexNewVector = 1
    for i, value in enumerate(vectorCropped): 
        print("i: ", i)
        print("nextIndex:", nextIndex)
        if len(newVector) >= 2:
            print(len(newVector));
            print(len(vector) - 1)
            if len(newVector) == len(vector) - 1:
                break;

            currentIndexNewVector = 1
            print("----- You entered the len(newVector) > 2 condition. -----")
            print("newVector: ", newVector)
            print("newVector[currentIndexNewVector]: ", newVector[currentIndexNewVector])
            print("vector[nextIndex]", vector[nextIndex])
            if vector[nextIndex] < newVector[currentIndexNewVector]:
                print("----- You entered the vector[nextIndex] < newVector[currentIndexNewVector] condition. -----")
                if(currentIndexNewVector == 1):
                    newVector.insert(currentIndexNewVector, vector[nextIndex])
                else:
                    for x in range(len(newVector)):
                        if x == 0: continue
                        print("newVector[x]:  ", newVector[x] )
                        print("newVector[currentIndexNewVector]:  ", newVector[currentIndexNewVector])

                        if newVector[x] == newVector[currentIndexNewVector]:
                            print("the current index of new vector: ",  newVector[currentIndexNewVector] )
                            newValueIndex = x
                            newVector.insert(x, vector[nextIndex])

                            print("New vector before checking if other numbers are menos: ", newVector)
                            
                            for indexY, y in enumerate(newVector):
                                print("y", y)
                                if newVector[newValueIndex] < y:
                                    print("New Vector ", newVector[newValueIndex])
                                    print("y", y)
                                    newVector.insert(indexY, newVector[newValueIndex])
                                else:
                                    if indexY == 0:
                                        break
                            break
                        else:
                            print("New vector after checking if other numbers are menos: ", newVector)
                            currentIndexNewVector += 1 
            elif vector[nextIndex] == newVector[currentIndexNewVector]:
                print("----- You entered the vector[nextIndex] == newVector[currentIndexNewVector] condition. -----")
                newVector.insert(currentIndexNewVector, vector[nextIndex])
            else:
                print("----- You entered the vector[nextIndex] > newVector[currentIndexNewVector] condition. -----")
                for x in range(len(newVector)):
                    if x == 0: continue

                    if vector[nextIndex] < newVector[x]:
                        print("CCCCCCCC")
                        newVector.insert(x, vector[nextIndex])
                        break
                    elif vector[nextIndex] == newVector[x]:
                        newVector.insert(x, vector[nextIndex])
                        break
                    elif vector[nextIndex] > newVector[len(newVector) - 1]:
                        print("BBBBBBBB")
                        newVector.append(vector[nextIndex])    

            nextIndex += 1
        else:
            if vector[nextIndex] < value:
                print("----- You entered the vector[nextIndex] < value condition. -----")

                print("Current i and value:", i, " - ", value)
                print("Next value of vector", vector[nextIndex])

                if value in newVector:
                    for x in range(len(newVector)): 
                        if newVector[x] == value:
                            if x == 0:
                                newVector.append(vector[nextIndex])
                                newVector.append(value)
                                break;
                            else:
                                newVector.insert(x, vector[nextIndex])
                                break
                else:
                    if vector[0] == vector[1]:
                        print("asdfsdaf")
                        newVector.append(vector[0])

                    newVector.append(vector[nextIndex])
                    newVector.append(vector[nextIndex - 1])
                
                nextIndex += 1
                print("New vector after  loop when next index < value: ", newVector)

            elif vector[nextIndex] == value:
                print("----- You entered the vector[nextIndex] == value condition. -----")
                newVector.append(value)
                newVector.append(value)
                nextIndex += 1
            else:
                print("----- You entered the else condition. -----")
                newVector.append(value)
                newVector.append(vector[nextIndex])
                nextIndex += 1
        
        if len(newVector) == len(vector) - 1:
            break

    print("FINAL NEW VECTOR: ", newVector)
    
    newVector.append(vector[len(vector) - 1])
    return newVector
