#motorway


def main():
    filename = "toll.txt"
    filenameTwo = "cars.txt"
    carsDic, ls = calculations(filename, filenameTwo)

    displayStats(carsDic, ls)

    

def displayStats(dic, ls):

    for plate in dic:
        print(f'{plate}: {dic[plate]["totPrice"]:.2f} toll paid ({dic[plate]["sections"]} covered in {dic[plate]["entrance"]})')

    print(f'The car that paid the highest toll has a {ls[0][1]} licence plate.')


def calculations(fOne, fTwo):
    toMiDic, miToDic, toMiList, miToList, carsDic = readFile(fOne, fTwo)
    ls = []
    
    for plate in carsDic:
        priceTot = carsDic[plate]["totPrice"]
        sectionsTot = carsDic[plate]["sections"]

        for travel in carsDic[plate]["travel"]:
            start, dest = travel[0], travel[1]
            
            #checking what way its going, tomi, mito?
            try:
                startInd, destInd = toMiList.index(start), toMiList.index(dest) #we check they exist in the list
            except ValueError:
                continue #we don't consider if there are cities not listed
            
            if startInd < destInd:
                #we are in tomi line
                for i in range(startInd, destInd):
                    place = toMiList[i]
                    singlePrice = toMiDic[place]["price"]
                    priceTot += singlePrice

                    sectionsTot += 1

            else:
                #we are in the mito line
                startInd, destInd = miToList.index(start), miToList.index(dest) #we already checked they existed, we just reverse them now
                for i in range(startInd, destInd):
                    place = miToList[i]
                    singlePrice = miToDic[place]["price"]
                    priceTot += singlePrice

                    sectionsTot += 1

        carsDic[plate]["totPrice"] = priceTot
        carsDic[plate]["sections"] = sectionsTot 

        #need to create a list to sort them with highest price
        ls.append([carsDic[plate]["totPrice"], plate])
        
    ls.sort(reverse=True)

    return carsDic, ls


        
def readFile(fOne, fTwo):
    toMiDic = {}
    miToDic = {}
    toMiList = []
    miToList = []
    carsDic = {}

    try: 
        with open(fOne, "r") as fTool:
            for line in fTool:
                line = line.strip().split(";")
                
                toMiDic[line[0]] = {"dest": line[1], "price": float(line[2])}
                miToDic[line[1]] = {"dest": line[0], "price": float(line[2])}

                toMiList.append(line[0])
            
            toMiList.append(line[1])

            miToList = list(toMiList)
            miToList.reverse()

        with open(fTwo, "r") as fCars:
            #we don't need the dates for our purpose
            for line in fCars:
                line = line.strip().split(";")

                plate = line[0]
                if plate not in carsDic:
                    carsDic[plate] = {"travel": [[line[1], line[2]]], "totPrice": 0, "entrance": 1, "sections": 0} #totPrice and sections to me updated
                else:
                    carsDic[plate]["travel"].append([line[1], line[2]])
                    carsDic[plate]["entrance"] += 1

        return toMiDic, miToDic, toMiList, miToList, carsDic
    except IOError:
        exit("ERROR: File not found.")
    except ValueError:
        exit("ERROR: File is not formatted correctly")


main()