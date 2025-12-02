shopping_list=[]

while True:
    print("1.Add to list")
    print("2.Remove item  list ")
    print("3.View list")
    print("4.Exit")

    Choice=int(input("Enter your choice: "))
    if Choice == 1:
        item=input( "what you want to add" )
        shopping_list.append(item)
        print(f"the {item} has been added to the list")
    
    elif Choice ==2:
        item=input("which item do you what to remove")
        shopping_list.remove(item)
        print(f"the {item} has been removed")
   
    elif Choice==3:
     for ay, item in enumerate(shopping_list, 1):
      print(f"{ay}. {item}")
   
    elif Choice==4:
       print("Goodbye!")
       break