import os
import sys
import termios
import tty
import select
from CORE import scheduler, storage
import time

def display_latest_metrics():
    gen = scheduler.scheduler()

    # Save the current terminal settings (for later restore)
    old_settings = termios.tcgetattr(sys.stdin)

    
    # sys.stdin.fileno() = file descriptor 0 (terminal input stream)
    tty.setcbreak(sys.stdin.fileno())  #  switch to cbreak mode, instant key detection (no Enter needed)
                                          # Change how to deliver input to file descriptor 0 ,(stdin) means the input only
    

    try:
        while True:

            metrics = next(gen)
            storage.buffer_metrics(metrics)

            # Clear the terminal screen (Windows = cls, Linux = clear)
            os.system("cls" if os.name == "nt" else "clear")

            print(metrics)
            print("\nPress 'q' to return to menu")

            time.sleep(1) # added sleep time to match scheduler speed (to connected loop must be in same speed)

            # select.select() checks whether stdin has any bytes  waiting.
            # If the user pressed a key, stdin becomes "readable" and appears in the first list.

            if select.select([sys.stdin], [], [], 0.1)[0]:
                
                key = sys.stdin.read(1) # read single key (cbreak mode) (1)byte

                if key.lower() == "q":
                    return

    finally:
        #  terminal restoration: This restores the terminal to normal mode: canonical input, safe shell behavior.
        
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
    
