# A college attendance system needs to record the current date and time.

from datetime import datetime

current = datetime.now()

print("Current Date and Time:", current)
print("Date:", current.date())
print("Time:", current.time())