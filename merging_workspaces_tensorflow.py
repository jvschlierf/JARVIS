import os
import shutil
import pandas as pd

### Merging "Workspaces" into "Dataset"

dirStart = 'Workspaces' # Directory with the download and unzipped workspaces
dirEnd = 'Dataset' # Directory with the merged dataset

if not os.path.exists(dirEnd):
    os.mkdir(dirEnd)
    print("Directory", dirEnd, "Created")
else:    
    print("Directory", dirEnd, "Already Exists")
    shutil.rmtree(dirEnd)
    os.mkdir(dirEnd)
    print("New Directory", dirEnd, "Created")

splits = ['test', 'train', 'valid']

for folder in splits:
    os.mkdir(os.path.join(dirEnd, folder))

# Workspaces

CH = "CLE - HOU" # Change names according to the unzipped directories
CC = "CLT - CHI"
LL = "LA - LDN"
MP = "MI - PHO"

Workspaces = [CH, CC, LL, MP]

# Merge all the annotations from the different workspaces

for split in splits:
    d = {}
    for workspace in Workspaces:
        d.update({workspace + '_' + split : pd.read_csv(os.path.join(dirStart, workspace, split, '_annotations.csv'))})
        pd.concat(d, axis=0).reset_index(drop=True).to_csv(os.path.join(dirEnd, split, '_annotations.csv'), index=False)


# Copy all the images from the different workspaces

for split in splits:
    for workspace in Workspaces:
        srcdir = os.path.join(dirStart, workspace, split)
        dstdir = os.path.join(dirEnd, split)
        for basename in os.listdir(srcdir):
            if basename.endswith('.jpg'):
                pathname = os.path.join(srcdir, basename)
                if os.path.isfile(pathname):
                    shutil.copy2(pathname, dstdir) 





