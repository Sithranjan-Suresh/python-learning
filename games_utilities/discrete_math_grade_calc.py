# UTD Grade Calculator
# Calculates your overall and letter grade based on your current scores

from statistics import mean

def drop_lowest(scores):
    if not scores:
        return None
    if len(scores) == 1:
        return scores[0]
    scores_sorted = sorted(scores)
    return mean(scores_sorted[1:])  # drops one lowest

def letter_grade(percent):
    if percent >= 95:
        return "A+"
    elif percent >= 85:
        return "A"
    elif percent >= 80:
        return "A-"
    elif percent >= 75:
        return "B+"
    elif percent >= 65:
        return "B"
    elif percent >= 60:
        return "B-"
    elif percent >= 55:
        return "C+"
    elif percent >= 45:
        return "C"
    elif percent >= 40:
        return "C-"
    elif percent >= 35:
        return "D+"
    elif percent >= 25:
        return "D"
    elif percent >= 20:
        return "D-"
    else:
        return "F"

# ---------------- YOUR GRADES HERE ----------------
homeworks = [89.55,88.61,97.02,97.15,98]   # update as you go
smartbooks = [100,100,100,100,100,100]  # update as you go
midterm = 80.6              # set to number when graded (e.g. 88)
final = None                # same here

# ---------------- CALCULATIONS ----------------
weights = {"hw": 25, "sb": 15, "midterm": 30, "final": 30}

hw_avg = drop_lowest(homeworks)
sb_avg = drop_lowest(smartbooks)

hw_contrib = (hw_avg * weights["hw"] / 100) if hw_avg else 0
sb_contrib = (sb_avg * weights["sb"] / 100) if sb_avg else 0
midterm_contrib = (midterm * weights["midterm"] / 100) if midterm else 0
final_contrib = (final * weights["final"] / 100) if final else 0

total = hw_contrib + sb_contrib + midterm_contrib + final_contrib

# normalize based on completed components
completed_weights = 0
if hw_avg: completed_weights += weights["hw"]
if sb_avg: completed_weights += weights["sb"]
if midterm: completed_weights += weights["midterm"]
if final: completed_weights += weights["final"]

if completed_weights > 0:
    current_grade = (total / completed_weights) * 100
    print(f"Current weighted grade (so far): {current_grade:.2f}% ({letter_grade(current_grade)})")
else:
    print("No grades entered yet.")

print(f"\nIf all missing items were 0, your overall = {total:.2f}% ({letter_grade(total)})")

# optional projection
proj_midterm = 80.6  # example: assume you score 90 on midterm
proj_final = 75    # and 85 on final
projection = hw_contrib + sb_contrib + (proj_midterm * weights["midterm"] / 100) + (proj_final * weights["final"] / 100)
print(f"If you score {proj_midterm}% midterm and {proj_final}% final → {projection:.2f}% ({letter_grade(projection)})")
