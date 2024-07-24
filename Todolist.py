def main():
    tasks = []
    
    while True:
        print("\n====== To-Do List =======");
        print("1.Add Task");
        print("2.Show Task");
        print("3.Mark Task Has Done");
        print("4.Exit");
        
        choice= input("Enter your Choice :- ");
        
        if choice == '1':
            print()
            n_tasks = int(input("How many Task you want to add: "))
            
            for i in range(n_tasks):
                task = input("Enter The Task: ")
                tasks.append({"task" : task , "done" : False})
                print("Task Added!")
                
        elif choice == '2':
            print("\n TAsks :")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"]else "Not Done"
                print(f"{index + 1}.{task['task']} -{status}")
                
        elif choice == '3':
            task_index = int(input("Enter the task number to mark as done :"))-1
            if 0 <= task_index < len(tasks):
                task[task_index]["done"] = True
                print("Task marked as done!")
                
            else:
                print("Invalid task number.")
                
        elif choice == '4':
            print("Exiting the to-do list..")
            break
        else:
            print("INvalid choice . Please try again")
if __name__=="__main__":
    main()