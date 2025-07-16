#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Secure Password Generator
Author: Your Name
Date: 2025
Description: Generates secure passwords with customizable criteria
"""

import secrets
import string
import random
import os

class PasswordGenerator:
def __init__(self):
self.uppercase = string.ascii_uppercase
self.lowercase = string.ascii_lowercase
self.numbers = string.digits
self.symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
self.ambiguous_characters = "001Il"

def clear_screen(self):
"""Clears the terminal screen"""
os.system('cls' if os.name == 'nt' else 'clear')

def show_title(self):
"""Displays the program title"""
print("=" * 40)
print("🔐 SECURE PASSWORD GENERATOR")
print("=" * 40)

def get_password_length(self):
"""Gets the desired password length"""
while True:
try:
length = int(input("Password length (8-128): "))
if 8 <= length <= 128:
return length
else:
print("❌ Length must be between 8 and 128 characters!")
except ValueError:
print("❌ For Please enter a valid number!")

def get_options(self):
"""Gets the character type options"""
opc
