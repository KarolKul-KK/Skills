import time
from textwrap import dedent
from gra_rozwinięcie import FrontDoor


def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {0} : {1} : {2}".format(int(hours), int(mins), sec))

input("Press Enter to start")
start_time = time.time()
FrontDoor.f_door()

input("Press Enter to stop")
end_time = time.time()

time_lapsed = end_time - start_time
time_convert(time_lapsed)