import glob
import pandas as pd
import os
import argparse

COLUMNS = ["filename", "label", "x", "y", "w", "h"]
PATH = "outputs_2811_valid/outputs_2811/*.txt"

def read_lines(file):
    results = []
    filesize = os.path.getsize(file)
    filename = file[6:]
    if filesize != 0:
        with open(file) as f:
            lines = f.readlines()
            for line in lines:
                split = line.split()
                split.insert(0, filename)
                results.append(split)

        return results
    else:
        return results

def gt2bb(path = PATH, return_csv = True):
    txt_files = glob.glob(path)
    rows = []
    for file in txt_files:

        image = read_lines(file)
        for bb in image:
            rows.append(bb)
    df = pd.DataFrame(columns =COLUMNS, data = rows)
    df.filename = df.filename.apply(lambda x: x[7:])

    if return_csv == True:
        df.to_csv("GT_bb.csv")

    return df

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path')

    args = parser.parse_args()
    gt2bb(path = args.path)