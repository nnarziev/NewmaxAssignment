from typing import List

class Node:
	def __init__(self, val=None, next=None):
		self.val = val
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None

	def insert_at_end(self, val: int):
		if val < 0 or val > 9:
			raise Exception('Every node in linked list must have value in range [0,9]')

		if self.head is None:
			self.head = Node(val, None)
			return
		itr = self.head
		while itr.next:
			itr=itr.next

		itr.next = Node(val, None)

	def insert_values(self, values: List[int]):
		for value in values:
			self.insert_at_end(value)
		self.validate_length()

	def validate_length(self):
		if self.get_length() < 1 or self.get_length() > 100:
			raise Exception('Length of linked list must be in range [1,100]')

	def get_length(self):
		cnt=0
		itr=self.head
		while itr:
			cnt+=1
			itr=itr.next
		return cnt
	
	def get_concatenated_values(self) -> str:
		itr=self.head
		result=''
		while itr:
			result+=str(itr.val)
			itr=itr.next
		return result


	def to_list(self):
		if self.head is None:
			print("Linked List is empty")
			return

		iter = self.head
		values_list=[]
		while iter:
			values_list.append(iter.val)
			iter = iter.next

		return values_list			
	
class Helpers:
	def reverse_string(data: str):
		return data[::-1]

	def get_sum(l1: LinkedList, l2: LinkedList) -> LinkedList:
		num1 = int(Helpers.reverse_string(l1.get_concatenated_values()))
		num2 = int(Helpers.reverse_string(l2.get_concatenated_values()))
		sum_list = [int(val) for val in Helpers.reverse_string(str(num1+num2))]

		result_ll = LinkedList()
		result_ll.insert_values(sum_list)

		return result_ll