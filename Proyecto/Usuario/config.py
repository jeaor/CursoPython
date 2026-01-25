import sqlite3
def ConfigStart():
    bd = sqlite3.connect("bd-si.db")
    return bd