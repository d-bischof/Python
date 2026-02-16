def ticketSeller() -> None:

<<<<<<< HEAD
    total_tickets: int = 0

    while True:

        ticket = input("Please enter the amount of tickets to buy (max 4): ")
=======
    all_tickets: int = 0

    while True:

        ticket = input("You can purchase up to 4 tickets how many would you like?: ")
>>>>>>> 2bd522c9d036328f01c6d18a8d69d7513e710e11
        try:
        #need to make user enters a non-zero integer that is not over 4
            ticket = int(ticket)
            if ticket > 4 or ticket <= 0:
                print("Please enter a number 1-4")
                continue

        except ValueError as e:
            print(e, "Please enter a number")
            continue

<<<<<<< HEAD
        total_tickets += ticket

        #enforce our constraint that only 20 tickets are available
        if total_tickets >= 20:
=======
        all_tickets += ticket

        #enforce our constraint that only 20 tickets are available
        if total_tickets >= 10:
>>>>>>> 2bd522c9d036328f01c6d18a8d69d7513e710e11
            print("Sorry there are no more tickets")
            break


def main():
    ticketSeller()

if __name__ == '__main__':
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> 2bd522c9d036328f01c6d18a8d69d7513e710e11
