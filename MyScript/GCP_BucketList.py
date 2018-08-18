
import GCP_ProjectSelect
import os
from datetime import datetime
import logging as log
import argparse
import json
import googleapiclient.discovery


def create_service():
    return googleapiclient.discovery.build('storage', 'v1')





if __name__ == '__main__':
    i_LogPath = os.getenv('TMPDIR', os.getcwd())
    i_LogName = "Log_Bucket" + datetime.now().strftime("%Y""%m""%d""%H""%M""%S") + ".log"
    i_LogLoc = os.path.join(i_LogPath, i_LogName)
    log.basicConfig(filename=i_LogLoc, level=log.DEBUG)
    log.info("Calling function get_project")
    i_project_name = GCP_ProjectSelect.get_project()
    print ("Project selected:::"+i_project_name)


