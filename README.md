Code for my website, at https://raihanjoty.github.io.
It is a fork from Adam Lopez's at https://alopez.github.io





#Generate papers

Sometimes `python3 scripts/parsebib.py papers/bibtex.bib` raises error due to python bib package error. checkout this error if yml file is empty. 

```

python3 scripts/parsebib.py papers/bibtex.bib  2>/dev/null  | perl -anpe 's/\t/    /g;' > _data/papers.yml

```

or 

python3 scripts/parsebib.py papers/bibtex-preprints.bib  2>/dev/null  | perl -anpe 's/\t/    /g;' > _data/preprints.yml


#Create individual pages for papers

```

python3 scripts/migrate_new.py _data/papers.yml  

```
