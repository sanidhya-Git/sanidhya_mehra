import sqlite3


conn = sqlite3.connect("user_data.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    email TEXT PRIMARY KEY,
    password TEXT NOT NULL
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS password_changes (
    email TEXT,
    old_password TEXT,
    new_password TEXT
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS email_changes (
    old_email TEXT,
    new_email TEXT
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS forgot_password_logs (
    email TEXT
)
""")

conn.commit()

def register():
    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()

    try:
        cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
        conn.commit()
        print("Registration successful!")
    except sqlite3.IntegrityError:
        print("This email is already registered.")

def login():
    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()

    cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
    result = cursor.fetchone()

    if result:
        print("You logged in successfully!")
    else:
        print("Login failed: Incorrect email or password.")

def forgot_password():
    email = input("Enter your registered email: ").strip()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    result = cursor.fetchone()

    if result:
        new_password = input("Enter your new password: ").strip()
        cursor.execute("UPDATE users SET password = ? WHERE email = ?", (new_password, email))
        conn.commit()

       
        cursor.execute("INSERT INTO forgot_password_logs (email) VALUES (?)", (email,))
        conn.commit()

        print("Password updated successfully!")
    else:
        print("Email not found.")

def update_password():
    email = input("Enter your email: ").strip()
    current_password = input("Enter your current password: ").strip()

    cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, current_password))
    result = cursor.fetchone()

    if result:
        new_password = input("Enter your new password: ").strip()
        cursor.execute("UPDATE users SET password = ? WHERE email = ?", (new_password, email))
        conn.commit()

        
        cursor.execute("INSERT INTO password_changes (email, old_password, new_password) VALUES (?, ?, ?)",
                       (email, current_password, new_password))
        conn.commit()

        print("Password changed successfully!")
    else:
        print("Incorrect email or current password.")

def change_email():
    current_email = input("Enter your current email: ").strip()
    password = input("Enter your password: ").strip()

    cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (current_email, password))
    result = cursor.fetchone()

    if result:
        new_email = input("Enter your new email: ").strip()
        try:
            cursor.execute("UPDATE users SET email = ? WHERE email = ?", (new_email, current_email))
            conn.commit()

           
            cursor.execute("INSERT INTO email_changes (old_email, new_email) VALUES (?, ?)",
                           (current_email, new_email))
            conn.commit()

            print("Email updated successfully!")
        except sqlite3.IntegrityError:
            print("The new email is already registered.")
    else:
        print("Incorrect email or password.")

def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Forgot Password")
        print("4. Update Password")
        print("5. Change Email")
        print("6. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            forgot_password()
        elif choice == "4":
            update_password()
        elif choice == "5":
            change_email()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

main()
    
