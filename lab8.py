import math


def display_menu():
    print("1 - Add Test") 
    print("2 - Remove Test") 
    print("3 - Clear Tests") 
    print("4 - Add Assignment") 
    print("5 - Remove Assignment") 
    print("6 - Clear Assignments") 
    print("D - Display Scores")
    print("Q - Quit") 

def _avg(_list):
    
    total = 0
    avg = 0
    for index in range(len(_list)):
        total = total + _list[index]
    avg = total / len(_list)
    return avg

def standard_deviation(_list):
    total = 0
    count = 0
    dev = 0
    dev_val_sq = 0
    avg = _avg(_list)
    for index in range(len(_list)):
        dev = _list[index]- avg #taking each value and subtracting the mean
        dev_val_sq = dev_val_sq + (math.pow(dev, 2))
        count = count + 1
    total = dev_val_sq / count
    return math.sqrt(total)
        
    

def add(_list, msg):
    temp = int(input(msg))
    if not(temp < 0 or temp >100):
            _list.append(temp)
    else:
        print("Not valid input enter a number between 0 to 100")
    
def remove(_list, msg):
    temp = int(input(msg))
    for index in range(len(_list)):
        if (_list[index] == temp):
            _list.remove(temp)
        else:
            
            print("Could not find that score to remove")


def main():
    option = '1'
    test = []
    assignment =[]
    while option !='Q':
        display_menu()
        option = input("==>")
        if option == '1':
            msg = "Enter the new Test score 0-100 ==>"
            add(test,msg)
        elif option == '2':
            msg = "Enter the Test to remove 0-100 ==>"
            remove(test, msg)
        elif option == '3':
            test.clear()
        elif option == '4':
            msg = "Enter the new Assignment score 0-100 ==>"
            add(assignment,msg)
        elif option == '5':
            msg = "Enter the Assignment to remove 0-100 ==>"
            remove(assignment, msg)
        elif option == '6':
            assignment.clear()
        elif option == 'D':
            if(len(test) == 0 and len(assignment) == 0):
                print(f"Type               #       min       max       avg       std ")
                print(f"=============================================================")
                print("Tests               0       n/a       n/a       n/a       n/a\
                      program              0       n/a       n/a       n/a       n/a")
                
            #standard_deviation(test)
            #pass
        elif option == 'Q':
            exit()
main()
