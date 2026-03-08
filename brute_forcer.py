import itertools
import string
import time

def brute_force_login(target_password):
    # Character set: lowercase letters + digits
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    
    print(f"[*] Starting Brute Force attack...")
    print(f"[*] Charset: {chars}")
    start_time = time.time()

    # Try lengths from 1 to 4 (limited for demo speed)
    for length in range(1, 5):
        for guess in itertools.product(chars, repeat=length):
            attempts += 1
            guess_pwd = ''.join(guess)
            
            # SIMULATION: In real scenario, this would be an HTTP request or SSH attempt
            if guess_pwd == target_password:
                end_time = time.time()
                return (guess_pwd, attempts, end_time - start_time)
                
            # Optional: Print progress every 1000 attempts
            if attempts % 1000 == 0:
               print(f"[*] Trying: {guess_pwd} (Total: {attempts})")

    return (None, attempts, time.time() - start_time)

if __name__ == "__main__":
    target = input("Set a mock password to crack (max 4 chars): ")
    
    print(f"[*] Cracking password hash for target...")
    result, tries, duration = brute_force_login(target)
    
    if result:
        print(f"\n[+] PASSWORD FOUND: {result}")
        print(f"[*] Attempts: {tries}")
        print(f"[*] Time taken: {round(duration, 4)} seconds")
    else:
        print("\n[-] Password not found in range.")
