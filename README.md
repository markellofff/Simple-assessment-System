# Simple-assessment-System
For internship in GreyNodes


Task
In this assignment, you are required to develop a simple Assessment Management System. The system allows a user to add, search and delete the details of students and assignments. The main program should first display a menu as follows. A user needs to select an operation from the main menu.
=======================================================
Welcome to the Student and Assessment Management System
<A>add details of a student.
<I>insert assignment marks of a student
<S>search assessment marks for a student.
<Q>quit.
=======================================================
Please select an option from the above:
If a user chooses the option <A> the program then asks them to enter a student ID, name, and course one by one. Once all details for a student are entered it will display the student ID, name, and course. Then the details of the student are added to the end of the students.txt file. Note that the student ID should not be the same as those already exist in the txt file and the format of the newly added record should be consistent with that of existing records.
Once the new record has been added, the system will then ask the user 'Do you want to enter details for another student (Y/N)?' 
•	If they enter 'Y', the system will allow them to enter details for another student as before.
•	If they enter 'N', the system will display the main menu again, otherwise, it will ask the same question again.
A typical example of the display of the program (once a user chooses the option <A>) can be as follows. Your program MUST follow the same display style.
Please enter the student ID: 11561234
Please enter the student name: Alan Parker
Please enter the course: MIT12
 
Thank You!
The details of the student you entered are as follows:
Student ID: 11561234
Student name: Alan Parker
Please enter the course: MIT12
 
The record has been successfully added to the students.txt file.
Do you want to enter details for another student (Y/N)? N
 =================================================================
 Welcome to the Student and Assessment Management System
 <A>add details of a student.
<I>insert assignment marks of a student
<S>search assessment marks for a student.
<Q>quit.
=================================================================
Please select an option from the above:
After the operation, the students.txt file will have the following content after the details of Alan Parker are entered.
 
If a user chooses the option <I> the program then asks them to enter a student ID, subject code, assessment number and marks one by one. Once all details for a student are entered it will display the student ID, subject code, assessment number and marks. Then the details of the assessment marks are added to the end of the assessments.txt file. Note that an assessment marks the record for a student should not be added if it already exists in the assessments.txt file and the format of the newly added record should be consistent with that of existing records.
Once the new record has been added, the system will then ask the user 'Do you want to enter marks for another assessment (Y/N)?' 
•	If they enter 'Y' the system will allow them to enter marks for another assessment as before. 
•	If they enter 'N' the system will display the main menu again, otherwise, it will ask the same question again.

A typical example of the display of the program (once a user chooses the option <A>) can be as follows. Your program MUST follow the same display style.
Please enter the student ID: 11561234
Please enter the subject code: ITC558
Please enter the assessment number: 1
Please enter assessment marks: 95
Thank You!
The details of the student you entered are as follows:
Student ID: 11561234
Subject code: ITC558
Assessment number: 1
Assessment marks: 95

The record has been successfully added to the assessments.txt file.
Do you want to enter marks for another assessment (Y/N)? N
 =================================================================
Welcome to the Student and Assessment Management System
 <A>add details of a student.
<I>insert assignment marks of a student
<S>search assessment marks for a student.
<Q>quit.
 =================================================================
Please select an option from the above:
After the operation, the assessments.txt file will have the following content after the marks of ITC558 of 11561234 are entered.
 
If a user chooses the option <S> from the main menu then the program asks the user to enter the student ID for whom they want to see details. To facilitate the search option you need to use an appropriate data structure such as List or Dictionary. The program then collects the student details from the students.txt file and assessment marks for that student from the assessments.txt file and displays them as follows (assuming the following student was searched for).
Please enter the student ID you want to search assessment marks for: 11561234
Thank You!
A student has been found:
Student ID: 11561234
Student name: Alan Parker
Course: MIT12

Subject Code    Assessment Number     Marks
ITC558              1                                    95

Do you want to search assessment marks for another student (Y/N)? N
Note: if more assessment marks are found for different subjects of the same student, they should be displayed one by one. 
After displaying the assessment marks the program prompts the user with the following message, 'Do you want to search assessment marks for another student (Y/N)?' 
•	If a user enters 'Y' then the program asks them to enter the student ID for whom the assessment marks need to be searched and displayed.
•	If the user enters 'N' then the program displays the main menu, otherwise, the program prompts the same message again.

Finally, the program quits if the user chooses the option <Q>.
Your program should be able to handle invalid inputs such as not-a-number or negative ages, heights and weights. 
You need to develop the system by completing the following three tasks:
Task 1 -
Draw flowchart/s that present the steps of the algorithm required to perform the task specified.
Task 2 -
Select six sets of test data that will demonstrate the 'normal' operation of your program; that is, test data that will demonstrate what happens when a VALID input is entered. Select three sets of test data that will demonstrate the 'abnormal' operation of your program. Note that all the three features: Add, Insert and Search should be tested.
Set it out in a tabular form as follows: test data type, test data, the reason it was selected, the output expected due to using the test data, and finally the output actually observed when the test data is used. It is important that the output listings (i.e., screenshots) are not edited in any way.
Test Data Table
Test data type	Test data	The reason it was selected	The output expected due to the use of the test data	The screenshot of the actual output when the test data are used
				
				
Task 3 -
Implement your algorithm in Python. Comment on your code as necessary to explain it clearly.
In addition, for this exercise, use multiple functions, instead of using a single function to do everything. Create a good design of the functions to make the best use of the code and avoid duplicate calculations. For example, you can have a function for calculating the weighted mark of an assignment and the function can be used for calculating all weighted marks. Avoid duplicate code.
You also need to design your program so that it has components that can be reused in another program if needed. Handle exceptions appropriately. Use appropriate data structure.
Run your program using the test data you have selected and complete the test data table above.
Your submission will consist of:
1.	Your algorithm through flowchart/s.
2.	The table recording your chosen test data and results (it can be in a Word or PDF file)
3.	Source code for your Python implementation
4.	Use functions and list for write the program.
Rationale
This assessment task will assess the following learning outcome/s:
•	be able to analyse the steps involved in a disciplined approach to problem-solving, algorithm development and coding.
•	be able to demonstrate and explain elements of good programming style.
•	be able to identify, isolate and correct errors; and evaluate the corrections in all phases of the programming process.
•	be able to interpret and implement algorithms and program code.
•	be able to apply sound program analysis, design, coding, debugging, testing and documentation techniques to simple programming problems.
•	be able to write code in an appropriate coding language.

 
