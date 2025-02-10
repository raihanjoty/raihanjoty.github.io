#!/bin/python
import yaml
import codecs
import sys
import os
import re
# -*- coding: utf-8 -*-
from yaml import Loader, SafeLoader

def main(file):
    try:
        with open(file, "r") as stream:
            # Print the content of the file for debugging
            content = stream.read()
            print(f"File content:\n{content}")
            
            # Reset file pointer to beginning
            stream.seek(0)
            
            # Try to load the YAML
            docs = yaml.safe_load(stream)
            
            if docs is None:
                print("Error: YAML file is empty or invalid")
                return
            
            if not isinstance(docs, list):
                docs = [docs]  # Convert single document to list
                
            dirname = os.path.dirname(sys.argv[0])
            
            for doc in docs:
                id = doc['id']
                newfile = open(dirname+"/../_papers/"+id+".html", "w")
                doc['layout'] = 'singlepaper'
                doc['picture'] = 'shafiq'
                string = yaml.dump(doc, explicit_start=True, default_flow_style=False, allow_unicode=True)
                string = re.sub("doc-url:\s*papers/", "doc-url: ", string)
                newfile.write(string)
                newfile.write("---\n\n")
                newfile.write("{% include singlepaper.html paper=page %}")
                newfile.close()
                
    except FileNotFoundError:
        print(f"Error: File '{file}' not found")
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main("../_data/papers.yml")
