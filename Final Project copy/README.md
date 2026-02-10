# PERSONAL BUDGET TRACKER

#### Video Demo: https://www.youtube.com/watch?v=UfE9GRvfK3U

#### Description:

My final project is a command-line data processing tool designed to help users audit their personal finances. I chose this project because I wanted to build something practical that I could actually use in my everyday life. The application allows you to set budget limits for different categories in a JSON file and then feed in a CSV file of your raw bank transactions.

The program automatically categorizes every transaction based on keyword rules (e.g., associating "Chipotle" with "Food" or "Uber" with "Transport") and calculates the total spending for each category. It then generates a formatted "Spending Report" in the terminal that compares your actual spending against your budget, while flagging any categories where you have gone over budget.

#### Files Breakdown:

**'project.py'**
This is the main driver of the program. It uses command-line arguments ('sys.argv') to accept a CSV filename from the user. Inside, 'main()' orchestrates the flow: loading the data, applying the categorization logic, and printing the final report. I implemented a 'keyword_rules' dictionary to handle the logic of sorting descriptions into categories, and used formatted strings to align the output table so it is easy to read.

**'test_project.py'**
This file contains my unit tests. I used the 'pytest' library to ensure my functions were working correctly. One challenge I faced was testing functions that rely on files existing. To solve this, I wrote tests that create temporary dummy files to verify that my 'load_budget' function reads data correctly, and other tests to ensure the program handles missing files gracefully (raising SystemExit if the input file is not found).

**'budget.json'**
I used a JSON file to store the budget categories and their limits. I chose JSON because a budget is aligned with a dictionary (key-value pairs such as "Food": 500), and Python's built-in JSON library makes it easy to load this configuration separately from the code.

**'transactions.csv'**
This file acts as the input data for the program. It contains the raw list of transactions (date, description, amount). Using CSV allows me to download real data from a bank account or create test data easily in Excel.

#### Design Choices:

One of the main decisions I made was to seperate the logic into distinct steps: loading, categorizing, and reporting. I debated whether to make the program interactive (e.g., asking the user to type in expenses one by one), but I decided a batch processing approach was better. This way, the user can download a whole month's history as a CSV, align the format with this 'date, description, amount' format, and process it all in a split second.

I also spent time on output formatting. Instead of just printing the raw numbers, I created a visual table using string alignment and added status indicators (e.g., "✅ Safe" or "❌ OVER") to provide visual feedback on the user's financial health.
