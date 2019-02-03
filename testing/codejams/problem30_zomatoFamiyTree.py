class Utility:
	@staticmethod
	# Python code to remove duplicate elements 
	def RemoveDuplicates(duplicate, exclusions):
		final_list = []
		for num in duplicate: 
			if num not in final_list and num not in exclusions:
				final_list.append(num)
		return final_list 

class Entity:
	def __init__(self, name, date_of_birth, sex):
		self.name = name
		self.date_of_birth = date_of_birth
		self.sex = sex

class GovernmentProof:
	def __init__(self, aadhar_id):
		self.aadhar_id = aadhar_id

class Relationship:
	def __init__(self, relationship_type):
		self.relationship_type = relationship_type
 
class Partner(Relationship):
	def __init__(self):
		Relationship.__init__(self, "Partner")
		self.start_date = ""
		self.type_of_partner = "marriage"

class Child(Relationship):
	def __init__(self):
		Relationship.__init__(self, "Child")
		self.type_of_child = "Legal"

class Parent(Relationship):
	def __init__(self):
		Relationship.__init__(self, "Parent")

class Relationships:
	def __init__(self):
		self.relationships = {
			Partner : [],
			Child : [],
			Parent : []
		}

	# TODO : some rules to be coded
	# A child can/cant have more than 2 parents maybe
	# Children can had out of marriage (illegal kids) 
	# Nodes with multiple partners ?? (bcoz why not, adultry is allowd now)

	def add_child(self, children_with_partners):
		for child in children_with_partners:
			self.add_child(child[0], child[1])

	def add_child(self, child, partner=None):
		if partner is None and len(self.relationships[Partner]) == 0 :
			# Add links from the parent 1 to child with no partner
			self.relationships[Child] = [(child)]
			# Add links from the child back to the single parent
			child.relationships[Parent] = [self]
		else:
			try:
				# Add links from the parent 1 to child with partner
				self.relationships[Child].append((child, partner))
				# Add links from the parent 2 to child with partner
				partner.relationships[Child].append((child, partner))
				# Add links from the child back to the parents
				child.relationships[Parent] = [self, partner]
			except:
				print("No partner specified")

	def add_partner(self, partner):
		# If partner not added already
		if partner not in self.relationships[Partner] and self not in partner.relationships[Partner]:
			# Link person 1 with person 2 as partner
			self.relationships[Partner].append(partner)
			# Link person 2 with person 1 as partner
			partner.relationships[Partner].append(partner)


class Person(Entity, GovernmentProof, Relationships):
	"""docstring for Person"""
	def __init__(self, name, sex, date_of_birth="", aadhar_id=""):
		Entity.__init__(self, name, date_of_birth, sex)
		GovernmentProof.__init__(self, aadhar_id)
		Relationships.__init__(self)

	def __repr__(self):
		return str(vars(self))

	def log(self):
		print(self.name + " has " + str(len(self.relationships[Partner])) + " partner, " + str(len(self.relationships[Child])) + " child, " + str(len(self.relationships[Parent])) + " parent")


