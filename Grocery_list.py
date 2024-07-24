def add_item(shopping_list):
    item = input("What will you be adding to the shopping list? ")
    shopping_list.append(item)
    print(f"{item} has been added to the list!")
    





def main():
    shopping_list = []
    while True:
        action = input('''
Shopping List Helper:
                       
1. Add item
2. Remove item
3. Print shopping list                       
4. Exit    
''' )
        
        if action == "1":  
            add_item(shopping_list) 
        elif action == "2": 
            subtraction()
        elif action == "3":
            division()
        elif action == "4":
            multiply()
            break
        else:
            print("ERROR PLEASE SELECT WHAT IS DISPLAYED")

main()