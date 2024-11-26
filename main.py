from circuit_simulation import run_simulator
from code import run
import threading
import time

state = None


def main():
    t1 = threading.Thread(target=run_simulator)
    t2 = threading.Thread(target=run)

    t1.start()
    time.sleep(0.5)
    t2.start()


main()
