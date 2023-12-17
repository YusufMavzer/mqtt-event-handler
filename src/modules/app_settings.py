
class AppSettings:
  
  _instance = None

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super(cls, cls).__new__(cls)
      cls._instance.config: dict[str, any] = {}
    return cls._instance
   
  def set(self, name: str, value: any):
    self._instance.config[name] = value
    return self
    
  def get(self, name: str) -> any:
    return self._instance.config.get(name)