# Grade planner considering unequal exam scores + "all-100" scenario for HW & quizzes
# Edit the top variables and run. Python 3.8+
#
# Where to update:
# - homework_scores, quiz_scores, attendance_scores: keep fractions (e.g., 27/30 or 0.9).
# - midterm1, midterm2, final_exam: set to integers 0..100 when available, or None if unknown.
# - TARGET: desired overall percent (e.g., 94.0)

# ---------------------- USER INPUT (edit these) ----------------------
homework_scores = [30/30, 26/30, 27.5/30, 28/30, 30/30]  # fractions OK
quiz_scores     = [9/10, 10/10, 10/10, 10/10]            # lowest quiz dropped already
attendance_scores = [1/1, 1/1, 1/1, 1/1]

# Put known exam results here as integers 0..100, or None if unknown:
midterm1 = None   # e.g. 92
midterm2 = None   # e.g. 95
final_exam = None # e.g. 93

TARGET = 94.0

# ---------------------- WEIGHTS (fixed) ----------------------
WEIGHTS = {
    "midterm1": 0.20,
    "midterm2": 0.20,
    "homework": 0.15,
    "quizzes": 0.15,
    "attendance": 0.05,
    "final": 0.25
}

# ---------------------- HELPERS ----------------------
def avg(lst):
    return sum(lst) / len(lst) if lst else 0.0

def grade_fraction(m1, m2, f, hw_scores, quiz_scores, att_scores):
    """Return final grade as fraction 0..1 given exam fractions m1,m2,f (each 0..1)."""
    total = 0.0
    total += avg(hw_scores) * WEIGHTS["homework"]
    total += avg(quiz_scores) * WEIGHTS["quizzes"]
    total += avg(att_scores) * WEIGHTS["attendance"]
    total += m1 * WEIGHTS["midterm1"]
    total += m2 * WEIGHTS["midterm2"]
    total += f  * WEIGHTS["final"]
    return total

def percent(frac):
    return frac * 100.0

