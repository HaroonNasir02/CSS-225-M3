# Muhammad Haroon Nasir
# August 6th, 2025

# ask user for their name and only greets them if its me or my instructor

myName = "Haroon"
instructorName = "Akshay"
username = input("What is your name?")

if username == myName:
    print(f"Hello {myName}")
elif username == instructorName:
    print(f"Hello {instructorName}")
else:
    print("Restricted access")