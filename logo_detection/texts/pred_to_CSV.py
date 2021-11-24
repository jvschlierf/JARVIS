import pandas as pd

with open('results/result.txt') as f:
    lines = f.read().split("""Enter Image Path:  Detection layer: 139 - type = 28 
 Detection layer: 150 - type = 28 
 Detection layer: 161 - type = 28 
/home/labuser/Darknet/Augment/darknet/build/darknet/x64/data/obj/valid/""")

COLUMNS = ["filename", "label", "left_x", "top_y", "width", "height"]

rows = []
for line in lines:
    line = line.splitlines()
    rows.append(line)

output = []
for row in rows[1:]:
    filename = row[0].split(":")[0][:-3]+"txt"
    for i in range(len(row))[1:]:
        try:
            label = row[i].split(":",1)[0]
            remaining1 = row[i].split(":", 1)[1].split("(")[1][:-1].split("  ")[1]
            remaining2 = row[i].split(":", 1)[1].split("(")[1][:-1].split("  ")[3]
            remaining3 = row[i].split(":", 1)[1].split("(")[1][:-1].split("  ")[5]
            remaining4 = row[i].split(":", 1)[1].split("(")[1][:-1].split("  ")[7]
        except:
            continue
        single = [filename, label, remaining1, remaining2, remaining3, remaining4]
        print(single)
        output.append(single)

df = pd.DataFrame(columns=COLUMNS, data= output)

labels_to_num = {
"Adidas":0,
"Apple Inc-":1,
"Chanel":2,
"Coca-Cola":3,
"Emirates":4,
"Hard Rock Cafe":5,
"Mercedes-Benz":6,
"NFL":7,
"Nike":8,
"Pepsi":9,
"Puma":10,
"Starbucks":11,
"The North Face":12,
"Toyota":13,
"Under Armour":14,
}
df.dropna()
df["label"] = df["label"].apply(lambda x: labels_to_num.get(x))
df.left_x = pd.to_numeric(df.left_x, errors="coerce")
df.top_y = pd.to_numeric(df.top_y, errors="coerce")
df.width = pd.to_numeric(df.width, errors="coerce")
df.height = pd.to_numeric(df.height, errors="coerce")
df.dropna(inplace=True)
# #

# df.top_y = df.top_y.astype('int')
# # df.astype({'top_y': 'Int64', })
#
df["y"] = (df["top_y"] + df["height"]/2)/608
df["x"] = (df["left_x"] + df["width"]/2)/608
df["w"] = df["width"]/608
df["h"] = df["height"]/608

df.to_csv("pred_bb.csv")
