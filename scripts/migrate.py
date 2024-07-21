#!/bin/python
import simpleyaml as yaml
#import yaml

import codecs
import sys
import os
import re

# -*- coding: utf-8 -*-
from simpleyaml import Loader, SafeLoader
#from yaml import Loader, SafeLoader


def main(file):
	stream = open(file, "r")
	docs = yaml.load(stream)
	dirname = os.path.dirname(sys.argv[0])
	for doc in docs:
		id=doc['id']

		newfile=open(dirname+"/../_papers/"+id+".html","w")
		#for item in doc.
		doc['layout']='singlepaper'
		doc['picture']='shafiq'

		string=yaml.dump(doc,explicit_start=True, default_flow_style=False,allow_unicode=True)
		string = re.sub("doc-url:\s*papers/", "doc-url: ", string)
#		print string
#		raw_input(' ')
		newfile.write(string)
		newfile.write("---\n\n")
		newfile.write("{% include singlepaper.html paper=page %}")


		newfile.close()



if __name__ == '__main__':
	if len(sys.argv) >1:
		main(sys.argv[1])
	else:
		main("../_data/papers.yml")
