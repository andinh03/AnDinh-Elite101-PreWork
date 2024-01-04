
print("Welcome to Chatbot 101!")
name = input("Please enter your name: ")
age = input(f"Nice to meet you {name}! How old are you? ")
print(f"Welcome, {name}! Oh, so youthful with your {age} years old! How can I help you? ")
print("")

def options_menu():
  print("Please choose from the following options:")
  print("1. Placeholder option 1")
  print("2. Placeholder option 2")
  print("3. Placeholder option 3")
  print("4. Exit the conversation")
  print("")

  
def user_selection():  
  number = int(input("Enter the number of your choice: "))
  
  if number == 1:
      print("Placeholder response 1")
  elif number == 2:
      print("Placeholder response 2")
  elif number == 3:
    print("Placeholder response 3")
  elif number == 4:
    print(f"Goodbye {name}! Have a nice day!")
  
options_menu()
user_selection()