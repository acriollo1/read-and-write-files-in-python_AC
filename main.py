# remember to fork this and push to github

# f = open('text.txt', 'r')
# print(f.readlines())
# f.close() 

# with open('text.txt', 'r') as f:
#   f_contents = f.readlines()
#   print(f_contents, end='')

#READING FILES
# employee_file = open("employees.txt", "r")
# # print(employee_file.read())
# # print(employee_file.readlines())
# # print(employee_file.readable())

# # print(employee_file.readline())
# # print(employee_file.readline())
# # print(employee_file.readline())

# # print(employee_file.readlines()[1])

# for employee in employee_file.readlines():
#   print(employee)
# employee_file.close()

#WRITING FILES
# employee_file = open("employees.txt", "a")
# employee_file.write("\nToby - Human Resources")
# employee_file.close()

# employee_file = open("employees.txt", "w")
# employee_file.write("\nToby - Human Resources")
# employee_file.close()


# with open('readme.txt', 'w') as f:
#   f.write('readme')

# #this overwrites the original content
# with open('readme.txt', 'w') as f:
#   f.write('i dont care')

# #this appends to the original content
# with open('readme.txt', 'a') as f:
#   f.write('\ni dont care 3xxx')

#Practice

# with open('practice.txt', 'w') as f:
#   f.write('')

with open('practice.txt', 'a') as f:
  f.write(input('Enter anything you want:'))