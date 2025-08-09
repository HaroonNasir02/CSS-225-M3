# Muhammad Haroon Nasir
# August 6th, 2025

# ask user for their name and only greets them if its me or my instructor

start = int(input("What day do you start break? (0 - 6)"))
stay = int(input("What is your length of stay?"))
end = (start + stay) % 7
print("You will return on day number: ", end)