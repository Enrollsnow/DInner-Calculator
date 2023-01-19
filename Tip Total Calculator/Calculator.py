bill = input("What was the total bill?\n")
tips = input("What percentage tip would you like to give? 10, 12, or 15\n")
split = input("How many people are you spliting with?\n")

new_total = float(bill)
new_tip = int(tips)
new_split = int(split)

tips_as_Percent = new_tip / 100
total_tip_amount = new_total * tips_as_Percent
total_bill = new_total + total_tip_amount
bill_per_person = total_bill / new_split
final_amount = round(bill_per_person, 2)
print(f"Each Person pays: ${final_amount}")