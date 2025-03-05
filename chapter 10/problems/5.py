import datetime

class train:
    sector = "Railways"
    seat = 500
    count = 0
    fare = "Rs 600"

    def __init__(self):
        print(f"Welcome to {self.sector}")
        print("============================\n")

    def status(self):
        print(f"No. of seats available: {self.seat}")
        print(f"Train fare: {self.fare}")

    def bookTicket(self, name,fromStation,toStation):
        if train.seat > 0:
            train.seat -= 1
            train.count += 1  # ✅ Correctly increment the count
            seat_no = train.count  # ✅ Assign seat number before printing

            print("Your ticket booking is successful!\n")
            print(f"TICKET Info:\nCustomer Name: {name}\nSeat No: {seat_no}")
            print(f"Train journey :\n\t FROM -> {fromStation} \n\t To -> {toStation} ")
            print(f"Booking Time: {datetime.datetime.now()}\n")  # ✅ Correct datetime usage
        else:
            print("Sorry, no seats available!")

        
customer1 = train()
customer1.status()
customer1.bookTicket("Riddhi","Kolkata","Howrah")

customer2 = train()
customer2.status()
customer2.bookTicket("Rohan","Palta","Khardah")