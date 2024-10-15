print("Welcome to the tip calculator robot! beep boop")
bill = float(input("What was the total bill good sir/lady? $"))
tip = int(input("How much would you like to tip? 10%, 12%, 15% or custom? "))
people = int(input("How many people should split this bill? "))
total_with_tip = tip / 100 * bill + bill
grand_total = round(total_with_tip / people, 2)
print(f"According to my calculations each person should pay: ${grand_total}")
