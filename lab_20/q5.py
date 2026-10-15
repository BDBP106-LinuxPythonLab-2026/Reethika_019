"""5. Shopping List Manager
Concepts: lists, while loop menu, append(), remove(), in, sort(), enumerate()
Build a menu-driven program that keeps running until the user picks Quit:
1. Add item 2. Remove item 3. View list 4. Sort list 5. Quit
Don't add duplicates (check case-insensitively). Print a friendly message when the user
tries to remove an item that isn't on the list. Show the list numbered from 1."""

shopping=[]
while True:
    print("1.Add 2.Remove 3.View list 4.Sort list 5.Quit")
    choice=input("Choice: ")
    if choice=="1":
        item=input("items: ").lower()
        if item in shopping:
            print("Already exist in the list")
        else:
            shopping.append(item)
    elif choice=="2":
        item=input("items: ").lower()
        if item in shopping:
            shopping.remove(item)
        else:
            print("Items not on the list")
    elif choice=="3":
        for i,items in enumerate(shopping,1):
            print(i,":",items)
    elif choice=="4":
        shopping.sort()
    elif choice=="5":
        break





