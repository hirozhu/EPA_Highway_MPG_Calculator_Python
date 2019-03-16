def main():
    print("Welcome to EPA Mileage Calculator")
    year = input("What year would you like to view data for? (2008 or 2009):")
    while year != "2008" and year != "2009":
        print("*Invalid input, please try again!")
        year = input("What year would you like to view data for? (2008 or 2009): ")

    if year == "2008":
        filename = "epaVehicleData2008(1).csv"
    elif year == "2009":
        filename = "epaVehicleData2009(1).csv"

    listMPG = []      # To create a list in which I put all the hwy MPG values in the CSV file (which is the 10th column of the CSV file)
    listCar = []      # To create a list to put all the car types in the CSV file (which is the 3rd column of the CSV file)
    fin = open(filename,"r")
    for line in fin:
        line = line.strip()
        dataList = line.split(",")

        if "VANS" in line or "PICKUP" in line:              # Eliminate all the lines with vans and pickup
            line = "empty"
        else:
            listMPG.append(dataList[9])
            listCar.append(dataList[2])

    fin.close()

    listMPG.remove(listMPG[0])                   # To remove the first item in the list which is the title "hwy mpg"
    listCar.remove(listCar[0])                   # To remove the first item in the list which is the title "MFR"

    maxValue = max(listMPG)                      # To look for the max value of the highway MPG list
    minValue = min(listMPG)                      # To look for the min value of the highway MPG list

    listMaxCar =[]                               # To create a list in which I put all the cars with max MPG value
    num1 = 0
    for num1 in range(0, len(listMPG) - 1):
        if listMPG[num1] == maxValue:
            listMaxCar.append(listCar[num1])
        num1 += 1
    maxCar = "\n".join(listMaxCar)

    listMinCar = []                              # To create a list in which I put all the cars with min MPG value
    num2 = 0
    for num2 in range(0, len(listMPG) - 1):
        if listMPG[num2] == minValue:
            listMinCar.append(listCar[num2])
        num2 += 1
    minCar = "\n".join(listMinCar)

    filename2 = input("Enter the filename to save results to:")
    fout = open(filename2,"w")
    print("""EPA Highway MPG Calculator (""",year,""")
---------------------------------
Maximum Mileage (highway):""",maxValue,"""
""",maxCar,"""
Minimum Mileage (highway): """,minValue,"""
""",minCar,file = fout)

    print("""Operation Success! Mileage data has been saved to""",filename2,"""
Thanks, and have a great day!""")



main()