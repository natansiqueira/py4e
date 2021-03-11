LOWEST_SCORE = 0.0
GREATEST_SCORE = 1.0

score = input("Enter Score: ")

score = float(score)

if score < LOWEST_SCORE or score > GREATEST_SCORE:
    print("The score must be greater or equal to", LOWEST_SCORE, "and less than or equal to", GREATEST_SCORE)
elif score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
else:
    print("F")