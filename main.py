import requests
import os
import json

directory_user_data = 'user_data'
directory_users = 'user_'
same_directory = 'user_data/user_'

os.mkdir(directory_user_data)

for i in range(7, 13):
    os.mkdir(same_directory + str(i))

    user = json.loads(requests.get('https://reqres.in/api/users', params={'id': str(i)}).text)
    user_email = user['data']['email']
    user_first_name = user['data']['first_name']
    user_last_name = user['data']['last_name']

    with open(f'user_{str(i)}.txt', 'w+') as file:
        file.write(f"Email: {user_email}\n")
        file.write(f"Имя: {user_first_name}\n")
        file.write(f"Фамилия: {user_last_name}\n")

    os.replace(f'user_{str(i)}.txt', f'user_data/user_{str(i)}/user_{str(i)}.txt')

    user_photo = requests.get(f'https://reqres.in/img/faces/{str(i)}-image.jpg')
    with open(f"file_{str(i)}.jpg", 'wb') as file:
        file.write(user_photo.content)

    os.replace(f'file_{str(i)}.jpg', f'user_data/user_{str(i)}/file_{str(i)}.jpg')