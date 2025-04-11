# This is a CLI accepting file-tool made to check occurene of each word in the text & check HIGEST OCCURED WORDS
import argparse #for accepting args
import string # for removing punctiuations
import sys # for exiting
#define & make file accepting argument function

def fileArgsParser():
    parser = argparse.ArgumentParser(
		description="ENTER THE FILE NAME TO CHECK OCCURENCE OF WORDS",
		epilog="eg -  main.py -f filename.txt (or md/csv)"
	)
    parser.add_argument("-f","--filename",help="ENTER THE FILE-NAME AFTER -f")
    parser.add_argument("-v","--verbose",action="store_true")
    #accept args now and collect them with values from arg of users & return
    
    return parser.parse_args()

def main():
    #accept the args here
    args = fileArgsParser()
    
    # 
    if args.verbose:print("VERBOSE MODE ON")
    if not args.filename:
        sys.exit("ERROR ! ENTER THE FILE-NAME") #abort the mission/exit
    
    #call the main function to check now
    if args.filename:
        filename1=args.filename
        #check filename entered :- print(filename1) 
        checkFile(filename1)

#
def checkFile(filename1):
    dictionary_occ_checker = {}
    try:
        with open(filename1,"r") as file1:
            for eachLine in file1:
                eachlineArray = eachLine.strip().split() #add , if -> seperation needed by ,
                for eachWord in eachlineArray:
                    #string -> punctuation contain all punctuations
                    eachWord=eachWord.strip(string.punctuation).lower() #checks *The the* in same way & removes all punctuations
                    if eachWord in dictionary_occ_checker:
                        dictionary_occ_checker[eachWord]+=1
                    else:
                        dictionary_occ_checker[eachWord]=1
            print(dictionary_occ_checker)
            try:
                input1=input('WANT TO SAVE - \n y/yes or n/no - ')
                if input1 in ['y','yes']:
                    input2=input("ENTER THE FILE-NAME TO SAVE - ")
                    if "." in input2:
                        save_to_file(dictionary_occ_checker,input2)
                        print('DONE CHECK - ',input2)
                    else:
                        input3 = input("Enter the extension you want (eg .txt ,.csv) ")
                        input2 = input2+input3
                        save_to_file(dictionary_occ_checker,input2)
                        print('DONE CHECK - ',input2)
                else:
                    for eachChar,occ in dictionary_occ_checker.items():
                        print(f"{eachChar} - {occ} ")
            except Exception as e :print('ERROR , ',e)
    except FileNotFoundError:print("FILE ISN'T THERE !!!")
    except Exception as e :print("ERROR ",e)
    

def save_to_file(dict,filename):
    try:
        with open(filename,"a") as newfile:
            for eachChar,occ in dict.items():
                newfile.write(f"{eachChar} - {occ} \n")
    except FileExistsError:print("FILE EXISTS BRO")
    except Exception as e :print("ERROR ! ",e)
if __name__ == "__main__":
    main()