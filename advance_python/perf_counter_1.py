#program to demostrate time module

from time import sleep, perf_counter

def task():
    print('Starting a task...')
    sleep(3)
    print('done')


start_time = perf_counter()

task()
task()

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')
