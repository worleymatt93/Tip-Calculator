print("Welcome to the tip calculator!\nLet's make sure you tip like a pro!")

total = float(input("What was the total bill? $"))
subtotal = float(input("What was the subtotal (total before tax)? $"))
tip_percentage = float(input("How much do you want to tip (percentage)? "))
people = int(input("How many people are splitting the bill? "))

tax = total - subtotal
tip = tip_percentage / 100 * subtotal

print(f"Each person should pay: ${(total + tip) / people:.2f}")
