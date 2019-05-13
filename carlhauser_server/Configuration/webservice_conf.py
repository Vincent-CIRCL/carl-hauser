# ==================== ------ STD LIBRARIES ------- ====================

from enum import Enum, auto
import logging
import sys, os

# ==================== ------ PERSONAL LIBRARIES ------- ====================
sys.path.append(os.path.abspath(os.path.pardir))

from carlhauser_server.Configuration.template_conf import FORMATTER as FORMATTER

class X_MODES(Enum):
    X = auto()
    Y = auto()

class Default_webservice_conf():
    def __init__(self):
        # Please note that CERT and KEY files must be in carl-hauser/carlhauser_server (where the flask server is)
        self.CERT_FILE = './cert.pem'
        self.KEY_FILE = './key.pem'