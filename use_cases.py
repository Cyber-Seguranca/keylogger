# use_cases.py
class RegisterKeyPress:
    def __init__(self, output_port):
        self.output_port = output_port

    def execute(self, key_press):
        self.output_port.write_to_log(key_press)
