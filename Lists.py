#1. Set the users varibale to be an empty list
users = []

assert users == [], f"Expected `users` to be [] but got: {repr(users)}"
#2. Add 'Kevin' 'bob' and alice to the users list in that order without reassigning the variables.
users.append('kevin')
users.append('bob')
users.append('alice')

assert users == ['kevin', 'bob', 'alice']

#3. Remove 'bob' from the `users` list without reassining the variables
del users[1]

assert users == ['kevin', 'alice'], f"Expected `users` to be ['kevin', 'alice'] but got: {repr(users)}"

#4. Reverse the users list and assign the results to `reverse_users`

rev_user = list(reversed(users))

print(rev_user)

assert rev_user == ['alice', 'kevin'], f"Expected `rev_user` to be ['alice', 'kevin'] but got: {repr(rev_user)}"

#5. Add the user 'melody' to users where 'bob' used to be
users.insert(1, 'Melody')

assert users == ['kevin', 'Melody', 'alice'], f"Expected `rev_user` to be [  'kevin', 'Melody', 'alice'] but got: {repr(users)}" 

#6. Add the users 'andy', 'wanda', and 'jim', to the users  list using a single command
users += ('andy', 'wanda', 'jim')

print(users)
#assert users == ['kevin', 'alice', 'andy', 'wanda', 'jim'], f"Expected `users` to be ['kevin', 'alice', 'andy', 'wanda', 'jim'] but got: {repr(users)}"

#7. Slice the users lists to return the 3rd and 4th items and assing the results to `center users`

center_users = users[2:4]

assert center_users == ['alice','andy'], f"Expected `center_users` to be ['andy','wanda'] but got : {repr(center_users)}"





