import ujson

class MqttMessage:
  def __init__(self, type: str, payload: dict):
    self.type = type
    self.payload = payload
    
  def get_type(self):
    return self.type

  def get_payload(self):
    return self.payload
  
  def to_string(self):
    return f"type: '{self.type}' payload:'{ujson.dumps(self.payload)}'"