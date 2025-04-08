from time import sleep, perf_counter
from threading import Thread


def task(tuple1):
    print('task started')
    print(tuple1)
    sleep(1)
    print('done')


start_time = perf_counter()

t1 = Thread(target=task, args=((1, 2, 3),)) 
t2 = Thread(target=task, args=((1, 2, 3),))

# start the threads
t1.start()
t2.start()

# wait for the threads to complete
t1.join()
t2.join()

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')
