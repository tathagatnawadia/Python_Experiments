#!/usr/bin/env python

import lxml, os
from lxml.html.clean import Cleaner
from lxml import etree


# Utility functions 

# CLASSES

class HTML_Cleaner(object):
	"""This class has
	1.Utility classes for removing javascript
	2.Utility classes for removing styles(inline, external)
	"""
	def __init__(self):
		super(HTML_Cleaner, self).__init__()
		self.cleaner = self.initilize_html_cleaner()
		self.javascript_filter()
		self.style_filter()
		self.kill_tags(['code', 'iframe'])
		self.remove_tags(['a', 'body', 'head'])
		#self.remove_attributes(['class', 'id', 'src', 'href'])
		
	def initilize_html_cleaner(self):
		return Cleaner()

	def javascript_filter(self):
		self.cleaner.javascript = True

	def style_filter(self):
		self.cleaner.style = True

	def kill_tags(self, tags):
		self.cleaner.kill_tags = tags

	def remove_tags(self, tags):
		self.cleaner.remove_tags = tags

	def remove_attributes(self, html_content, attributes):
		node = lxml.html.fromstring(html_content)
		for attribute in attributes:
			attribute_picker = '//*[@' + attribute + ']'
			for tag in node.xpath(attribute_picker):
				tag.attrib.pop(attribute)
		return node

	def operate(self, html_content):
		f1 = " ".join(self.cleaner.clean_html(html_content).split())
		f2 = self.remove_attributes(f1, ['class', 'id', 'src', 'href'])
		return etree.tostring(f2, pretty_print=False).rstrip()

# CONFIG

source_directory = 'data/source'
destination_directory = 'data/destination'
util = HTML_Cleaner()

for filename in os.listdir(source_directory):
    if filename.endswith(".html") or filename.endswith(".htm") or filename.endswith(".xml"): 
        html_content = open(os.path.join(source_directory, filename), 'r').read()
        no_html_content = util.operate(html_content)

        write_to_file = open(os.path.join(destination_directory, filename), 'wb')
        write_to_file.write(no_html_content)
        write_to_file.close()
        continue
    else:
        continue