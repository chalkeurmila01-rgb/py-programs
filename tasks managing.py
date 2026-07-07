#To-Do-List
tasks=[]
while True:
    print("1.Add 2.View 3.Exit")
    c=input("Choice:")
    if c=="1": tasks.append(input("Task:"))
    elif c=="2":
        [print(i+1,t) for i,t in enumerate(tasks)]
    else:
        break