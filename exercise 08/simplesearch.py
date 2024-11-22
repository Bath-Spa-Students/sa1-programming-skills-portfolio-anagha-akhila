# Initialize the list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
# Optional Requirement: Allow the user to input the search term
search_term = input("Enter the name you want to search for: ").strip()
# Implement the search functionality
if search_term in names:
    print(f"{search_term} is in the list.")
else:
    print(f"{search_term} is not in the list.")
