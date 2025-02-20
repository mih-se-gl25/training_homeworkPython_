import os
import sys
import logging
import json

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
     
g = EditFields(ImportJson()())
g.set_new_port("SET_0",11343431)
g.set_new_port("SET_7",955434599)
g.set_new_by_MediaInterfaceConf_statusConf1(key="VERSION",value=22222.0)
save_in_file(g.fin())
