import os
import pandas as pd
import shutil

Folders = [name for name in os.listdir() if os.path.isdir(os.path.join("", name)) and name[0] != "."]
#since we copy our images into the darknet folder structure, we check if darknet is present
try:
    Folders.remove("darknet")
except ValueError:
    raise Exception("Please clone darknet into this folder.")

#we keep running lists of our images for train, test validate
temp_train = []
temp_valid = []
temp_test = []

for i in Folders:
    #remove roboflow descriptors
    os.remove(i + "README.dataset.txt")
    os.remove(i + "README.dataset.txt")
    subfolders = [name for name in os.listdir() if os.path.isdir(os.path.join("", name)) and name[0] != "."]
    temp_train += [f for f in os.listdir(i + "/train") if f.endswith(".jpg")]

    if "test" in subfolders:
        temp_valid += [f for f in os.listdir(i + "/valid") if f.endswith(".jpg")]
        temp_test += [f for f in os.listdir(i + "/test") if f.endswith(".jpg")]

    for j in subfolders:
        [shutil.move(i + "/" + j + "/" + f, "Data/" + j + "/") for f in os.listdir(i + "/" + j) if not f.endswith(".labels")]

        try:
            os.rmdir(i + "/" + j)
        except OSError:
            try:
                os.remove(i + "/" + j + "/" + "_darknet.labels")
                os.rmdir(i + "/" + j)


shutil.move(i + "/train/_darknet.labels", "Data/train")
shutil.move(i + "/valid/_darknet.labels", "Data/valid")
shutil.move(i + "/test/_darknet.labels", "Data/test")


# list the content of train and test by retaining only the *jpg files
temp_train = [f for f in os.listdir("Data/train") if f.endswith(".jpg")]
temp_valid = [f for f in os.listdir("Data/valid") if f.endswith(".jpg")]
temp_test = [f for f in os.listdir("Data/test") if f.endswith(".jpg")]

# add the path we are working in
train_loc = [os.getcwd() + "/train/" + f for f in temp_train]
valid_loc = [os.getcwd() + "/valid/" + f for f in temp_valid]
test_loc = [os.getcwd() + "/test/" + f for f in temp_test]

# convert to pandas
train_df = pd.DataFrame(train_loc)
valid_df = pd.DataFrame(valid_loc)
test_df = pd.DataFrame(test_loc)

# export the files in the destination folder
# make sure you set index=False and header=False as the txt files
# need to have just locations and nothing else
train_df.to_csv("./darknet/data/train.txt", index=False, header=False)
valid_df.to_csv("./darknet/data/valid.txt", index=False, header=False)
test_df.to_csv("./darknet/data/test.txt", index=False, header=False)
