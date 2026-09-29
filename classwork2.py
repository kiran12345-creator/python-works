student_grades={'Alice':98,'Bob':85,'Charlie':74,'Mike':70}\

print("grade of charlie is", student_grades['Charlie'])
student_grades["Bob"]=90         #changing bobs marks to 90
student_grades["Sam"]=75         #adding a new key and value
print(len(student_grades))       #returning how many students

#----------------------------------------------------------------------------------#
student_marks={'Arun':{'maths':30,'science':35,'english':40,'history':33},
               'Amal':{'maths':40,'science':45,'english':48,'history':43},
               'Anu':{'maths':45,'science':46,'english':47,'history':49}}

print(student_marks["Amal"]["history"])  #returning amal's history mark
student_marks["Arun"]["maths"]=35        # changing arun's math mark to 35
print(student_marks.values())            # returning marks of all students