def solve_and_print(hw_scores, quiz_scores, att_scores, m1_known, m2_known, f_known, target, label="SCENARIO"):
    print("\n" + "="*60)
    print(f"SCENARIO: {label}")
    print("="*60)
    hw_avg = avg(hw_scores)
    quiz_avg = avg(quiz_scores)
    att_avg = avg(att_scores)
    contrib = hw_avg*WEIGHTS["homework"] + quiz_avg*WEIGHTS["quizzes"] + att_avg*WEIGHTS["attendance"]
    completed_weight = WEIGHTS["homework"] + WEIGHTS["quizzes"] + WEIGHTS["attendance"]
    known_contrib = contrib
    known_weight = completed_weight
    if m1_known is not None:
        known_contrib += (m1_known/100.0) * WEIGHTS["midterm1"]
        known_weight += WEIGHTS["midterm1"]
    if m2_known is not None:
        known_contrib += (m2_known/100.0) * WEIGHTS["midterm2"]
        known_weight += WEIGHTS["midterm2"]
    if f_known is not None:
        known_contrib += (f_known/100.0) * WEIGHTS["final"]
        known_weight += WEIGHTS["final"]

    current_display_grade = (known_contrib / known_weight * 100.0) if known_weight>0 else 0.0
    print("----- CURRENT STATUS -----")
    print(f"Homework avg: {hw_avg*100:.2f}%   Quizzes avg: {quiz_avg*100:.2f}%   Attendance avg: {att_avg*100:.2f}%")
    print(f"Completed weight: {known_weight*100:.1f}%")
    print(f"Current grade (based on completed items): {current_display_grade:.2f}%")
    print(f"Points contributed so far to final grade: {percent(known_contrib):.2f}% / 100%")

    # Ranges for search
    range_m1 = [m1_known] if m1_known is not None else list(range(0,101))
    range_m2 = [m2_known] if m2_known is not None else list(range(0,101))
    range_f  = [f_known] if f_known is not None else list(range(0,101))

    target_frac = target / 100.0
    best_by_sum = None        # minimize sum m1+m2+f
    best_by_max = None        # minimize max(m1,m2,f)
    solutions_found = 0

    # Search integer combos 0..100
    for m1_int in range_m1:
        for m2_int in range_m2:
            for f_int in range_f:
                m1_frac = m1_int / 100.0
                m2_frac = m2_int / 100.0
                f_frac  = f_int  / 100.0
                final_frac = grade_fraction(m1_frac, m2_frac, f_frac, hw_scores, quiz_scores, att_scores)
                if final_frac >= target_frac - 1e-12:
                    solutions_found += 1
                    s = m1_int + m2_int + f_int
                    mx = max(m1_int, m2_int, f_int)
                    overall_pct = percent(final_frac)
                    cand = (s, mx, m1_int, m2_int, f_int, overall_pct)
                    # minimize (sum, max) lexicographically
                    if best_by_sum is None or (s, mx) < (best_by_sum[0], best_by_sum[1]):
                        best_by_sum = cand
                    # minimize (max, sum)
                    if best_by_max is None or (mx, s) < (best_by_max[1], best_by_max[0]):
                        best_by_max = cand

    if solutions_found == 0:
        print(f"\nNo integer combination of remaining exams (0-100) can reach {target}% in this scenario.")
        return

    print(f"\nFound {solutions_found} integer solution(s) (0..100) that reach >= {target}%.\n")

    if best_by_sum:
        s, mx, m1_best, m2_best, f_best, overall = best_by_sum
        print("-> Minimal SUM combo (minimizes M1+M2+Final):")
        print(f"   Midterm1: {m1_best}%, Midterm2: {m2_best}%, Final: {f_best}%")
        print(f"   Sum = {m1_best + m2_best + f_best}, Highest = {mx}%")
        print(f"   Overall with this combo: {overall:.2f}%\n")

    if best_by_max:
        s2, mx2, m1_b2, m2_b2, f_b2, overall2 = best_by_max
        print("-> Minimal MAX combo (minimizes the largest single exam score):")
        print(f"   Midterm1: {m1_b2}%, Midterm2: {m2_b2}%, Final: {f_b2}%")
        print(f"   Max single exam = {mx2}%, Sum = {m1_b2 + m2_b2 + f_b2}")
        print(f"   Overall with this combo: {overall2:.2f}%\n")

    # Also print equal-score needed on all remaining unknown exams (useful summary)
    # Compute points already locked (including known exams)
    locked_pts = (avg(hw_scores) * WEIGHTS["homework"] +
                  avg(quiz_scores) * WEIGHTS["quizzes"] +
                  avg(att_scores) * WEIGHTS["attendance"])
    if m1_known is not None:
        locked_pts += (m1_known/100.0) * WEIGHTS["midterm1"]
    if m2_known is not None:
        locked_pts += (m2_known/100.0) * WEIGHTS["midterm2"]
    if f_known is not None:
        locked_pts += (f_known/100.0) * WEIGHTS["final"]
    locked_weight = 0.0
    locked_weight += WEIGHTS["homework"] + WEIGHTS["quizzes"] + WEIGHTS["attendance"]
    if m1_known is not None:
        locked_weight += WEIGHTS["midterm1"]
    if m2_known is not None:
        locked_weight += WEIGHTS["midterm2"]
    if f_known is not None:
        locked_weight += WEIGHTS["final"]
    remaining_weight = 1.0 - locked_weight
    if remaining_weight > 0:
        needed_frac = max(0.0, (target_frac - locked_pts) / remaining_weight)
        print(f"-> If you scored the SAME percent on ALL remaining unknown exams, you'd need: {percent(needed_frac):.2f}% on each.")
    else:
        print("-> No remaining exams in this scenario.")

# ---------------------- RUN: current-real scenario ----------------------
solve_and_print(homework_scores, quiz_scores, attendance_scores, midterm1, midterm2, final_exam, TARGET, label="CURRENT SCORES")

# ---------------------- RUN: hypothetical scenario where all HW & quizzes are 100% ----
hw_all100 = [1.0] * len(homework_scores)  # same number of HW entries, all 100%
quiz_all100 = [1.0] * len(quiz_scores)    # same number of quizzes, all 100%
# attendance left as-is (user said perfect attendance earlier; keep actual attendance)
solve_and_print(hw_all100, quiz_all100, attendance_scores, midterm1, midterm2, final_exam, TARGET, label="ASSUME HW & QUIZZES = 100%")

# ---------------------- USAGE NOTES ----------------------
print("\nNotes:")
print("- Edit midterm1, midterm2, final_exam at the top when you get those scores (integers 0..100).")
print("- The solver searches integer percentages 0..100 for unknown exams and returns minimal combos.")
print("- To get decimal precision (e.g., 0.1%), request a finer search; it will be slower.")
