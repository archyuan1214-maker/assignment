"""
Questionnaire: For what purposes did you use Generative AI / LLMs when completing your assignment?
[] Not at all
[] Which ones did you use? (e.g., ChatGPT, Bard, etc.) _____________
[] Explaining programming concepts
[] Practicing coding exercises
[] Debugging code
[] Reviewing your Python code
[] Optimizing code
[] Writing or completing code
[] Other (please specify): _____________

"""  



"""
Imagine you are developing an interactive python program for managing the students of your class.
Your task is to create a Python program that interacts with the user to collect and analyze data.
The program should perform the following tasks:

  
    1. Create an empty dictionary called student_data. Add Information of 10 current ITECK studdents. Each key will be the student's name. Each value will be another dictionary with "age" and "country".

    2.Collect student information manually. Ask the user to enter information for 2 additional students. For each student: Prompt for name, age, and country. Store the information in student_data using the student’s name as the key.
    Allow the user to skip a student by pressing Enter for the name.
    
    3. Calculate the average age of the students. Create a list of ages manually using the dictionary values. Use sum() and len() to calculate the average. Print the average age.
    
    4. Create a set called students_countries to store unique countries.

    7. Create a list called young_students that includes the names of students who are younger than the average age. Print the list of young students.

    8 .Print out the list of young students and the set of unique countries.
    
    9. 
    Extra Challenges (Optional):
    Calculate and print the total number of students. Calculate and print the percentage of students under the average age.


Deliverables:

Submission on Github
Upload on ILIAS

"""
student_data = {}
student_data["Rosa"] = {"age": 22, "country": "Cambodia"}
student_data["Andrea"] = {"age": 24, "country": "Italy"}
student_data["Clara"] = {"age": 25, "country": "Italy"}
student_data["Steffin"] = {"age": 27, "country": "France"}
student_data["Mattias"] = {"age": 22, "country": "Germany"}

A_name=input("Enter the name of the first student:")
A_age=int(input("Enter the age of the first student:"))
A_country=input("Enter the country of the first student:")
student_data[A_name] = {"age": A_age, "country": A_country}

B_name=input("Enter the name of the second student:")
B_age=int(input("Enter the age of the second student:"))
B_country=input("Enter the country of the second student:")
student_data[B_name] = {"age": B_age, "country": B_country}

Student_age=[student_data["Rosa"]["age"],
             student_data["Andrea"]["age"],
             student_data["Clara"]["age"],
             student_data["Steffin"]["age"],
             student_data["Mattias"]["age"],
             student_data[A_name]["age"],
             student_data[B_name]["age"]]

total_age=sum(Student_age)
student_number=len(Student_age)
Student_ave_age=total_age/student_number
print("The average age of the students is:"+str(Student_ave_age))


students_countries={student_data["Rosa"]["country"],
             student_data["Andrea"]["country"],
             student_data["Clara"]["country"],
             student_data["Steffin"]["country"],
             student_data["Mattias"]["country"],
             student_data[A_name]["country"],
             student_data[B_name]["country"]}


young_students=[]
if student_data["Rosa"]["age"]<Student_ave_age:
    young_students.append("Rosa")
if student_data["Andrea"]["age"]<Student_ave_age:
    young_students.append("Andrea")
if student_data["Clara"]["age"]<Student_ave_age:
    young_students.append("Clara")
if student_data["Steffin"]["age"]<Student_ave_age:
    young_students.append("Steffin")
if student_data["Mattias"]["age"]<Student_ave_age:
    young_students.append("Mattias")
if student_data[A_name]["age"]<Student_ave_age:
    young_students.append(A_name)
if student_data[B_name]["age"]<Student_ave_age:
    young_students.append(B_name)

print("The young students are:",young_students)
print("Those students are from these countries:",students_countries)  #可以不加str用，分割

