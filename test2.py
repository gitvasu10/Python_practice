#print("Kumud Malasi")
#-----------23/02/24----------------------
'''age = 24
name = "Shashwat"

print("My name is " +name +" and age is = "+age)'''

#--------------------------24/02/2024-----------------------------------

# behaviour of python lists while deleting the values from them

# testList = [1,2,3,4,5,6]
# for i in testList:
#     testList.remove(i)
# print(testList)

#Using enumerate() with lists
# testList = [1,2,3,4,5,6,7,8,9,0,9,9,7,10]
# for index, value in enumerate(testList):
#     print(f"Index = {index}, Value = {value}")

#--------------25/02/2024----------------------------------------

name = input("Enter the name: ")
substring = input("Which substring you want to search for: ")
count = 0
for i in range(len(name)-len(substring)+1):
    if(name[i:].startswith(substring)):
        count += 1
print(f"The count of {substring} in {name} is {count}")