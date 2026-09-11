a=float(input("marks for subject 1:"))
b=float(input("marks for subject 2:"))
c=float(input("marks for subject 3:"))
d=float(input("marks for subject 4:"))
e=float(input("marks for subjeect 5:"))
total_marks_obtained=(a+b+c+d+e)
total_marks_possible=float(input("total marks possible:"))

percentage =(total_marks_obtained/total_marks_possible*100)
print("percentage recieved:",percentage)
                                
if percentage>90.0:
    print(" 'excellent , keep up the good work'~Aarav ")

elif 90>percentage>70:
    print(" 'keep working , ur doing good'~Aarav")

elif percentage<70:
     print(" 'work hard'~ Aarav ")
     
input("\npress Enter to exit...")
