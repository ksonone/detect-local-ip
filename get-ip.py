# Get Local IP Address
# Author : Kapil H. Sonone

from detectip import LocalIpDetector

ip = LocalIpDetector.TryToGetLocalIp()
print("IP Detected : ", ip)