import subprocess
import time

def open_calculator_continuously():
    try:
        while True:
            subprocess.run("calc", check=True)
            time.sleep(0.1) 
            print("Calculator opened successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to open Calculator: {e}")
    except KeyboardInterrupt:
        print("Script terminated by user.")

if __name__ == "__main__":
    open_calculator_continuously()
