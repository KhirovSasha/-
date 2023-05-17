import time
import os

while True:
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    directory = 'time'

    if not os.path.exists(directory):
        os.makedirs(directory)

    filename = os.path.join(directory, f"{current_time.replace(':', '')}.txt")
        
    with open(filename.replace(' ', ''), "w") as f:
        f.write(current_time)
