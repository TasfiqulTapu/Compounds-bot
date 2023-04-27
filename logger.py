from datetime import datetime


class Logger():
  def __init__(self, logfile=None, channel=None):
    self.logfile = logfile
    self.START_BOLD = "\033[1m"
    self.END_BOLD = "\033[22m"
    self.ENDC = "\033[0m"
    self.ERROR_RED = "\033[31m"
    self.INFO_CYAN = "\033[36m"
    self.THREAD_GREEN = "\033[32m"
    self.GUILD_YELLOW = "\033[33m"
  
  def log(self, msg, type):
    log_msg = ""
    if type == "ERR":  
      log_msg = self.formatter(msg, type, self.ERROR_RED)
    elif type == "INFO":
      log_msg = self.formatter(msg, type, self.INFO_CYAN)
    elif type == "THREAD":
      log_msg = self.formatter(msg, type, self.THREAD_GREEN)
    elif type == "ADD" or type == "REM":
      log_msg = self.formatter(msg, type, self.GUILD_YELLOW)

    if self.logfile: self.file_log(msg,type)

    print(log_msg)


  def formatter(self, msg, type, color):
    now = datetime.now()
    time = now.strftime("[%d-%b-%y %H:%M:%S]")
    return f"{self.START_BOLD}{time}{color}[{type}]{self.ENDC}{self.END_BOLD} {msg}"

  def file_log(self, msg, type):
    now = datetime.now()
    time = now.strftime("[%d-%b-%y %H:%M:%S]")
    with open(self.logfile, "a") as f:
      f.write(f"{time}[{type}] {msg}\n")



logger = Logger()