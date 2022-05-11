import requests
import os
import json
from threading import Thread

page_number = int(input("Введи номер страницы \t"))
users = json.loads(requests.get(f'https://reqres.in/api/users?page={page_number}').text)
user = users['data']
directory = 'user_data/'
os.mkdir(directory)


def parse_data():

    for i in range(len(user)):
        same_directory = directory + 'id_' + str(user[i]['id'])
        os.mkdir(same_directory)
        with open(same_directory + "/user_info.txt", 'w+') as file:
            file.write(f"Email: {str(user[i]['email'])}\t"
                       f"Имя: {str(user[i]['first_name'])}\t"
                       f"Фамилия: {str(user[i]['last_name'])}\t")
        with open(same_directory + "/photo.jpg", 'wb') as file:
            response = requests.get(user[i]['avatar'])
            file.write(response.content)

Thread(target=parse_data).start()
Thread(target=parse_data).start()
Thread(target=parse_data).start()
Thread(target=parse_data).start()