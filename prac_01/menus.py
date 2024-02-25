"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""

name = input("Enter your name : ")
print("(h)ello")
print("(g)oodbye")
print("(q)uit")
user_input = input(">>>")
if user_input == "h":
    print("Hello", name)
elif user_input == "g":
    print("Goodbye", name)
elif user_input == "q":
    print("Finished")
else:
    print("Invalid choice")