# Python dictionary
# Dictionaries have a key and a value pair. The key is unique and the value can be any data type.

student_grades = {
    "John": 85,
    "Jane": 90,
    "Bob": 92
}

print(student_grades) # prints the entire dictionary
print(student_grades["John"]) # prints the value associated with the key "John"
print(student_grades["Jane"]) # prints the value associated with the key "Jane"
print(student_grades["Bob"]) # prints the value associated with the key "Bob"

# Assign a key to a variable and use it to access the value
student_1 = "John"
print(f"Grade for {student_1}: {student_grades[student_1]}") # prints the grade for John
student_2 = "Jane"
print(f"Grade for {student_2}: {student_grades[student_2]}") # prints the grade for Jane
student_3 = "Bob"
print(f"Grade for {student_3}: {student_grades[student_3]}") # prints the grade for Bob

#! What if I have 1000 key:value pairs?

#? Loop is coming up in a very soon lesson

honor_roll_student = student_grades.get("Jane") # assign the value of Jane's grade to a variable
print(f"Honor roll student: {honor_roll_student}") # type: ignore

# Update the value of John's grade
student_grades["John"] = 95 # Updates the value of John's grade to 95
print(f"Updated grade for John: {student_grades['John']}") # prints the updated grade for John

# Delete with pop() method
student_grades.pop("Bob") # Deletes the key "Bob" and its associated value
print(f"Grade for Bob: {student_grades.get('Bob', 'Student not found')}")

# Check for a student in the dictionary
if "Jane" in student_grades:
    print(f"Jane's grade is: {student_grades['Jane']}")
else:
    print("Jane is not in the dictionary")

    #? You can loop through the dictionary to print all key:value pairs. This will be covered 