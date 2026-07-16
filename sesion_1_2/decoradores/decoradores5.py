import time
import datetime

def log(fn):
    def wrapper():
        tiempo = datetime.datetime.now()
        print(fn(), tiempo)
    return wrapper


@log
def get_name():
    return "El profe usa mac y esta muy orgulloso de ello"


get_name()