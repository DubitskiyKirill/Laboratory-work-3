import unittest
from main import app
class TestStringMethods(unittest.TestCase):
    def test_page(self):  # тестируем функцию, которая отвечает за главную страницу
        tester = app.test_client(self)  # создаем клиент для тестирования
        response = tester.get('/')  # отправляем GET-запрос на главную страницу
        self.assertEqual(response.status_code, 200)  # проверяем, что код ответа равен 200

    def test_konvert_type_1(self):#Проверка перевода в доллары
        tester = app.test_client(self)  # создаем клиент для тестирования
        response = tester.post("/", content_type='multipart/form-data', data={'num_1': 1000, 'options': 1})#Ввод параметров
        self.assertIn('12.490632025980513', response.data.decode())

    def test_konvert_type_2(self):  #Проверка перевода в евро
        tester = app.test_client(self)  # создаем клиент для тестирования
        response = tester.post("/", content_type='multipart/form-data', data={'num_1': 1000,'options': 2})  # Ввод параметров
        self.assertIn('11.641443538998836', response.data.decode())

    def test_konvert_type_3(self):  # #Проверка перевода из долларов
        tester = app.test_client(self)  # создаем клиент для тестирования
        response = tester.post("/", content_type='multipart/form-data', data={'num_1': 100, 'options': 3})  # Ввод параметров
        self.assertIn('8006.', response.data.decode())

    def test_konvert_type_4(self):  # #Проверка перевода из евро
        tester = app.test_client(self)  # создаем клиент для тестирования
        response = tester.post("/", content_type='multipart/form-data', data={'num_1': 100, 'options': 4})  # Ввод параметров
        self.assertIn('8590.', response.data.decode())

if __name__ == '__test__':
    unittest.test()