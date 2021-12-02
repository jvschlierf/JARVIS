# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                Bocconi University                                     #
#                       20600: Deep Learning for Computer Vision                        #
#                                   Group JARVIS                                        #
#                                Merging Workspaces                                     #
#                                                                                       #
# This script takes a directory containing multiple Roboflow workspaces in order to     #
# merge them together in a freshly created directory. In particular, the annotations    # 
# are merged in a single csv file, and all the images are moved in the same directories,#
# depending on the required split (default is train, valid, test)                       #
#                                                                                       #                 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


import os
import shutil
import pandas as pd

def merging_tf(dirStart, dirEnd, Workspaces, Splits = ['test', 'train', 'valid']):

    if not os.path.exists(dirEnd):
        os.mkdir(dirEnd)
        print("Directory", dirEnd, "Created")
    else:    
        print("Directory", dirEnd, "Already Exists")
        shutil.rmtree(dirEnd)
        os.mkdir(dirEnd)
        print("New Directory", dirEnd, "Created")

    for folder in Splits:
        os.mkdir(os.path.join(dirEnd, folder))

    # Merge all the annotations from the different workspaces

    for split in Splits:
        d = {}
        for workspace in Workspaces:
            d.update({workspace + '_' + split : pd.read_csv(os.path.join(dirStart, workspace, split, '_annotations.csv'))})
            pd.concat(d, axis=0).reset_index(drop=True).to_csv(os.path.join(dirEnd, split, '_annotations.csv'), index=False)


    # Copy all the images from the different workspaces

    for split in Splits:
        for workspace in Workspaces:
            srcdir = os.path.join(dirStart, workspace, split)
            dstdir = os.path.join(dirEnd, split)
            for basename in os.listdir(srcdir):
                if basename.endswith('.jpg'):
                    pathname = os.path.join(srcdir, basename)
                    if os.path.isfile(pathname):
                        shutil.copy2(pathname, dstdir) 





