print("Day 3 - Strings Practice")

#Q1 Create a variable containing a sentence print it. Then print the length of the sentence, the first character and the last character.
sentence="Python is a high-level programming language."
print("Sentence:",sentence)
print("Length of the sentence:",len(sentence))
print("First character:",sentence[0])
print("Last character:",sentence[-1])

#Q2 Create a variable containing your name. Print the name in uppercase, lowercase, and title case.
name="Zulekha Golandaz"
print("Name in uppercase:",name.upper())    
print("Name in lowercase:",name.lower())
print("Name in title case:",name.title())

#Q3 Create word="Programming" and print first character, last character, first 5 characters, last 4 characters and the completer word in reverse order.
word="Programming"
print("First character:",word[0])
print("Last character:",word[-1])
print("First 5 characters:",word[:5])
print("Last 4 characters:",word[-4:])
print("Complete word in reverse order:",word[::-1])

#Q4 Create variables for: name, age, course. Then produce one properly formatted sentence using an f-string.
name="Zulekha Golandaz"
age=20
course="Python Programming"
print(f"My name is {name}, I am {age} years old and I am learning {course}.")

#Q5 Create variables for: first_name, last_name, birth_year. Use string operations to create a simple username.
first_name="Zulekha"
last_name="Golandaz"
birth_year=2006
username=f"{first_name.lower()}{last_name.lower()}{birth_year}"
print("Username:",username)
