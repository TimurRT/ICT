import csv

class Charscter_sims():

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

class Person_eat:

    def eat_smthg(self, person, product_name, count):
        with open("message_file.csv", "a+", newline='') as message_file:
            person_eat = person
            food = product_name
            food_count = count
            person_eat_information = (f'Кушал:{person_eat},'
                    f''f'Съел:{food},'
                    f''f'Количество:{food_count},')
            writer = csv.writer(message_file)
            writer.writerow([person_eat_information])

    def eat_smithing(self,person, product_name, count):
        with open('food.csv', 'a') as file:
            file.write(f'{person},{product_name},{count}')

eat = Person_eat()

person = Charscter_sims('Tom', 'Soros', 30)
eat.eat_smthg(person, 'Шоколадка', 3)
