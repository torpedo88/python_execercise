# Create an empty variables email  
emails = {}

assert emails == {}, f"Expected `emails` to be {{}} but got : {repr(emails)}"

# Add the intial dict list of name and emails.

emails['ashley'] = 'ashley@gmail.com'
emails['craig']   = 'craig@gmail.com'
emails['elizabeth'] = 'elizabeth@gmail.com'

assert emails == {
    'ashley': 'ashley@gmail.com',
    'craig': 'craig@gmail.com',
    'elizabeth': 'elizabeth@gmail.com'
}, f" Expected `emails` to be {{'ashley': 'ashley@gmail.com', 'craig': 'craig@gmail.com', 'elizabeth': 'elizabeth@gmail.com'}} but got: {repr(emails)}"

# Delete Craig from the email lists

del emails['craig']

assert emails == { 
    'ashley': 'ashley@gmail.com',
    'elizabeth': 'elizabeth@gmail.com'
}, f"Expected `emails` to be {{'ashley': 'ashley@gmail.com', 'elizabeth': 'elizabeth@gmail.com'}} but got: {repr(emails)}"

# Add dalton to the email lists.

emails["dalton"] = "dalton@gmail.com"

assert emails == {
    'ashley': 'ashley@gmail.com',
    'dalton': 'dalton@gmail.com',
    'elizabeth': 'elizabeth@gmail.com'
}, f" Expected `emails` to be {{'ashley': 'ashley@gmail.com', 'dalton': 'dalton@gmail.com', 'elizabeth': 'elizabeth@gmail.com'}} but got: {repr(emails)}"

# extract the users from the email list

users = list(emails.keys())
users.sort()

assert users == ['ashley', 'dalton', 'elizabeth'], f"Expected `users` to be ['ashley', 'dalton', 'elizabeth'] but got : {repr(users)}"

# extract emails from the dict and saving to the list of emails_lists

email_list = list(emails.values())
email_list.sort()

assert email_list == ['ashley@gmail.com','dalton@gmail.com','elizabeth@gmail.com'], f"Expected `email_list` to be ['ashley@gmail.com','dalton@gmail.com','elizabeth@gmail.com'] but got : {repr(email_list)}"


# Extract key value pairs

pairs = list(emails.items())
pairs.sort()

assert pairs == [('ashley', 'ashley@gmail.com'), 
                ('dalton', 'dalton@gmail.com'), 
                ('elizabeth', 'elizabeth@gmail.com')], f"Expected `pairs` to be [('ashley', 'ashley@gmail.com'), ('dalton', 'dalton@gmail.com'), ('elizabeth', 'elizabeth@gmail.com')] but got : {repr(pairs)}"


