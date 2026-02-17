import csv, sys, datetime
import matplotlib.pyplot as plt, matplotlib.ticker as mtick
from typing import Any

def main() -> None:
    """Entry point: loads transactions from CSV, categorizes spend, prints budget status, and generates a chart."""
    if len(sys.argv) != 2: sys.exit("Usage: python project.py transactions.csv")
    BUDGET_TARGETS = {"Rent": 1200.00, "Food": 600.00, "Transport": 200.00, 
                      "Shopping": 300.00, "Utilities": 150.00}
    RULES = {
        "Rent": ["Rent", "Management", "Landlord"],
        "Food": ["Doordash", "Chipotle", "Shake Shack", "Sweetgreen"],
        "Transport": ["Uber", "Lyft", "MTA", "Taxi"],
        "Shopping": ["Amazon", "Target", "Walmart"],
        "Utilities": ["Con Edison", "Verizon", "Internet"]
    }
    print(f"Processing {sys.argv[1]}...")
    # 1. Ingest and wrangle data 
    transactions = get_clean_data(sys.argv[1])
    if not transactions: sys.exit("Error: No valid data found.")
    # 2. Analyze spending
    totals = {c: 0.0 for c in BUDGET_TARGETS}
    totals["Other"] = 0.0
    for t in transactions:
        category = "Other"
        # Check description against rules
        for cat, keywords in RULES.items():
            if any(k.lower() in t["desc"] for k in keywords):
                category = cat
                break
        totals[category] += t["amount"]
    # 3. Report
    print(f"\n{'CATEGORY':<12} | {'BUDGET':<8} | {'ACTUAL':<8} | {'STATUS'}")
    print("-" * 45)
    for cat, limit in BUDGET_TARGETS.items():
        actual = totals[cat]
        status = "OVER" if (limit - actual) < 0 else "Safe"
        print(f"{cat:<12} | ${limit:<8,.0f} | ${actual:<8,.0f} | {status}")
    if totals["Other"] > 0:
        print(f"{'-'*45}\n{'Other':<12} | {'N/A':<8} | ${totals['Other']:<8,.0f} | Review!")
    visualize_data(BUDGET_TARGETS, totals)

def get_clean_data(filename: str) -> list[dict[str, Any]]:
    """Ingests CSV and handles type conversion (float/date)."""
    # Expected columns: Date, Description, Amount (case-insensitive)
    clean_rows = []
    try:
        with open(filename, encoding="utf-8-sig") as f:
            for row in csv.DictReader(f):
                # Normalize keys and clean amount string 
                r = {k.strip().lower(): (v or "") for k, v in row.items() if k}
                amt_str = r.get("amount", "").replace("$", "").replace(",", "").strip()
                if not amt_str: continue
                try:
                    # Handle accounting negatives e.g. ($100)
                    if "(" in amt_str and ")" in amt_str:
                        amt_str = "-" + amt_str.replace("(", "").replace(")", "")
                    # Handle date formats (4 digit year vs. 2 digit year)
                    d_str = r.get("date", "").strip()
                    if not d_str: continue
                    fmt = "%m/%d/%Y" if len(d_str.split("/")[-1]) == 4 else "%m/%d/%y"
                    clean_rows.append({
                        "date": datetime.datetime.strptime(d_str, fmt),
                        "desc": r.get("description", "").strip().lower(),
                        "amount": float(amt_str)
                    })
                except (ValueError, TypeError): continue
    except FileNotFoundError: sys.exit("File not found")
    return clean_rows

def visualize_data(targets: dict[str, float], actuals: dict[str, float]) -> None:
    """Generates comparison bar chart."""
    categories = list(targets.keys())
    x = range(len(categories))
    plt.figure(figsize=(7, 3))
    plt.bar([i-0.125 for i in x], targets.values(), 0.25, label="Budget", color="silver")
    plt.bar([i+0.125 for i in x], [actuals[c] for c in categories], 0.25, label="Actual", color="#4682b4")
    plt.xticks(list(x), categories)
    plt.gca().yaxis.set_major_formatter(mtick.StrMethodFormatter("${x:,.0f}"))
    plt.title("Budget vs. Actual Spending")
    plt.legend()
    plt.tight_layout()
    plt.savefig("spending_chart.png")
    plt.close()
    print("\nChart generated: spending_chart.png")

if __name__ == "__main__":
    main()