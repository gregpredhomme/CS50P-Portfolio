import csv
import json
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python project.py transactions.csv")
    csv_filename = sys.argv[1]

    keyword_rules = {
        "Rent": ["Rent", "Management", "Landlord"],
        "Food": ["Doordash", "Chipotle", "Shake Shack", "Sweetgreen"],
        "Transport": ["Uber", "Lyft", "MTA", "Taxi"],
        "Shopping": ["Amazon", "Target", "Walmart"],
        "Utilities": ["Con Edison", "Verizon", "Internet"]
    }

    print(f"Loading data from {csv_filename}...")
    transactions = load_transactions(csv_filename)

    budget_targets = load_budget("budget.json")

    spending_totals = calculate_spend_by_category(transactions, keyword_rules)

    print("\n" + "=" * 55)
    print("SPENDING REPORT".center(55))
    print("=" * 55)
    print(f"{'Category':<15} | {'Budget':<10} | {'Actual':<10} | {'Status':<10}")
    print("-" * 55)

    for category, limit in budget_targets.items():
        actual = spending_totals.get(category, 0.0)
        diff = limit - actual

        status = "✅ Safe"
        if diff < 0:
            status = "❌ OVER"
        print(f"{category:<15} | ${limit:<9.2f} | ${actual:<9.2f} | {status}")

    other_spend = spending_totals.get("Other", 0.0)
    if other_spend > 0:
        print("-" * 55)
        print(f"{'Other':<15} | {'N/A':<10} | ${other_spend:<9.2f} | ⚠️ Review")

    print("=" * 55)
    total_budget = sum(budget_targets.values())
    total_spent = sum(spending_totals.values())
    total_diff = total_budget - total_spent
    total_status = "✅ Safe" if total_diff >= 0 else "❌ OVER"

    print(f"{'TOTAL':<15} | ${total_budget:<9.2f} | ${total_spent:<9.2f} | {total_status}")


def load_transactions(filename):
    """
    Reads a CSV file and returns a list of dictionaries.
    Each dictionary represents a transaction.
    """
    transactions = []
    try:
        with open(filename, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"])
                transactions.append(row)
    except FileNotFoundError:
        sys.exit(f"Could not find {filename}")

    return transactions


def load_budget(filename):
    """
    Reads a JSON file and returns a dictionary of category: limit.
    """
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        sys.exit(f"Could not find {filename}")


def categorize_transaction(description, rules):
    """
    Takes a transaction description (str) and a dictionary of rules.
    Returns the category name (str).
    """
    description = description.lower()

    for category, keywords in rules.items():
        for keyword in keywords:
            if keyword.lower() in description:
                return category
    return "Other"


def calculate_spend_by_category(transactions, rules):
    """
    Takes a list of transactions.
    Returns a dictionary of category: total_spent.
    """
    spending = {}

    for t in transactions:
        category = categorize_transaction(t["description"], rules)

        if category in spending:
            spending[category] += t["amount"]
        else:
            spending[category] = t["amount"]
    return spending

if __name__ == "__main__":
    main()
