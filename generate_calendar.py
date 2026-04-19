import datetime
from ics import Calendar, Event

# 1. 基础配置 (2026-04-19 状态)
# 这一天：一队早、二队休、三队中、四队夜
start_date = datetime.date(2026, 4, 19)

# 班次循环：中(0), 夜(1), 早(2), 休(3)
# 我们只取首字母，进一步节省空间
shifts = ["中", "夜", "早", "休"]

# 2026-04-19 对应的班次索引
# 一队早(2), 二队休(3), 三队中(0), 四队夜(1)
team_offsets = [2, 3, 0, 1]

# 使用半角数字，这是最省宽度的方案
team_icons = ["1", "2", "3", "4"]

c = Calendar()

# 生成未来 3 年的排班 (1095天)
for d in range(1095):
    curr = start_date + datetime.timedelta(days=d)
    
    # 计算四个队的班次文字
    s = [shifts[(d + offset) % 4] for offset in team_offsets]
    
    # 【超级瘦身版：1中2夜3早4休】
    # 全程无空格、无特殊符号，确保在极窄的月视图里不换行、不截断
    summary = f"{team_icons[0]}{s[0]}{team_icons[1]}{s[1]}{team_icons[2]}{s[2]}{team_icons[3]}{s[3]}"
    
    e = Event()
    e.name = summary
    e.begin = curr
    e.make_all_day() # 设为全天事件
    c.events.add(e)

# 导出文件
with open('shifts.ics', 'w', encoding='utf-8') as f:
    f.writelines(c.serialize_iter())

