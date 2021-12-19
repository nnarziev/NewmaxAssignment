import unittest 
import main
import random


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.l1 = main.LinkedList()

    def test_insert_at_end(self):
        self.l1.insert_at_end(5)
        self.assertEqual(self.l1.to_list(), [5])
        self.l1.insert_at_end(1)
        self.assertEqual(self.l1.to_list(), [5,1])

    def test_insert_at_end_wrong_negative_value(self):
        with self.assertRaises(Exception) as ex:
            self.l1.insert_at_end(-1)        
        self.assertEqual(str(ex.exception), 'Every node in linked list must have value in range [0,9]')

    def test_insert_at_end_wrong_positive_value(self):
        with self.assertRaises(Exception) as ex:
            self.l1.insert_at_end(10)        
        self.assertEqual(str(ex.exception), 'Every node in linked list must have value in range [0,9]')

    def test_insert_values(self):
        values = [1,2,3]
        self.l1.insert_values(values)
        self.assertEqual(self.l1.to_list(), values)

    def test_insert_values_wrong_list_length(self):
        values = [random.randint(0,9) for i in range(110)]
        
        with self.assertRaises(Exception) as ex:
            self.l1.insert_values(values)        
        self.assertEqual(str(ex.exception), 'Length of linked list must be in range [1,100]')

    def test_get_concatenated_values(self):
        values = [1,2,3]
        self.l1.insert_values(values)
        self.assertEqual(self.l1.get_concatenated_values(), '123')


class TestHelpers(unittest.TestCase):

    def setUp(self):
        self.l1 = main.LinkedList()
        self.l2 = main.LinkedList()

    def test_get_sum_case1(self):
        self.l1.insert_values([2,4,3])
        self.l2.insert_values([5,6,4])
        result_ll = main.Helpers.get_sum(self.l1, self.l2)
        self.assertEqual(result_ll.to_list(), [7,0,8])

    def test_get_sum_case2(self):
        self.l1.insert_values([0])
        self.l2.insert_values([0])
        result_ll = main.Helpers.get_sum(self.l1, self.l2)
        self.assertEqual(result_ll.to_list(), [0])

    def test_get_sum_case3(self):
        self.l1.insert_values([9,9,9,9,9,9,9])
        self.l2.insert_values([9,9,9,9])
        result_ll = main.Helpers.get_sum(self.l1, self.l2)
        self.assertEqual(result_ll.to_list(), [8,9,9,9,0,0,0,1])


if __name__ == '__main__':
    unittest.main()
 		