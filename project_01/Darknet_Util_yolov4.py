import os
import pandas as pd
import shutil

Folders = [name for name in os.listdir() if os.path.isdir(os.path.join("", name)) and name[0] != "."]
#since we copy our images into the darknet folder structure, we check if darknet is present
try:
    Folders.remove("darknet")
except ValueError:
    raise Exception("Please clone darknet into this folder.")

try:
    os.mkdir("darknet/build/darknet/x64/data/obj/")
    os.mkdir("darknet/build/darknet/x64/data/obj/test/")
    os.mkdir("darknet/build/darknet/x64/data/obj/valid/")
except FileExistsError:
    pass

#we keep running lists of our images for train, test validate
temp_train = []
temp_valid = []
temp_test = []
names_bool = True


for i in Folders:
    #remove roboflow descriptors
    os.remove(i + "README.dataset.txt")
    os.remove(i + "README.dataset.txt")
    subfolders = [name for name in os.listdir() if os.path.isdir(os.path.join("", name)) and name[0] != "."]

    #We check if we have a test subfolder to distinguish between a regular set (containing all 15 classes, train,
    # validate & test data and an augmented set (containing only train data, and not for all classes)
    temp_train += [f for f in os.listdir(i + "/train") if f.endswith(".jpg")]
    if "test" in subfolders:
        temp_valid += [f for f in os.listdir(i + "/valid") if f.endswith(".jpg")]
        temp_test += [f for f in os.listdir(i + "/test") if f.endswith(".jpg")]

        [shutil.move(i + "/test/" + f, "darknet/build/darknet/x64/data/obj/test/") for f in os.listdir(i + "/test/")]
        [shutil.move(i + "/valid/" + f, "darknet/build/darknet/x64/data/obj/test/") for f in os.listdir(i + "/valid/")]
        subfolders.remove("test")
        subfolders.remove("valid")
        # we try to move the label files to the function specified by darknet
        if names_bool:
            os.rename(i + "/test/_darknet.labels", "darknet/build/darknet/x64/data/obj.names")
            names_bool = False

    for j in subfolders:
        os.remove(i + "/" + j + "/" + "_darknet.labels")
        [shutil.move(i + "/" + j + "/" + f, "darknet/build/darknet/x64/data/obj/") for f in os.listdir(i + "/" + j)]

        try:
            os.rmdir(i + "/" + j)
        except OSError:
            pass


# add the path we are working in
train_loc = [os.getcwd() + "darknet/build/darknet/x64/data/obj/" + f for f in temp_train]
valid_loc = [os.getcwd() + "darknet/build/darknet/x64/data/obj/valid/" + f for f in temp_valid]
test_loc = [os.getcwd() + "darknet/build/darknet/x64/data/obj/test/" + f for f in temp_test]

# convert to pandas
train_df = pd.DataFrame(train_loc)
valid_df = pd.DataFrame(valid_loc)
test_df = pd.DataFrame(test_loc)

# export the files in the destination folder
# make sure you set index=False and header=False as the txt files
# need to have just locations and nothing else
train_df.to_csv("darknet/build/darknet/x64/data/train.txt", index=False, header=False)
valid_df.to_csv("darknet/build/darknet/x64/data/valid.txt", index=False, header=False)
test_df.to_csv("darknet/build/darknet/x64/data/test.txt", index=False, header=False)
