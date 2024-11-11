from scheduler import Scheduler
from parser import Parser

import argparse
import os


YELLOW = "\033[33m"
CYAN = "\033[36m"
BOLD = "\033[1m\033[37m"
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

desc = "select the best class according to your schedule"
clap = argparse.ArgumentParser(description=desc)
clap.add_argument("file", type=str, help="path to the schedule TOML file")
args = clap.parse_args()

path = args.file
if not os.path.exists(path):
    raise RuntimeError(f"{BOLD}{RED}[ERROR]{RESET} {path}: no such file exists")
elif not path.endswith(".toml"):
    raise RuntimeError(f"{BOLD}{RED}[ERROR]{RESET} {path}: must be a TOML file")

p = Parser(path)
c = p.parse()

print(f"{BOLD}============== [SCHEDULER] =============={RESET}")
print(f"{BOLD}{GREEN}[TAKEN]{RESET}")
[print(str(c.pretty())) for c in c["taken_classes"]]
print()
print("=========================================")
print(f"{BOLD}{YELLOW}[WANTED]{RESET}")
[print(str(c.pretty())) for c in c["wanted_classes"]]
print()
print(f"{BOLD}========================================={RESET}")

s = Scheduler(c["taken_classes"], c["wanted_classes"])
s.report()

