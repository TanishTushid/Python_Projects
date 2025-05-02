#(using string function)

email = input("enter your Email: ")  #g@g.in
k=0 
j=0
d=0
if len(email) >= 6:           #1. 
    if email[0].isalpha():    #2.
        if "@" in (email) and (email.count("@")==1):    #3.        # for @ and its only one
            if ((email[-4]=="." ) ^ (email[-3]==".")):  #5.          # fot the dot's and where come
                for i in email:                                # loop for space and alphabet in not upper
                    if i ==i.isspace():
                      k = 1
                    elif i.isalpha():
                        if i == i.upper():  
                            j = 1
                    elif i.isdigit():                          # for the digit
                        continue
                    elif i == "_" or i == "." or i =="@":      #for the valid sign
                        continue
                    else:                                      #no another sign valid
                        d = 1
                    
                    if k == 1 or j == 1 or d == 1 :
                        print("wrong Email 5.")
                    else:
                        print("Right Email")
            else:
                print("wrong Email 4.")
        else:
            print("wrong Email 3.")
    else:
        print("wrong Email 2.")
else:
    print("wrong Email 1.")
