import time
import multiprocessing
import argparse


def cpu_stress():
    while True:
        pass

def ram_stress():
    memory = []
    while True:
        memory.append(' ',*10**6)


 # Ram and Cpu pressure

# MAIN


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ram AND Cpu Stress")

    parser.add_argument(
        "--duration" , type=int , default=60 , help="Duration is 60 Add MAX 1000000 :)"
    )
    parser.add_argument(
        "--cpu" , action="store_true" , help="Enable Cpu Stress"
    )
    parser.add_argument(
        "--ram", action="store_true" , help="Enable Ram Stress"
        )
    args = parser.parse_args()
    processes = []

    if args.cpu:
        cpu_process = multiprocessing.Process(target=cpu_stress)

    if args.ram:
        ram_process = multiprocessing.Process(target=ram_stress)

    for process in processes:
        process.start()


    try:
        print(f"Running Stress test")
    finally:
        for process in processes:
            process.terminate()    


    for process in processes:
        process.join()

    print("Stress Test Completed !")                
