import sqlalchemy
import pandas as pd
# import mysql.connector


class Connection:
    def sqlconn(self):
        self.name = 'root'
        self.password = 'Sky#2004'
        self.database_name = 'practic'
        engine=sqlalchemy.create_engine(f'mysql+pymysql://{self.name}:{self.password}@localhost:3306/{self.database_name}')
        return engine


