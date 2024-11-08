# password_generator.py
import random
import string

class PasswordGenerator:
    def __init__(self):
        self.uppercase = string.ascii_uppercase
        self.lowercase = string.ascii_lowercase
        self.numbers = string.digits
        self.symbols = string.punctuation
        self.character_pool = ""

    def add_character_pool(self, include_uppercase, include_lowercase, include_numbers, include_symbols):
        self.character_pool = ""
        if include_uppercase:
            self.character_pool += self.uppercase
        if include_lowercase:
            self.character_pool += self.lowercase
        if include_numbers:
            self.character_pool += self.numbers
        if include_symbols:
            self.character_pool += self.symbols

    def generate(self, length):
        if length <= 0 or not self.character_pool:
            raise ValueError("Invalid length or character pool.")
        
        password = ''.join(random.choice(self.character_pool) for _ in range(length))
        return password

    def validate(self, length):
        if length <= 0:
            raise ValueError("Password length must be greater than zero.")
        if not self.character_pool:
            raise ValueError("No character types selected.")
