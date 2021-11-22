
import sys

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

def removeFirstNode(head):
	if not head:
		return None
	temp = head

	head = head.next
	temp = None
	return head

def push(head, data):
	if not head:
		return Node(data)
	temp = Node(data)
	temp.next = head
	head = temp
	return head

if __name__=='__main__':

	head = None

	head = push(head, 12)
	head = push(head, 29)
	head = push(head, 11)
	head = push(head, 23)
	head = push(head, 8)

	head = removeFirstNode(head)
	
	while(head):
		print("{} ".format(head.data), end ="")
		head = head.next

