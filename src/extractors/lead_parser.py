thonpython
class LeadParser:
 """Parses unstructured lead dictionaries."""

 def parse(self, raw: dict) -> dict:
 return {
 "name": raw.get("name", "").strip(),
 "company": raw.get("company", "").strip(),
 "title": raw.get("title", "").strip(),
 "email": raw.get("email", "").strip(),
 "phone": raw.get("phone", "").strip(),
 "website": raw.get("website", "").strip(),
 "linkedin": raw.get("linkedin", "").strip(),
 "location": raw.get("location", "").strip(),
 }