# J.A.R.V.I.S.

Files in the duplicate_images branch:

### duplicate_images.ipynb: <br>
In this notebook we identify duplicate images in order to avoid leakages into validation and test set. The process is divided into 2 parts:
- Average hashing to find quickly potential duplicates. We call them "potential" as in our experience this algorithm suffers from false positives.
- Translate the images into tensors to find actual duplicates, using the library difPy (https://github.com/elisemercury/Duplicate-Image-Finder). This is process is way more accurate, but too slow to be applied to the entire dataset

### duplicate_finder.py: <br>
This script takes a directory as input and uses average hashing to identify potential duplicates, returning a list of potential duplicate pairs.

### duplicates_to_delete.csv: <br>
List of images to delete to eliminate lower quality duplicates from the original dataset

### duplicates_pairs.csv: <br>
List of duplicate pairs
