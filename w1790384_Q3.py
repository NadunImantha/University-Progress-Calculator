# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
#Student ID: w1790384
#Date: 17/04/2020


Progress=0
Trailing=0
Retriever=0
Excluded=0

def process_credit(x):      # x is nuber of credits
    name = input(x)
    try:
        name = int(name)
        if name in range(0, 121, 20):
            return name
                
        else:
            print(" Range Error...")
            print(" Try again...")
            return process_credit(x)
    except ValueError:
        print(" Please enter integer value of credit...")
        print(" Try again...")
        return process_credit(x)

while True:
    Pass= process_credit("Enter your number of pass credit: ")
    Defer = process_credit("Enter your number of defer credit: ")
    Fail = process_credit("Enter your number of fail credit: ")

    total_credit = Pass + Defer + Fail
    if total_credit != 120:
        print(" Your total credit is incorrect...")
        print(" Try again...\n")

    elif Pass == 120 and Defer == 0 and Fail == 0 :
        print("Progress\n")
        Progress = Progress + 1

    elif Pass==100 and (Defer in range(0,21,20)) and (Fail in range(0,21,20)):
        print("Progress – module trailer\n")
        Trailing = Trailing + 1

    elif (Pass in range(0,81,20)) and (Defer in range(0,121,20)) and (Fail in range(0,61,20)):
        print("Do not Progress – module retriever\n")
        Retriever = Retriever + 1

    elif (Pass in range(0,41,20)) and (Defer in range(0,41,20)) and (Fail in range(80,121,20)):
        print("Exclude\n")
        Excluded = Excluded + 1
            
    else:
        print("Something went wrong...\n")

    end = str.lower(input("Press 'q' to quit the program or Press 'any button' to continue: "))
    if end == "q" :
        break

print("Progress ","Trailing ","Retriever ","Excluded ")
while True:
    if Retriever==0 and Progress==0 and Retriever==0 and Excluded==0:
        break

    if Progress > 0:
        print("*".rjust(4), end="")
        Progress -= 1
    else:
        print(" ".rjust(4), end="")


    if Trailing > 0:
        print("*".rjust(10), end="")
        Trailing -= 1
    else:
        print(" ".rjust(10), end="")


    if Retriever > 0:
        print("*".rjust(11), end="")
        Retriever -= 1
    else:
        print(" ".rjust(11), end="")


    if Excluded > 0:
        print("*".rjust(10))
        Excluded -= 1
    else:
        print(" ".rjust(10))
