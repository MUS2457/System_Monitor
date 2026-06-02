import os
import sys
import termios
import tty
import select
from CORE import scheduler, storage
import time

def display_latest_metrics():
    gen = scheduler.scheduler()

    # ---------------- TERMINAL MODE SETUP ----------------
    # Save the current terminal settings.
    # This includes: input mode, echo, canonical mode, control chars, etc.
    # We MUST save this so we can restore the terminal later.
    old_settings = termios.tcgetattr(sys.stdin)

    # Switch terminal to "cbreak mode".
    # - Characters are delivered instantly (no Enter needed)
    # - No line buffering
    # - Perfect for real-time key detection
    # sys.stdin.fileno() = file descriptor 0 (terminal input stream)
    tty.setcbreak(sys.stdin.fileno())
    # -----------------------------------------------------

    try:
        while True:

            metrics = next(gen)
            storage.buffer_metrics(metrics)

            # Clear the terminal screen (Windows = cls, Linux = clear)
            os.system("cls" if os.name == "nt" else "clear")

            print(metrics)
            print("\nPress 'q' to return to menu")

            # IMPORTANT:
            # Sleep 1 second so the display loop runs at the same rhythm
            # as the scheduler loop. If display is too fast, scheduler
            # cannot update and time appears frozen.
            time.sleep(1)

            # ---------------- NON-BLOCKING KEY CHECK ----------------
            # select.select() checks if input is available on stdin.
            # It takes 3 lists:
            #   [read_list], [write_list], [error_list]
            # We only care about reading, so the other two are empty.
            #
            # Timeout = 0.1 seconds → do NOT block the loop.
            #
            # If a key was pressed, sys.stdin appears in the first list.
            if select.select([sys.stdin], [], [], 0.1)[0]:
                # Read exactly ONE character (no Enter needed because cbreak mode)
                key = sys.stdin.read(1)

                # If user pressed 'q', exit the function
                if key.lower() == "q":
                    return
            # ---------------------------------------------------------

    finally:
        # ---------------- TERMINAL RESTORATION ----------------
        # This restores the terminal to normal mode:
        # - canonical input
        # - echo on
        # - backspace works
        # - Enter required
        # - safe shell behavior
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
    
