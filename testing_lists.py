"""testing_things = ['apple', 'banana', 'cherry']


option = input ("enter in a fruit: ")
option2 = input ("second fruit choice: ")
testing_things.append(option)   #adds one thing
testing_things.insert(option, option2)    # adds multiple things
testing_things.extend(2, option)    #adds something in a specific position"""


#modulas %2 give the remander of stuff if zero than its even of zero
filtered = []
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers:
    if i % 2 is 0:
        filtered.append(i)

print(filtered)

filtered_names = []
names = ["Alex", "Alexandra", "Ben", "Benjamin", "Cat", "Catherine", "Dan"]

for o in names:
    for len in o:
        if o >= 5:
            filtered_names.append(o)
print(filtered_names)

