
class ServiceProvider:
  
  _instance = None
  
  def __new__(cls):
    if cls._instance is None:
      cls._instance = super(cls, cls).__new__(cls)
      cls._instance.services: dict[str, any] = {}
    return cls._instance
   
  def register(self, name: str, service: any):
    self._instance.services[name] = service
    return self
    
  def get(self, name: str) -> any:
    return self._instance.services.get(name)