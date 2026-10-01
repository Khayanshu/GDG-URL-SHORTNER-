# Mini URL Shortener

import random

FILE_NAME = "urls.txt"
LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def ensure_file():
    with open(FILE_NAME, "a", encoding="utf-8"):
        pass

def read_lines():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        ensure_file()
        return []

def make_code():
    lines = read_lines()
    while True:
        code = ""
        for _ in range(6):
            code += random.choice(LETTERS)

        used = any(line.split()[0] == code for line in lines if line.strip())
        if not used:
            return code

def shorten():
    url = input("Enter URL: ").strip()
    if not (url.startswith("http://") or url.startswith("https://")):
        print("Invalid URL. It must start with http:// or https://")
        return
    if " " in url:
        print("Invalid URL. It cannot have spaces.")
        return

    code = make_code()
    with open(FILE_NAME, "a", encoding="utf-8") as f:
        f.write(code + " " + url + "\n")
    print("Short code:", code)

def resolve():
    code = input("Enter short code: ").strip()
    for line in read_lines():
        parts = line.strip().split()
        if parts and parts[0] == code:
            print("Original URL:", parts[1])
            return
    print("Code not found.")

def show_list():
    lines = read_lines()
    if len(lines) == 0:
        print("Nothing saved yet.")
        return

    for line in lines:
        parts = line.strip().split()
        if parts:
            print(parts[0], "->", parts[1])

ensure_file()
while True:
    print()
    print("1. Shorten a URL")
    print("2. Get original URL from a code")
    print("3. List all URLs")
    print("4. Quit")
    choice = input("Choose (1-4): ").strip()
    if choice == "1":
        shorten()
    elif choice == "2":
        resolve()
    elif choice == "3":
        show_list()
    elif choice == "4":
        break
    else:
        print("Please type 1, 2, 3 or 4.")
