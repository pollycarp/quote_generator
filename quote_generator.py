# import the random module to help[ us select a random quote
import random


# function to load quotes from a text file
def load_quotes(filename):
    """
    reads the quotes from the given file. Each line is considered as a seperate line. Return a list of quotes.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        # Read all lines in the file
        quotes = file.readlines()
    # Remove any leading/trailing whitespace and empty lines
    return [quote.strip() for quote in quotes if quote.strip()]


# Function to pick one random quote from the list
def get_random_quote(quotes):
    """
    Returns a random quote from the list of quotes.
    """
    return random.choice(quotes)


# Main function - entry point of the program
def main():
    # Load quotes from the text file
    quotes = load_quotes('quotes.txt')

    # Get a random quote
    random_quote = get_random_quote(quotes)

    # Display quote to the user
    print("\n🍃 Your Quote of the Day 🍃")
    print(f'"{random_quote}"\n')


# This ensures the main() functiom runs only if this file is executed directly
if __name__ == "__main__":
    main()
