import time

current_time = time.time()

print(f"Seconds since January 1, 1970: {current_time:,.4f} or {current_time:.2e} in scientific notation")

print(time.strftime("%b %d %Y", time.gmtime(current_time)))