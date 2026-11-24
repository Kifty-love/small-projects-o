# replace name1 and name2 with the names and student variables with true (for presence) and false (for absence)!!! ☆
student1 = False
student2 = False
name1 = "Andrei"
name2 = "Eliza"

# unchangeble below this line :(
pr_call = "Present. Now printing no. of classes."
pr_call2 = "Roll calling..."
pr_end = "Ended presence call."

def cl_at(a, b, c):
    for i in range(a, b, c):
        print(i)
    return "↑ Classes"

def presence(a, b):
    print(f"{pr_call2}")
    if a and b:
        print(f"{pr_call}")
        print(f"{cl_at(1, 6, 1)}")
    elif a or b:
        if a == True:
            print(f"There is only {name1}")
        else:
            print(f"There is only {name2}")
        print(f"{pr_call}")
        print(f"{cl_at(1, 6, 2)}")
    else:
        print("There is no one present.")
        print(f"{name1} and {name2} are absent.")
    print(f"{pr_end}")

presence(student1, student2)

# "if" and "else/elif" statement practice and function practice <3 (with f-strings)

# made by 1oana ☆