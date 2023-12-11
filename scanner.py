from socket import *
import sys
import time
# from threading import Thread, Lock
# from queue import Queue
# import argparse
# Get user input on scan target

target = input("Enter scan target: ")
targetIP = gethostbyname(target)

# get start time
st = time.time()

print("_" * 30)
print("Scanning target...", targetIP)
print("_" * 30)

def scan():
    try:
        # small port range for quick use
        for port in range (1,1000):
            s = socket(AF_INET, SOCK_STREAM)
            result = s.connect_ex((targetIP, port))
            if result == 0:
                print("Port {}: Open".format(port))
            s.close()
    except KeyboardInterrupt:
        print("Operation cancelled by user.")
        sys.exit()
    except error:
        print("Could not connect to server.")
        sys.exit()
scan()

# get end time
et = time.time()

elapsed_time = et - st

print('Time spent: ', elapsed_time, 'seconds.')


# -- Begin the threading madness --
# Could only get one connection, wouldn't close and move to next
# # number of threads. I want to use threading so we can scan multiple ports
# simultaneously
# thread_ct = 150
# q = Queue()
# print_lock = Lock()
# # Function to testing port status
# def port_scan(port):
# s = socket()
# # while True:
# try:
# s.connect((host, port))
# except:
# with print_lock:
# print(f"{host:15}:{port:5} is closed ", end='\r')
# else:
# with print_lock:
# print(f"{host:15}:{port:5} is open ")
# finally:
# s.close()
# # if not s:
# # break
# def scan_thread():
# global q
# while True:
# # get port number
# worker = q.get()
# # scan the port
# port_scan(worker)
# # tells the queue that scanning that port is finished
# q.task_done
# def main(host, ports):
# global q
# for t in range(thread_ct):
# # start the thread
# t = Thread(target=scan_thread)
# # the current running thread will end when the main thread ends
# t.daemon = True
# # start daemon thread from above
# t.start()
# for worker in ports:
# # use the worker to put each port into the queue for scanning
# q.put(worker)
# q.join()
# # I want to be able to pass hosts and ports from the CLI, so I use an argument
parses (argparse)
# if __name__ == "__main__":
# parser = argparse.ArgumentParser(description="Your new favorite port scanner!
Made by Robert James.")
# parser.add_argument("host", help="The scan target")
# parser.add_argument("--ports", "-p", dest="port_range", default="1-65535")
# args = parser.parse_args()
# host, port_range = args.host, args.port_range
# start_port, end_port = port_range.split("-")
# start_port, end_port = int(start_port) , int(end_port)
# ports = [ p for p in range(start_port, end_port)]
# # get end time
# et = time.time()
# # execution time (in wall time)
# elapsed_time = time.time() - st
# print('Time spent:', time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
# main(host, ports)