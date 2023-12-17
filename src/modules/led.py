import machine, time

class Led:
  def __init__(self, pin: int = int(2)):
    self.pin = machine.Pin(pin, machine.Pin.OUT)
   
  def turn_on(self):
    self.pin.value(0)
    
  def turn_off(self):
    self.pin.value(1)
  
  def blink(self, num_blinks ,delay_in_ms: int = int(200)):
    for _ in range(num_blinks):
      self.turn_on()
      time.sleep_ms(delay_in_ms)
      self.turn_off()
      time.sleep_ms(delay_in_ms)