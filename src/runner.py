thonpython
import json
import logging
from pathlib import Path
from extractors.lead_parser import LeadParser
from extractors.verification_tools import verify_email, format_phone
from outputs.excel_exporter import export_to_excel

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

def load_input_sources():
 input_file = Path("data/inputs.sample.txt")
 if not input_file.exists():
 logging.error("Input file missing: data/inputs.sample.txt")
 return []

 with open(input_file, "r") as f:
 return [line.strip() for line in f if line.strip()]

def load_sample_leads():
 sample_path = Path("data/sample_leads.json")
 if not sample_path.exists():
 logging.error("Missing sample_leads.json")
 return []

 with open(sample_path, "r") as f:
 return json.load(f)

def main():
 logging.info("Starting Lead Scraper...")

 urls = load_input_sources()
 leads_raw = load_sample_leads()

 parser = LeadParser()

 processed_leads = []
 for item in leads_raw:
 parsed = parser.parse(item)

 parsed["email"] = verify_email(parsed.get("email"))
 parsed["phone"] = format_phone(parsed.get("phone"))

 processed_leads.append(parsed)

 out_path = "output.xlsx"
 export_to_excel(processed_leads, out_path)

 logging.info(f"Scraping completed. Exported {len(processed_leads)} leads to {out_path}")

if __name__ == "__main__":
 main()