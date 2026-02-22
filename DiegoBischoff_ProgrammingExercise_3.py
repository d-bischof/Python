from functools import reduce

def getUserInput() -> list[float]:

    #keep entered prices here as floats
    priceList: list[float] = []

    #ask for prices until 'exit' entered
    while True:
        userInput = input("Enter a price (or 'exit' to finish): ")

        #quit
        if userInput.lower() == 'exit':
            break

        #strip a leading '$' 
        if userInput and userInput[0] == '$':
            userInput = userInput[1:]
        try:
            #try converting to float and append
            price = float(userInput)
            priceList.append(price)

        except ValueError:
            print("Invalid input. Please enter a valid price or 'exit' to finish.")
            continue

    #return list
    return priceList


def main():
    #pull the list of prices from the prompt function
    prices: list[float] = getUserInput()

    #return if no prices were entered
    if not prices:
        print("No prices entered.")
        return

    #compute total highest and lowest
    total: float = reduce(lambda x, y: x + y, prices)
    highest: float = reduce(lambda x, y: x if x > y else y, prices)
    lowest: float = reduce(lambda x, y: x if x < y else y, prices)

    print()

    #print results formatted to 2 decimal places
    print(f"The highest price is ${highest:.2f}")
    print(f"The lowest price is ${lowest:.2f}")
    print(f"The total price is ${total:.2f}")


if __name__ == "__main__":
    main()