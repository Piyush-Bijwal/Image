# The script would list the projects accessible to signed user.

import argparse
import json
import googleapiclient.discovery
from pprint import pprint
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
from oauth2client.client import GoogleCredentials
import logging as log
from datetime import datetime
import os



credentials = GoogleCredentials.get_application_default()

service = discovery.build('cloudresourcemanager', 'v1', credentials=credentials)

def project_list(i_name):
    i_cnt = 0
    proj_list = []
    request = service.projects().list()
    while request is not None:
        response = request.execute()
#       print response
        for project in response['projects']:
            p_prj_parent = project['parent']
            if i_name in project['name'] and "organization" in p_prj_parent['type']:
 #              pprint(p_prj_parent)
                proj_list.append(project['name'])
#                pprint(str(i_cnt)+") "+str(project['name'])+":::"+str(p_prj_parent['type']))
 #               pprint("------------------------------------------------")
                i_cnt = i_cnt + 1
        request = service.projects().list_next(previous_request=request, previous_response=response)
    return proj_list


def project_name():
    i_name = input("Enter part of the project name: ")
    print (i_name)
    proj_list = project_list(i_name)
    if not proj_list:
        project_selected = ""
    else:
        i_cnt = 0
        for project_nme in proj_list:
            print (str(i_cnt)+") "+project_nme)
            i_cnt = i_cnt+1
        try:
            i_list = input("Enter line number of project name from list above: ")
        except:
            print ("Incorrect value selected")
            project_selected = ""
            return project_selected
        try:
            project_selected = proj_list[i_list]
        except:
            print ("Incorrect value selected")
            log.warning("Incorrect value selected")
            project_selected = ""
    return project_selected


def get_project():
    i_prj_nme = input("Do you know exact project name? (Y/n)")
    if i_prj_nme.upper() == "Y":
        i_name = raw_input("Enter project name: ")
        prj_name1 = project_list(i_name)
        try:
            prj_name = prj_name1[0]
        except:
            log.error("Incorrect value selected")
            print("Incorrect value selected")
            exit(1)
    else:
        prj_name = project_name()
    if not prj_name:
        print ("No project selected or project doesn't exist.")
        log.info("No project selected or project doesn't exist.")
        return 1
    else:
        print (prj_name)
        log.info("Project selected::: "+str(prj_name))
        return prj_name


if __name__ == '__main__':
    i_LogPath = os.getenv('TEMPDIR', os.getcwd())
    i_LogName = "Log_" + datetime.now().strftime("%Y""%m""%d""%H""%M""%S") + ".log"
    i_LogLoc = os.path.join(i_LogPath, i_LogName)
    log.basicConfig(filename=i_LogLoc, level=log.INFO)
    get_project()




##########
#Client ID: 699000165671-0ased8rk4gagtalu7gffiofipm5utpl8.apps.googleusercontent.com
#Client secret: BUHvsi9kIFOJewqmkEAKE4h3
##########