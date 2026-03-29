expances=[]

print("Welcome To Kharcha Pani")
while True:
    print("==============MENU===========")
    print("1. Add Kharcha")
    print("2. Kharcha List")
    print("3. Total Kharcha")
    print("4. Exit")
    print("--------------------------------------")
    choice = int(input("Enter Your Choice (1,2,3,4..etc) : "))
    print("--------------------------------------")
    if choice==1:
        date=input("Enter Date (ddmmyy) : ")
        amount=float(input("Enter Your Amount (Rupee) : "))
        remarks=input("Enter Remarks : ")
        expenceData={
            "date" : date,
            "amount":amount,
            "remarks":remarks
        }
        expances.append(expenceData)
        print("Expance Saved Now Bro....")
    elif choice==2:
        if len(expances)==0:
            print("Koi Bhi kharcha nhi hua hai ... Pahle jake kharcha karo bhai")
            
        else:
            i=0
            for ex in expances:
                i=i+1
                print(f"SR No . {i} | Date :{ex["date"]} | Amount :{ex["amount"]}  | Remarks :{ex["remarks"]} ")
    elif choice==3:
        total=0
        for ex in expances:
            total=total+ex["amount"]
        print(f"Total Kharch : {total}")
    elif choice==4:
        print("Done Bro ! You Are Exit ")
        break
    else:
        print("Invalid Input")
        
     

