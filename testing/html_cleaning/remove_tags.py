#!/usr/bin/env python

import lxml, os
from lxml.html.clean import Cleaner
from lxml import etree


# Utility functions 

# CLASSES
import json 

class Config():
	def __init__(self, filename):
		self.file_path = filename
		self.settings = json.load(open(self.file_path))

	def dump(self):
		print self.file_path
		print self.settings

class HTML_Cleaner(object):
	"""This class has
	1.Utility classes for removing javascript
	2.Utility classes for removing styles(inline, external)
	"""
	def __init__(self, config=None):
		super(HTML_Cleaner, self).__init__()
		self.cleaner = self.initilize_html_cleaner()
		self.load_configuration(config)
		#self.remove_attributes(['class', 'id', 'src', 'href'])
	def initilize_html_cleaner(self):
		self.attributes = {}
		return Cleaner()

	def load_configuration(self, config):
		# Basic javascript and style filters
		self.javascript_filter(config.settings['removal']['absolute']['javascript'])
		self.style_filter(config.settings['removal']['absolute']['css'])

		# Kill list of tags
		kill_list = []
		for kill_tag in config.settings['removal']['tags']['destructive']:
			if config.settings['removal']['tags']['destructive'][kill_tag] == True:
				kill_list.append(kill_tag)
		self.kill_tags_filter(kill_list)

		# Remove list of tags
		remove_list = []
		for remove_tag in config.settings['removal']['tags']['constructive']:
			if config.settings['removal']['tags']['constructive'][remove_tag] == True:
				remove_list.append(remove_tag)
		self.remove_tags_filter(remove_list)

		# Remove list of attributes
		attribute_list = []
		for attribute in config.settings['removal']['attributes']:
			if config.settings['removal']['attributes'][attribute] == True:
				attribute_list.append(attribute)
		self.remove_attributes_filter(attribute_list)

		
	def javascript_filter(self, enabled=False):
		self.cleaner.javascript = enabled

	def style_filter(self, enabled=False):
		self.cleaner.style = enabled

	def kill_tags_filter(self, tags):
		self.cleaner.kill_tags = tags

	def remove_tags_filter(self, tags):
		self.cleaner.remove_tags = tags

	def remove_attributes_filter(self, attributes):
		self.attributes["remove"] = attributes

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
html_configuration_file = 'config.json'

config_handler = Config(html_configuration_file)
html_handler = HTML_Cleaner(config_handler)

for filename in os.listdir(source_directory):
    if filename.endswith(".html") or filename.endswith(".htm") or filename.endswith(".xml"): 
        html_content = open(os.path.join(source_directory, filename), 'r').read()
        no_html_content = html_handler.operate(html_content)

        write_to_file = open(os.path.join(destination_directory, filename), 'wb')
        write_to_file.write(no_html_content)
        write_to_file.close()
        continue
    else:
        continue