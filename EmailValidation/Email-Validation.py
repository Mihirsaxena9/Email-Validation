email=input(" Enter the Email Address : ")
k,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if("@" in email) and (email.count("@")==1):
            if(email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i==i.isspace():	
                        k=1
                    elif i.isalpha():			 	 
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1:
                    print("Invalid Email Address - Blank Spaces are not Allowed ")
                elif j==1:
                    print("Invalid Email Address - Upper Case Letters are not Allowed ")
                elif d==1:
                    print("Invalid Email Address - Invalid Character or Symbol is Used ")
                else:
                    print("Valid Email Address")
            else:
                print("Invalid Email Address - Domain Name is Invalid or Not Present")
        else:
            print("Invalid Email Address - @ Symbol is Missing or Used more than 1 time in the Email")
    else:
        print("Invalid Email Address - First Letter Should be an Alphabet")
else:
	print(" Invalid Email Address - Length is less than 6")