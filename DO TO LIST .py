import os
def display():
  print("To-Do App List")
  print("...........")
  print("1. View To-Do List")
  print("2.Add To-Do")
  print("3.Complete To-Do")
  print("4.Quit")
def view():
  try:
    with open("todo.txt")as file:
      tasks=file.readlines()
      if not tasks:
        print("No tasks in the to-do list.")
      else:
        for i,task in enumerate(tasks):
          print(f"{i}.{task.strip( )}")
  except FileNotFoundError:
    print("To-Do list is empty")
def add():
  task=input("Enter task:")
  with open("todo.txt","a")as file:
    file.write(task+"\n")
    print(f"Task'{task}' added successfully")
def complete():
  view()
  try:
    task_num=int(input("Enter the number of the task to mark as complete:"))
    with open("todo.txt","r") as file:
      tasks=file.readlines()
    if 1<=task_num<=len(tasks):
      complete=tasks.pop(task_num-1)
      with open("todo.txt","w")as file:
        file.writelines(tasks)
      print(f"Task'{complete.strip()}' marked as complete")
    else:
      print("Invalid task number")
  except ValueError:
    print("please enter a valid number")
def main():
  while True:
    display()
    choice=input("Enter your choice(1 to 4): ")
    if choice=="1":
      view()
    elif choice=="2":
      add()
    elif choice=="3":
      complete()
    elif choice=="4":
      print("Thank you for using the to-do app")
      break
    else:
      print("Invalid choice")
if __name__ == "__main__":
  main()
