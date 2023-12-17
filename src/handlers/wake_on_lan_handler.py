import ustruct
from data_types.mqtt_message import MqttMessage
from handlers.base_handler import BaseHandler
from modules.udp_broadcaster import UdpBroadcaster

class WakeOnLanHandler(BaseHandler):
  def _create_magic_packet(self, macaddress: str) -> bytes:
    if len(macaddress) == 17:
      sep = macaddress[2]
      macaddress = macaddress.replace(sep, "")
    elif len(macaddress) != 12:
      raise ValueError("Incorrect MAC address format")
    data = b'FF' * 6 + (macaddress * 16).encode()
    send_data = b''
    for i in range(0, len(data), 2):
      send_data = send_data + ustruct.pack(b'B', int(data[i: i + 2], 16))
    return send_data
  
  def can_handle(self, message: MqttMessage):
    return message.get_type() == "WakeOnLan"
    
  def handle(self, message: MqttMessage):
    mac_address = str(message.get_payload().get('mac_address'))
    magic_packet = self._create_magic_packet(mac_address)
    broadcaster = UdpBroadcaster()
    broadcaster.send_broadcast(magic_packet)
    broadcaster.close()
