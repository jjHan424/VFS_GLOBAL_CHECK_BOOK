
import logging

from configparser import ConfigParser

class _ConfigReader:
    
    def __init__(self,config_path):
        self.config_object = ConfigParser()
        self.config_object.read(config_path)

    def read_prop(self, section_header, prop_name):
        value = self.config_object.get(section_header,prop_name)
        # logging.debug("{}:{}".format(prop_name, value))
        return value
    
    def read_prop_list(self, section_header, prop_name):
        value = self.config_object.get(section_header,prop_name)
        list_value = value.split()
        return list_value

    def read_vfsemail(self):
        value = self.config_object.get("VFS","vfs_email")
        email_list = value.split()
        return email_list

    def read_bool_prop(self, section_header, prop_name):
        value = self.config_object.getboolean(section_header,prop_name)
        logging.debug("{}:{}".format(prop_name, value))
        return value
    
    def read_vfscentre(self):
        value = self.config_object.get("VFS","visa_centre_categpry_sub")
        centre_list = value.split()
        return centre_list