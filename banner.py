def generate_banner():
    banner = r"""
  ____  _   _    _    _   _ ____  ___    _    ____   
 / ___|| | | |  / \  | | | |  _ \|_ _|  / \  |  _ \  
 \___ \| |_| | / _ \ | |_| | |_) || |  / _ \ | |_) | 
  ___) |  _  |/ ___ \|  _  |  _ < | | / ___ \|  _ <  
 |____/|_| |_/_/   \_\_| |_|_| \_\___/_/   \_\_| \_\ 
                                                     
"""
    print(banner)

def menu():
    print("Welcome to Your Termux Tool!")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("You selected Option 1")
        print("Link: www.youtube.com")
    elif choice == "2":
        print("You selected Option 2")
        # Add the functionality for Option 2
    elif choice == "3":
        print("You selected Option 3")
        # Add the functionality for Option 3
    elif choice == "4":
        print("Exiting...")
        return
    else:
        print("Invalid choice. Please try again.")
        menu()

# Call the function to generate the banner
generate_banner()

# Call the menu function to display the menu and handle user input
menu()
