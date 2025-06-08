# # import the random module to help[ us select a random quote
# import random
#
#
# # function to load quotes from a text file
# def load_quotes(filename):
#     """
#     reads the quotes from the given file. Each line is considered as a seperate line. Return a list of quotes.
#     """
#     with open(filename, 'r', encoding='utf-8') as file:
#         # Read all lines in the file
#         quotes = file.readlines()
#     # Remove any leading/trailing whitespace and empty lines
#     return [quote.strip() for quote in quotes if quote.strip()]
#
#
# # Function to pick one random quote from the list
# def get_random_quote(quotes):
#     """
#     Returns a random quote from the list of quotes.
#     """
#     return random.choice(quotes)
#
#
# # Main function - entry point of the program
# def main():
#     # Load quotes from the text file
#     quotes = load_quotes('quotes.txt')
#
#     # Get a random quote
#     random_quote = get_random_quote(quotes)
#
#     # Display quote to the user
#     print("\n🍃 Your Quote of the Day 🍃")
#     print(f'"{random_quote}"\n')


# import the requests module to make the HTTP requests
import requests


# Function to get a random quote from the quotable API
def get_random_quote():
    """
    Fetches a random quote from the quotable API
    Returns the quote content and the author.
    """
    try:
        # URL of the Quotable API endpoint
        url = "https://zenquotes.io/api/quotes"

        # Make a get request to the API
        response = requests.get(url)

        # Raise an error if the request failed (status code != 200)
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Extract the quote text and author
        quote = data[0]['q']
        author = data[0]['a']

        return quote, author

    except requests.RequestException as e:
        # Handle network error gracefully
        print(f"Error fetching quote: {e}")
        return None, None


# Main function - entry point of the program
def main():
    # Get a random quote
    quote, author = get_random_quote()

    # Check if we got a valid quote
    if quote:
        print("\n🍃 Your Qoute of the Day 🍃")
        print(f'"{quote}')
        print(f'- {author}\n')
    else:
        print("Could not retreive a quote at this time. Please try again later")


# This ensures the main() functiom runs only if this file is executed directly
if __name__ == "__main__":
    main()
