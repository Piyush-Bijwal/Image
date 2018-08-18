


import os
import sys
from datetime import datetime

def exit_code():
    ERR_CODE=$1
    ERR_MSG=$2
    Log_Msg "::: Failed with error message \n\t\t $ERR_MSG"
    exit 1

def Log_Msg(i_LogLoc,i_Msg,i_MegCode):
    i_time = datetime.now().strftime("%Y""%m""%d""%H""%M""%S")
try:
    filelog = open(i_LogLoc1,"w")
    filelog.writelines("")
    filelog.close()
except:
    print(NameError)




i_LogPath = os.getenv('TMPDIR',os.getcwd())
i_LogName="Log_"+datetime.now().strftime("%Y""%m""%d""%H""%M""%S")+".log"
i_LogLoc=os.path.join(i_LogPath,i_LogName)


import os
from google.appengine.api import app_identity

bucket_name = os.environ.get('BUCKET_NAME',app_identity.get_default_gcs_bucket_name())


