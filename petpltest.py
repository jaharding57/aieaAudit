from pyswip import Prolog

# Initialize Prolog
prolog = Prolog()

# Load the Prolog file
prolog.consult("petfacts.pl")

# Example Queries
# 1. Find all enemies
print("Enemies:")
for result in prolog.query("enemy(X, Y)"):
    print(result)

# 2. Check if two pets are friends
print("\nAre Gunnar and Romo friends?")
query_result = list(prolog.query("friend(gunnar, romo)"))
if query_result:
    print("Yes, they are friends.")
else:
    print("No, they are not friends.")

# 3. Find all roommates
print("\nRoommates:")
for result in prolog.query("roommates(X, Y)"):
    print(result)

