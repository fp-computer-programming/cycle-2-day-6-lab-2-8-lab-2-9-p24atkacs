"""
Create a Python file named lab_2-8.py
A team needs to score 15 points to win a gold medal, between 12-14 points to win a silver medal, 
and between 9-11 point to win a bronze medal. A team does not earn a medal if they earn 8 or fewer points.
Write a program using nested if else statements where a user can input the number of points a team scored and the medal that they earned is displayed.

"""
score = int(input("Enter the number of points scored by the team: "))

if score >= 12 and score <= 15:
    medal = "Gold"
elif score >= 9 and score <= 11:
    medal = "Bronze"
elif score >= 12 and score <= 14:
    medal = "Silver"
else:
    medal = "No Medal"

print(f"The team earned a {medal} medal.")
