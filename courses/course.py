# Let the user enter the number of courses
num_courses = int(input("How many courses do you have in this semester? "))
while True:
    if (num_courses <0):
     print("Invalid course number! Please enter a valid grade between 0 and 100.")
     num_courses = int(input("How many courses do you have in this semester? "))
    else:
        # Calculate and print the average GPA
        total_gpa = 0

        for i in range(num_courses):
                print(i)
                try:
                    grade = float(input(f"What is your grade(in 100) for course {i + 1}?: "))
                    while grade > 100 or grade < 0:
                        print("Invalid grade! Please enter a valid grade between 0 and 100.")
                        grade = float(input(f"What is your grade(in 100) for course {i + 1}?: "))
                    if grade >= 90:
                     total_gpa += 4
                    elif grade >= 80:
                     total_gpa += 3
                    elif grade >= 70:
                     total_gpa += 2
                    elif grade >= 60:
                     total_gpa += 1
                    else:
                     total_gpa += 0

                except ValueError:
                    print("Invalid input! Please enter a numeric value.")

        average_gpa = total_gpa / num_courses

        if type(average_gpa) == str:
            print(average_gpa)  # Print the error message for invalid grade
        else:
            print(f"Average GPA: {average_gpa:.2f}")
        break
