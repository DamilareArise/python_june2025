# types mode
# r -> read only
# w -> write only
# x -> create
# t -> text
# b -> byte
# a -> append
# try:
#     file = open(r'C:\python_june\ussd_pro.py')
#     print(file.read())
#     # print(file.read(500))
#     # print(file.readline(500))
#     # print(file.readlines())
#     file.close()
#     # print(file.read())  # this will throw an error because the file is already closed
    
# except Exception as e:
#     print(e)

# with open(r'C:\python_june\ussd_pro.py', 'r') as file:
    # print(file.read())
    

    
# print(file.read())

with open(r"C:\Users\Welcome\OneDrive\Desktop\page11.pdf", 'w') as file:
    file.write('Hellooo...\n')
    
# with open('page1.txt', 'a') as file:
#     file.write('Hellooo...\n')

# with open('page1.pdf', 'x') as file:
#     file.write('Hellooo...\n')

import os 

# os.mkdir('new_folder')
# os.rmdir('config')
# os.remove('page1.txt')

# print(os.path.exists(r'C:\Users\Welcome\OneDrive\Desktop\page11.pdf'))


# with open('president_height.csv') as file:
#     data = file.readlines()
#     data.pop(0)
#     # print(data)
    
#     names = []
#     heights = []
#     for line in data:
#         # print(line)
#         splitted = line.split(',')
#         names.append(splitted[1])
        
#         height = int(splitted[2].strip('\n'))
        
#         heights.append(height)

#     print(names)
#     print(heights)
#     # for name, height in zip(names, heights):
#     #     query = "INSERT INTO president_height (name, height) VALUES (%s, %s);"
#     #     value = (name, height)
        






# JSON -> javascripts object notation
import json
# students = [
#     {"name": "John", "age": 20},
#     {"name": "Alice", "age": 22},
#     {"name": "Bob", "age": 21}
# ]
# print(type(names))
# json_names = json.dumps(names)
# print(type(json_names))
# print(json_names[0])

# names = json.loads(json_names)
# print(type(names))


# with open('db.json', 'w') as file:
#     json_names = json.dumps(students)
#     file.write(json_names)

# with open("db.json") as file:
#     data = file.read()
#     data = json.loads(data)
#     print(data[0])