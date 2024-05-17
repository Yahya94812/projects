import os
os.system("cls")

try:
    f=open("data.txt","r")
    f.close()
except FileNotFoundError:
    print("creating data.txt file")
    f=open("data.txt","w")
    f.close()

def add_tasks():

    print(end="\n\n")

    print(50*"-")
    print("--Add tasks--")
    print(50*"-")
        
    with open("data.txt","r") as f:
        str_no=len(f.readlines())

    with open("data.txt","+a") as f:
        while(True):
            task=input(f"{str_no+1}. ")
            if task=='':
                print(50*"-")
                break
            f.write(task)
            f.write("\n")
            str_no+=1

    print(end="\n\n")



def read_task():

    print(end="\n\n")

    print(50*"-")
    print("--Reading tasks--")
    print(50*"-")

    with open("data.txt","r") as f:
        t_no=1
        tasks=f.readlines()
        if len(tasks)==0:
            print("\n\n--Empty--\n\n")
        for task in tasks:  
            print(f"{t_no}. {task}",end="")#str in file already contain "\n"
            t_no+=1

    print(50*"-")    


def delete_task():
    print(end="\n\n")
    read_task()

    print("--Deleting task--")
    print(50*"-")

    with open("data.txt","r") as f:
        data=f.readlines()
        
    str_no=int(input("Enter the si.no of the task to delete or press '0' for delete all :"))
    if str_no==0:
        with open("data.txt","w") as f:
            pass
        return

    
    if (str_no>len(data)):
        print("this task does't exist !")
        print(50*"-")
        return
    
    data[str_no-1]=''

    with open("data.txt","w") as f:
        f.writelines(data)

    print(50*"-")
    print(end="\n\n")

read_task()
print(end="\n\n")

while(True):
    x=input("press 'a' for adding or 'd' for deleting task :" )
    if x=='a':
        os.system("cls")
        add_tasks()
        

    elif x=='d':
        os.system("cls")
        delete_task()
        read_task()    
    elif x=='':
        break
    else:
        continue
    