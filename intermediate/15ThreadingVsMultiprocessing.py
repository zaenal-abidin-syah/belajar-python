# from multiprocessing import Process
# import os 
# import time

# def squareNumbr():
#     for i in range(100):
#         i+i
#         time.sleep(0.1)

# processes=[]
# num_prosesses=os.cpu_count()


# # create prosess

# for i in range(num_prosesses):
#     p=Process(target=squareNumbr)
#     processes.append(p)

# # start
# for i in processes:
#     p.start()

# for i in processes:
#     p.join()

# print('end main')







from threading import Thread
import os 
import time

def squareNumbr():
    for i in range(100):
        i+i
        time.sleep(0.1)

threads=[]
num_threads=10


# create prosess

for i in range(num_threads):
    t=Thread(target=squareNumbr)
    threads.append(t)

# start
for i in threads:
    t.start()

for i in threads:
    t.join()

print('end main')

