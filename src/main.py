# This is your main script.
import sys, machine
sys.path.append("/")

from handlers.wake_on_lan_handler import WakeOnLanHandler
from modules.service_provider import ServiceProvider
from modules.logger import Logger
from modules.mqtt_subscriber import MqttSubscriber
from modules.wifi import Wifi
from modules.led import Led
from modules.app_settings import AppSettings

service_provider = ServiceProvider()

def setup():
  appsettings = AppSettings()
  appsettings.set("wifi_ssid", "REPLACE_WITH_WIFI_SSID")
  appsettings.set("wifi_password", "REPLACE_WITH_WIFI_PASSWORD")
  appsettings.set("mqtt_broker", "REPLACE_WITH_MQTT_BROKER")
  appsettings.set("mqtt_client_id", "REPLACE_WITH_MQTT_CLIENT_ID")
  appsettings.set("mqtt_port", "REPLACE_WITH_MQTT_PORT")
  appsettings.set("mqtt_user", "REPLACE_WITH_MQTT_USER")
  appsettings.set("mqtt_password", "REPLACE_WITH_MQTT_PASSWORD")
  appsettings.set("mqtt_topic", "REPLACE_WITH_MQTT_TOPIC")

  service_provider.register("appsettings", appsettings)
  service_provider.register("logger", Logger())
  service_provider.register("led",  Led(2))
  service_provider.register("wifi", Wifi())
  service_provider.register("mqtt", MqttSubscriber())
  
def main():
  print("\nLaunching NodeMCU")
  setup()

  try:
    logger: Logger = service_provider.get("logger")
    led: Led = service_provider.get("led")
    wifi: Wifi = service_provider.get("wifi")
    mqtt: MqttSubscriber = service_provider.get("mqtt")
    
    led.blink(5)
    wifi.connect()
    led.turn_on()
    
    mqtt.register_handler(WakeOnLanHandler())
    mqtt.subscribe()
    
  except Exception as ex:
    logger.log_error(f"An unexpected error occurred: {ex}")
  finally:
    machine.reset()

if __name__ == "__main__":
  main()