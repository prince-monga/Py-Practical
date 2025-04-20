str1 = "Hey"
str2 = "Prince Arora"
str3 = "  Welcome to Jammu!  "

print("\nString Slicing:")
print("First 3 characters of str1:", str1[:3])
print("Last 3 characters of str2:", str2[-3:])
print("Middle characters of str3:", str3[2:10])

print("\nString Functions:")
print("Uppercase:", str1.upper())
print("Lowercase:", str2.lower())

print("\nString Searching and Replacing:")
print("Find 'Prince' in str3:", str3.find("Prince"))
print("Replace 'Welcome' with 'Hey':", str3.replace("Welcome", "Hey"))

print("\nString Splitting and Joining:")
words = str3.split()  
print("Splitting str3:", words)
joined_str = "-".join(words)
print("Joining words with '-':", joined_str)
