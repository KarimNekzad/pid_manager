from pid_excepts import *


class PIDManager:
    MIN_PID = 300
    MAX_PID = 5000

    pid_list = [-1]

    @staticmethod
    def allocate_map():
        if PIDManager.pid_list[0] != -1:
            raise MapAllocationError("PID map already allocated")

        # Zero initializes a list of PIDs whose size is 1 + the difference of the max and min legal PID.
        # +1 because the range of 300 and 5000 are inclusive, therefore, we need 1 more than max - min
        PIDManager.pid_list = [0] * (PIDManager.MAX_PID - PIDManager.MIN_PID + 1)
        return 1

    @staticmethod
    def allocate_pid():
        if PIDManager.pid_list[0] == -1:
            raise PIDAllocationError("Must allocate map before allocating pid")

        for i in range(len(PIDManager.pid_list)):
            if PIDManager.pid_list[i] == 0:
                PIDManager.pid_list[i] = 1
                return i + PIDManager.MIN_PID  # Ensures PID is within range

        raise PIDAllocationError("All PIDs in use")

    @staticmethod
    def release_pid(pid):
        # Converts the 'pid' parameter to a valid index for the pid_list
        pid_index = pid - PIDManager.MIN_PID

        if PIDManager.pid_list[0] == -1:
            raise ReleaseError("Must allocate map before releasing pid")

        if pid_index > len(PIDManager.pid_list)-1 or pid_index < 0:
            raise OutOfBoundsError("PID " + str(pid) + " is out of bounds")

        if PIDManager.pid_list[pid_index] == 0:
            raise ReleaseError("PID " + str(pid) + " is already empty")
        else:
            PIDManager.pid_list[pid_index] = 0
            print("Released PID", str(pid))
