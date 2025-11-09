"""
Questionnaire: For what purposes did you use Generative AI / LLMs when completing your assignment?
[] Not at all
[] Which ones did you use? (e.g., ChatGPT, Bard, etc.) ______chatGPT_______
[1] Explaining programming concepts
[1] Practicing coding exercises
[] Debugging code
[] Reviewing your Python code
[] Optimizing code
[] Writing or completing code
[] Other (please specify): _____________

"""  


"""
Assignment 3: Building Information Modeling (BIM) Tool

Think of an inspiring building, pavilion, or structure that you would like to explore more.

Imagine you are developing a Building Information Modeling (BIM) Tool that stores information about different building elements of your chosen building inspiration.
Your task is to create a Python program that interacts with the user to collect and analyze data using dictionaries, loops, built-in functions, user-defined functions (UDFs), and lambda functions.
The program should perform the following tasks:


1. Create a dictionary called building_elements that will store information about various building elements.
Each element should be identified by a unique key (e.g., a string or integer).
The value associated with each key should be another dictionary containing information such as the following:

key: The unique key for the element. (e.g. InW.01.23)
type: The type of the building element (e.g., "wall," "window," "door," etc.).
room: The name of the room assigned to the element (e.g., "living room," "staircase," etc.).
length: The length of the element in meters.
height: The height of the element in meters.
thickness: The width of the element in meters.
or other

2. Create a function called add_element that allows users to add a new building element to the building_elements dictionary.
This function should contained the previous parameters you defined:

3. Use lambda functions for calculate_area and calculate_volume.

4. Create a function called get_elements_by_type to list elements of a chosen type (e.g., "wall," "window," "door").

5. Use built-in functions like sum(), max(), or len() to summarize data.

6. Include a menu loop allowing users to repeatedly perform actions until they choose to exit.
"""



# 1. Create a dictionary called building_elements that will store information about various building elements.
# Each element should be identified by a unique key (e.g., a string or integer).
# The value associated with each key should be another dictionary containing information such as the following: 

# building_elements={}
# A1={"type":"wall", "room":"livin room","length":1.2,"height":1.5,"thickness":0.3}
# building_elements["A1"]=A1
# print(building_elements)

building_elements={}
building_elements["W1"]={"type":"wall","room":"living room","length":3.5,"height":3.3,"thickness":0.3}
building_elements["W2"]={"type":"wall","room":"bed room","length":4,"height":3.3,"thickness":0.2}
building_elements["Wi1"]={"type":"window","room":"bed room","length":1.2,"height":1.5,"thickness":0.3}
building_elements["Wi2"]={"type":"window","room":"living room","length":1.5,"height":1.5,"thickness":0.3}
building_elements["D1"]={"type":"door","room":"bed room","length":0.9,"height":2.1,"thickness":0.3}
building_elements["D2"]={"type":"door","room":"living room","length":1.2,"height":2.1,"thickness":0.3}

# 2. Create a function called add_element that allows users to add a new building element to the building_elements dictionary.
# This function should contained the previous parameters you defined:

def AddElement():
    key=str(input("Please enter the unique key for the element:"))
    type=input("Please enter the type of the building element:")
    room=input("Please enter the room of the building element:")
    length=float(input("Please enter the length of the building element:"))
    height=float(input("Please enter the height of the building element:"))
    thickness=float(input("Please enter the thickness of the building element:"))

    building_elements[key]={"type":type,"room":room,"length":length,"height":height,"thickness":thickness}
        




# 3. Use lambda functions for calculate_area and calculate_volume.

calculate_area=lambda length,height:length*height
calculate_volume=lambda length,height,thickness:length*height*thickness

# 4. Create a function called get_elements_by_type to list elements of a chosen type (e.g., "wall," "window," "door").

# def GetElementsByType():
#     element_type_list=[]
#     element_type=input("please enter the type of building element you want to search for:")
    
#     while True:
    
#         if element_type in building_elements[key]["type"]:
#             for key in building_elements:
#                 if building_elements[key]["type"]==element_type:
#                     element_type_list.append(key)
#                     print(element_type_list,"are",element_type)
#             break

#         else:
#             print("No such element type.")
#             element_type=input("please enter again:")

def GetElementsByType():
    element_type_list=[]
    element_type=input("please enter the type of building element you want to search for:")
    type_list=[]
    for key in building_elements:
            type_list.append(building_elements[key]["type"])
    while True:
        if element_type in type_list:
            for key in building_elements:
                if building_elements[key]["type"]==element_type:
                   element_type_list.append(key)
            print(element_type_list,"are",element_type)    
            break         
        else:
            print("No such element type")
            element_type=input("Please enter again:")


#  5. Use built-in functions like sum(), max(), or len() to summarize data.

height_sum=sum(building_elements[key]["height"] for key in building_elements)
height_max=max(building_elements[key]["height"] for key in building_elements)
length_sum=sum(building_elements[key]["length"] for key in building_elements)
length_max=max(building_elements[key]["length"] for key in building_elements)
thickness_max=max(building_elements[key]["thickness"] for key in building_elements)

# 6. Include a menu loop allowing users to repeatedly perform actions until they choose to exit.
while True:
    if input("Add a new element?Yes or Exit?")=="Exit":
        break
    else:
        AddElement()


for key in building_elements:
    area=calculate_area(building_elements[key]["length"],building_elements[key]["height"])
    volume=calculate_volume(building_elements[key]["length"],building_elements[key]["height"],building_elements[key]["thickness"])
    print("for",key,":","area is",area,"volume is",volume)

while True:
    if input("Want to find a type of element?Yes or Exit?")=="Exit":
        break
    else:
        GetElementsByType()
    
print("The total height of all elements is:",height_sum,"\n"
      "The total length of all elements is:",length_sum,"\n"
      "The max height of all elements is:",height_max,"\n"
      "The max length of all elements is:",length_max,"\n"
      "The max thickness of all elements is:",thickness_max)