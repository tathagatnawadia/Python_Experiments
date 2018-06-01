class Node:
	def __init__(self):
		self.next = {}
		self.alphabet = None
		self.word_marker = False
	def add_item(self, string):
		if len(string) == 0:
			self.word_marker = True
			return

		key = string[0]
		string = string[1:]

		if key in self.next.keys():
			self.next[key].add_item(string)
		else:
			node = Node()
			self.next[key] = node
			node.add_item(string)
	def search(self, string):
		if len(string) > 0:
			key = string[0]
			string = string[1:]
			if key in self.next.keys():
				self.next[key].search(string)
			else:
				print("No match")
		else:
			if self.word_marker == True:
				print("Matched")
			else:
				print("No match")


a = Node()
a.add_item("abcd")
a.add_item("abced")
a.add_item("black")
print(a)
a.search("black")
