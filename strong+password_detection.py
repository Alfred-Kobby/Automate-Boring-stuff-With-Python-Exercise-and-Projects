import re

password_matcher = re.compile(r'^(?=.*[A-Z])(?=.*\W)(?=.*[a-z])(?=.*\d).{8,}$')
strong_password = password_matcher.match("mnpwo1@Twtt")

if strong_password is None:
    print("Password is weak")
else:
    print("Password is strong")
