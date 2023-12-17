import socket, time, struct
from modules.service_provider import ServiceProvider
from modules.wifi import Wifi
from modules.logger import Logger

class UdpBroadcaster:
  def __init__(self):
    self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    self._logger: Logger = ServiceProvider().get("logger")
  
  def send_broadcast(self, data , port:int = int(9)):
    try:
      wifi: Wifi = ServiceProvider().get("wifi")
      broadcast_address = (wifi.get_broadcast_address(), port)
      self.udp_socket.sendto(data, broadcast_address)
      time.sleep(3)
      self._logger.log_info("Broadcast packet sent successfully.")
    except Exception as e:
      self._logger.log_error("Error sending broadcast packet:", e)

  def close(self):
    self.udp_socket.close()
    self._logger.log_info("Socket closed.")
