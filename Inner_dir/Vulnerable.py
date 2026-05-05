import os
import subprocess
import sqlite3
import pickle
import requests

# -------------------------------
# 1. Hardcoded Secret
# -------------------------------
API_KEY = "sk-test-1234567890abcdef"   # ⚠ hardcoded secret


# -------------------------------
# 2. Command Injection pattern
# -------------------------------
def run_user_command(user_input):
    # ⚠ vulnerable: user-controlled input passed to shell
    os.system(f"echo Running {user_input}")


# -------------------------------
# 3. eval usage (code injection)
# -------------------------------
def evaluate_expression(expr):
    # ⚠ vulnerable: arbitrary code execution pattern
    return eval(expr)


# -------------------------------
# 4. Insecure deserialization
# -------------------------------
def load_data(data):
    # ⚠ vulnerable: pickle execution
    return pickle.loads(data)


# -------------------------------
# 5. SQL Injection pattern
# -------------------------------
def get_user(username):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE name = '{username}'"  # ⚠ SQL injection
    cursor.execute(query)

    return cursor.fetchall()


# -------------------------------
# 6. Insecure HTTP request
# -------------------------------
def fetch_data(url):
    # ⚠ no timeout / validation
    return requests.get(url)




# -------------------------------
# 8. subprocess misuse
# -------------------------------
def run_subprocess(cmd):
    # ⚠ shell=True
    subprocess.call(cmd, shell=True)


# -------------------------------
# Dummy main
# -------------------------------
if __name__ == "__main__":
    run_user_command("test")
    print(evaluate_expression("2+2"))
