import os
import numpy as np
import shutil


Homer = '/homer_simpson'
Bart = '/bart_simpson'
Burns = '/charles_montgomery_burns'
Krusty = '/krusty_the_clown'
Lisa = '/lisa_simpson'
Milhouse = '/milhouse_van_houten'
Marge = '/marge_simpson'
Moe = '/moe_szyslak'
Ned = '/ned_flanders'
Principal = '/principal_skinner'

def train_test_split():
    print("########### Train Test Val Script started ###########")

    root_dir = 'data/lab01_split'
    classes_dir = [Homer, Bart, Burns, Krusty, Lisa, Milhouse, Marge, Moe, Ned, Principal]

    processed_dir = 'data/lab01'

    val_ratio = 0.15
    test_ratio = 0.15

    for cls in classes_dir:
        # Creating partitions of the data after shuffeling
        print("$$$$$$$ Class Name " + cls + " $$$$$$$")
        src = processed_dir + cls  # Folder to copy images from

        allFileNames = [f for f in os.listdir(src) if not f.startswith('.')]# Skip hidden files
        np.random.shuffle(allFileNames)
        train_FileNames, val_FileNames, test_FileNames = np.split(np.array(allFileNames),
                                                                  [int(len(allFileNames) * (1 - (val_ratio + test_ratio))),
                                                                   int(len(allFileNames) * (1 - val_ratio)),
                                                                   ])

        train_FileNames = [src + '//' + name for name in train_FileNames.tolist()]
        val_FileNames = [src + '//' + name for name in val_FileNames.tolist()]
        test_FileNames = [src + '//' + name for name in test_FileNames.tolist()]

        print('Total images: '+ str(len(allFileNames)+1))
        print('Training: '+ str(len(train_FileNames)+1))
        print('Validation: '+ str(len(val_FileNames)+1))
        print('Testing: '+ str(len(test_FileNames)+1))

        # # Creating Train / Val / Test folders (One time use)
        os.makedirs(root_dir + '/train//' + cls)
        os.makedirs(root_dir + '/val//' + cls)
        os.makedirs(root_dir + '/test//' + cls)

        # Copy-pasting images
        for name in train_FileNames:
            shutil.copy(name, root_dir + '/train//' + cls)

        for name in val_FileNames:
            shutil.copy(name, root_dir + '/val//' + cls)

        for name in test_FileNames:
            shutil.copy(name, root_dir + '/test//' + cls)

    print("########### Train Test Val Script Ended ###########")

train_test_split()