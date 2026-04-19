import datetime
from ics import Calendar, Event

# 1. 基础配置 (2026-04-19 状态)
start_date = datetime.date(2026, 4, 19)
shifts = ["中班", "夜班", "早班", "大休"]
team_offsets = [2, 3, 0, 1]
team_icons = ["❶", "❷", "❸", "❹"]

c = Calendar()

# 生成未来 3 年的排班
for d in range(1095):
    curr = start_date + datetime.timedelta(days=d)
    s = [shifts[(d + offset) % 4] for offset in team_offsets]
    
    # 最终美化版排版
    line1 = f"{team_icons[0]}队·{s[0]}  ┋  {team_icons[1]}队·{s[1]}"
    line2 = f"{team_icons[2]}队·{s[2]}  ┋  {team_icons[3]}队·{s[3]}"
    
    e = Event()
    e.name = f"{line1}\n{line2}"
    e.begin = curr
    e.make_all_day()
    c.events.add(e)

with open('shifts.ics', 'w', encoding='utf-8') as f:
    f.writelines(c.serialize_iter())
