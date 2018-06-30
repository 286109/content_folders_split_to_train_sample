# content_folders_split_to_train_sample

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
