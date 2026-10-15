"""9. Password Validator
Concepts: "until" loop, for over characters, isupper()/islower()/isdigit(), a set of special
characters, flags
Keep asking for a password until it meets all of these rules:
• at least 8 characters
• at least one uppercase letter, one lowercase letter and one digit
• at least one special character from {"!", "@", "#", "$", "%", "&", "*"}
• no spaces
• doesn't contain the word "password" in any case
After each failed attempt, list every rule that was broken, not just the first one."""
special_characters={"!", "@", "#", "$", "%", "&", "*"}
def check_password():
    while True:
        password=input("Enter your password: ")
        #flags
        has_upper=False
        has_lower=False
        has_digit=False
        has_special=False
        has_space=False
        for ch in password:
            if ch.isupper():
                has_upper=True
            if ch.islower():
                has_lower=True
            if ch.isdigit():
                has_digit=True
            if ch in special_characters:
                has_special=True
            if ch ==" ":
                has_space=True
        errors=[]
        if len(password)<8:
            errors.append("Must be 8 characters long")
        if not has_upper:
            errors.append("Must conatin atleast one uppercase letter")
        if not has_lower:
            errors.append("Must contain atleast one lower case letter")
        if not has_digit:
            errors.append("Must conatain atleast one digit")
        if not has_special:
            errors.append("Must conatin atleast one special characters  (! @ # $ % & *)")
        if has_space:
            errors.append("Must not conatin spaces in your password")
        if "password" in password.lower():
            errors.append("Your password must not conatin password as your password")
        if not errors:
            print("The password you have entered is correct")
            break
        print("Passowrd rejected.Do follow the above rules")
        for e in errors:
            print(" -",e)
check_password()

