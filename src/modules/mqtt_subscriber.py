import ujson
from umqtt.simple import MQTTClient
from handlers.base_handler import BaseHandler
from modules.service_provider import ServiceProvider
from modules.led import Led
from data_types.mqtt_message import MqttMessage
from modules.logger import Logger
from modules.app_settings import AppSettings

class MqttSubscriber:
  def __init__(self): 
    config = AppSettings().get
    server:str = config("mqtt_broker")
    client_id:str = config("mqtt_client_id")
    port:int = config("mqtt_port")
    user:str = config("mqtt_user")
    password:str = config("mqtt_password")
    self._topic:str = config("mqtt_topic")
    
    self._mqtt_client = MQTTClient(client_id, server, port = port, user=user, password=password)
    self._handlers: list[BaseHandler] = []
    self._logger: Logger = ServiceProvider().get("logger")

  def _handle_message(self, topic, message):
    services = ServiceProvider()
    led: Led =  services.get("led")
    
    string_data = message.decode('utf-8')
    data:dict = ujson.loads(string_data)
    msg = MqttMessage(data.get("type"), data.get("payload"))
    self._logger.log_info(msg.to_string())
    led.blink(3)
    for handler in self._handlers:
      if handler.can_handle(msg):
        handler.handle(msg)

  def subscribe(self):
    try:
      self._mqtt_client.connect()
      self._mqtt_client.set_callback(lambda topic, message: self._handle_message(topic, message))
      self._mqtt_client.subscribe(self._topic)
      self._logger.log_info(f"Subscribed to topic: {self._topic}")
      while True:
        self._mqtt_client.wait_msg()
    finally:
      self._mqtt_client.disconnect()

  def register_handler(self, handler: BaseHandler):
    self._handlers.append(handler)
