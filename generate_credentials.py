from faker import Faker

faker = Faker('ru_RU')

def generate_random_credentials():
    # Генерируем имя
    first_name = faker.first_name()
    last_name = faker.last_name()
    address = faker.address()
    phone = faker.phone_number()
       
    return first_name, last_name, address, phone