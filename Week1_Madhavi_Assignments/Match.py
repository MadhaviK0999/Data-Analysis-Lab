#HW 9 Example : Return true when the given email is correct format otherwise return false for incorrect format.
import re
def validate_email(email):
    pattern = r"[\w\.-]+@[\w\.-]+\.[a-zA-Z]+"
    if re.match(pattern, email):
        return True
    else:
        return False

print("test@example.com -->" ,validate_email('test@example.com') )
print("Hello -->" ,validate_email('Hello ') )
                     
