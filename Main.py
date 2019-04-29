from room import Room


def house_carpet():
    try:
        house = []
        total_square_meters = 0

        print('Welcome to the carpet company')
        print('===================================')
        rooms = int(input('How many room would you like carpeted? '))
        counter = 0

        while rooms > 0:
            counter += 1
            width = int(input('Please enter the rooms width: '))
            length = int(input('Please enter the rooms length: '))
            unit_of_measurement = str(input('Please enter the rooms unit of measurement: '))

            new_room = Room(width, length, unit_of_measurement)
            new_room.calculate_area()
            new_room.print_details()

            total_square_meters += new_room.calculate_area()

            house.append('Room ' + str(rooms))
            house.append(new_room.width)
            house.append(new_room.length)
            rooms -= 1

        house.append(total_square_meters)

        stairs_price = ()
        stairs = input('Does the house have any stairs? Yes/No ')
        if stairs.lower() == 'yes':
            no_of_stairs = int(input('How many steps are there in total? '))
            stairs_price = no_of_stairs * 5

        carpet_price = 0
        carpet_type = int(input('Would you like Wool Carpet 1) or Polyester Carpet 2)'))
        if carpet_type == 1:
            carpet_price = total_square_meters * 30
        elif carpet_type == 2:
            carpet_price = total_square_meters * 20
        else:
            print('Oops! You made an error')

        if total_square_meters <= 20:
            labour_cost = 60
        else:
            labour_cost = 100

        total_cost = stairs_price + labour_cost + carpet_price

        print('===================================')
        print('===================================')
        print('Number of Rooms       ', counter)
        print('Total Meters Squared  ', total_square_meters.__round__(2))
        print('===================================')
        print('Carpet Cost          €', carpet_price.__round__(2))
        print('Stairs Cost          €', stairs_price)
        print('Labour Cost          €', labour_cost)
        print('===================================')
        print('Total Cost           €', total_cost.__round__(2))

        finish = str(input('Would you like to price another house? Yes/No '))
        if finish.lower() == 'yes':
            house_carpet()
        else:
            print('Thank you for visiting.')

    except Exception:
        print('You entered incorrect data. Please re-submit your info')


house_carpet()
