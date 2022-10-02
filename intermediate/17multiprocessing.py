from multiprocessing import Process, Value, Array, Lock
import time
import os

# def square_number():
#     for i in range(1000):
#         i * i
# if __name__=="__main__":
#     processes=[]
#     num_processes=os.cpu_count()
#     # number of cpu on the machine. usually a good choice for the number of processes

#     # create processes and asign a function for each proses
#     for i in range(num_processes):
#         process=Process(target=square_number)
#         processes.append(process)

#     # start all processes
#     for process in processes:
#         process.start()
    
#     # wait for all processes to finish
#     # block the main program until these processes are finished

#     for process in processes:
#         process.join()











# def add_100(number):
#     for i in range(100):
#         time.sleep(0.01)
#         number.value+=1



# if __name__=="__main__":
#     shared_number=Value('i',0)
#     print('number at beginning is', shared_number.value)

#     p1=Process(target=add_100, args=(shared_number,))
#     p2=Process(target=add_100, args=(shared_number,))



#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     print('number at end is ', shared_number.value)















# def add_100(number, lock):
#     for i in range(100):
#         time.sleep(0.01)
#         lock.acquire()
#         number.value+=1
#         lock.release()



# if __name__=="__main__":

#     lock=Lock()
#     shared_number=Value('i',0)
#     print('number at beginning is', shared_number.value)

#     p1=Process(target=add_100, args=(shared_number,lock))
#     p2=Process(target=add_100, args=(shared_number,lock))



#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     print('number at end is ', shared_number.value)











def add_100(numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        for number in numbers:
            number+=1
            


if __name__=="__main__":

    lock=Lock()
    shared_array=Array('d', [0.0, 100.0, 200.0])
    print('array at beginning is', shared_array[:])

    p1=Process(target=add_100, args=(shared_array,lock))
    p2=Process(target=add_100, args=(shared_array,lock))



    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('array at end is', shared_array[:])
