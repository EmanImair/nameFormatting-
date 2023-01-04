def nameFormatting (fName ,lName ):
    if fName=="" or lName=="":
        print("you entered an valid value , please make sure that the first name and list name "
              "are not empty")
    else :
        full_name=fName + " " + lName
        return full_name.title()

firstName = input("First Name:  ")
lastName= input("Last Name : ")

user_name = nameFormatting(firstName,lastName)


print(f"user name :  {user_name} " )
