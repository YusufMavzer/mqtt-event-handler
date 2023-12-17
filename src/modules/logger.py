import utime

class Logger:
  def __get_utc_time_iso8601(self) -> str:
    current_time = utime.time()
    utc_time = utime.localtime(current_time)
    iso8601_time = "{:04}-{:02}-{:02}T{:02}:{:02}:{:02}Z".format(
        utc_time[0], utc_time[1], utc_time[2],
        utc_time[3], utc_time[4], utc_time[5]
    )
    return iso8601_time
    
  def log_info(self, message: str):
    print(f"Info: [{self.__get_utc_time_iso8601()}] {message}")
  
  def log_warning(self, message: str):
    print(f"Warning: [{self.__get_utc_time_iso8601()}] {message}")
    
  def log_error(self, message: str):
    print(f"Error: [{self.__get_utc_time_iso8601()}] {message}")