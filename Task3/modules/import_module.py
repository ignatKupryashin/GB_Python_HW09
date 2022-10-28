from modules.import_modules.txt_import import txt_import
from modules.import_modules.xml_import import xml_import
from modules.import_modules.csv_import import csv_import

def import_interface(filename):
    try:
        open(filename)
    except:
        print("Указанный файл отстутствует")
        return
    file_extention = filename[filename.rindex(".") + 1:]
    if file_extention in ["txt","csv","xml"]:

        if file_extention == "txt":
            txt_import(filename)

        elif file_extention == "xml":
            xml_import(filename)

        elif file_extention == "csv":
            csv_import(filename)

