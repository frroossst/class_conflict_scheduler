from parser import Parser
from scheduler import Scheduler


p = Parser("schedule.toml")
c = p.parse()

YELLOW = "\033[33m"
CYAN = "\033[36m"
BOLD = "\033[1m\033[37m"
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

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
