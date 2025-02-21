class Hotel:
    def __init__(self, name, total_rooms):
        self.name = name
        self.rooms = [{'room_id': i+1, 'available': True, 'price': 100} for i in range(total_rooms)]  

    def show_available_rooms(self):
        print(f"\nAvailable rooms in {self.name}:")
        available_rooms = [room for room in self.rooms if room['available']]
        if available_rooms:
            for room in available_rooms:
                print(f"Room ID: {room['room_id']}, Price: ${room['price']}")
        else:
            print("No rooms available.")
    
    def book_room(self, room_id):
        room = next((room for room in self.rooms if room['room_id'] == room_id), None)
        if room and room['available']:
            room['available'] = False  
            print(f"\nRoom {room_id} booked successfully!")
            return room
        else:
            print("\nSorry, the room is not available.")
            return None

    def view_bookings(self):
        print(f"\nCurrent bookings in {self.name}:")
        booked_rooms = [room for room in self.rooms if not room['available']]
        if booked_rooms:
            for room in booked_rooms:
                print(f"Room ID: {room['room_id']}, Price: ${room['price']}, Status: Booked")
        else:
            print("No bookings yet.")
            

def main():
    hotel = Hotel("Sunshine Hotel", 5)  

    while True:
        print("\nWelcome to the Hotel Booking System!")
        print("1. View available rooms")
        print("2. Book a room")
        print("3. View current bookings")
        print("4. Exit")
        
        choice = input("\nEnter your choice: ")

        if choice == '1':
            hotel.show_available_rooms()
        elif choice == '2':
            room_id = int(input("\nEnter the room ID you want to book: "))
            hotel.book_room(room_id)
        elif choice == '3':
            hotel.view_bookings()
        elif choice == '4':
            print("Thank you for using the hotel booking system!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()