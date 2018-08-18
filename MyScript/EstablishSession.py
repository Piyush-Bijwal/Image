import os
from httplib2 import Http
from pprintpp import pprint
from googleapiclient import discovery
from apiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
from google.cloud import datastore



def storageconnect(CredPath):
    SCOPE = ['https://www.googleapis.com/auth/devstorage.read_write']
    credentials = service_account.Credentials.from_service_account_file(CredPath, scopes=SCOPE)
    return credentials


def projectconnect(CredPath):
    SCOPE = ['https://www.googleapis.com/auth/cloud-platform']
    credentials = service_account.Credentials.from_service_account_file(CredPath, scopes=SCOPE)
    return credentials


#http_auth = credentials.authorize(Http())

def object_list(credentials,BUCKET_NAME):
    service = discovery.build('storage', 'v1', credentials=credentials)
    request = service.objects().list(bucket=BUCKET_NAME)
    try:
        response = request.execute()
    except HttpError as error:
        print("HttpError: %s" % str(error))
        raise
    except Exception as error:
        print("%s: %s" % (error.__class__.__name__, str(error)))
        raise
    #print(response)
    return response

def process_obj(obj_list):
    for items in obj_list['items']:
        t_str = 'print ('
        t_elements = ''
        for items_list in items:
            t_str = t_str+'items[\''+items_list+'\'],'
            t_elements = t_elements +" "+ items_list
        t_str = t_str+')'
        #print (t_elements)
        exec(t_str)


def datastore_client(project_id):
    return datastore.Client(project_id)

def project_details(projectcred):
    service = discovery.build('cloudresourcemanager', 'v1', credentials=projectcred)
    request = service.projects().list()
    try:
        response = request.execute()
    except Exception as error:
        print("%s: %s" % (error.__class__.__name__, str(error)))
        raise
    return response


if __name__ == '__main__':
    CredPath = os.getenv('GOOGLE_CLIENT_SECRETS')
    BUCKET_NAME = os.environ['GOOGLE_DEFAULT_BUCKET']
    storagecred = storageconnect(CredPath)
    obj_list = object_list(storagecred, BUCKET_NAME)
    projectcred = projectconnect(CredPath)
    prjlis = project_details(projectcred)
    project_id=prjlis['projects'][0]['projectId']
    print (project_id)
    datastore_client(project_id)


