import re

def generate_email(name, website):
    if not name or not website or website == "Not Available":
        return None
    
    domain = website.replace("https://", "").replace("http://", "").split("/")[0]
    first = name.split()[0].lower()

    return f"{first}@{domain}"

def validate_email(email):
    if not email:
        return None

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return email if re.match(pattern, email) else None