class Airline:
    # Статические поля
    default_id = ''
    Destination = 'No name'
    Flight_number = ''
    Aircraft_type = 'No type'
    Departure_time = 'No time'
    DaysOfTheWeek = 'No day'


    def __init__(self, id, name, number, type, time, day):
        self.id_airline = id
        self.destination = name
        self.number_airline = number
        self.type_airline = type
        self.time_airline = time
        self.day_airline = day


    def get_id(self):
        return self.id_airline

    def get_destination(self):
        return self.destination

    def get_number(self):
        return self.number_airline

    def get_address(self):
        return self.type_airline

    def get_time(self):
        return self.time_airline

    def get_day(self):
        return self.day_airline



def info(item):
    print(f'Destination: {AlltheAirlines[item].get_destination()}')
    print(f'Number_airline {AlltheAirlines[item].get_number()}')
    print(f'Time_airline {AlltheAirlines[item].get_time()}')
    print(f'Day of the week {AlltheAirlines[item].get_day()}')
    print(f'Airline id: {AlltheAirlines[item].get_id()}')
    print('---------------')


AlltheAirlines = [Airline('12a', 'Moscow', 'SU1234', 'Пассажирский', '12:25', 'Понедельник'),
                  Airline('13b', 'London', 'SA1234', 'Пассажирский', '13:30', 'Вторник'),
                  Airline('14d', 'London', 'SM3214', 'Пассажирский', '13:30', 'Понедельник'),
                  Airline('15a', 'London', 'SA1234', 'Пассажирский', '15:30', 'Четверг'),
                  Airline('15b', 'Paris', 'SQ9876', 'Пассажирский', '13:40', 'Понедельник'),
                  Airline('15c', 'London', 'SA1234', 'Пассажирский', '12:20', 'Среда'),
                  Airline('16a', 'Paris', 'SQ9876', 'Пассажирский', '12:40', 'Четверг'),
                  Airline('16b', 'Moscow', 'SQ9876', 'Пассажирский', '17:40', 'Воскресенье'),
                  Airline('16c', 'Paris', 'SQ9876', 'Пассажирский', '13:40', 'Суббота'),
                  Airline('17a', 'Moscow', 'SM5643', 'Пассажирский', '18:30', 'Воскресенье'),
                  Airline('17b', 'London', 'SM5643', 'Пассажирский', '18:20', 'Суббота'),
                  Airline('17c', 'Paris', 'GH1999', 'Пассажирский', '11:40', 'Понедельник'),
                  Airline('18a', 'Paris', 'KL1767', 'Пассажирский', '11:20', 'Вторник'),
                  Airline('18b', 'Paris', 'KL1967', 'Пассажирский', '13:50', 'пятница'),
                  Airline('18c', 'London', 'KS1967', 'Пассажирский', '21:50', 'Понедельник'),
                  Airline('19a', 'Moscow', 'TR1634', 'Пассажирский', '22:20', 'Вторник'),
                  Airline('19b', 'London', 'TR1967', 'Пассажирский', '11:30', 'Среда'),
                  Airline('19c', 'Paris', 'BN1967', 'Пассажирский', '13:40', 'Понедельник'),
                  Airline('20a', 'Moscow', 'KL3217', 'Пассажирский', '22:40', 'Четверг')]



def search_destination(d):
    for i in range(len(AlltheAirlines)):
        if AlltheAirlines[i].get_destination() == d:
            info(i)


def search_day(f):
    for i in range(len(AlltheAirlines)):
        if AlltheAirlines[i].get_day() == f:
            info(i)



des = input('Enter destination:Moscow,London,Paris \n')
search_destination(des)
week = (input('Enter the day of the week  \n'))
search_day(week)