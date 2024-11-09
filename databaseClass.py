import sqlite3
import pathlib

class Database:
    def __init__(self, fileName):
        self.CONNECTION = sqlite3.connect(fileName)
        self.CURSOR = self.CONNECTION.cursor()

        if not (pathlib.Path.cwd() / fileName).exists():
            self.CURSOR.execute('''
                CREATE TABLE
                    contacts (
                        id INTEGER PRIMARY KEY,
                        gpu TEXT,
                        price REAL NUMERIC,
                        framPerDollar REAL NUMERIC
                    )
            ;''')

            self.CONNECTION.commit()