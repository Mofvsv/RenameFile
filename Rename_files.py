import os
def rename_files():
    #get file names from a folder
    file_list = os.listdir(r"C:\Users\TheHomie\Documents\Udacity\Github\python\Rename_file\prank")
    print(file_list)
    save_path = os.getcwd()
    print("Current working directory" + save_path)
    os.chdir(r"C:\Users\TheHomie\Documents\Udacity\Github\python\Rename_file\prank") # I can't figure out how to go into the prank sub directory
    print("Current working directory" + save_path)

    #for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(save_path)

rename_files()
