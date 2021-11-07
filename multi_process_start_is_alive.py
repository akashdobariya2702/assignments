import random
import time
from multiprocessing import Process

def func(no):
  print(f'func: starting {no}')
  # custom codes
  time.sleep(random.randrange(1, 4))
  print(f'func: finishing {no}')
  return no

def get_api_data():
    jobs = []
    # steps 1, 2, 3
    for i in range(1, 4):
        p = Process(target=func, args=(i,))
        jobs.append(p)
        p.start()

    # wait till steps 1, 2, 3 multiple tasks completed
    while len(jobs) > 0:
        jobs = [job for job in jobs if job.is_alive()]

    # step 4
    func(4)

    jobs = []
    # steps 5, 6
    for i in range(5, 7):
        p = Process(target=func, args=(i,))
        jobs.append(p)
        p.start()

    # wait till steps 5, 6 multiple tasks completed
    while len(jobs) > 0:
        jobs = [job for job in jobs if job.is_alive()]

    # step 7
    result = func(7)

    return result

get_api_data()
