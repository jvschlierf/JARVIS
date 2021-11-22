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
                   
#        if len(duplicates) != 0:
#            a = input("Do you want to delete these {} Images? Press Y or N:  ".format(len(duplicates)))
#            space_saved = 0

#            if(a.strip().lower() == "y"):

#                for duplicate in duplicates:
#                    space_saved += os.path.getsize(os.path.join(self.dirname,duplicate))
                    
#                    os.remove(os.path.join(self.dirname,duplicate))
#                    print("{} Deleted Succesfully".format(duplicate))
    
#                print("\n\nYou saved {} mb of Space".format(round(space_saved/1000000),2))
#        else:
#            print("No Duplicates Found")
        
        return duplicates