from project import load_transactions, categorize_transaction, calculate_spend_by_category

def test_load_transactions():
    data = load_transactions("transactions.csv")

    assert len(data) > 0

    first_row = data[0]
    assert first_row["description"] == "Uber"
    assert first_row["amount"] == 20.25

    assert isinstance(first_row["amount"], float)


def test_categorize_transaction():
    test_rules = {
        "Transport": ["Uber", "Lyft"],
        "Food": ["Chipotle", "Doordash"]
    }

    assert categorize_transaction("Uber Trip", test_rules) == "Transport"
    assert categorize_transaction("uber trip", test_rules) == "Transport"
    assert categorize_transaction("Chipotle Mexican Grill", test_rules) == "Food"
    assert categorize_transaction("Random Store", test_rules) == "Other"

def test_calculate_spend_by_category():
    transactions = [
        {"description": "Uber Trip", "amount": 20.0},
        {"description": "Lyft Ride", "amount": 15.0},
        {"description": "Chipotle", "amount": 12.0},
        {"description": "Unknown Store", "amount": 50.0}
    ]

    rules = {
        "Transport": ["Uber", "Lyft"],
        "Food": ["Chipotle"]
    }

    result = calculate_spend_by_category(transactions, rules)
    assert result["Transport"] == 35.0
    assert result["Food"] == 12.0
    assert result["Other"] == 50.0
