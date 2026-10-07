# Functions
import time
#! Functions without Parameters
#? NASA Themed Examples
def launch_countdown():
    print("T-minus 10 seconds and counting...")
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    print("lift off! the rocket has launched into space.")

launch_countdown()

#On monday NASA launches rocket 1
launch_countdown()


