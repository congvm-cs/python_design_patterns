class Computer():
    def make_sound(self):
        print("Beep")

    def show_loading_screen(self):
        print("Loading...")

    def close_all(self):
        print("Closing..")


class ComputerFacade():
    def __init__(self, computer):
        self.computer = computer

    def turn_on(self):
        self.computer.show_loading_screen()
        self.computer.make_sound()

    def turn_off(self):
        self.computer.show_loading_screen()
        self.computer.close_all()


if __name__ == "__main__":
    computer = Computer()

    computer_facade = ComputerFacade(computer)
    computer_facade.turn_on()
    computer_facade.turn_off()
