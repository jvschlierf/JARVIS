# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                Bocconi University                                     #
#                       20600: Deep Learning for Computer Vision                        #
#                                   Group JARVIS                                        #
#                                  Darknet Utility                                      #
#                                                                                       #
# This program seeks to simplify the import and preparation steps for the use of darknet#
# It takes the unzipped Roboflow folders, places the files into the darknet structure   #
# and lastly creates the required data.txt files that will be used for training.        #
# The commented out lines are used to delete the files from the folders that we pulled  #
# the pictures in to from Roboflow. Lastly, we check the copied files for duplicates.   #
#                                                                                       #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


import os
import pandas as pd
import shutil
import csv
import re

Folders = [name for name in os.listdir(os.getcwd()) if os.path.isdir(os.path.join("", name)) and name[0] != "."]
#since we copy our images into the darknet folder structure, we check if darknet is present
try:
    Folders.remove("darknet")
except ValueError:
    raise Exception("Please clone darknet into this folder.")


duplicates = []

try:
    with open("duplicates_to_delete.csv", 'r') as read_obj: 
        for row in csv.reader(read_obj):
            duplicates.append(row)
except:
    raise Exception("Please ensure duplicate file is present in this folder.")



try:
    os.mkdir("darknet/data/train/")
    os.mkdir("darknet/data/test/")
    os.mkdir("darknet/data/valid/")
except FileExistsError:
    pass

#we keep running lists of our images for train, test validate
temp_train = []
temp_valid = []
temp_test = []
# names_bool = True


for i in Folders:
    print("Moving folder " + i)
    #remove roboflow descriptors
    # os.remove(i + "/README.dataset.txt")
    # os.remove(i + "/README.roboflow.txt")
    subfolders = [name for name in os.listdir(i) if os.path.isdir(os.path.join(i, name)) and name[0] != "."]

    #We check if we have a test subfolder to distinguish between a regular set (containing all 15 classes, train,
    # validate & test data and an augmented set (containing only train data, and not for all classes)
    temp_train += [f for f in os.listdir(i + "/train") if f.endswith(".jpg")]
    if "test" in subfolders:
        temp_valid += [f for f in os.listdir(i + "/valid") if f.endswith(".jpg")]
        temp_test += [f for f in os.listdir(i + "/test") if f.endswith(".jpg")]

        # we try to move the label files to the function specified by darknet
        # if names_bool:
        #     shutil.copy(i + "/test/_darknet.labels", "darknet/data/obj.names")
        #     names_bool = False
        
        # try:
        #     # os.remove(i + "/test/" + "_darknet.labels")
        #     # os.remove(i + "/valid/" + "_darknet.labels")
        # except:
        #     pass

        [shutil.copy(i + "/test/" + f, "darknet/data/test/") for f in os.listdir(i + "/test/")]
        [shutil.copy(i + "/valid/" + f, "darknet/data/valid/") for f in os.listdir(i + "/valid/")]
        
        subfolders.remove("test")
        subfolders.remove("valid")

        # os.rmdir(i + "/valid")
        # os.rmdir(i + "/test")


    for j in subfolders:
        # try:
        #     os.remove(i + "/" + j + "/" + "_darknet.labels")
        # except:
        #     pass
        [shutil.copy(i + "/" + j + "/" + f, "darknet/data/train/") for f in os.listdir(i + "/" + j)]

        # try:
        #     os.rmdir(i + "/" + j)
        # except OSError:
        #     pass
    
    # try:
    #         os.rmdir(i)
    # except OSError:
    #         pass

counter = 0
print("Finished moving files, Checking for duplicates.")
for i in ('train', 'valid', 'test'):
    for j in os.listdir('darknet/data/' + i):
        for k in duplicates:
            test_p = k[0] + '*'
            if re.match(test_p, j):
                os.remove(os.join('darknet/data/' + i + '/' + j))
                counter += 1
    print("Finished checking " + i + " for duplicates.")
    print("Found & removed " + str(counter) + " duplicates.")

# add the path we are working in
train_loc = [os.getcwd() + "/darknet/data/train/" + f for f in temp_train]
valid_loc = [os.getcwd() + "/darknet/data/valid/" + f for f in temp_valid]
test_loc = [os.getcwd() + "/darknet/data/test/" + f for f in temp_test]

# convert to pandas
train_df = pd.DataFrame(train_loc)
valid_df = pd.DataFrame(valid_loc)
test_df = pd.DataFrame(test_loc)

# export the files in the destination folder
# make sure you set index=False and header=False as the txt files
# need to have just locations and nothing else
train_df.to_csv("darknet/data/train.txt", index=False, header=False)
valid_df.to_csv("darknet/data/valid.txt", index=False, header=False)
test_df.to_csv("darknet/data/test.txt", index=False, header=False)
