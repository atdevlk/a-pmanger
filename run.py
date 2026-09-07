from cryptography.fernet import Fernet, InvalidToken
from rich.prompt import Prompt 
from rich.table import Table
from rich.console import Console
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
import sqlite3
import base64
import hashlib
import tempfile
import os


#define colors
g = "\033[92m"
r = "\033[91m"
rs = "\033[0m"


banner = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡶⢤⡀⠀⠀⠀⢀⡇⡄⠈⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⡇⡄⢙⢦⣀⣀⣼⠁⠂⠀⠀⠙⢦⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠘⡇⡇⠀⠁⡍⠁⠀⠀⠈⠁⠂⠀⢈⠳⡄⠀⠀⠀⠀⠀⠀
⠀⠰⡇⢀⠀⡐⠁⠀⠀⠀⠀⠀⢀⡴⣋⡄⠹⣆⠀⠀⠀⠀⠀
⠀⠀⣗⠈⢅⣀⣀⣀⡀⠀⠀⠀⠛⠛⠤⠤⠤⡸⣆⣠⠟⢲⡄
⠀⠀⣿⠀⠰⠒⣺⠟⠁⢀⣠⠤⠶⡄⡁⠀⢀⠆⢹⠁⣠⠞⠁
⠀⠀⢻⡀⢀⠞⠑⠒⢄⢣⡀⠀⠀⡇⠈⠉⠀⣠⣾⡜⠃⠀⠀
⢀⣤⣼⣇⠈⠠⠤⠄⠊⠀⠑⠤⢠⣃⣠⠴⢛⡿⠋⠀⠀⠀⠀
⠸⢤⣄⣈⡓⡦⠤⠤⠤⠴⠖⠚⠋⠉⠀⢸⡍⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠉⠉⠛⠛⠒⢷⠀⠀⠀⠀⠀⠀⢷⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⡃⠀⠀⠀⠀⠀⠘⡃⠀⠀⠀⠀⠀
  ╭────── · · ୨୧ · · ──────╮
  |        \033[92mA-pmanger\033[0m       |
  ╰────── · · ୨୧ · · ──────╯
"""



console = Console()
session = PromptSession()
completer = WordCompleter(["help", "add", "show"], ignore_case=True)

conn = sqlite3.connect("store")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS passwords(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        password TEXT
        )
               """)

def help():
    h = Table()
    h.add_column("command")
    h.add_column("about")
    #add rows 
    h.add_row("add", "Encrypt and save email and password")
    h.add_row("show", "Data decryption using the key")
    console.print(h)



def manual_key(password: str, salt: bytes = None):
    if salt is None:
        salt = os.urandom(16)
    hash_key = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 200_000)
    key =  base64.urlsafe_b64encode(hash_key), salt
    return key


                                 
def encrypt_file():
    password = Prompt.ask("Enter key: ", password=True)
    key, salt = manual_key(password)
    cipher = Fernet(key)

    with open("store", "rb") as f:
        file_data = f.read()
    
    dir_ = os.path.dirname(os.path.abspath("store.encrypted")) or "."
    fd, temp_path = tempfile.mkstemp(dir=dir_)
    #file encrypt 
    encrypt_data = cipher.encrypt(file_data)
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(salt + encrypt_data)
        os.replace(temp_path, "store.encrypted")
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

    os.system("shred -u -z -n 3 store")



def decrypt_file():
    password = Prompt.ask("Enter password: ", password=True)

    with open("store.encrypted", "rb") as f:
        raw = f.read()
    salt, decrypt_data = raw[:16], raw[16:]
    key, _ = manual_key(password, salt)
    cipher = Fernet(key)
    file_data = cipher.decrypt(decrypt_data)
    
    conn = sqlite3.connect(":memory:")
    conn.deserialize(file_data)
    cur = conn.execute("SELECT * FROM passwords")
    rows = cur.fetchall()
    conn.close()
    #create table with rich
    t = Table()
    t.add_column("ID")
    t.add_column("Email")
    t.add_column("Password")

    for row in rows:
        t.add_row(str(row[0]), str(row[1]), str(row[2]))
    #print table in console
    console.print(t)


print(banner)
wrong_try = 1

while True:
    cmd = session.prompt("Pmanger: ", completer=completer)

    if cmd == "add":
        while True:
            email = Prompt.ask("Enter Email")
            password = Prompt.ask("Enter Password")
            cursor.execute(
                "INSERT INTO passwords(email, password) VALUES (?,?)", 
                (email, password))
            conn.commit()
            encrypt_file()
            break

    elif cmd == "show":
        try:
            decrypt_file()
        except InvalidToken:
            print(f"[{r}!{rs}] invalid key")

    elif cmd == "help":
        help()

    elif cmd == "exit":
        break

    else:
        if wrong_try == 2:
            print(f"[{r}!{rs}]try command: {r}help{rs}")
        else:
            print(f"[{r}!{rs}] Command not found")
        
        wrong_try = wrong_try + 1

    
