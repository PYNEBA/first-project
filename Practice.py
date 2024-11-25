print("WELCOME TO THE BILLING SYSTEM")
user_response = input("If you are a new user or old (type 'new' or 'old'): ").strip().lower()

# Keep prompting until valid input
while user_response not in ("new", "old"):
    print("Enter as 'new' or 'old'!")
    user_response = input("If you are a new user or old (type 'new' or 'old'): ").strip().lower()

# Password setup and validation for new users
if user_response == "new":
    user_email = input("Enter your email: ").strip()
    print("Password Requirements:")
    print("- At least 8 characters long")
    print("- Contains at least one uppercase letter")
    print("- Contains at least one lowercase letter")
    print("- Contains at least one number")
    print("- No spaces allowed")

    while True:
        password = input("Enter a password: ").strip()
        reasons = []  # Reset reasons each attempt

        # Password validation checks
        if len(password) < 8:
            reasons.append("Must be at least 8 characters.")
        if not any(char.islower() for char in password):
            reasons.append("Must contain at least one lowercase letter.")
        if not any(char.isupper() for char in password):
            reasons.append("Must contain at least one uppercase letter.")
        if not any(char.isdigit() for char in password):
            reasons.append("Must contain at least one number.")
        if " " in password:
            reasons.append("Password should not contain spaces.")

        # Provide feedback if the password is invalid
        if not reasons:
            print("Password is valid! You have successfully set up your account.")
            break  # Password meets all criteria; exit loop
        else:
            print("Password is invalid for the following reasons:")
            for reason in reasons:
                print(f"- {reason}")
            print("Please try again.")

elif user_response == "old":
    print("Welcome back! You are now logged in.")

# Bill Calculation Section
print("\nWelcome to the Bill Calculator")

# Collect user input for bill amount and tax rate, with error handling
while True:
    try:
        bill_amount = float(input("Enter the bill amount: $"))
        tax_rate = float(input("Enter the tax rate (%): "))
        break
    except ValueError:
        print("Please enter valid numbers for the bill and tax rate.")

# Calculate tax amount and initial total
tax_amount = (bill_amount * tax_rate) / 100
total_with_tax = bill_amount + tax_amount

# Ask if user wants to add a tip
tip_response = input("Would you like to add a tip? (yes/no): ").strip().lower()
total_bill = total_with_tax  # Default total amount

# Tip processing if user wants to add a tip
if tip_response == "yes":
    tip_type = input("Enter tip type: amount ($) or percentage (%): ").strip()

    # Process based on tip type
    if tip_type == "$":
        while True:
            try:
                tip_amount = float(input("Enter the tip amount in dollars: $"))
                total_bill += tip_amount
                break
            except ValueError:
                print("Please enter a valid number for the tip amount.")

    elif tip_type == "%":
        while True:
            try:
                tip_percent = float(input("Enter the tip percentage: "))
                tip_amount = (total_with_tax * tip_percent) / 100
                total_bill += tip_amount
                break
            except ValueError:
                print("Please enter a valid number for the tip percentage.")
    else:
        print("Invalid input for tip type. Proceeding without a tip.")

# Display final bill summary
print(f"\n--- Bill Summary ---")
print(f"Original Bill: ${bill_amount:.2f}")
print(f"Tax Amount (@{tax_rate}%): ${tax_amount:.2f}")
if tip_response == "yes" and tip_type in ("$", "%"):
    print(f"Tip Amount: ${tip_amount:.2f}")
print(f"Total Payable Bill: ${total_bill:.2f}")




