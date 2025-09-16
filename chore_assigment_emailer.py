import ezgmail
import random

emails = []
chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']

for i in range(3):
    email_address = input(f'Enter {i + 1} email address for chore assignment: \n')
    emails.append(email_address)


# Initialize ezgmail
ezgmail.init()

# About to assign chores per email
assigned_chores = {}
for i in range(len(chores)):
    randomChore = random.choice(chores)
    randomEmail = random.choice(emails)
    chores.remove(randomChore)
    assigned_chores.setdefault(randomEmail, randomChore)

for k, v in assigned_chores.items():
    email_message_body = f'You have been assigned chore {v}'
    ezgmail.send(k, "Chores", email_message_body)
