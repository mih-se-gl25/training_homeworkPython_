import argparse
import sys
from bs4 import BeautifulSoup
from colorama import Fore, init, Style


init(autoreset=True)

def set_color_and_return(sev: str, message: str, file:str="empty"):
    
    try:
        if sev == "LOG_ERROR":
            print(f"{Fore.RED}{message}{Style.RESET_ALL}\n"+file)
        if sev == "LOG_INIT":
            print(f"{Fore.BLUE}{message}{Style.RESET_ALL}\n"+file)    
        if sev == "LOG_FLOW":
            print(f"{Fore.GREEN}{message}{Style.RESET_ALL}\n"+file)    
        if sev == "LOG_INFO":
            print(f"{Fore.LIGHTBLUE_EX}{message}{Style.RESET_ALL}]\n"+file)
    except:
        print(f"{Fore.LIGHTBLUE_EX}{message}{Style.RESET_ALL}]\n"+file)
    pass


def import_xml():
    try:    
        with open('Decoder.xml',"r", encoding="utf-8") as xlmFile:
            raw = xlmFile.read()
        soup= BeautifulSoup(raw, "xml")
        return soup
    except FileNotFoundError:
        print("not found file.xml")
        sys.exit(0)

def get_file_path(xml, id_file):
    file_list = xml.find_all("File")
    outFile =""
    for file in file_list:
        file_path = file.get("ID")
        try:
            if file_path == id_file:
                outFile = file.get_text().replace("\\","")
                return outFile
        except Exception:
                print("not found file")
                sys.exit(0)
        

def return_message_bt_id(id:str):
    messages = import_xml().find_all("Message")
    out_message = ""
    for message in messages:
        iterable_id= message.get("ID")
        if iterable_id == id:
            out_message = message
            break
    id_file = out_message.get("File")

    sever= out_message.get("Severity")
    path = get_file_path(import_xml(),id_file)
    set_color_and_return(sev=sever,message=out_message, file=path)


def main():
    parser = argparse.ArgumentParser(description="search in xml ", formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("id")
    args = parser.parse_args()
    return_message_bt_id(args.id)

    
if __name__ =="__main__":
    main()