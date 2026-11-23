# Exponential growth: each member adds 9 new members per day

def member_growth(days, initial=1, recruit=9):
    members = initial
    print(f"Day 0: {members} member(s)")
    for day in range(1, days + 1):
        members = members * (1 + recruit)
        print(f"Day {day}: {members:,} member(s)")
    return members

total = member_growth(days=9)
print(f"\nAfter 9 days: {total:,} members")
