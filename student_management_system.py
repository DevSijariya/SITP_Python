class Student:
    def __init__(self,Name,Roll_no,Marks):
        self.Name = Name
        self.Roll_no = Roll_no
        self.Marks =Marks

    def acceptstudentData(self,Name,Roll_no,Marks):
        ob=Student(Name,Roll_no,Marks)
        l.append(ob)

    def Display_Student_details(self,ob):
        print("Name : ",ob.Name)
        print("Roll no : ",ob.Roll_no)
        print("Marks : ",ob.Marks)
        print("\n")
        
    def Search_Student_Details(self,roll_no):
        for i in range(l.__len__()):
            if(l[i].Roll_no==roll_no):
                return i
            
    def Delete_Student_Details(self,roll_no):
        i=obj.Search_Student_Details(roll_no)
        del l[i]
    
l=[]
obj=Student('',0,0)
print("Enter the Task you want to Perform.\n")
while True:
    x=int(input("Enter 1 for Accept Data\n2for Display\n3 for Search Data\n4 For Delete Data\n")) 
    if x==1:
        N=input("\nEnter Student Name ")
        R=int(input("Enter Student Roll "))
        M=int(input("Enter Student Mark "))
        print('\n')
        obj.acceptstudentData(N,R,M)
    elif x==2:
        print("List are : \n")
        for i in range(l.__len__()):
            obj.Display_Student_details(l[i])
    elif x==3:
        r1=int(input("Enter the roll number of Student you want to search "))
        s=obj.Search_Student_Details(r1)
        obj.Display_Student_details(l[s])
    elif x==4:
        r1=int(input("Enter the roll no you want to delete data "))
        obj.Delete_Student_Details(r1)
        print("Deletion Successfully !!")
    else:
        print("Exit Succesfuuly ! ")
        break
