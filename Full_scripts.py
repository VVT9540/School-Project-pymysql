import sys
import pymysql
import os

def teacher(x1,x2,x3,x4,x5):
    def create_question_paper():
        dbcon=pymysql.connect(host="localhost",user="root",passwd="mydatabase",database='teacher')
        cur=dbcon.cursor()
        Q=f"update teacher_pi set que_no={x4}+1 where id={x1};"
        cur.execute(Q)
        dbcon.commit()
        dbcon.close()
        print(f"The ID for your question paper is {x5[0:2]}{x1}0{x4}")
        print("Please keep the question paper identity for future references")
        file_name=f"{x5[0:2]}{x1}0{x4}"
        f1=open(f"{file_name}.txt","x")
        anslist=[]
        count=1
        choice2="Y"
        while choice2 in ["Y","y"]:
            print(f"Enter the {count} MCQ type question you want to enter")
            a=input("")
            print("enter it's options")
            o1=input("Enter 1 OPTION: ")
            o2=input("Enter 2 OPTION: ")
            o3=input("Enter 3 OPTION: ")
            o4=input("Enter 4 OPTION: ")
            que=f"{a}$1.{o1}$2.{o2}$3.{o3}$4.{o4}"
            f1.write(que)
            f1.write("\n")
            ans=int(input("Enter correct option number: "))
            anslist.append(ans)
            print(f"Do you want to add {count+1} question")
            choice2=input("Enter 'Y' or 'N'")
            count+=1
        f1.write(str(anslist))
        f1.close()
        dbcon=pymysql.connect(host="localhost",user="root",passwd="mydatabase",database='students')
        cur=dbcon.cursor()
        Q=f"create table student_data_{x5[0:2]}{x1}0{x4}(STID int(3) primary key,Name varchar(30),Class varchar(4),Sec char(1),Marks int(2));"
        cur.execute(Q)
        Q=f"alter table student_data_section_A add {file_name} int(2);"
        cur.execute(Q)
        Q=f"alter table student_data_section_B add {file_name} int(2);"
        cur.execute(Q)
        dbcon.close()

    def edit_previous_question_paper():
        a=input("enter the ID for your Question Paper: ")
        f1=open(f"{a}.txt","r")
        f2=open(f"abc.txt","x")
        var4=f1.readlines()
        Questions=var4[:-1]
        anslist=list(var4[-1])
        anslist_org=[]
        for i in range(0,len(anslist)):
            try:
                x=int(anslist[i])
                print(anslist[i])
                anslist_org.append(x)
            except:
                pass
        c=0
        for i in Questions:
            var7=i
            b=str(var7)
            var8=b.split("$")
            print(var7)
            var11=""
            count=1
            if (i[-1]=="n") and (i[-2]=="\""):
                var9=var8[:-2]
            else:
                var9=var8
            print(var9)
            for j in var9:
                print(j)
            var10=input("Do you want to change This Question?(y or n)")
            if var10 in ["y","Y"]:
                print(f"Enter the {count} MCQ type question you want to enter")
                a1=input("")
                print("enter it's options")
                o1=input("Enter 1 OPTION: ")
                o2=input("Enter 2 OPTION: ")
                o3=input("Enter 3 OPTION: ")
                o4=input("Enter 4 OPTION: ")
                que=f"{a1}$1.{o1}$2.{o2}$3.{o3}$4.{o4}"
                f2.write(que)
                f2.write("\n")
                ans=int(input("Enter correct option number: "))
                anslist_org[c]=(ans)
            else:
                f2.write(var7)
            c+=1
        f2.write(str(anslist_org))
        f1.close()
        f2.close()
        os.remove(f"{a}.txt")
        os.rename("abc.txt",f"{a}.txt")


    def show_student_report():
        print("Choose from the options given below :")
        print("1. See whole students report")
        print("2. See particular student report")
        print("3. See Section wise students report")
        print("4. See rank wise students report")
        print("5. Exit Report Section")
        choice=int(input("Enter your choice"))
        while True:
            if choice==1:
                whole_student_report()
            elif choice==2:
                particular_student_report()
            elif choice==3:
                sectionwise_student_report()
            elif choice==4:
                rankwise_student_report()
            else:
                break
            choice=int(input("Enter your next choice"))

    def whole_student_report():
        dbcon=pymysql.connect(host="localhost",user="root",passwd="mydatabase",database="STUDENTS")
        cur=dbcon.cursor()
        var2=input("Enter the ID for the test:")
        Q=f"SELECT * FROM student_data_{var2};"
        cur.execute(Q)
        a=cur.fetchall()
        for i in a:
            print(i,end=" ")
        print("Records Ended")
        dbcon.close()

    def particular_student_report():
        dbcon=pymysql.connect(host="localhost",user="root",passwd="mydatabase",database="STUDENTS")
        cur=dbcon.cursor()
        var1=int(input("Enter ID of student: "))
        var2=input("Enter the ID for the test:")
        Q=f"SELECT * FROM student_data_{var2} where STID={var1};"
        cur.execute(Q)
        a=cur.fetchall()
        for i in a:
            print(i,end=" ")
        dbcon.close()
    def sectionwise_student_report():
        dbcon=pymysql.connect(host="localhost",user="root",passwd="mydatabase",database="STUDENTS")
        cur=dbcon.cursor()
        var1=input("Enter the Section of Class: ")
        var2=input("Enter the ID for the test:")
        Q=f"SELECT * FROM student_data_{var2} where SEC={var1};"
        cur.execute(Q)
        a=cur.fetchall()
        for i in a:
            print(i,end=" ")
        print("Records Ended")
        dbcon.close()
    def rankwise_student_report():
        dbcon=pymysql.connect(host="localhost",user="root",passwd="mydatabase",database="STUDENTS")
        cur=dbcon.cursor()
        var2=input("Enter the ID for the test:")
        Q=f"SELECT * FROM student_data_{var2} ORDER BY MARKS DESC;"
        cur.execute(Q)
        a=cur.fetchall()
        for i in a:
            print(i,end=" ")
        print("Records Ended")
        dbcon.close()
    print("Choose from the options given below :")
    print("1. Create Question Paper")
    print("2. Edit previous Question Papers")
    print("3. Show student Report")
    print("4. Sign Out")
    choice=int(input("Enter your choice: "))
    while True:
        if choice==1:
            create_question_paper()
        elif choice==2:
            edit_previous_question_paper()
        elif choice==3:
            show_student_report()
        else:
            print("Program successfully ended")
            sys.exit()
        print("Choose from the options given below :")
        print("1. Create Question Paper")
        print("2. Edit previous Question Papers")
        print("3. Show student Report")
        print("4. Sign Out")
        choice=int(input("Enter your next choice: "))

