'''
Docstring for mini_quiz

refer to read me

quiz has a total of 2 questions. 

each question has 3 tries 
correct on 1st try -- 10 points
correct on 2nd try -- 5 points 
correct on 3rd try -- 2 points
wrong on 3rd try -- 0 points 

if 1st question is correct in 2 tries or less, proceed to 2nd question 

'''

def get_1():
    answer = input("What is the capital of England?: ")
    if answer == "london":
        print("Q1 10 points")
        return True
    else:
        answer = input("What is the capital of England?: ")
        if answer == "london":
            print("Q1 5 points")
            return True
        answer = input("What is the capital of England?: ")
        if answer == "london":
            print("Q1 2 points")
        else:
            print("Q1 0 points")


def get_2():
    answer = input("What is the capital of Italy?: ")
    if answer == "rome":
        print("Q2 10 points")
        return
    else:
        answer = input("What is the capital of Italy?: ")
        if answer == "rome":
            print("Q2 5 points")
            return
        answer = input("What is the capital of Italy?: ")
        if answer == "rome":
            print("Q2 2 points")
        else:
            print("Q2 0 points")

t = get_1()
if t == True:
    get_2()
