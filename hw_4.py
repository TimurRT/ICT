import requests
import os


directory_user_data = 'user_data'
directory_users = 'user_'
same_directory = 'user_data/user_'



os.mkdir(directory_user_data)
for i in range(1, 7):
    os.mkdir(same_directory + str(i))
    user = requests.get('https://reqres.in/api/users', params={'id': str(i)})
    user = str(user.text)
    with open("user_" + str(i), 'w+') as file:
        file.write(user)



os.replace('user_1', 'user_data/user_1/user_1')
os.replace('user_2', 'user_data/user_2/user_2')
os.replace('user_3', 'user_data/user_3/user_3')
os.replace('user_4', 'user_data/user_4/user_4')
os.replace('user_5', 'user_data/user_5/user_5')
os.replace('user_6', 'user_data/user_6/user_6')