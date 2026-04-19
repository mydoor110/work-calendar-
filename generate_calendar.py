import datetime
from ics import Calendar, Event

# 1. 配置 (2026-04-19 状态)
start_date = datetime.date(2026, 4, 19)
shifts = ["中", "夜", "早", "休"]
team_offsets = [2, 3, 0, 1]
team_icons = ["①", "②", "③", "④"]

c = Calendar()

# 生成未来 3 年
for d in range(1095):
    curr = start_date + datetime.timedelta(days=d)
    s = [shifts[(d + offset) % 4] for offset in team_offsets]
    
    # 【7字符极致压缩】
    # 去掉所有空格和分隔符，确保月视图不截断
    summary = f"{team_icons[0]}{s[0]}{team_icons[1]}{s[1]}{team_icons[2]}{s[2]}{team_icons[3]}{s[3]}"
    
    e = Event()
    e.name = summary
    e.begin = curr
    e.make_all_day()
    c.events.add(e)

with open('shifts.ics', 'w', encoding='utf-8') as f:
    f.writelines(c.serialize_iter())

