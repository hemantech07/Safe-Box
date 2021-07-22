from kry import *
dataDict = {}

def authenticate():
    c=3
    while c>0:
        key = int(input("Enter Master Password - "))
        if key==pk:
            return key
        else:
            c-=1
            print(str(c) + " more attempts left!")
    return -1

def addNew(webName):
    print("\nEnter details for " + webName)
    usr = input("\nEnter Username - ")
    pwd = input("Enter Password - ")
    eusr = encrypt(pk, usr)
    epwd = encrypt(pk, pwd)
    tup = (eusr, epwd)
    dataDict[webName] = tup

def retrieve(webName):
    tup = dataDict.get(webName)
    if tup==None:
	    print("No details found for " + webName)
    else:
        print("\nRetrieving details for " + webName)
        usr = decrypt(pk, tup[0])
        pwd = decrypt(pk, tup[1])
        print("Username - " + usr + "\nPassword - " + pwd)

def updateData(webName):
    tup = dataDict.get(webName)
    if tup==None:
        print("No details found for " + webName)
    else:
        usr = decrypt(pk, tup[0])
        print("Username - " + usr)
        new = input("Enter new password - ")
        pwd = encrypt(pk, new)
        tup = (tup[0], pwd)
        dataDict[webName] = tup
        print("Updation successful!")

def main():
    print("\n\n***PASSWORD MANAGER***\n\n")
    auth = authenticate()
    if auth>0:
        print("\n***Welcome User***")
        choice=0
        while choice!=4:
            choice = int(input("\n1. Add\n2. Retrieve\n3. Update\n4. Exit\n\nEnter Choice: "))
            if choice==1:	
                web = input('\nEnter website: ')
                addNew(web)

            elif choice==2:
                web = input('\nEnter website: ')
                retrieve(web)

            elif choice==3:
                web = input('\nEnter website: ')
                updateData(web)

            elif choice==4:
                exit()

            else:
                print("Invalid choice, please try again!\n")

    else:
        print("Authentication Failed")

if __name__ == '__main__':
    main()