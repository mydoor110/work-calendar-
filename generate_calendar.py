import datetime
from ics import Calendar, Event

# 1. 基础配置 (2026-04-19 状态)
start_date = datetime.date(2026, 4, 19)
# 简化班次名，只留一个字，防止手机端截断
shifts = ["中", "夜", "早", "休"]
team_offsets = [2, 3, 0, 1]
team_icons = ["❶", "❷", "❸", "❹"]

c = Calendar()

# 生成未来 3 年的排班
for d in range(1095):
    curr = start_date + datetime.timedelta(days=d)
    # 获取每个队的单字状态 (如: "早")
    s = [shifts[(d + offset) % 4] for offset in team_offsets]
    
    # 【极致美化排版】
    # 使用双竖线隔离，增加间距，确保在月视图也能看全
    line1 = f"{team_icons[0]}{s[0]}  ‖  {team_icons[1]}{s[1]}"
    line2 = f"{team_icons[2]}{s[2]}  ‖  {team_icons[3]}{s[3]}"
    
    e = Event()
    e.name = f"{line1}\n{line2}"
    e.begin = curr
    e.make_all_day()
    c.events.add(e)

with open('shifts.ics', 'w', encoding='utf-8') as f:
    f.writelines(c.serialize_iter())

