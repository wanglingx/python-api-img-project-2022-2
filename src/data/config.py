import mysql.connector
import yaml
from yaml.loader import SafeLoader

class Connector:
    def ConnectorMysql():
        with open('./databaseInfo.yaml') as f:
            myInfo = yaml.load(f,Loader=SafeLoader)
            mydb = mysql.connector.connect(
                host = myInfo[0].HOST,
                user = myInfo[0].USER,
                passwd=myInfo[0].PWD,
                database=myInfo[0].DATABASE_NAME,
                auth_plugin=myInfo[0].AUTH_PLUGIN
            )

        print("Connection Success !")
        return mydb
