import csv
import requests

# 파일 경로 설정
input_file_path = 'users.csv'
api_url = 'http://127.0.0.1:8000/accounts/signup/'  # Django 서버의 회원 가입 엔드포인트

# 입력 파일 읽고 데이터 변환
def read_and_prepare_user_data(file_path):
    users = {}
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user_id = row['id']
            if user_id not in users:
                users[user_id] = {
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'username': row['username'],
                    'email': row['email'],
                    'password1': 'defaultpassword1234!',
                    'password2': 'defaultpassword1234!',
                }
   
    return list(users.values())

# 사용자 데이터로 회원 가입 API 호출
def register_users(users, api_url):
    for user in users:
        response = requests.post(
            api_url,
            data=user
        )
        if response.status_code == 201:
            print(f"User {user['username']} registered successfully.")
        else:
            print(f"Failed to register user {user['username']}. Response: {response.text}")

users = read_and_prepare_user_data(input_file_path)
register_users(users, api_url)
