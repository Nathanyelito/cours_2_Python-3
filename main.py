def task1():
    dict1 = {}
    for i in range(1,11):
        dict1[i] = i**2
    return dict1



def task2():
    var1 = task1()
    for k,v in var1.items():
        print(f"La clé {k} et son carré est {v}")


def task3():
    reps = []
    register = {}
    
    while True:
        id = input("What is your ID ?")
        if id == "":
            break
        age = input("What is your age ?")
        name = input("What is your full name ?")
        adress = input("What is your adress ?")
        reps.append(age)
        reps.append(name)
        reps.append(adress)
        register[id] = reps
    print(register)
task3()