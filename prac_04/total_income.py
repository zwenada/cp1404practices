def main():
    """Display income report for incomes over a given number of periods."""
    income_list = []
    number_of_periods = int(input("How many periods? "))

    for period in range(1, number_of_periods + 1):
        income = get_income_input(period)
        income_list.append(income)

    print_income_report(number_of_periods, income_list)

def get_income_input(period):
    """Get and return the income input for the specified period using an f-string."""
    return float(input(f"Enter income for period {period}: "))

def print_income_report(periods, incomes):
    """Print the income report for the given periods and incomes."""
    print("\nIncome Report\n----------------")
    total = 0
    for period in range(1, periods + 1):
        income = incomes[period - 1]
        total += income
        print(f"Period {period:2} -   Income: ${income:10.2f}   Total: ${total:10.2f}")

main()
