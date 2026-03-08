import sys
import port_scanner
import brute_forcer

def main_menu():
    while True:
        print("\n--- CODTECH PENETRATION TESTING TOOLKIT ---")
        print("1. Port Scanner")
        print("2. Brute Force Tool")
        print("3. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            target = input("Enter Target IP: ")
            port_scanner.scan_target(target)
        elif choice == '2':
            pwd = input("Enter Mock Password to Crack: ")
            brute_forcer.brute_force_login(pwd)
        elif choice == '3':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main_menu()
