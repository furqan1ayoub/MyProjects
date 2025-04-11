#do basic dir enumeration & save the correct and found -> in file
import requests
import argparse
import sys
def argumentsParsing():
    parser = argparse.ArgumentParser(
        description="DIRECOTRY ENUMERATOR (safe use only!)",epilog="usecase eg - >  dirBuster.py -u url.com ")
    parser.add_argument("-u","--url",help="Enter the url after -u ")
    parser.add_argument("-v","--verbose",action="store_true")
    parser.add_argument("-o","--output",help="output file where to save the outputs -o ")
    parser.add_argument("-w", "--wordlist", default="dirFile.txt", help="Wordlist file for directory enumeration")
    #now return the args with values of users
    return parser.parse_args()
def main():
    #put all in dic
    args = argumentsParsing()
    #do now main work
    if not args.url:sys.exit("error ! ENTER URL with -u ")
    if args.verbose:print("VERBOSE MODE ON...")
    #
    if args.url:
        url=args.url
        output_file = args.output
        if not args.wordlist:
            print('NO WORDLIST FILE PROVIDEd using (default)- dirFile.txt')
            dirEnumerator(url, "dirFile.txt",output_file)
        else:
            wordlist_file=args.wordlist
            print(f"Using your wordlist file - {wordlist_file}")
            dirEnumerator(url,wordlist_file ,output_file)
def dirEnumerator(url, filename,output_file):
    try:
        with open(filename, "r") as dirFile:
            with open(output_file,"w") as newFile:
                tabs = "\t"*10 #just spacing and making heading clear
                newFile.write(f"{tabs}WORKING LINKS / DIRECOTIRES \n")
            for eachLine in dirFile:
                eachLine = eachLine.strip() # for whitespace remove
                if eachLine and eachLine[0] == "/": # to check eachline has sth in it
                    
                    # add now the dir & make full url to try
                    full_url = url.rstrip("/") +"/" + eachLine.strip().lstrip("/") #add (impt), rstip-> is kinda removes the last rstrip
                    try:
                        response = requests.get(full_url)
                        if response.status_code == 200:
                            print(f"FOUND - {eachLine} {[response.status_code]} ",)\
                            #call
                            save_to_file(output_file,full_url)
                        elif response.status_code in [301,302]: 
                            print(f"REDIRECTED - {eachLine} {response.status_code}")
                        else:print(f"NOT FOUND - {eachLine} {response.status_code}")
                    except requests.RequestException as e :
                        print(f"Error - {e}")
    except FileNotFoundError:
        print("FILE NOT FOUND")
    except Exception as e:
        print("error -->", e)

def save_to_file(output_file,full_url):
    try:
        with open(output_file,"a") as newFile:
            newFile.write(f"{full_url}\n")
    except ValueError:print('ENTER VALID NAME ')
    except Exception as e :print('ERROR ',e)
if __name__ == "__main__":
    main()
    print("DONE !!")