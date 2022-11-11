def Grade_cal(sub1:int, sub2: int, sub3: int , sub:  int, sub4:  int , sub5: int ) : 
    avg= (sub+sub1+ sub3 + sub4 + sub5 + sub2) / 6 
        
    if avg >= 90:
        print("Grade: A")
    elif avg >= 80:
        print("Grade: B")
    elif avg >= 70:
        print("Grade: C")
    elif avg >=60:
        print("Grade: D")
    else:
        print("Grade: F")

if __name__  == '__main__ ': 
    sub1=int(input("First subject: "))
    sub2=int(input("Second subject: "))
    sub3=int(input("Third subject: "))
    sub4=int(input("Fourth subject: "))
    sub5=int(input("Fifth subject: "))
    sub=int(input("Sixth subject: "))

    print(Grade_cal (sub,  sub1, sub2 , sub3, sub4, sub5 ))
    