class Mail:
    def __init__(self, email):
        self.email = email

    def used_email(self):
      
        print("The email address is",  self.email.lower())

email = Mail(str(input(f"Enter the email address :")))
email.used_email()

assert email == [   ], f"Expected `rev_user` to be ['alice', 'kevin'] but got: {repr(rev_user)}"

# this is a test for git hub


