# Detect Local IP Address
# Author : Kapil H. Sonone

import socket
import struct
import os

# A helper class try to detect the local IP of the device.
class LocalIpDetector:

    @staticmethod
    def TryToGetLocalIp():
        # Find the local IP. Works on Windows and Linux. Always gets the correct routable IP.
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ip = ""
        try:
            # doesn't even have to be reachable
            s.connect(('1.1.1.1', 1))
            ip = s.getsockname()[0]
        except Exception:
            pass
        finally:
            s.close()
        return ip