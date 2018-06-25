"""
    This script is taking some base dir and randomly splits
    its subfolders content into to two folders (Train and Test)
    subdirectories with the same names as origin.
    Script is executing for current dir, if other dir was not
    passed to console.


    Assumed, that file structe is like this:
    /Clothes/Active_Wear
              /Heels
              /Dress
             /.........
             /.........

    and turn it into

    /Clothes/Train/Active_Wear
                           /Heels
                           /Dress
                           /.......
                           /.........

                  /Test/Active_Wear
                          /Heels
                          /Dress
                          /........
                          /........

    You can run this from "/Clothes" folder just like this
         "python3 pathtoscript/scriptname.py".
    Or u can run it from another folder, but you should pass path to "Clothes"
    folder like this
        "python3 train_test_split.py "/home/blind/Clothes".
"""

import os, sys, shutil, math
from random import shuffle


def train_test_split(base_path):
    test_dir_name = 'Test'
    train_dir_name = 'Train'

    # Partition for files to use in train and in test
    train_part = 0.5
    test_part = 1 - train_part

    # List of directories with content (e.g. photos)
    content_dirs = os.listdir(base_path)

    # !!! There should not be any folder with test_dir_name  or train_dir_name
    # in a base dir

    # Create Train and Test dirs in base dir
    os.mkdir(os.path.join(base_path, test_dir_name))
    os.mkdir(os.path.join(base_path, train_dir_name))

    # For every dir with content
    for cd in content_dirs:
        # Shuffle list of files
        fl = os.listdir(os.path.join(base_path, cd))
        shuffle(fl)

        src_cd_path = os.path.join(base_path, cd)
        test_cd_path = os.path.join(os.path.join(base_path, test_dir_name), cd)
        train_cd_path = os.path.join(os.path.join(base_path, train_dir_name), cd)

        # Create dirs with the same name in Test and Train dirs
        os.mkdir(test_cd_path)
        os.mkdir(train_cd_path)

        # Send part of shuffled list to Train/cd
        for i in range(math.ceil(fl.__len__() * train_part)):
                src = os.path.join(src_cd_path, fl[i])
                dst = os.path.join(train_cd_path, fl[i])
                shutil.move(src, dst)

        # The rest send to Test/cd
        for i in range(math.ceil(fl.__len__() * train_part), fl.__len__()):
                src = os.path.join(src_cd_path, fl[i])
                dst = os.path.join(test_cd_path, fl[i])
                shutil.move(src, dst)


if __name__ == '__main__':
    # if no console arg (path) for script, do stuff for current folder
    base_path = os.curdir if (len(sys.argv) == 1) else sys.argv[1]
    train_test_split(base_path)
