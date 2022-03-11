import mysql.connector
from alive_progress import alive_bar, styles
from datetime import datetime


class SQLConnection:
    def __init__(self, h, u, p, iotName):
        self.iotName = iotName
        with alive_bar(unknown="dots_waves", title='Connecting to Database', stats=False, elapsed=False, calibrate=5,
                       monitor=False) as bar:
            self.mydb = mysql.connector.connect(
                host=h,
                user=u,
                password=p
            )
            bar()
        self.cursor = self.mydb.cursor()

        self.formatDB()

    def formatDB(self):
        with alive_bar(title='Formatting Database') as bar:
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS LineCounter")

            self.cursor.execute("USE LineCounter;")

            self.cursor.execute("""CREATE TABLE IF NOT EXISTS Cameras
                (
                  id              INT unsigned NOT NULL AUTO_INCREMENT,
                  cameraName      VARCHAR(150) NOT NULL,
                  peopleCount     VARCHAR(150) NOT NULL,                
                  lastUpdated     VARCHAR(150) NOT NULL,                
                  PRIMARY KEY     (id)                                  
                );
                """)

            self.cursor.execute("SELECT * FROM Cameras WHERE cameraName = \'{}\';".format(self.iotName))

            if len(self.cursor.fetchall()) == 0:
                print("a")
                self.cursor.execute("INSERT INTO Cameras (cameraName, peopleCount, lastUpdated) VALUES ('{}', 0,0);".format(self.iotName))
                self.mydb.commit()
            bar()

    def updateDB(self, peopleCount):
        self.cursor.execute("UPDATE Cameras SET peopleCount = \'{}\', lastUpdated = \'{}\' WHERE cameraName = \'{}\';".format(peopleCount, datetime.now(), self.iotName))
        self.mydb.commit()

