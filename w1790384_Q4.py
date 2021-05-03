# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
#Student ID: w1790384
#Date: 17/04/2020


Pass = [120, 100, 100, 80, 60, 40, 20, 20, 20, 0]
Defer = [0, 20, 0, 20, 40, 40, 40, 20, 0, 0]
Fail = [0, 0, 20, 20, 20, 40, 60, 80, 100, 120]

list = []
i=0
Progress=0
Trailing=0
Retriever=0
Excluded=0

while i<10:
    credit = Pass[i] or Defer[i] or Fail[i]

    if credit == str(credit):
        list.append('do not enter integer values.')

    elif credit not in range(0,121,20):
        list.append('credits out of range.')

    elif (Pass[i] + Defer[i] + Fail[i]) != 120:
        list.append('total credit is incorrect.')

    elif Pass[i] == 120 and Defer[i] == 0 and Fail[i] == 0:
        list.append('progression outcome is Progress.')
        Progress += 1

    elif Pass[i] == 100 and (Defer[i] in range(0,21,20)) and (Fail[i] in range(0,21,20)):
        list.append('progression outcome is Progress – module trailer.')
        Trailing += 1

    elif (Pass[i] in range(20,81,20)) and (Defer[i] in range(20,41,20)) and (Fail[i] in range(20,61,20)):
        list.append('progression outcome is Do not Progress – module retriever.')
        Retriever += 1

    elif (Pass[i] in range(0,21,20)) and (Defer[i] in range(0,21,20)) and (Fail[i] in range(80,121,20)):
        list.append('progression outcome is Exclude.')
        Excluded += 1

    i += 1

for student_no in range(len(list)):
    print("your", student_no+1, " student", list[student_no])

print()
print("Progress\t", Progress, ":", "*" * Progress)
print("Trailing\t", Trailing, ":", "*" * Trailing)
print("Retriever\t", Retriever, ":", "*" * Retriever)
print("Excluded\t", Excluded, ":", "*" * Excluded)
total = Progress + Trailing + Retriever + Excluded
print(total, "progression outcomes in total")
