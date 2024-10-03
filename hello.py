def greet(name):
    return f"Hello, {name}!"

def farewell(name):
    return f"Goodbye, {name}!"


if __name__ == "__main__":
    while True:
        choice = input("Do you want to greet one person or multiple people? (one/multiple/exit): ").strip().lower()
        if choice == "one":
            name = input("Enter your name: ").strip()
            if name:
                print(greet(name))
            else:
                print("Name cannot be empty.")
        elif choice == "multiple":
            names = input("Enter names separated by commas: ").strip().split(',')
            names = [name.strip() for name in names if name.strip()]
            if names:
                greetings = greet_multiple(names)
                for greeting in greetings:
                    print(greeting)
            else:
                print("Names cannot be empty.")
        elif choice == "exit":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 'one', 'multiple', or 'exit'.")