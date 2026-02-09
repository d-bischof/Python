def ticketSeller() -> None:

    total_tickets: int = 0

    while True:

        ticket = input("You can purchase up to 4 tickets how many would you like?: ")
        try:
        #need to make user enters a non-zero integer that is not over 4
            ticket = int(ticket)
            if ticket > 4 or ticket <= 0:
                print("Please enter a number 1-4")
                continue

        except ValueError as e:
            print(e, "Please enter a number")
            continue

        total_tickets += ticket

        #enforce our constraint that only 20 tickets are available
        if total_tickets >= 10:
            print("Sorry there are no more tickets")
            break


def main():
    ticketSeller()

if __name__ == '__main__':
    main()
