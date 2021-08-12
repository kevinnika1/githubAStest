import os
import logging
import datetime
import cadspy

logger = logging.getLogger(__name__)

def infer(credentials, parameters):
    """
    Demo root function, customise as needed.

    :param str text: String to return
    """
    ##
    # Example of unpacking credentials to connect to ICW
    ##
    icw = cadspy.DatabaseConnection(user=credentials['ICW']['user'],
                                    password=credentials['ICW']['password'])

    raise NotImplementedError
