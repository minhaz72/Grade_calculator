print('Enter your marks:')
sub1=int(input("First subject: "))
sub2=int(input("Second subject: "))
sub3=int(input("Third subject: "))
sub4=int(input("Fourth subject: "))
sub5=int(input("Fifth subject: "))
 
avg=(sub1+sub2+sub3+sub4+sub5)/5
 
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