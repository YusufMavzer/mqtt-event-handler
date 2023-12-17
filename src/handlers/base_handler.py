from data_types.mqtt_message import MqttMessage

class BaseHandler:  
  def can_handle(self, message: MqttMessage):
    pass
  
  def handle(self, message: MqttMessage):
    pass
