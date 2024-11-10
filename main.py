from parser import Parser
from scheduler import Scheduler


p = Parser("schedule.toml")
c = p.parse()

print("[TAKEN]")
[print(str(c)) for c in c["taken_classes"]]
print("===")
print("[WANTED]")
[print(str(c)) for c in c["wanted_classes"]]
print("===")

s = Scheduler(c["taken_classes"], c["wanted_classes"])
s.generate_report()
