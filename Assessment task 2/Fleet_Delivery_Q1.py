# Fleet Delivery Q1
def combine_trucks(trucks, first_truck, second_truck):

    trucks_cargo =trucks[first_truck-1] + trucks[second_truck-1] #combines the load found in bboth trucks 
    if first_truck == second_truck:
     print(" ERROR : same truck has been inputted twice") #demonstrates the boundary case and avoids it
     print(f' this would however =',trucks_cargo)
     exit()
    print(trucks_cargo)                           # prints the combined total
    print("first truck:", trucks[first_truck-1],", second truck:",trucks[second_truck-1])  #shows the amount of cargo in each truck
                           # TODO: return the total packages in first_truck and second_truck
    pass
def main():
    trucks = [4, 7, 2, 6, 9]
    combine_trucks(trucks, 2, 4)  # Expected: 13 note: i have removed print since the code now works 
    combine_trucks(trucks, 1, 3)  # Expected: 6
main()
 