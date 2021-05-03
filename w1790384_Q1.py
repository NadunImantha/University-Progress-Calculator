# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1790384
# Date: 17/04/2020


def process_credit(x):  # x is number of credit
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
    Pass = process_credit("Enter your number of pass credit: ")
    Defer = process_credit("Enter your number of defer credit: ")
    Fail = process_credit("Enter your number of fail credit: ")

    total_credit = Pass + Defer + Fail
    if int(total_credit) != 120:
        print(" Your total credit is incorrect...")
        print(" Try again...")

    elif Pass == 120 and Defer == 0 and Fail == 0:
        print(" Progress")

    elif Pass==100 and (Defer in range(0,21,20)) and (Fail in range(0,21,20)):
        print(" Progress – module trailer")

    elif (Pass in range(0,81,20)) and (Defer in range(0,121,20)) and (Fail in range(0,61,20)):
        print(" Do not Progress – module retriever")

    elif (Pass in range(0,41,20)) and (Defer in range(0,41,20)) and (Fail in range(80,121,20)):
        print(" Exclude")

    else:
        print(" Something went wrong...")

    print()