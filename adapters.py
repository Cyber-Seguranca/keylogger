# adapters.py
class FileLogOutputPort:
    def __init__(self, log_file):
        self.log_file = log_file

    def write_to_log(self, key_press):
        try:
            with open(self.log_file, 'a') as f:
                f.write('{}\n'.format(key_press.key_char))
        except AttributeError:
            with open(self.log_file, 'a') as f:
                f.write('{}\n'.format(key_press))
