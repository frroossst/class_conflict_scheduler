from parser import Parser
from scheduler import Schedule


p = Parser("schedule.toml")
c = p.parse()
[print(cls, end="\n===\n") for cls in c]

s = Schedule(c)
print(s.check_conflicts())
