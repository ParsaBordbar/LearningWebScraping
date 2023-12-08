import re

myString = """Adding Interactivity Some 
things on the screen update in response to
user input. For example, clicking an image 
gallery switches the active image. In
React, data that changes over time is
called state. You can add state to any
component, and update it as needed. In 
this chapter, you’ll learn how to write
components that handle interactions, 
update their state, and display different
output over time."""

print(re.match(r"^A", myString))
print(re.match(r"e$", myString))
# print(re.match(r"^A", myString))
# print(re.match(r"^A", myString))
# print(re.match(r"^A", myString))
