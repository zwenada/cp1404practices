def determine_score_status(score):
    if score < 0:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    else:
        return "Passable"

def main():
    score = float(input("Enter score: "))
    status = determine_score_status(score)
    print(status)

main()
