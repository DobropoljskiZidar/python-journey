hours = float(input("How many hours you worked this week? "))
rate = float(input("What your hourly rate is? "))

if hours <0 or hours >100:
    "The input does not look right"
elif hours >40:
    regular_hours = 40
    ot_hours = hours - 40
else:
    regular_hours = hours
    ot_hours = 0

regular_pay = regular_hours * rate
ot_pay = ot_hours * rate * 1.5
total_pay = regular_pay + ot_pay

if hours > 40:
    print(f"Total pay: {total_pay: .2f}")
    print(f"Overtime pay: {ot_pay: .2f} ({ot_hours} hours of overtime)")
else:
    print(f"Total pay: {total_pay: .2f}")
if hours < 30:
    print(f"Under 30")
elif hours <= 45:
    print(f"30 to 45")
else:
    print(f"Over 45")


