# %%

from datetime import datetime
import time

# %%

inicio = datetime.now()

time.sleep(5)

final = datetime.now()

# %%

def timer(function):

    def wrapper():

        inicio = datetime.now()
        function()
        final = datetime.now()
        tempo = final - inicio
        print(tempo)
        return tempo
    return wrapper

# %%

@timer
def hello() -> str:
    time.sleep(5)
    return 'Ola mundo do flask'

# %%