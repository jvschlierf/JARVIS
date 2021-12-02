# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                Bocconi University                                     #
#                       20600: Deep Learning for Computer Vision                        #
#                                   Group JARVIS                                        #
#                                 Duplicate Finder                                      #
#                                                                                       #
# This script takes a directory as input and uses average hashing to identify potential #
# duplicates, returning a list of potential duplicate pairs.                            #
#                                                                                       #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


from PIL import Image
import os
import numpy as np
from tqdm.notebook import tqdm
import imagehash


class DuplicateFinder:

    def __init__(self,dirname,hash_size = 8):
        self.dirname = dirname
        self.hash_size = hash_size
        
    def find_duplicates(self):

        fnames = os.listdir(self.dirname)
        hashes = {}
        duplicates = []
        print("Finding Duplicates Now\n")
        c = 0
        for image in tqdm(fnames):
            with Image.open(os.path.join(self.dirname,image)) as img:
                temp_hash = imagehash.average_hash(img, self.hash_size)
                if temp_hash in hashes:
                    print("Duplicate {} \nfound for Image {}".format(image,hashes[temp_hash]))
                    duplicates.append((hashes[temp_hash], image))
                    c += 1
                    print("Number of Duplicates: ", c, "\n")
                else:
                    hashes[temp_hash] = image
        
        return duplicates
