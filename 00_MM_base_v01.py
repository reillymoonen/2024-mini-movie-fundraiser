# functions go here

# Checks user has entered yes / no to a question
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("PLease enter yes or no")


# checks that user response is not blank
def not_blank(question):
    while True:
        response = input(question)

        # if the response is blank, output error
        if response == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return response


# main routine starts here

# set maximum number of tickets below
MAX_TICKETS = 3
tickets_sold = 0

want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes":
    print("Instructions go here")

print()

# loop to sell tickets
while tickets_sold < MAX_TICKETS:
    name = not_blank("Enter your name (or 'xxx' to quit) ")

    if name == 'xxx':
        break

    tickets_sold += 1

# output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congratulations you have sold all the tickets")
else:
    print("You have sold {} ticket/s. There is {} ticket/s"
          "remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))
