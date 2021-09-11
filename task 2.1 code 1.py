# Mail information - By Amaal Nuha Mecci

def mail_info(state,city,zip,house,street): # Parameters to insert mailing info into
    print(f"Your mailing address is: \n {house} {street} \n {city} , {state} {zip}")

# Loop to allow entry of mailing address as many times as desired
while True:
    state = input("Enter your home state in its two letter abbreviation: ")
    # Validation check to ensure that the string consists of only two letters

    while len(state) != 2:
        state = input("Only two letters can be used, please try again: ")
    city = input("Enter your home city: ")
    zip = int(input("Enter your zip code: "))
    house = int(input("Enter your house number: "))
    street = input("Enter your street name: ")

    # System message to ask user to confirm their chosen mailing address or to change it
    message = int(input(f"Mailing information: {state} \n {city} \n {zip} \n {house} \n {street} \n Press 1 to confirm and exit, or press 0 to re-enter your info."))

    # This is to check the inputs from the message prompt to determine whether the loop should end or if the loop must continue
    if message == 1:
        break
    elif message == 0:
        continue


mail_info(state,city,zip,house,street)



