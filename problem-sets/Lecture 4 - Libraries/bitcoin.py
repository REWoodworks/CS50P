# Bitcoin is a form of digital currency, otherwise known as cryptocurrency. Rather than rely on a central authority like a bank, Bitcoin instead relies on a distributed network, otherwise known as a blockchain, to record transactions.

# Because there’s demand for Bitcoin (i.e., users want it), users are willing to buy it, as by exchanging one currency (e.g., USD) for Bitcoin.

# In a file called bitcoin.py, implement a program that:

# Expects the user to specify as a command-line argument the number of Bitcoins, 𝑛, that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
# Queries the API for the CoinCap Bitcoin Price Index at rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey. You should replace YourApiKey with the actual API key you obtained from your CoinCap account dashboard, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:
# import requests

# try:
#     ...
# except requests.RequestException:
#     ...
# Outputs the current cost of 𝑛 Bitcoins in USD to four decimal places, using , as a thousands separator.

import sys
import requests


def main():

    if len(sys.argv) < 2:
        sys.exit("please enter a number")

    try:
        coin = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=66a0f926a80b44c5d988f9a0e0d72b8fd5cddfd2a333dde7d3b74113e74c615b"
        )

    except requests.RequestException:
        sys.exit("Request exception")
        # print(type(response))
        # print(type(datadict))

    # this entire section is overkill and not required by the projeect,  A keyerror returns here because after 5 calls in a minute, the type assigned to datadict is not a dictionary, though it is a json file.  When the code tries to run a dict function on itm the keys arent there and the key error id returned.
    #
    try:
        datadict = response.json()
        price = float(datadict["data"]["priceUsd"])
    except KeyError:
        sys.exit("Too many attempts, wait one minute")

    print(f"{price * coin:,.4f}")

    # CHECKING a JSON return
    # response = requests.get (some api)
    # data = response.json()
    # json.dumps(data, indent=2)
    # print(data)


main()
