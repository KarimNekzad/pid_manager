from pid_manager import PIDManager
from pid_excepts import *


# Text file containing output
f = open("output.txt", "w")

# Successfully allocates PID map
try:
    result = PIDManager.allocate_map()
    if result == 1:
        s = "PID map allocated."
        print(s)
        f.write(s + "\n")
except MapAllocationError as e:
    print("Error:", str(e))
    f.write("Error: " + str(e) + "\n")

# Tries to allocate a PID map again, which raises an exception
try:
    PIDManager.allocate_map()
except MapAllocationError as e:
    print("Error:", str(e))
    f.write("Error: " + str(e) + "\n")

# Allocates 3 PIDs
for i in range(3):
    try:
        pid = PIDManager.allocate_pid()
        s = "Allocated PID " + str(pid)
        print(s)
        f.write(s + "\n")
    except PIDAllocationError as e:
        print("Error:", e)
        f.write("Error: " + str(e) + "\n")
        break

# Attempts to release 5 PIDs, which is more than currently allocated, raising an exception
for i in range(5):
    try:
        PIDManager.release_pid(i + PIDManager.MIN_PID)
        f.write("Released PID " + str(i + PIDManager.MIN_PID) + "\n")
    except OutOfBoundsError as e:
        print("Error:", e)
        f.write("Error: " + str(e) + "\n")
        break
    except ReleaseError as e:
        print("Error:", e)
        f.write("Error: " + str(e) + "\n")
        break

# Attempts to release a PID out of bounds
try:
    PIDManager.release_pid(5001)
except OutOfBoundsError as e:
    print("Error:", e)
    f.write("Error: " + str(e) + "\n")
except ReleaseError as e:
    print("Error", e)
    f.write("Error: " + str(e) + "\n")

# Attempts to release a PID out of bounds again
try:
    PIDManager.release_pid(299)
except OutOfBoundsError as e:
    print("Error:", e)
    f.write("Error: " + str(e) + "\n")
except ReleaseError as e:
    print("Error", e)
    f.write("Error: " + str(e) + "\n")

# Releases a PID within bounds
try:
    PIDManager.release_pid(5000)
except OutOfBoundsError as e:
    print("Error:", e)
    f.write("Error: " + str(e) + "\n")
except ReleaseError as e:
    print("Error:", e)
    f.write("Error: " + str(e) + "\n")

# Attempts to allocate 5 more PIDs than there are available
for i in range(len(PIDManager.pid_list) + 5):
    try:
        PIDManager.allocate_pid()
        # Not printing success messages because this would print 4701 times
    except PIDAllocationError as e:
        print("Error:", e)
        f.write("Error: " + str(e) + "\n")
        break

# Size of PID map displayed. Size is 4701 instead of 4700 because the range of
# 300 and 5000 are inclusive, thus requiring the list to be 1 larger than max - min.
s = "Length of PID map: " + str(len(PIDManager.pid_list))
print(s)
f.write(s + "\n")

# Close output text file
f.close()
