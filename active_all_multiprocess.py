import multiprocessing
import active_deactive_mail_check
import os

def checkWithMultiProcess(numProcess, init, end, iter):
    interval = round((end - init)/numProcess)
    print(f'interval: {interval}')

    toChkRng = []
    for i in range(0, numProcess, 1):
        # print(end - interval*(numProcess - i))
        toChkRng.append(end - interval*(numProcess - i) + 1)
    toChkRng[0] = 0
    toChkRng.append(end)
    print(toChkRng)
    input()
    
    ## creating processes
    processes = [multiprocessing.Process(target=active_deactive_mail_check.checkActiveInactiveCorrupted,
                                         args=('total_active_inactive_list.txt',
                                                f'/output/active_all_{iter}.txt',
                                                f'/output/inactive_all_{iter}.txt',
                                                f'/output/corrupt_all_{iter}.txt',
                                                toChkRng[i], toChkRng[i+1])) for i in range(numProcess)]

    for process in processes:
        # starting processes 
        process.start() 
    
        # process IDs 
        print("ID of process: {}".format(process.pid)) 
    
    for process in processes:
        # wait until processes are finished 
        process.join()


if __name__ == '__main__':
    # printing main program process id 
    print("ID of main process: {}".format(os.getpid())) 
  
    checkWithMultiProcess(6, 1, 11887, 6)