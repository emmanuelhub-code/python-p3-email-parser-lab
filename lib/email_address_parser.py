# your code goes here!

# lib/email_address_parser.py
import re

class EmailAddressParser:
    def __init__(self, addresses):
        self.addresses = addresses

    def parse(self):
        # Split by commas or whitespace
        candidates = re.split(r'[,\s]+', self.addresses.strip())
        # Simple regex for valid emails
        email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
        # Filter only valid emails, remove duplicates, sort alphabetically
        valid_emails = {email for email in candidates if email_pattern.fullmatch(email)}
        return sorted(valid_emails)
