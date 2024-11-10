from parser import Parser
from scheduler import Schedule


p = Parser("schedule.toml")
c = p.parse()

print("[TAKEN]")
[print(str(c)) for c in c["taken_classes"]]
print("===")
print("[WANTED]")
[print(str(c)) for c in c["wanted_classes"]]
print("===")
