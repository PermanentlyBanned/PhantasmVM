#!/usr/bin/env python3
import random
import time
import threading
from collections import deque

class PhantasmVM:
    def __init__(self):
        self.concentration = 1.0
        self.command_queue = deque()
        self.log = []
        self.running = True
        self.lock = threading.Lock()
        self.current_os = random.choice([
            "DreamKernel vX",
            "MindOS Beta",
            "NoSource OS",
            "PhantomOS",
            "Illusoft"
        ])

    def display_banner(self):
        banner = """
===============================================
       Welcome to PhantasmVM - Imagination Edition
===============================================
Enter your commands if you dare! Keep your mind in the game:
'focus' to refuel your brain, 'meditate' for a power nap,
'status' to check your mental OS, 'log' for your mess of commands,
or 'exit' to face reality.
"""
        print(banner)

    def update_os(self):
        self.current_os = random.choice([
            "DreamKernel vX",
            "MindOS Beta",
            "NoSource OS",
            "PhantomOS",
            "Illusoft",
            "NeuroNet OS",
            "EtherealOS",
            "LudicrousOS"
        ])

    def simulate_distraction(self):
        distraction = random.choice([0.05, 0.1, 0.15, 0.2])
        with self.lock:
            self.concentration -= distraction
            self.log.append(f"Distraction: -{int(distraction*100)}% focus lost")
        if self.concentration < 0.3:
            print("\n*** Major distraction!!! Your brain is napping...***")
            print("PhantasmVM is rebooting because you were daydreaming...\n")
            self.restart_vm()

    def restart_vm(self):
        with self.lock:
            self.concentration = 1.0
            self.command_queue.clear()
            self.log.append("PhantasmVM was restarted after a mental breakdown.")
        self.update_os()
        print(f"Reboot complete. Your new OS is: {self.current_os}\n")

    def process_commands(self):
        while self.running:
            if self.command_queue:
                command = self.command_queue.popleft()
                self.execute_command(command)
            else:
                if random.random() < 0.15:
                    self.simulate_distraction()
                time.sleep(0.5)

    def execute_command(self, command):
        self.update_os()
        print(f"\nAttempting to run '{command}' on {self.current_os}...")
        time.sleep(random.uniform(0.2, 1.0))
        if random.random() > self.concentration:
            print("*** Oops! You lost focus mid-command! ***")
            self.log.append(f"Command '{command}' failed: loss of focus.")
            self.restart_vm()
        else:
            print(f"'{command}' executed flawlessly on {self.current_os}!")
            self.log.append(f"Command '{command}' executed successfully.")
        with self.lock:
            self.concentration = max(self.concentration - random.uniform(0.01, 0.05), 0)

    def start(self):
        self.display_banner()
        thread = threading.Thread(target=self.process_commands, daemon=True)
        thread.start()
        while self.running:
            user_input = input("Enter command: ").strip().lower()
            if user_input == "exit":
                print("\nPhantasmVM shutting down... Welcome back to reality!")
                self.running = False
            elif user_input == "focus":
                with self.lock:
                    self.concentration = min(self.concentration + 0.3, 1.0)
                    self.log.append("Focus command: brain boost activated.")
                print("Your brain is recharged! (Maybe...)\n")
            elif user_input == "meditate":
                print("Meditate mode: take a deep breath...")
                time.sleep(2)
                with self.lock:
                    self.concentration = 1.0
                    self.log.append("Meditation complete: full focus restored.")
                print("Ahhh... back to perfect focus!\n")
            elif user_input == "status":
                with self.lock:
                    print(f"Current OS: {self.current_os}")
                    print(f"Concentration: {int(self.concentration*100)}%")
                    print(f"Commands in Queue: {len(self.command_queue)}\n")
            elif user_input == "log":
                print("\nRecent Activity:")
                for entry in self.log[-10:]:
                    print(f"- {entry}")
                print("")
            elif user_input:
                with self.lock:
                    self.command_queue.append(user_input)
                    self.log.append(f"Queued command: '{user_input}'.")
                print(f"Your command '{user_input}' has been added to the queue.\n")

if __name__ == "__main__":
    vm = PhantasmVM()
    vm.start()
