import csv
import matplotlib.pyplot as plt
import sys
import datetime 

BUDGET_TARGETS = {
    "Rent": 2000.00,
    "Food": 600.00,
    "Transport": 200.00,
    "Shopping": 300.00,
    "Utilities": 150.00
}

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
    raw_data = load_transactions(csv_filename)

    clean_data = wrangle_data(raw_data)

    if not clean_data:
        print("Error: No valid transactions parsed. Please check CSV file headers.")
        return 

    spending_totals = calculate_spend_by_category(clean_data, keyword_rules)

    # CLI report
    print("\n" + "=" * 55)
    print("SPENDING REPORT".center(55))
    print("=" * 55)
    print(f"{'Category':<15} | {'Budget':<10} | {'Actual':<10} | {'Status':<10}")
    print("-" * 55)

    for category, limit in BUDGET_TARGETS.items():
        actual = spending_totals.get(category, 0.0)
        diff = limit - actual

        status = "Safe"
        if diff < 0:
            status = "OVER"
        print(f"{category:<15} | ${limit:<9.2f} | ${actual:<9.2f} | {status}")

    # check uncategorized spend
    other_spend = spending_totals.get("Other", 0.0)
    if other_spend > 0:
        print("-" * 55)
        print(f"{'Other':<15} | {'N/A':<10} | ${other_spend:<9.2f} | Review!")
    print("=" * 55)
    print("\nGenerating chart...")
    visualize_data(BUDGET_TARGETS, spending_totals)

def load_transactions(filename):
    """
    Reads a CSV list of dicts and handles BOM if present.
    """
    data = []
    try:
        with open(filename, mode="r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        sys.exit(f"File not found: {filename}")
    return data

def wrangle_data(raw_data):
    """
    Cleans raw strings to proper types (float/datetime).
    Handles accounting negatives e.g. ($100).
    """
    clean_rows = []
    
    #handle unformatted CSV headers (case sensitivity/spaces)
    for row in raw_data:
        norm = {}
        for k, v in row.items():
            if k is not None:
                norm[k.strip().lower()] = v

        amt = norm.get("amount", "")
        date_str = norm.get("date", "")
        desc = norm.get("description", "")

        if amt is None: amt = ""
        if date_str is None: date_str = ""
        if desc is None: desc = ""

        if not str(amt).strip() or not str(date_str).strip():
            continue 
        
        try:
            #fix currency formatting 
            amt_clean = str(amt).replace("$", "").replace(",", "").strip()
            #handle accounting negative format (100) -> -100
            if "(" in amt_clean and ")" in amt_clean:
                amt_clean = amt_clean.replace("(", "-").replace(")", "")
            
            val = float(amt_clean)

            #parse date (try both standard formats)
            d_str = str(date_str).strip()
            try:
                d_obj = datetime.datetime.strptime(d_str, "%m/%d/%Y")
            except ValueError:
                d_obj = datetime.datetime.strptime(d_str, "%m/%d/%y")

            desc_clean = str(desc).strip()

            clean_rows.append({
                "date": d_obj,
                "description": desc_clean,
                "amount": val
            })
        except ValueError:
            continue 
        
    return clean_rows


def categorize_transaction(desc, rules):
    """
    Matches keywords 
    """
    if not desc:
        return "Other"
    
    desc_lower = desc.lower()

    for category, keywords in rules.items():
        for keyword in keywords:
            if keyword.lower() in desc_lower:
                return category
    return "Other"


def calculate_spend_by_category(transactions, rules):
    """
    Takes a list of transactions.
    Returns a dictionary of category: total_spent.
    """
    totals = {}

    for t in transactions:
        category = categorize_transaction(t["description"], rules)
        totals[category] = totals.get(category, 0) + t["amount"]
    return totals 

def visualize_data(targets, actuals):
    """
    Saves comparison bar chart to png.
    """
    categories = list(targets.keys())
    t_vals = [targets[c] for c in categories]
    a_vals = [actuals.get(c, 0.0) for c in categories]

    x = range(len(categories))
    width = 0.4

    plt.figure(figsize=(10, 6))
    plt.bar([i - width/2 for i in x], t_vals, width=width, label="Budget", color="lightgray")
    plt.bar([i + width/2 for i in x], a_vals, width=width, label="Actual", color="#4682b4")

    plt.xticks(list(x), categories, rotation=30, ha="right")
    plt.ylabel("Amount ($)")
    plt.title("Budget vs. Actual")
    plt.legend()
    plt.tight_layout()

    plt.savefig("spending_chart.png")
    plt.close()
    print("Chart saved: spending_chart.png")

if __name__ == "__main__":
    main()
