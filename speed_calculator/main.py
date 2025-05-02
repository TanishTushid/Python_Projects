#typing speed calculator

from time import *         #for time
import random as r         #for random choice


# for the mistake you did in typing

def mistake(para_test,user_test):
    error = 0
    for i in range(len(para_test)):
        try:
            if para_test[i] != user_test[i]:          #out of index range
                error = error + 1                     # error counting
        except :
            error = error + 1
    return error

#time delay

def speed_time(time_s,time_e,userinput):
    # time round off
    time_delay = time_e - time_s
    time_Round = round(time_delay,2)
    #speed
    speed = len(userinput) / time_Round
    return round(speed)

while True:
    check = input("Are you want to give test Yes / No : ")
    if check == "Yes":
        #paragraph 

        test = ["Paragraph writing in English is an essential skill that helps students and professionals express their thoughts clearly and effectively.",
        "A well-written paragraph consists of a topic sentence, supporting details, and a concluding sentence, all arranged logically.",
        "It allows writers to organise their ideas and convey them in a structured way, making their writing more engaging and impactful.",
        "Whether it’s for essays, articles, or creative writing, mastering paragraph writing is a crucial step toward becoming a confident and proficient writer in English."]

        # chice random para
        test = r.choice(test)

        #print

        print("***** speed calculator *****")
        print(test)
        print()
        print()

        #for the time

        time_1 = time()                 #initial time
        user_test = input("Enter: ")
        time_2 = time()                 #ending time


        # calling the function

        print("Speed: ", speed_time(time_1,time_2,user_test),"W/sec")
        print("error : ", mistake(test,user_test))

    elif check == "No": 
        print("Thank you you visit")
        break

    else:
        print("Wrong Input")
        

