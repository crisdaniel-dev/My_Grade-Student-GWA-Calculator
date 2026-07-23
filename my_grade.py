print("\n[ My_Grade | Created by: Crisdaniel M. Inot ]\n")
print("________________________________")
print("|                               |")
print("| Choose your desired option:   |")
print("| 1 - View my Subjects/Courses  |")
print("| 2 - Calculate my average      |")
print("| 3 - None of the above         |")
print("|_______________________________|")

try:                                                                  #if input is string or empty the program stop
    choice = int(input("Enter your choice: "))
except ValueError:
    print("\nInvalid Input, Please Input a digit value\n")
    exit()

if choice < 1 or choice > 3:                                          #if input is < 1 or > 3, the program stop
    print("\nInvalid Input, Please Try Again!!\n")
    exit()
elif choice == 1:                                                     #if input is == 1, View the Subjects/Courses
    print("_______________________")
    print("|                      |")
    print("|     College Year     |")
    print("|     1 - 1st Year     |")
    print("|     2 - 2nd Year     |")
    print("|     3 - 3rd Year     |")
    print("|     4 - 4th Year     |")
    print("|______________________|")

    try:
        college_year = int(input("Enter here: "))
    except ValueError:
        print("\nInvalid Input, Please Try Again!!\n")
        exit()

    if college_year < 1 or college_year > 4:
        print("\nInvalid input try again!\n")
        exit()
    elif college_year == 1:                        #1st Year Subject/Course
        print("_____________________")
        print("|                   |")
        print("|  Which Semester?  |")
        print("| 1 - 1st Semester  |")
        print("| 2 - 2nd Semester  |")
        print("|___________________|")
        try:
            semester = int(input("Enter here: "))
        except ValueError:
            print("\nInvalid Input, Please Try Again!!\n")
            exit()

        if semester == 1:
            print("\n[1st Year, First Semester]")
            print("__________________________________________________________________")
            print("|                |                                      |         |")
            print("| Course Code    |         Descriptive Title            |  Units  |")
            print("|________________|______________________________________|_________|")
            print("| GEC-RPF        | Readings in Philippine History       |    3    |")
            print("| GEC-MMW        | Mathematics in the Modern World      |    3    |")
            print("| GEC-TEM        | The Entrepreneurial Mind             |    3    |")
            print("| CC 111         | Introduction to Computing            |    3    |")
            print("| CC 112         | Computer Programming 1 (Lec)         |    2    |")
            print("| CC 112 L       | Computer Programming 1 (Lab)         |    3    |")
            print("| PE 1           | Physical Education 1                 |    2    |")
            print("| NSTP 1         | National Service Training Program 1  |    3    |")
            print("|_________________________________________________________________|")
            print("| Total Units:                                              22    |")
            print("|_________________________________________________________________|")
        elif semester == 2:
            print("\n[1st Year, Second Semester]")
            print("__________________________________________________________________")
            print("|                |                                      |         |")
            print("| Course Code    |         Descriptive Title            |  Units  |")
            print("|________________|______________________________________|_________|")
            print("| GEC-PC         | Purposive Communication              |    3    |")
            print("| GEC-STS        | Science, Technology and Society      |    3    |")
            print("| GEC-US         | Understanding the Self               |    3    |")
            print("| CC 123         | Computer Programming 2 (Lec)         |    2    |")
            print("| CC 123 L       | Computer Programming 2 (Lab)         |    3    |")
            print("| PC 121         | Fundamentals of Information Systems  |    3    |")
            print("| PC 122         | Organization and Management Concepts |    3    |")
            print("| PE 2           | Physical Education 2                 |    2    |")
            print("| NSTP 2         | National Service Training Program 2  |    3    |")
            print("|_________________________________________________________________|")
            print("| Total Units:                                              25    |")
            print("|_________________________________________________________________|")
        

    elif college_year == 2:                       #2nd Year Subject/Course
        print("_____________________")
        print("|                   |")
        print("|  Which Semester?  |")
        print("| 1 - 1st Semester  |")
        print("| 2 - 2nd Semester  |")
        print("|___________________|")
        try:
            semester = int(input("Enter here: "))
        except ValueError:
            print("\nInvalid Input, Please Try Again!!\n")
            exit()

        if semester == 1:
            print("\n[2nd Year, First Semester]")
            print("________________________________________________________________________")
            print("|                |                                            |         |")
            print("| Course Code    |         Descriptive Title                  |  Units  |")
            print("|________________|____________________________________________|_________|")
            print("| GEC-E          | Ethics                                     |    3    |")
            print("| GEE-ES         | Environmental Science                      |    3    |")
            print("| GEC-LWR        | Life and Works of Rizal                    |    3    |")
            print("| CC 214         | Data Structures and Algorithms (LEC)       |    2    |")
            print("| CC 214 L       | Data Structures and Algorithms (LAB)       |    3    |")
            print("| PC 213         | Professional Issues in Information Systems |    3    |")
            print("| PC 214         | Financial Management                       |    3    |")
            print("| AP 1           | Computer Architecture and Organization     |    3    |")
            print("| PE 3           | Physical Education 3                       |    2    |")
            print("|_______________________________________________________________________|")
            print("| Total Units:                                                    25    |")
            print("|_______________________________________________________________________|")
        elif semester == 2:
            print("\n[2nd Year, Second Semester]")
            print("________________________________________________________________________")
            print("|                |                                            |         |")
            print("| Course Code    |         Descriptive Title                  |  Units  |")
            print("|________________|____________________________________________|_________|")
            print("| GEC-TCW        | The Contemporary World                     |    3    |")
            print("| GEE-GSPS       | Gender and Society with Peace Studies      |    3    |")
            print("| GEE-PEE        | People and the Earth's Ecosystems          |    3    |")
            print("| CC 225         | Information Management (Lec)               |    2    |")
            print("| CC 225 L       | Information Management (Lab)               |    3    |")
            print("| PC 225         | IT Infrastructure and Network Technologies |    3    |")
            print("| PC 226         | Business Process Management                |    3    |")
            print("| AP 2           | Web I: Client Development                  |    3    |")
            print("| PE 4           | Physical Education 4                       |    2    |")
            print("|_______________________________________________________________________|")
            print("| Total Units:                                                    25    |")
            print("|_______________________________________________________________________|")
       

    elif college_year == 3:                        #3rd Year Subject/Course
        print("_____________________")
        print("|                   |")
        print("|  Which Semester?  |")
        print("| 1 - 1st Semester  |")
        print("| 2 - 2nd Semester  |")
        print("|___________________|")
        try:
            semester = int(input("Enter here: "))
        except ValueError:
            print("\nInvalid Input, Please Try Again!!\n")
            exit()

        if semester == 1:
            print("\n[3rd Year, First Semester]")
            print("__________________________________________________________________")
            print("|                |                                      |         |")
            print("| Course Code    |         Descriptive Title            |  Units  |")
            print("|________________|______________________________________|_________|")
            print("| PC 317         | System Analysis and Design(Lec)      |    2    |")
            print("| PC 317 I       | System Analysis and Design(Lab)      |    3    |")
            print("| PC 318         | Enterprise Architecture              |    3    |")
            print("| PC 319         | Evaluation of Business Performance   |    3    |")
            print("| PC 3110        | Quantitative Methods                 |    3    |")
            print("| AP 3           | Web II: Web Application Development  |    3    |")
            print("| AP 4           | Database Administration DBMS         |    3    |")
            print("|_________________________________________________________________|")
            print("| Total Units:                                              20    |")
            print("|_________________________________________________________________|")
        elif semester == 2:
            print("\n[3rd Year, Second Semester]")
            print("_______________________________________________________________________________")
            print("|                |                                                   |         |")
            print("| Course Code    |         Descriptive Title                         |  Units  |")
            print("|________________|___________________________________________________|_________|")
            print("| GEC-AA         | Art Appreciation                                  |    3    |")
            print("| PC 3211        | IS Project Management 1                           |    3    |")
            print("| PC 32112       | Capstone Project 1                                |    3    |")
            print("| P Elec 1       | Data Mining                                       |    3    |")
            print("| P Elec 2       | Customer Relationship Management                  |    3    |")
            print("| CC 326         | Application Development and Emerging Technologies |    3    |")
            print("| AP 5           | Foundations of Software Engineering               |    3    |")
            print("| AP 6           | System Administration and Maintenance             |    3    |")
            print("|______________________________________________________________________________|")
            print("| Total Units:                                                           24    |")
            print("|______________________________________________________________________________|")
        

    elif college_year == 4:                        #4th Year Subject/Course
        print("_____________________")
        print("|                   |")
        print("|  Which Semester?  |")
        print("| 1 - 1st Semester  |")
        print("| 2 - 2nd Semester  |")
        print("|___________________|")
        try:
            semester = int(input("Enter here: "))
        except ValueError:
            print("\nInvalid Input, Please Try Again!!\n")
            exit()

        if semester == 1:
            print("\n[4th Year, First Semester]")
            print("____________________________________________________________________")
            print("|                |                                        |         |")
            print("| Course Code    |         Descriptive Title              |  Units  |")
            print("|________________|________________________________________|_________|")
            print("| GEE-FE         | Functional English                     |    3    |")
            print("| PC 4113        | IS Strategy Management and Acquisition |    3    |")
            print("| PC 4114        | Capstone Project 2                     |    3    |")
            print("| P Elec 3       | Enterprise Systems                     |    3    |")
            print("| P Elec 4       | IT Audit and Controls                  |    3    |")
            print("|___________________________________________________________________|")
            print("| Total Units:                                                15    |")
            print("|___________________________________________________________________|")
        elif semester == 2:
            print("\n[4th Year, Second Semester]")
            print("__________________________________________________________________")
            print("|                |                                      |         |")
            print("| Course Code    |         Descriptive Title            |  Units  |")
            print("|________________|______________________________________|_________|")
            print("| PC 4215        | On-the-Job Training(OJT)             |    9    |")
            print("|_________________________________________________________________|")
            print("| Total Units:                                               9    |")
            print("|_________________________________________________________________|")
        