class RelationshipManager:
	root_node = None
	# TODO : sex may not be the only point of filtering
	@staticmethod
	def get_children(node, sex=None):
		child_list = []
		for child in node.relationships[Child]:
			if sex is not None and child[0].sex == sex:
				child_list.append(child[0])
			if sex is None:
				child_list.append(child[0])
		return child_list

	@staticmethod
	def get_partner(node, sex=None):
		partner_list = []
		for partner in node.relationships[Partner]:
			if sex is not None and partner.sex == sex:
				partner_list.append(partner)
			if sex is None:
				partner_list.append(partner)
		return partner_list

	@staticmethod
	def get_parent(node, sex=None):
		parent_list = []
		for parent in node.relationships[Parent]:
			if sex is not None and parent.sex == sex:
				parent_list.append(parent)
			if sex is None:
				parent_list.append(parent)
		return parent_list


	@staticmethod
	def find_name(name, node):
		if node.name == name:
			return node
		for partner in RelationshipManager.get_partner(node):
			if partner.name == name:
				return partner

		for child in RelationshipManager.get_children(node):
			if_found = RelationshipManager.find_name(name, child)
			if if_found is not None:
				return if_found
		return None

	# This map has the core logic of finding relationships
	relationship_map = {
		'father' : [ [(Parent, "M")] ],
		'mother' : [ [(Parent, "F")] ],
		'son'    : [ [(Child, "M")] ],
		'daughter' : [ [(Child, "F")] ],
		'brothers' : [[(Parent,), (Child, "M")]],
		'sisters'  : [[(Parent,), (Child, "F")]],  
		'paternal uncle' : [ [(Parent, "M"), (Parent,), (Child, "M")], 
							 [(Parent, "M"), (Parent,), (Child, "F"), (Partner,) ] ],
		'grand daughter' : [ [(Child,), (Child, "F")]],
		'sister in law'  : [ [(Partner,), (Parent,), (Child, "F")],
							 [(Parent,), (Child,), (Partner, "F")]],
		'cousins'		 : [ [(Parent,), (Parent,), (Child,), (Child,)] ],
	}

	@staticmethod
	def apply_rules(node, rule_type):
		gender_rule = None
		if len(rule_type) == 2:
			gender_rule = rule_type[1]
		if rule_type[0] == Parent:
			return RelationshipManager.get_parent(node, sex=gender_rule)
		elif rule_type[0] == Child:
			return RelationshipManager.get_children(node, sex=gender_rule)
		elif rule_type[0] == Partner:
			return RelationshipManager.get_partner(node, sex=gender_rule)

	@staticmethod
	def get_relations(name, relationship_type, root=None):
		name_node = RelationshipManager.find_name(name, root)
		#name_node.log()
		for mappings in RelationshipManager.relationship_map[relationship_type]:
			dynamic_list = [name_node]
			exclude = []
			for rule in mappings:
				new_list = []
				# print("Applying rule : ", rule)
				while len(dynamic_list) != 0:
					ss = dynamic_list.pop()
					# print("Exclude, ", end="")
					# ss.log()
					# We gotta do, what we gotta do
					exclude.append(ss)
					new_list.extend(RelationshipManager.apply_rules(ss, rule))
					new_list = Utility.RemoveDuplicates(new_list, exclusions=exclude)
				dynamic_list = new_list[:]
				# TODO : apply memoization to avoid duplicate relationship finding
				# TODO : Advanced caching to 
			RelationshipManager.print_relations(dynamic_list)
				# print("Applying rule ", rule, "-->", len(RelationshipManager.apply_rules(name_node, rule)))

			# print("---")
	@staticmethod
	def print_relations(relation_list):
		for relation in relation_list:
			relation.log()


# def person
shan = Person(name="Shan" , sex="M")
anga = Person(name="Anga", sex="F", aadhar_id="2392 23233 23244")

ish = Person("Ish", "M")
chit = Person("Chit", "M")
vich = Person("Vich", "M")
satya = Person("Satya", "F")

shan.add_partner(anga)
shan.add_child(ish, anga)
shan.add_child(vich, anga)
shan.add_child(satya, anga)
shan.add_child(chit, anga)

ambi = Person("Ambi", "F")
lika = Person("Lika", "F")
vyan = Person("Vyan", "M")

chit.add_partner(ambi)
vich.add_partner(lika)
satya.add_partner(vyan)

# Making the second family tree
drita = Person("Drita", "M")
jaya = Person("Jaya", "F")
vrita = Person("Vrita", "M")
jata = Person("Jata", "M")
driya = Person("Driya", "F")
mnu = Person("Mnu", "M")

chit.add_child(drita, ambi)
chit.add_child(vrita, ambi)
jaya.add_partner(drita)
jaya.add_child(jata, drita)
jaya.add_child(driya, drita)
driya.add_partner(mnu)

vila = Person("Vila", "M")
jnki = Person("Jnki", "F")
chika = Person("Chika", "F")
kpila = Person("Kpila", "M")
lavnya = Person("lavnya", "F")
gru = Person("gru", "M")

vich.add_child(vila, lika)
vich.add_child(chika, lika)
vila.add_partner(jnki)
chika.add_partner(kpila)
vila.add_child(lavnya, jnki)
lavnya.add_partner(gru)

satvy = Person("Satvy", "F")
asva = Person("Asva", "M")
savya = Person("Savya", "M")
krpi = Person("Krpi", "F")
saayan = Person("Saayan", "M")
mina = Person("Mina", "F")
kriya = Person("Kriya", "M")
misa = Person("Misa", "M")

satya.add_child(satvy, vyan)
satya.add_child(savya, vyan)
satya.add_child(saayan, vyan)
satvy.add_partner(asva)
savya.add_partner(krpi)
saayan.add_partner(mina)
krpi.add_child(kriya, savya)
mina.add_child(misa, saayan)

# RelationshipManager.find_name("lavnya", shan).log()
RelationshipManager.root_node = shan

# Driver code 

# Problem1 : input : Name and Relationship, output : names in the relationship

query_name = "Chika"
query_relationship = "sister in law"
print(query_name, " ", query_relationship, " are -------")
RelationshipManager.get_relations(query_name, query_relationship, root=shan)

print("***********************************************************************")

query_name = "Chika"
query_relationship = "cousins"
print(query_name, " ", query_relationship, " are -------")
RelationshipManager.get_relations(query_name, query_relationship, root=shan)

print("***********************************************************************")

# Problem2 : input : add child , output : OK 

# This follows the rule - husband.add_child(Child, wife) or vice versa wife.add_child(Child, husband)
# E.g. satya.add_child(saayan, vyan)





