import time
from datetime import datetime

epoch = time.time()
epoch_formated = f"{epoch:,.4f}"
epoch_scientific = f"{epoch:.2e}"

now = datetime.now()
now_formated = now.strftime("%b %d %Y")

print(
    f"Seconds since January 1, 1970: {epoch_formated} "
    f"or {epoch_scientific} in scientific notation"
)
print(now_formated)
