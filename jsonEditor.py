from netaddr import EUI
import sys
import logging
import json
import argparse
import re
from dateutil.parser import parse

logger = logging.getLogger(__name__)



class ImportJson:
    def __call__(self, file='JSON.json'):
        try:
            self.file = file
            with open(self.file) as f:
                self.jsonRaw = json.load(f)
        except FileNotFoundError:
            logger.error("json file(JSON.json) not found")
            sys.exit(0)
        return self.jsonRaw


def save_in_file(obj):
    try:
        with open('outJson.json', 'w') as f:
            json.dump(obj, f)
    except Exception:
        logger.error("something happened with write ")
        sys.exit(0)
    


class EditFields:
    def __init__(self, imp):
        self.imp = imp
        
    def set_new_port(self, this_key: str, this_value: int, section="Port Settings"):
        self.imp[section][this_key] = this_value
        pass

    def set_new_by_MediaInterfaceConf_statusConf1(self, key:str, value
                                                  , section="Media Interface Settings",keyFirst="Network Status Indicator Configuration 1"):
        self.imp[section][keyFirst][key] = value
        pass

    def fin (self):
        return self.imp
     
    def set_manual(self, value, key, key2=None, key3=None):
        if key2 and key3:
            self.imp[key][key2][key3] = value
        elif key2:
            self.imp[key][key2] = value
        else:
            raise logger.error("incorrect input")
        pass


    
def set_bool(value) -> bool: 
    if value == "true":
        return True
    elif value == "false":
        return False

def set_time(value):
    return str(parse(value))
    
def set_hex(value):
    return int(value, 0)

def is_decimal(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def set_type(value):
    hex_pattern = r"^0[xX][0-9a-fA-F]+$"
    try:
        if value.lower() in {"true","false"} :
            return set_bool(value=value.lower())
        elif bool(re.fullmatch(hex_pattern, value)) == True:
            return set_hex(value=value)
        
        elif value.isdigit() or (value.startswith("-") and value[1:].isdigit()):
            return int(value)
        
        elif is_decimal(value) == True:
            return float(value)
        
        elif bool(parse(value)) == True:
            return set_time(value)
        
        else:
            return value()
    except ValueError:
        return value
# I can use netaddr EUI(value) for work with mac address but in current task it`s str format
# hex, decimal, bool, date-time !!
    
def main():
    parser = argparse.ArgumentParser(description="json editor", formatter_class=argparse.RawDescriptionHelpFormatter)
    
    parser.add_argument("value")
    parser.add_argument("key")
    parser.add_argument("--key2",help="(optional)")
    parser.add_argument("--key3",help="(optional)")
    args = parser.parse_args()
    
    program = EditFields(ImportJson()())
    
    program.set_manual(set_type(args.value), args.key, args.key2, args.key3)
    save_in_file(program.fin())
    
if __name__ =="__main__":
    main()

# program = EditFields(ImportJson()())
# program.set_manual(set_type("-9"), "Interface Settings","2nd_interface")
# save_in_file(program.fin())
    
    
    