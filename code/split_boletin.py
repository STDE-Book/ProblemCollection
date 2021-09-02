# -*- coding: utf-8 -*-
"""
Reads the tex files with collections of problems in spanish and english, and
creates a single main tex file.

Each problem is moved to a separate file containing both the spanish and english
version.

This code was used to generate the DB of problems, one per file, in 2015. It is
likely not needed anymore

Created on Aug 22 2015
@author: Jesus Cid.
"""

import os
import re
import sys


if __name__ == "__main__":

    # Location and names of the source files
    folder = 'B2'
    fname_es = 'B2 - Problems_201509.tex'
    fname_en = 'B2 - Problems_201509_english.tex'
    fpath_es = folder + '/' + fname_es
    fpath_en = folder + '_english/' + fname_en

    # Location and names of the output files
    newfolder = 'new' + folder
    dbfolder = newfolder + '/db'

    # Create ouput folders
    if os.path.exists(newfolder):
        print "Output folder " + newfolder + "already exists (as a directory \
               or as a file). Remove it before calling this script"
        sys.exit()
    else:
        os.makedirs(newfolder)
        os.makedirs(dbfolder)

    # Begining and end of each problem
    start = '\\\\question'
    stop = '\\\\end{solution}'
    start0 = '\\question'
    stop0 = '\\end{solution}'

    # Read file
    text_es = open(fpath_es).read()
    text_en = open(fpath_en).read()

    # Read all problems in separate strings
    pattern = start + '(.+?)' + stop
    probs_es = re.findall(pattern, text_es, re.DOTALL)
    probs_en = re.findall(pattern, text_en, re.DOTALL)

    np = len(probs_es)
    if np != len(probs_en):
        print "The number of exercises in both documents is not the same"
        sys.exit()

    # Main loop. Joins the spanish and english versions of each problem n
    # and moves them to a single file.
    for i in range(np):

        # Path of the problem file
        fprob = dbfolder + '/Dec20xx_Cx_Px_' + str(i+1) + '.tex'

        # Spanish and english versions
        prob_es_i = start0 + probs_es[i] + stop0
        prob_en_i = start0 + probs_en[i] + stop0

        # Write to file
        with open(fprob, "a+") as f:
            f.write('\\ifspanish\n\n' + prob_es_i +
                    '\n\n\\else\n\n' + prob_en_i +
                    '\n\n\\fi')

        # Replace text of the problem in the main file to an '\input' LaTeX
        # command
        newtext = '\\input{' + 'db/Dec20xx_Cx_Px_' + str(i+1) + '.tex}\n'
        text_es = text_es.replace(prob_es_i, newtext)

    # Save main tex file.
    main_tex = newfolder + '/TMDEproblems.tex'
    with open(main_tex, "a+") as f:
            f.write(text_es)
