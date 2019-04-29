from converter import Converter


class Room:
    no_of_rooms = 0

    def __init__(self, width_in, length_in, unit_measurement_in):
        self.width = width_in
        self.length = length_in

        self.unit_of_measurement = unit_measurement_in
        self.no_of_rooms += 1

    def calculate_area(self):
        area = self.width * self.length
        changed_area = Converter.convert_unit(area, self.unit_of_measurement)
        return changed_area

    def print_details(self):
        print('===================================')
        print('Room Measurements')
        print('===================================')
        print('Room Width       ', self.width, 'meters')
        print('Room Length      ', self.length, 'meters')
        print('===================================')
        print('Room Area        ', self.calculate_area().__round__(), 'meters squared')
        print('===================================')

#
# room1 = Room(10, 10, 'yards')
# room1.calculate_area()
# room1.print_details()
#
# room1 = Room(10, 10, 'meters')
# room1.calculate_area()
# room1.print_details()

