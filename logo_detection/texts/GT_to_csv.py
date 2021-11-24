import glob
import pandas as pd
import os
import numpy as np

txt_files = glob.glob("images/*.txt")

def read_lines(filename):
    results = []
    filesize = os.path.getsize(filename)
    if filesize != 0:
        with open(filename) as file:
            lines = file.readlines()
            for line in lines:
                split = line.split()
                split.insert(0, filename)
                results.append(split)

        return results
    else:
        return results

COLUMNS = ["filename", "label", "x", "y", "w", "h"]

rows = []
for file in txt_files:

    image = read_lines(file)
    for bb in image:
        rows.append(bb)



df = pd.DataFrame(columns =COLUMNS, data = rows)
df.filename = df.filename.apply(lambda x: x[7:])
df.to_csv("GT_bb.csv")