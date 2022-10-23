# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Room:
    def get_name(self):
        return 42


class Street:
    def get_room(self) -> Room:
        return Room()


class City:
    def get_street(self) -> Street:
        return Street()

    def population(self):
        return 100500


class Country:
    def get_city(self) -> City:
        return City()


class Planet:
    def get_contry(self) -> Country:
        return Country()


class Person:
    def __init__(self, room_number, city_pop):
        self.room_number = room_number
        self.city_pop = city_pop

    def get_person_room(self):
        return self.room_number

    def get_city_population(self):
        return self.city_pop


if __name__ == '__main__':
    city = City()
    room = Room()
    person = Person(room.get_name(), city.population())
    print(person.get_person_room())
    print(person.get_city_population())
