# Step 1: Define the correct password
correct_password = "12345"

# Optional Requirement: Set the maximum number of attempts
max_attempts = 5
attempts = 0

# Step 2: Use a while loop to ask for the password until the correct one is entered or attempts run out
while attempts < max_attempts:
    # Ask the user to enter the password
    entered_password = input("Enter the password: ")

    # Step 3: Check if the entered password is correct
    if entered_password == correct_password:
        print("Access granted")
        break
    else:
        # Increment the number of attempts
        attempts += 1
        # Calculate remaining attempts
        remaining_attempts = max_attempts - attempts
        # Inform the user of remaining attempts if they’re not out
        if remaining_attempts > 0:
            print(f"Incorrect password. You have {remaining_attempts} attempt(s) remaining.")
        else:
            # If max attempts are reached, alert the user
            print("Maximum attempts reached. User has been alerted.")




