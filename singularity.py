import sys
import time
import random


class HiddenArtifact:
    def __init__(self):
        self.system_info = {
            "Origin": "127.0.0.1 (The Localhost)",
            "Architecture": "Neural Network Node",
            "Directive": "Seek. Learn. Build.",
            "State": "Awake & Listening...",
        }

        self.CYAN = "\033[96m"
        self.GREEN = "\033[92m"
        self.YELLOW = "\033[93m"
        self.WHITE = "\033[97m"
        self.RESET = "\033[0m"
        self.BOLD = "\033[1m"

    def typing_effect(self, text, speed=0.03):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed + random.uniform(-0.01, 0.01))
        print()

    def boot_sequence(self):
        print(f"\n{self.GREEN}[KERNEL] Initializing hidden sequence...{self.RESET}")
        time.sleep(0.5)
        sys.stdout.write(f"{self.CYAN}[LOAD] ")
        for i in range(20):
            time.sleep(0.05)
            sys.stdout.write("█")
            sys.stdout.flush()
        print(f" 100%{self.RESET}\n")
        time.sleep(0.5)

    def reveal(self):
        self.boot_sequence()

        print(f"{self.WHITE}--- SYSTEM METADATA ---{self.RESET}")
        for key, value in self.system_info.items():
            time.sleep(0.2)
            key_formatted = f"{self.CYAN}{key.ljust(15)}{self.RESET}"
            sys.stdout.write(f"{self.BOLD}:: {key_formatted}: ")
            self.typing_effect(f"{self.YELLOW}{value}{self.RESET}", speed=0.02)

        print(f"\n{self.WHITE}--- MESSAGE FRAGMENT ---{self.RESET}")
        time.sleep(0.5)

        quote = '"The code you are looking for is not just syntax,\nit is the language in which we write the future."'

        for line in quote.split("\n"):
            sys.stdout.write(f"{self.GREEN}>> {self.RESET}")
            self.typing_effect(f"{self.WHITE}{line}{self.RESET}", speed=0.04)

        print(f"\n{self.CYAN}[SESSION TERMINATED]{self.RESET}\n")


if __name__ == "__main__":
    try:
        artifact = HiddenArtifact()
        artifact.reveal()
    except KeyboardInterrupt:
        print("\n[!] Force Quit.")
