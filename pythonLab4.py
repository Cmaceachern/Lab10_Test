import math

# print("{:10f}".format(math.pi))
# # print({math.pi:5f})
# # print({math.pi:3f})
# # print({math.pi:.0f})

# startInt = int(input("Give the start value: "))
# endInt = int(input("Give the end value: "))
#
#
#
# count = 1
# for i in range(startInt,endInt):
#     print(i, i**2, i**3, i**4)


answerKey = (A,C,True,False, "Heap", "Matrix")

def examgrader (name, answers):
    incorrect_counter = 0
    for i in range(len(answers)):
        if answers[i] != answerKey[i]:
            print("Question {} is incorrect. You put {}. The correct answer is {}".format(i, answers[i], answerKey[1] ))
            incorrect_counter += 1

    num_grade = incorrect_counter / len(answerKey) * 100
    gradeletter= lettergrade(num_grade)

    print("{} got {} questions wrong ")






