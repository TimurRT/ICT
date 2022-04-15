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

    FilePath_user_information = os.path.join(f"{same_directory + str(i)}", 'user_info.txt')
    with open(FilePath_user_information, 'w') as file:
        file.write(f"Email: {user_email}\n")
        file.write(f"Имя: {user_first_name}\n")
        file.write(f"Фамилия: {user_last_name}\n")


    user_photo = requests.get(f'https://reqres.in/img/faces/{str(i)}-image.jpg')
    FilePath_user_photo = os.path.join(f"{same_directory + str(i)}", 'user_photo.jpg')
    with open(FilePath_user_photo, 'wb') as file:
        file.write(user_photo.content)