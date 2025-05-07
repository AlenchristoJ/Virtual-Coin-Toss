import random
def coin_toss():
    result = random.choice(["Heads", "Tails"])
    return result
def run_session():
    print("Welcome to the Virtual Coin Toss!")
    print("----------------------------------") 
    while True:
        try:
            num_flips = int(input("How many times would you like to flip the coin? "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        heads_count = 0
        tails_count = 0
        for i in range(num_flips):
            result = coin_toss()
            print(f"Flip {i + 1}: {result}")
            if result == "Heads":
                heads_count += 1
            else:
                tails_count += 1
        total = heads_count + tails_count
        if total > 0:
            heads_percentage = (heads_count / total) * 100
            tails_percentage = (tails_count / total) * 100
        else:
            heads_percentage = 0
            tails_percentage = 0
        print("\n--- Results ---")
        print(f"Heads: {heads_count} ({heads_percentage:.2f}%)")
        print(f"Tails: {tails_count} ({tails_percentage:.2f}%)")
        choice = input("\nDo you want to flip again? (yes/no): ").lower()
        if choice != "yes":
            print("Thanks for playing! Goodbye!")
            break
        print("\nRestarting the session...\n")
run_session()