elif choice == 2:
    print("_______________________")
    print("|                      |")
    print("|     College Year     |")
    print("|     1 - 1st Year     |")
    print("|     2 - 2nd Year     |")
    print("|     3 - 3rd Year     |")
    print("|     4 - 4th Year     |")
    print("|______________________|")
    try:
        college_year = int(input("Enter here: "))
    except ValueError:
            print("\nInvalid Input, Please Try Again!!\n")
            exit()

    if college_year < 1 or college_year > 4:
        print("Invalid input try again!")
        exit()
    elif college_year == 1:                            #1st Year, Calculate General Average
        print("_____________________")
        print("|                   |")
        print("|  Which Semester?  |")
        print("| 1 - 1st Semester  |")
        print("| 2 - 2nd Semester  |")
        print("|___________________|")

        try:
            semester = int(input("Enter here: "))
        except ValueError:
            print("\nInvalid Input, Please Try Again!!\n")
            exit()

        if semester == 1:
            print("\n[1st Year, First Semester]")
            print("\nEnter your grade for each subject:")

            try:
                s1 = float(input("Readings in Philippine History(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()

            if s1 < 1.0 or s1 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try: 
                s2 = float(input("Mathematics in the Modern World(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s2 < 1.0 or s2 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s3 = float(input("The Entrepreneurial Mind(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s3 < 1.0 or s3 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s4 = float(input("Introduction to Computing(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s4 < 1.0 or s4 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s5 = float(input("Computer Programming 1 (Lec)(1-2): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s5 < 1.0 or s5 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s6 = float(input("Computer Programming 1 (Lab)(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s6 < 1.0 or s6 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s7 = float(input("Physical Education 1(1-2): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s7 < 1.0 or s7 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s8 = float(input("National Service Training Program 1(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s8 < 1.0 or s8 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            total = (s1*3) + (s2*3) + (s3*3) + (s4*3) + (s5*2) + (s6*3) + (s7*2) + (s8*3)
            average = total / 22
            if average == 1.0:
                remarks = "Excellent (highest)"
            elif average <= 2.5:
                remarks = "Passing"
            elif average <= 3.0:
                remarks = "Lowest passing"
            elif average <= 4.0:
                remarks = "Conditional / Incomplete (in some schools)"
            elif average <= 5.0:
                remarks = "Failed (lowest)"
            else:
                remarks = "GG"

            print("\n\n")
            print("=======================================================")
            print("                 GWA CALCULATOR RESULT                 ")
            print("=======================================================")
            print("\nYear Level : 1st Year")
            print("Semester   : First Semester")
            print("\n-------------------------------------------------------")
            print("Subject                                          Grade ")
            print("-------------------------------------------------------")
            print("Readings in Philippine History                    : " + str(s1))
            print("Mathematics in the Modern World                   : " + str(s2))
            print("The Entrepreneurial Mind                          : " + str(s3))
            print("Introduction to Computing                         : " + str(s4))
            print("Computer Programming 1 (Lec)                      : " + str(s5))
            print("Computer Programming 1 (Lab)                      : " + str(s6))
            print("Physical Education 1                              : " + str(s7))
            print("National Service Training Program 1               : " + str(s8))
            print("\n-------------------------------------------------------")
            print("Final Result")
            print("-------------------------------------------------------")
            print("GWA        : " + str(average))
            print("Remarks    : " + remarks)
            print("\n=======================================================")
            print("Created by: Crisdaniel M. Inot")
            print("=======================================================")

        elif semester == 2:
            print("\n[1st Year, Second Semester]")
            print("\nEnter your grade for each subject:")

            try:
                s1 = float(input("Purposive Communication(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s1 < 1.0 or s1 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s2 = float(input("Science, Technology and Society(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s2 < 1.0 or s2 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s3 = float(input("Understanding the Self(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s3 < 1.0 or s3 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s4 = float(input("Computer Programming 2 (Lec)(1-2): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s4 < 1.0 or s4 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s5 = float(input("Computer Programming 2 (Lab)(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s5 < 1.0 or s5 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s6 = float(input("Fundamentals of Informaton System(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s6 < 1.0 or s6 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s7 = float(input("Organization and Management Concepts(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s7 < 1.0 or s7 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s8 = float(input("Physical Education 2(1-2): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s8 < 1.0 or s8 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s9 = float(input("National Service Training Program 2(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s9 < 1.0 or s9 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            total = (s1*3) + (s2*3) + (s3*3) + (s4*2) + (s5*3) + (s6*3) + (s7*3) + (s8*2) + (s9*3)
            average = total / 25

            if average == 1.0:
                remarks = "Excellent (highest)"
            elif average <= 2.5:
                remarks = "Passing"
            elif average <= 3.0:
                remarks = "Lowest passing"
            elif average <= 4.0:
                remarks = "Conditional / Incomplete (in some schools)"
            elif average <= 5.0:
                remarks = "Failed (lowest)"
            else:
                remarks = "GG"

            print("\n\n")
            print("=======================================================")
            print("                 GWA CALCULATOR RESULT                 ")
            print("=======================================================")
            print("\nYear Level : 1st Year")
            print("Semester   : Second Semester")
            print("\n-------------------------------------------------------")
            print("Subject                                          Grade ")
            print("-------------------------------------------------------")
            print("Purposive Communication                           : " + str(s1))
            print("Science, Technology and Society                   : " + str(s2))
            print("Understanding the Self                            : " + str(s3))
            print("Computer Programming 2 (Lec)                      : " + str(s4))
            print("Computer Programming 2 (Lab)                      : " + str(s5))
            print("Fundamentals of Informaton System                 : " + str(s6))
            print("Organization and Management Concepts              : " + str(s7))
            print("Physical Education 2                              : " + str(s8))
            print("National Service Training Program 2               : " + str(s9))
            print("\n-------------------------------------------------------")
            print("Final Result")
            print("-------------------------------------------------------")
            print("GWA        : " + str(average))
            print("Remarks    : " + remarks)
            print("\n=======================================================")
            print("Created by: Crisdaniel M. Inot")
            print("=======================================================")


    elif college_year == 2:                            #2nd Year, Calculate General Average
        print("_____________________")
        print("|                   |")
        print("|  Which Semester?  |")
        print("| 1 - 1st Semester  |")
        print("| 2 - 2nd Semester  |")
        print("|___________________|")
        try:
            semester = int(input("Enter here: "))
        except ValueError:
            print("\nInvalid Input, Please Try Again!!\n")
            exit()

        if semester == 1:
            print("\n[2nd Year, First Semester]")
            print("\nEnter your grade for each subject:")

            try:
                s1 = float(input("Ethics(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s1 < 1.0 or s1 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s2 = float(input("Environmental Science(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s2 < 1.0 or s2 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s3 = float(input("Life and Works of Rizal(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s3 < 1.0 or s3 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s4 = float(input("Data Structures and Algorithms (LEC)(1-2): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s4 < 1.0 or s4 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s5 = float(input("Data Structures and Algorithms (LAB)(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s5 < 1.0 or s5 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s6 = float(input("Professional Issues in Information Systems(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s6 < 1.0 or s6 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s7 = float(input("Financial Management(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s7 < 1.0 or s7 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s8 = float(input("Computer Architecture and Organization(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s8 < 1.0 or s8 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s9 = float(input("Physical Education 3(1-2): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s9 < 1.0 or s9 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            total = (s1*3) + (s2*3) + (s3*3) + (s4*2) + (s5*3) + (s6*3) + (s7*3) + (s8*3) + (s9*2)
            average = total / 25

            if average == 1.0:
                remarks = "Excellent (highest)"
            elif average <= 2.5:
                remarks = "Passing"
            elif average <= 3.0:
                remarks = "Lowest passing"
            elif average <= 4.0:
                remarks = "Conditional / Incomplete (in some schools)"
            elif average <= 5.0:
                remarks = "Failed (lowest)"
            else:
                remarks = "GG"

            print("\n\n")
            print("=======================================================")
            print("                 GWA CALCULATOR RESULT                 ")
            print("=======================================================")
            print("\nYear Level : 2nd Year")
            print("Semester   : First Semester")
            print("\n-------------------------------------------------------")
            print("Subject                                          Grade ")
            print("-------------------------------------------------------")
            print("Ethics                                            : " + str(s1))
            print("Environmental Science                             : " + str(s2))
            print("Life and Works of Rizal                           : " + str(s3))
            print("Data Structures and Algorithms (LEC)              : " + str(s4))
            print("Data Structures and Algorithms (LAB)              : " + str(s5))
            print("Professional Issues in Information Systems        : " + str(s6))
            print("Financial Management                              : " + str(s7))
            print("Computer Architecture and Organization            : " + str(s8))
            print("Physical Education 3                              : " + str(s9))
            print("\n-------------------------------------------------------")
            print("Final Result")
            print("-------------------------------------------------------")
            print("GWA        : " + str(average))
            print("Remarks    : " + remarks)
            print("\n=======================================================")
            print("Created by: Crisdaniel M. Inot")
            print("=======================================================")
          
        elif semester == 2:
            print("\n[2nd Year, Second Semester]")
            print("\nEnter your grade for each subject:")

            try:
                s1 = float(input("The Contemporary World(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s1 < 1.0 or s1 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s2 = float(input("Gender and Society with Peace Studies(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s2 < 1.0 or s2 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()
                
            try:
                s3 = float(input("People and the Earth's Ecosystems(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s3 < 1.0 or s3 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s4 = float(input("Information Management (Lec)(1-2): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s4 < 1.0 or s4 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s5 = float(input("Information Management (Lab)(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s5 < 1.0 or s5 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s6 = float(input("IT Infrastructure and Network Technologies(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s6 < 1.0 or s6 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s7 = float(input("Business Process Management(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s7 < 1.0 or s7 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s8 = float(input("Web I Client Development(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s8 < 1.0 or s8 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s9 = float(input("Physical Education 4(1-2): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s9 < 1.0 or s9 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            total = (s1*3) + (s2*3) + (s3*3) + (s4*2) + (s5*3) + (s6*3) + (s7*3) + (s8*3) + (s9*2)
            average = total / 25

            if average == 1.0:
                remarks = "Excellent (highest)"
            elif average <= 2.5:
                remarks = "Passing"
            elif average <= 3.0:
                remarks = "Lowest passing"
            elif average <= 4.0:
                remarks = "Conditional / Incomplete (in some schools)"
            elif average <= 5.0:
                remarks = "Failed (lowest)"
            else:
                remarks = "GG"

            print("\n\n")
            print("=======================================================")
            print("                 GWA CALCULATOR RESULT                 ")
            print("=======================================================")
            print("\nYear Level : 2nd Year")
            print("Semester   : Second Semester")
            print("\n-------------------------------------------------------")
            print("Subject                                          Grade ")
            print("-------------------------------------------------------")
            print("The Contemporary World                            : " + str(s1))
            print("Gender and Society with Peace Studies             : " + str(s2))
            print("People and the Earth's Ecosystems                 : " + str(s3))
            print("Information Management (Lec)                      : " + str(s4))
            print("Information Management (Lab)                      : " + str(s5))
            print("IT Infrastructure and Network Technologies        : " + str(s6))
            print("Business Process Management                       : " + str(s7))
            print("Web I Client Development                          : " + str(s8))
            print("Physical Education 4                              : " + str(s9))
            print("\n-------------------------------------------------------")
            print("Final Result")
            print("-------------------------------------------------------")
            print("GWA        : " + str(average))
            print("Remarks    : " + remarks)
            print("\n=======================================================")
            print("Created by: Crisdaniel M. Inot")
            print("=======================================================")
 

    elif college_year == 3:                            #3rd Year, Calculate General Average
        print("_____________________")
        print("|                   |")
        print("|  Which Semester?  |")
        print("| 1 - 1st Semester  |")
        print("| 2 - 2nd Semester  |")
        print("|___________________|")
        try:
            semester = int(input("Enter here: "))
        except ValueError:
            print("\nInvalid Input, Please Try Again!!\n")
            exit()

        if semester == 1:
            print("\n[3rd Year, First Semester]")
            print("\nEnter your grade for each subject:")

            try:
                s1 = float(input("System Analysis and Design(Lec)(1-2): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s1 < 1.0 or s1 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s2 = float(input("System Analysis and Design(Lab)(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s2 < 1.0 or s2 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s3 = float(input("Enterprise Architecture(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s3 < 1.0 or s3 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s4 = float(input("Evaluation of Business Performance(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s4 < 1.0 or s4 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s5 = float(input("Quantitative Methods(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s5 < 1.0 or s5 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s6 = float(input("Web II: Web Application Development(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s6 < 1.0 or s6 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s7 = float(input("Database Administration DBMS(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s7 < 1.0 or s7 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            total = (s1*2) + (s2*3) + (s3*3) + (s4*3) + (s5*3) + (s6*3) + (s7*3)
            average = total / 20

            if average == 1.0:
                remarks = "Excellent (highest)"
            elif average <= 2.5:
                remarks = "Passing"
            elif average <= 3.0:
                remarks = "Lowest passing"
            elif average <= 4.0:
                remarks = "Conditional / Incomplete (in some schools)"
            elif average <= 5.0:
                remarks = "Failed (lowest)"
            else:
                remarks = "GG"

            print("\n\n")
            print("=======================================================")
            print("                 GWA CALCULATOR RESULT                 ")
            print("=======================================================")
            print("\nYear Level : 3rd Year")
            print("Semester   : First Semester")
            print("\n-------------------------------------------------------")
            print("Subject                                          Grade ")
            print("-------------------------------------------------------")
            print("System Analysis and Design(Lec)                   : " + str(s1))
            print("System Analysis and Design(Lab)                   : " + str(s2))
            print("Enterprise Architecture                           : " + str(s3))
            print("Evaluation of Business Performance                : " + str(s4))
            print("Quantitative Methods                              : " + str(s5))
            print("Web II: Web Application Development               : " + str(s6))
            print("Database Administration DBMS                      : " + str(s7))
            print("\n-------------------------------------------------------")
            print("Final Result")
            print("-------------------------------------------------------")
            print("GWA        : " + str(average))
            print("Remarks    : " + remarks)
            print("\n=======================================================")
            print("Created by: Crisdaniel M. Inot")
            print("=======================================================")
            
        elif semester == 2:
            print("\n[3rd Year, Second Semester]")
            print("\nEnter your grade for each subject:")

            try:
                s1 = float(input("Art Appreciation(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s1 < 1.0 or s1 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s2 = float(input("IS Project Management 1(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s2 < 1.0 or s2 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s3 = float(input("Capstone Project 1(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s3 < 1.0 or s3 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s4 = float(input("Data Mining(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s4 < 1.0 or s4 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s5 = float(input("Customer Relationship Management(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s5 < 1.0 or s5 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s6 = float(input("Application Development and Emerging Technologies(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s6 < 1.0 or s6 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s7 = float(input("Foundations of Software Engineering(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s7 < 1.0 or s7 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s8 = float(input("System Administration and Maintenance(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s8 < 1.0 or s8 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            total = (s1*3) + (s2*3) + (s3*3) + (s4*3) + (s5*3) + (s6*3) + (s7*3) + (s8*3)
            average = total / 24

            if average == 1.0:
                remarks = "Excellent (highest)"
            elif average <= 2.5:
                remarks = "Passing"
            elif average <= 3.0:
                remarks = "Lowest passing"
            elif average <= 4.0:
                remarks = "Conditional / Incomplete (in some schools)"
            elif average <= 5.0:
                remarks = "Failed (lowest)"
            else:
                remarks = "GG"

            print("\n\n")
            print("=======================================================")
            print("                 GWA CALCULATOR RESULT                 ")
            print("=======================================================")
            print("\nYear Level : 3rd Year")
            print("Semester   : Second Semester")
            print("\n-------------------------------------------------------")
            print("Subject                                          Grade ")
            print("-------------------------------------------------------")
            print("Art Appreciation                                  : " + str(s1))
            print("IS Project Management 1                           : " + str(s2))
            print("Capstone Project 1                                : " + str(s3))
            print("Data Mining                                       : " + str(s4))
            print("Customer Relationship Management                  : " + str(s5))
            print("Application Development and Emerging Technologies : " + str(s6))
            print("Foundations of Software Engineering               : " + str(s7))
            print("System Administration and Maintenance             : " + str(s8))
            print("\n-------------------------------------------------------")
            print("Final Result")
            print("-------------------------------------------------------")
            print("GWA        : " + str(average))
            print("Remarks    : " + remarks)
            print("\n=======================================================")
            print("Created by: Crisdaniel M. Inot")
            print("=======================================================")
    

    elif college_year == 4:                            #4th Year, Calculate General Average
        print("_____________________")
        print("|                   |")
        print("|  Which Semester?  |")
        print("| 1 - 1st Semester  |")
        print("| 2 - 2nd Semester  |")
        print("|___________________|")
        try:
            semester = int(input("Enter here: "))
        except ValueError:
            print("\nInvalid Input, Please Try Again!!\n")
            exit()

        if semester == 1:
            print("\n[4th Year, First Semester]")
            print("\nEnter your grade for each subject:")

            try:
                s1 = float(input("Functional English(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s1 < 1.0 or s1 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s2 = float(input("IS Strategy Management and Acquisition(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s2 < 1.0 or s2 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s3 = float(input("Capstone Project 2(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s3 < 1.0 or s3 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s4 = float(input("Enterprise Systems(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s4 < 1.0 or s4 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            try:
                s5 = float(input("IT Audit and Controls(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s5 < 1.0 or s5 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()

            total = (s1*3) + (s2*3) + (s3*3) + (s4*3) + (s5*3)
            average = total / 15

            if average == 1.0:
                remarks = "Excellent (highest)"
            elif average <= 2.5:
                remarks = "Passing"
            elif average <= 3.0:
                remarks = "Lowest passing"
            elif average <= 4.0:
                remarks = "Conditional / Incomplete (in some schools)"
            elif average <= 5.0:
                remarks = "Failed (lowest)"
            else:
                remarks = "GG"

            print("\n\n")
            print("=======================================================")
            print("                 GWA CALCULATOR RESULT                 ")
            print("=======================================================")
            print("\nYear Level : 4th Year")
            print("Semester   : First Semester")
            print("\n-------------------------------------------------------")
            print("Subject                                          Grade ")
            print("-------------------------------------------------------")
            print("Functional English                                : " + str(s1))
            print("IS Strategy Management and Acquisition            : " + str(s2))
            print("Capstone Project 2                                : " + str(s3))
            print("Enterprise Systems                                : " + str(s4))
            print("IT Audit and Controls                             : " + str(s5))
            print("\n-------------------------------------------------------")
            print("Final Result")
            print("-------------------------------------------------------")
            print("GWA        : " + str(average))
            print("Remarks    : " + remarks)
            print("\n=======================================================")
            print("Created by: Crisdaniel M. Inot")
            print("=======================================================")
            
        elif semester == 2:
            print("\n[4th Year, Second Semester]")
            print("\nEnter your grade for this subject:")

            try:
                s1 = float(input("On-the-Job Training(OJT)(1-3): "))
            except:
                print("\nInvalid Input!!! Please input a digit value only\n")
                exit()
            if s1 < 1.0 or s1 > 5.0:
                print("\nInvalid Input!!! Please input between (1.0 - 5.0)")
                exit()
        
            total = (s1*9)
            average = total / 9

            if average == 1.0:
                remarks = "Excellent (highest)"
            elif average <= 2.5:
                remarks = "Passing"
            elif average <= 3.0:
                remarks = "Lowest passing"
            elif average <= 4.0:
                remarks = "Conditional / Incomplete (in some schools)"
            elif average <= 5.0:
                remarks = "Failed (lowest)"
            else:
                remarks = "GG"

            print("\n\n")
            print("=======================================================")
            print("                 GWA CALCULATOR RESULT                 ")
            print("=======================================================")
            print("\nYear Level : 4th Year")
            print("Semester   : Second Semester")
            print("\n-------------------------------------------------------")
            print("Subject                                          Grade ")
            print("-------------------------------------------------------")
            print("On-the-Job Training(OJT)                          : " + str(s1))
            print("\n-------------------------------------------------------")
            print("Final Result")
            print("-------------------------------------------------------")
            print("GWA        : " + str(average))
            print("Remarks    : " + remarks)
            print("\n=======================================================")
            print("Created by: Crisdaniel M. Inot")
            print("=======================================================")
            
            
elif choice == 3:
    print("\nNone of the above")
