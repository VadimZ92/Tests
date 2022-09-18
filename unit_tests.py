from main import directories, documents, new_shelf, delete_number, addition, \
                 traffic, name_output, dir_output, ListAllDoc, main
import unittest
from parameterized import parameterized


class TestFunction(unittest.TestCase):
    # @parameterized.expand([
    #       ("2207 876234", "Василий Гупкин"),
    #       ("11-2", "Геннадий Покемонов"),
    #       ("10006", "Аристарх Павлов")
    #     ])
    def test_name_output(self):
        etalon = "Василий Гупкин"
        result = name_output(documents, number="2207 876234")
        self.assertEqual(etalon, result)
        self.assertIsInstance(result, str)

    def test_dir_output(self):
        etalon = "1"
        result = dir_output(directories, number="2207 876234")
        self.assertEqual(etalon, result)


    def test_ListAllDoc(self):
        etalon = ['passport', '2207 876234', 'Василий Гупкин',
                  'invoice', '11-2', 'Геннадий Покемонов',
                  'insurance', '10006', 'Аристарх Павлов']
        result = ListAllDoc(documents)
        self.assertEqual(etalon, result)



    def test_addition(self):
        etalon = [{'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
                  {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
                  {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'},
                  {'type': 'passport', 'number': '123', 'name': 'ivan'}],\
                  {'1': ['2207 876234', '11-2', '5455 028765', '123'], '2': ['10006'], '3': []}
        result = addition(documents, directories, name="ivan", type="passport", number="123", direct="1")
        self.assertEqual(etalon, result)


    def test_delete_number(self):
        etalon = [{'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
                  {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},],\
                  {'1': ['2207 876234', '11-2', '5455 028765'], '2': [], '3': []}
        result = delete_number(documents, directories, number="10006")
        self.assertEqual(etalon, result)


    def test_traffic(self):
        etalon = {'1': ['2207 876234', '5455 028765'], '2': ['10006'], '3': ['11-2']}
        result = traffic(directories, number="11-2", direct="3")
        self.assertEqual(etalon, result)


    def test_new_shelf(self):
        etalon = {'1': ['2207 876234', '11-2', '5455 028765'], '2': ["10006"], '3': [], '4': []}
        result = new_shelf(directories, direct='4')
        self.assertEqual(etalon, result)


if __name__ == "__main__":
    unittest.main()

