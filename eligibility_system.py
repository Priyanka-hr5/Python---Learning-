# # ASSIGNMENT: Student Scholarship & Placement Eligibility System

# Developed using Python
# A student’s scholarship, placement eligibility, and bonus benefits depend on several conditions.
name=input("Enter student name:")
Age = int(input("Enter your age: "))
Marks = int(input("Enter your marks (0-100): "))
Attendance = float(input("Enter your attendance %: "))

Project_Completion = input("Has Completed Project? (yes/no): ").lower()
Python_Skill = input("Knows Python? (yes/no): ").lower()
SQL_Skill = input("Knows SQL? (yes/no): ").lower()

print("\n----Evaluation Result----")


# # Rules:
# Step 1 - Basic Eligibility
print("welcome",name)
if Age >= 18 and Age <= 30 and Attendance >= 85:
    print("You are eligible for evaluation")


    # Step 2 - Scholarship Logic

    if Marks >= 85:
        print("Scholarship: Full Scholarship")
    elif Marks >= 70 and Marks < 85:
        print("Scholarship: Partial Scholarship")
    else:
        print("Scholarship: No Scholarship")


    # Step 3 - Placement Eligibility

    if Project_Completion == "yes":
        print("Placement: You are eligible for placement")
        if Python_Skill == "yes" and SQL_Skill == "yes":
            print("Placement Category 1 : You are eligible for premium placement companies.")
        elif Python_Skill == "yes" or SQL_Skill == "yes":
            print("Placement category 2: You are eligible for standard placement companies.")
        else: 
            print("Placement: Not Eligible - (No Technical Skills)")
    else:
        print("Placement: You are not eligible for placement - (Project Not Completed)")


    # Step 4 - Special Bonus

    if Marks >= 90 and Attendance >= 90 and Project_Completion == "yes":
        print("You also get a performance excellence bonus")
else:
    print("You are not eligible for evaluation")





