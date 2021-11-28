import pandas as pd
import argparse

COLUMNS = ["filename", "label","confidence", "left_x", "top_y", "width", "height"]
LABELS2NUM = {
    "Adidas": 0,
    "Apple Inc-": 1,
    "Coca-Cola": 2,
    "Emirates": 3,
    "Hard Rock Cafe": 4,
    "Mercedes-Benz": 5,
    "NFL": 6,
    "Nike": 7,
    "Pepsi": 8,
    "Puma": 9,
    "Starbucks": 10,
    "The North Face": 11,
    "Toyota": 12,
    "Under Armour": 13,
}

TO_SPLIT = """Enter Image Path:  Detection layer: 139 - type = 28 
 Detection layer: 150 - type = 28 
 Detection layer: 161 - type = 28 
/home/labuser/Darknet/Augment/darknet/data/test/"""

def read_data(path = PATH):
    with open(path) as f:
        lines = f.read().split(TO_SPLIT)



    rows = []
    for line in lines:
        line = line.splitlines()
        rows.append(line)

    output = []
    for row in rows[1:]:
        filename = row[0].split(":")[0][:-3] + "txt"
        for i in range(len(row))[1:]:
            try:
                label = row[i].split(":", 1)[0]
                confidence = row[i].split(":", 1)[1].split("%")[0]
                remaining1 = row[i].split(":", 1)[1].split("(")[1][:-1].split("  ")[1]
                remaining2 = row[i].split(":", 1)[1].split("(")[1][:-1].split("  ")[3]
                remaining3 = row[i].split(":", 1)[1].split("(")[1][:-1].split("  ")[5]
                remaining4 = row[i].split(":", 1)[1].split("(")[1][:-1].split("  ")[7]
            except:
                continue
            single = [filename, label, confidence, remaining1, remaining2, remaining3, remaining4]
            output.append(single)
    return output

def pred2bb(path, return_csv = True):
    output = read_data(path)
    df = pd.DataFrame(columns=COLUMNS, data=output)
    df.dropna()
    df["label"] = df["label"].apply(lambda x: LABELS2NUM.get(x))
    df.confidence = pd.to_numeric(df.confidence, errors="coerce")
    df.left_x = pd.to_numeric(df.left_x, errors="coerce")
    df.top_y = pd.to_numeric(df.top_y, errors="coerce")
    df.width = pd.to_numeric(df.width, errors="coerce")
    df.height = pd.to_numeric(df.height, errors="coerce")
    df.dropna(inplace=True)

    df["y"] = (df["top_y"] + df["height"] / 2) / 640
    df["x"] = (df["left_x"] + df["width"] / 2) / 640
    df["w"] = df["width"] / 640
    df["h"] = df["height"] / 640

    if return_csv == True:
        df.to_csv("pred_bb.csv")
    print(df.head())
    return df

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    args = parser.parse_args()
    pred2bb(path = args.path)