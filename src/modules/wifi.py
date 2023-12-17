import network, time
from modules.service_provider import ServiceProvider
from modules.logger import Logger
from modules.app_settings import AppSettings

class Wifi:
  def __init__(self, time_out_in_seconds = int(30)):
    config = AppSettings().get
    self.ssid = config("wifi_ssid")
    self.password = config("wifi_password")
    self.timout = time_out_in_seconds * 1000
    self.nic = network.WLAN(network.STA_IF)
    self.nic.active(True)
    self._logger: Logger = ServiceProvider().get("logger")
    self._logger.log_info(f"SSID: {self.ssid} PASS: {self.password}")
   
  def is_connected(self):
    return bool(self.nic.isconnected())
  
  def get_mac_address(self):
    mac = self.nic.config('mac')
    return ":".join("{:02X}".format(b) for b in mac)
  
  def get_ip_address(self):
    if self.is_connected():
      return self.nic.ifconfig()[0]
    return ""
  
  def get_broadcast_address(self):
    if self.is_connected():
        ip_address, subnet_mask, _, _ = self.nic.ifconfig()
        ip_parts = list(map(int, ip_address.split('.')))
        subnet_parts = list(map(int, subnet_mask.split('.')))
        broadcast_parts = [ip_parts[i] | (~subnet_parts[i] & 255) for i in range(4)]
        return '.'.join(map(str, broadcast_parts))
    return ""
  
  def connect(self, use_static_ip=False, static_ip=None):
    self._logger.log_info("Attempting to connect to Wi-Fi.")
    if self.is_connected():
      self._logger.log_info(self.get_ip_address())
      self._logger.log_info(self.get_broadcast_address())
      self._logger.log_info(self.get_mac_address())
      return
    
    self.nic.connect(self.ssid, self.password)
    start_time = time.ticks_ms()
    
    while not self.is_connected():
      is_timeout = time.ticks_ms() - start_time > self.timout
      if is_timeout:
        self._logger.log_info("Connection timeout. Unable to connect to Wi-Fi.")
        break
      time.sleep(1)
    
    if not self.is_connected():
      self.connect()
    
    self._logger.log_info(self.get_ip_address())
    self._logger.log_info(self.get_broadcast_address())
    self._logger.log_info(self.get_mac_address())
    self._logger.log_info("Connected to Wi-Fi.")