thonpython
import re

def verify_email(email: str) -> str:
 if not email:
 return ""
 pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
 return email if re.match(pattern, email) else ""

def format_phone(phone: str) -> str:
 if not phone:
 return ""
 digits = re.sub(r"\D", "", phone)

 if len(digits) == 10:
 return f"+1 {digits[:3]} {digits[3:6]} {digits[6:]}"
 elif len(digits) > 10:
 return f"+{digits[:-10]} {digits[-10:-7]} {digits[-7:-4]} {digits[-4:]}"
 return phone