# J.A.R.V.I.S.
This is a repo for the Computer Vision project, which is a part of the DSBA 2020-2022.


duplicate_images: <br>
In this notebook we identify duplicate images in order to avoid leakages into validation and test set. The process is divided into 2 parts:
- Average hashing to find quickly potential duplicates. We call them "potential" as in our experience this algorithm suffers from false positives.
- Translate the images into tensors to find actual duplicates, using the library difPy (https://github.com/elisemercury/Duplicate-Image-Finder). This is process is way more accurate, but too slow to be applied to the entire dataset


