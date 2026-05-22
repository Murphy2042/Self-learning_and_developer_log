tasks=[]
print("=====To-do lis=====")
print("1. add task")
print('2. view tasks')
print('3. Delect task')
print('4. Exit')
    
while True:
    
    choice=input("please choose the service")
    if choice=='1':
        task_added=input("please input your new task:")
        tasks.append(task_added)
        print('Task added succesfully!')
    
    elif choice=='2':
        for index,task in enumerate(tasks,start=1):
            print(index,task)
    
    elif choice=='3':
        num=int(input("Enter the index of task you have finished"))
        item_completed=tasks.pop(num-1)
        print('you have completed '+item_completed+"succesfully !")
        
    elif choice=='4':
         print("goodbye!")
         break
     
    else:
        print('Invalid choice, please input again')
        
