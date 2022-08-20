Code for my website, at https://raihanjoty.github.io.
It is a fork from Adam Lopez's at https://alopez.github.io




#Generate papers

```

python3 scripts/parsebib.py papers/bibtex.bib  2>/dev/null  | perl -anpe 's/\t/    /g;' > _data/papers.yml

```

#Create individual pages for papers

```

python2 scripts/migrate.py _data/papers.yml  

```