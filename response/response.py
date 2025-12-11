from validator_collection import validators, checkers, errors

email_ad = input("What is your email? ")

assess = checkers.is_email(email_ad)

if assess == True:
    print("Valid")
else:
    print("Invalid")
