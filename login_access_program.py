# Simple Login System

ADMIN_NAME = "admin"
ADMIN_PASSWORD = "1122"
ADMIN_EMAIL = "admin1122@gmail.com"


def login():
    print("=== Login System ===")

    name = input("Enter your name: ").strip()
    password = input("Enter your password: ").strip()
    email = input("Enter your email: ").strip()

    if name == ADMIN_NAME and password == ADMIN_PASSWORD and email == ADMIN_EMAIL:
        print(f"\nWelcome Admin {name} ✅")
    else:
        print("\nWrong credentials ❌")


login()
