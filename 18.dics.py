# Creating a dictionary
student = {
    "name": "prince",
    "age": 21,
    "course": "BCA",
    "grade": "A+"
}

# 1. Accessing values using keys
print("Student Name:", student["name"])
print("Student Age:", student.get("age"))  # Using get() method

# 2. Adding a new key-value pair
student["city"] = "Sirsa"
print("After adding city:", student)

# 3. Updating an existing value
student["grade"] = "A++"
print("After updating grade:", student)

# 4. Removing a key-value pair using pop()
removed_value = student.pop("age")
print("Removed age:", removed_value)
print("After pop:", student)

# 5. Removing the last inserted item using popitem()
removed_item = student.popitem()
print("Removed item:", removed_item)
print("After popitem:", student)

# 6. Checking if a key exists
print("Is 'course' key present?", "course" in student)
print("Is 'age' key present?", "age" in student)

# 7. Getting all keys
print("Keys in dictionary:", student.keys())

# 8. Getting all values
print("Values in dictionary:", student.values())

# 9. Getting all key-value pairs
print("Key-Value pairs:", student.items())

# 10. Copying the dictionary
student_copy = student.copy()
print("Copied dictionary:", student_copy)

# 11. Clearing all elements from dictionary
student.clear()
print("After clearing dictionary:", student)
