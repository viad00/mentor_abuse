#!/usr/bin/python3
# This is a sample Python script.
import json
from bs4 import BeautifulSoup
import requests
from tests import generate_test


BASE = 'https://mentor.h1n.ru'
HEAD = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
JAR = None
TESTS = {
    #"1. Математический аппарат и общие сведения электродинамики": 535,
    "2.Уравнения Максвелла": 393,  # +
    "3. Комплексная амплитуда поля. Теорема Умова-Пойтинга.": 398,  # +
    "4. Классификация радиоволн.": 408,
    "5. Распространение волн в свободном пространстве": 508,
    "6. Основное уравнение радиолокации": 609,
    "7. Интерференционная формула": 418,
    "8.Упрощение интерференционной формулы": 550,
    "9.Учет факторов поверхности для радиоволн": 424,
}


def login(username='И48316', password='И48316'):
    response = requests.post(url=f'{BASE}/authorization.php',data={'username': username,'password': password},headers=HEAD,allow_redirects=False)
    if response.status_code != 302:
        raise Exception(f'Failed to login! {username}:{password}')
    jar = response.cookies
    JAR = jar
    response = requests.get(url=f'{BASE}/stud_main.php', cookies=jar,
                             headers=HEAD, allow_redirects=True)
    soup = BeautifulSoup(response.text, 'html.parser')
    id = soup.find_all(id='h_id')[0].get('value')
    token = soup.find_all(id='h_aT')[0].get('value')
    name = soup.find_all(id='h_name')[0].get('value')
    return {'id':id, 'token':token, 'name':name, 'jar':jar}


def get_not_passed_tests(user):
    dict = {
        'AccessToken': user['token'],
        'DisciplineId': "114",
        'Sem': "1",
        'StudentId': user['id'],
        'Year': "2020",
    }
    resp = requests.post(f'{BASE}/app_get_test_result.php',headers=HEAD,json=dict,cookies=JAR)
    tests_names = [x["Name"] for x in json.loads(resp.text)['DiaryRecords'] if x["Value"] == "0"]
    tests = [TESTS[x] for x in tests_names if x in TESTS]
    return tests


def pass_test(test,user):
    new_test = [generate_test(test=test,id=user["id"],token=user["token"])]
    resp = requests.post(f'{BASE}/app_write_test_result.php', headers=HEAD, json=new_test, cookies=JAR)
    print(test, resp.text)


if __name__ == '__main__':
    user = login()
    print(f'{user}')
    tests_to_pass = get_not_passed_tests(user)
    print(tests_to_pass)
    #pass_test(test=408,user=user)

