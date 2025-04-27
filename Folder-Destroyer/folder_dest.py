#folder / file destroyer with --force flag

import argparse
import os
import shutil
import sys
import time
def argParsingFunc():
    parser = argparse.ArgumentParser(description="FOLDER DESTROYER",epilog="syntax - folder_dest.py -p path")
    parser.add_argument("--overwrite",action="store_true",help="Overwrites every File - Danger!")
    parser.add_argument("--force",action="store_true",help="deletes forcefully everything Danger!")
    parser.add_argument("-p","--path",help="PATH OF THE FOLDER ")
    return parser.parse_args()

def main():
    args = argParsingFunc()
    path=args.path
    if not args.path:
        sys.exit("path not specified Error !")
    if not os.path.exists(path):
        sys.exit("Folder/Path DOENS'T EXIST")
    if not os.path.isdir(path):
        sys.exit("PATH IS A FILE not dir...")
    if args.path and os.path.isdir(path) :
        isForce=False
        isoverwriten = False
        if args.force:
            isForce = True
        if args.overwrite:
            isoverwriten=True
        folderEmpytDelete(path,isForce,isoverwriten)
        
        
def folderEmpytDelete(path,forceDel,overwrite):
        try:
            if forceDel:
                if overwrite:
                    input1=input("ARE YOU USING AT YOUR OWN RESPOSNSIBILITY... - ")
                    if input1 in ["yes","y","ye"]:
                         isOverwritted=True
                         for root,dirs,files in os.walk(path):
                             for eachFile in files:
                                 new_path = os.path.join(root,eachFile)
                                 overwritee(new_path,eachFile)
                    elif input1.lower() in ["no","n",""]:
                        print("STOPPED THE OVERWRITING FUNCTION !")
                    else:
                        print("INVALID INPUT...")
                else:
                    print("NOT OVERWRITTEN !")
                    isOverwritted=False
                while True:
                    confirmInput = input("Are you sure you want to delete?  y/n - ")
                    if confirmInput.lower() in ["y","ye","yes"]:
                        print("DELETING.....")
                        time.sleep(0.5)
                        shutil.rmtree(path) #alll
                        if isOverwritted:
                            print("1)changed content \n2)deleted the folder !! (hope used in your own env) .....")
                        break
                    elif confirmInput.lower() in ["n","no",""]:
                        print("STOPPED THE PROCESS....! \n Bye")
                        break
                    else:print("INVALID INPUT ! TRY AGAIN ")
            else:
                print("DELETING THE EMPTY DIRECTORY....")
                time.sleep(0.5)
                os.rmdir(path) #only for blank ones  
        except PermissionError:print("PERMISSION NOT ALLOWED !")
        except Exception as fe :print("ERROR - ",fe)
        except FileNotFoundError :print("file not found...")
        
        
def overwritee(file_path,eachFile):
    try:
        with open(file_path,"wb") as file:
            file.write(os.urandom(1022333))
    except PermissionError:print("NO PERMISSION FOR THIS FILE ",eachFile)
    except FileNotFoundError :print("file not found...")
    except Exception as fe:print("ERROR -",fe)
main()