def Student(s1,s2,s3,s4):
    while True:
        print("Choose from the options given below :")
        print("1. See your personal info")
        print("2. Give Exam")
        print("3. See your Previous Exam Statistics")
        print("4. Sign Out")
        choice=int(input("Enter your choice : "))
        if choice==1:
            dbcon=pymysql.connect(host="localhost",user="root",passwd="mydatabase",database='students')
            cur=dbcon.cursor()
            Q=f"Select * from Student_PI where STID={s1};"
            cur.execute(Q)
            s11=cur.fetchall()
            print(s11)
            dbcon.close()

        elif choice==2:
            a18=input("Enter the Id for the test: ")
            f1=open(f"{a18}.txt","r")
            var4=f1.readlines()
            Questions=var4[:-1]
            anslist=var4[-1]
            anslist_org=[]
            for i in range(0,len(anslist)):
                try:
                    x=int(anslist[i])
                    anslist_org.append(x)
                except:
                    pass
            answers=[]
            for i in Questions:
                var7=i
                b=str(var7)
                var8=b.split("$")
                var11=""
                for i in var8:
                    if (i[-1]=="n") and (i[-2]=="\""):
                        var9=var8[:-2]
                    else:
                        var9=var8
                for j in var9:
                    print(j)
                a17=input('Enter correct option number: ')
                answers.append(int(a17))
            om=0
            tm=len(anslist_org)*4
            print(answers)
            print(anslist_org)
            for i in range(0,len(answers)):
                if answers[i]==anslist_org[i]:
                    om+=4
                elif answers[i]=="":
                    pass
                if answers[i]!=anslist_org[i]:
                    om-=1
            print(f"Marks obtained are {om}/{tm}")
            f1.close()

            dbcon=pymysql.connect(host="localhost",user="root",passwd="mydatabase",database='students')
            cur=dbcon.cursor()
            Q=f"insert into student_data_{a18} values({s1},'{s4}','{s3}','{s2}',{om});"
            cur.execute(Q)
            a21=a18[0:3]
            Q=f"update student_data_section_{s2} set {a18}={om} where stid={s1};"
            cur.execute(Q)
            dbcon.commit()
            dbcon.close()

        elif choice==3:
            try:
                dbcon=pymysql.connect(host="localhost",user="root",passwd="mydatabase",database='students')
                cur=dbcon.cursor()
                Q=f"Select * from student_data_section_{s2} where STID={s1};"
                cur.execute(Q)
                s14=cur.fetchall()
                print(s14)
                dbcon.close()
            except:
                print("No test given")
        else:
            print("Program Successfully closed")
            sys.exit()

def stdlog():
    dbcon=pymysql.connect(host="localhost",user="root",passwd="mydatabase",database='students')
    cur=dbcon.cursor()
    s1=int(input('Enter ID: '))
    pwd=int(input("Enter psswd: "))
    Q=f"select password from Student_PI where STID={s1};"
    cur.execute(Q)
    a=cur.fetchall()
    c=a[0][0]
    if c==pwd:
        print("Passoword is correct.")
        Q=f"select class,sec,name from student_pi where Stid={s1};"
        cur.execute(Q)
        a23=cur.fetchall()
        s2=a23[0][1]
        s3=a23[0][0]
        s4=a23[0][2]
        print(s1,s2,s3,s4)
        Student(s1,s2,s3,s4)
    else:
        print("Incorrect combination")
        sys.exit()
    dbcon.close()

def teclog():
    dbcon=pymysql.connect(host="localhost",user="root",passwd="mydatabase",database='teacher')
    cur=dbcon.cursor()
    x1=int(input('Enter ID: '))
    x2=int(input("Enter psswd: "))
    Q=f"select password from Teacher_PI where ID={x1};"
    cur.execute(Q)
    a=cur.fetchall()
    c=a[0][0]
    if c==x2:
        print("Passoword is correct.")
        Q=f"select teacher_pi.subject_name,que_no,subject_code from teacher_pi,subject_codes where teacher_pi.subject_name=subject_codes.subject_name and teacher_pi.id={x1};"
        cur.execute(Q)
        a12=cur.fetchall()
        x3=a12[0][2]
        x4=a12[0][1]
        x5=a12[0][0]
        teacher(x1,x2,x3,x4,x5)
    else:
        print("Incorrect combination")
        sys.exit()
    dbcon.close()


def main():
    print("You are\n 1. A Teacher\n 2. A Student")
    z=int(input("Enter option [1 or 2]: "))
    if z==1:
        teclog()
    elif z==2:
        stdlog()
    else:
        print("program terminated")
main()
