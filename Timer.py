import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Fire in the hole!!')

try:
    t = input("Enter the time in seconds: ")
    
    if not t.isdigit():
        raise ValueError("Input must be a positive integer.")

    t = int(t)

    if t < 0:
        raise ValueError("Time cannot be negative.")

    countdown(t)

except ValueError as e:
    print(f"Invalid input: {e}")
