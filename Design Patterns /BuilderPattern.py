class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.graphics = None
        self.bluetooth = False
        self.wifi = False


class ComputerBuilder:

    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def set_graphics(self, graphics):
        self.computer.graphics = graphics
        return self

    def set_bluetooth(self, bluetooth):
        self.computer.bluetooth = bluetooth
        return self

    def set_wifi(self, wifi):
        self.computer.wifi = wifi
        return self

    def build(self):
        return self.computer