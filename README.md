# GitHub Issue Tracker LDA Summarizer

https://github.com/abramhindle/lda-chapter-tutorial/blob/main/Gensim-LDA-Tutorial.ipynb

# Use

`jupyter lab ./Gensim-LDA-Tutorial.ipynb`

Original instructions:

To mirror the repo run:

```
bash gh.sh USERNAME / REPO
```

after editing config.json to look something like

    {
         "GHUSERNAME":"yourgithubaccount",
         "GHPASSWORD":"thepasswordtoyourgithubaccount"
    }

an out directory will be made, a Everything.svg generated in the base dir.


To use existing data:

```
python lda_from_json.py --file data/boostrap/large.json --passes 10 --alpha 0.01 --beta 0.01 --topics 20
```

# Deps

For the current Gensim version you need these:

- Python3
- PyGithub
- scipy
- numpy
- matplotlib
- A github account

You can install most of this via:
```
pip3 install --user PyGithub gensim scipy numpy matplotlib jupyterlab
```

For the original version you need these:

A lot of libraries :(

- Vowpal Wabbit
- Ruby
  - Octokit
- R
  - zoo

In ubuntu 14.04:

sudo apt-get update
sudo apt-get install git r-cran-zoo r-cran-zoo ruby curl vim-gnome r-cran-zoo r-base-core python-nltk build-essential vowpal-wabbit libxml-xpath-perl libxml-dom-perl libjson-perl emacs24
sudo gem install octokit
sudo cpan -f VCI

in R you can optionally install:
    
   install.packages("corrplot")
   install.packages("doMC")
   install.packages("foreach")

# Files

- Gensim-LDA-Tutorial.ipynb - gensim version of the notebook
- bug-tracker-to-json.pl - convert an issues.xml to an appropriate format
- git-grep.pl - convert a git repo to an appropriate format
- lda_from_json.py - run lda on issues and commits 
- lda.py - lda lib
- lda-to-csv.pl - convert lda output to csv for R
- plotter.R - R to make plots and run the study
- project.sh - how to extract a project in the data directory

# Files

In general:

(C) 2013 Abram Hindle

All code here is licensed under the Apache 2.0 unless otherwise specified.

Furthermore if you are an academic. Cite our work! 

```
@inproceedings{hindle2012rri,
	Author = {Abram Hindle and Christian Bird and Thomas Zimmermann and Nachiappan Nagappan},
	Title = {Relating Requirements to Implementation via Topic Analysis: Do Topics Extracted from Requirements Make Sense to Managers and Developers?},
	Booktitle = {Proceedings of the 28th IEEE International Conference on Software Maintenance},
	Year = {2012},
	Publisher = {IEEE}
}
```

# Wait how many languages?

Uh python, ruby, perl, bash and R?
