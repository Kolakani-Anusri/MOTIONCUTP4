import random

def coin_toss():
    """Simulate a single coin toss."""
    return random.choice(['Heads', 'Tails'])

def simulate_coin_flips(num_flips):
    """Simulate multiple coin flips and count the results."""
    heads_count = 0
    tails_count = 0

    for _ in range(num_flips):
        result = coin_toss()
        if result == 'Heads':
            heads_count += 1
        else:
            tails_count += 1

    return heads_count, tails_count

def display_results(heads_count, tails_count, total_flips):
    """Display the results of the coin tosses."""
    print(f"\nTotal Flips: {total_flips}")
    print(f"Heads: {heads_count} ({(heads_count / total_flips) * 100:.2f}%)")
    print(f"Tails: {tails_count} ({(tails_count / total_flips) * 100:.2f}%)")

def main():
    """Main function to run the coin toss simulation."""
    while True:
        try:
            num_flips = int(input("Enter the number of coin flips you want to perform: "))
            if num_flips <= 0:
                print("Please enter a positive integer.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        heads_count, tails_count = simulate_coin_flips(num_flips)
        display_results(heads_count, tails_count, num_flips)

        repeat = input("Do you want to perform another session? (yes/no): ").strip().lower()
        if repeat != 'yes':
            print("Thank you for using the Virtual Coin Toss simulator!")
            break

if __name__ == "__main__":
    main()