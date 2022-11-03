from validator_collection import validators, errors


email = input("What's your email address? ")

try:
    if email_address := validators.email(email):
        print("Valid")
except errors.InvalidEmailError:
    print("Invalid")