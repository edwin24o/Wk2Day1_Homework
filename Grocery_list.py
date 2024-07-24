def add_item(shopping_list):
    item = input("What will you be adding to the shopping list? ")
    shopping_list.append(item)
    print(f"{item} has been added to the list!")
    
def remove_item(shopping_list):
    item = input("What would you like to remove from the list? ")
    if item in shopping_list:
      shopping_list.remove(item)
      print(f"'{item}' has been removed from the shopping list.")
    else:
        print(f"WAIT! '{item}' is not in the shopping list")

def print_list(shopping_list):
    if shopping_list:
        print("Shopping list:")
        for item in shopping_list:
            print(f"- {item}")
    else:
        print("Your shopping list is EMPTY")

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
            remove_item(shopping_list)
        elif action == "3":
            print_list(shopping_list)
        elif action == "4":
            print('GOODBYE!!')
            break
        else:
            print("ERROR PLEASE SELECT WHAT IS DISPLAYED")

main()