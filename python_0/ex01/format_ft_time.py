import time
from datetime import datetime


epoch = time.time()
epoch_formated = f"{epoch:,.4f}"
epoch_scientific = f"{epoch:.2e}"

now = datetime.now()
now_formatted = now.strftime("%b %d %Y")

print("Seconds since January 1, 1970: " + epoch_formated + " or " + epoch_scientific + " in scientific notation")
print(now_formatted)
