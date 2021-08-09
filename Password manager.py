Title = input("Enter The name of platform :" )
Email = input("what Email did You used their : " )
UserName = input("What Username did You used their : ") 
password = input("what was the password: ")

if __name__ == "__main__":
    file = open(Title + ".txt" , "a")
    file.write("Plattform:" + Title + "\n")
    file.write("E-Mail Adresse:" + Email + "\n")
    file.write("Username:" + UserName + "\n")
    file.write("Passwort:" + password + "\n")
    file.write("\n")
