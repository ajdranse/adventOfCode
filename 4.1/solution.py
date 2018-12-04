import datetime
import re
import sys

class Line:
    def __init__(self, dt, text):
        if dt.hour == 23:
            dt = dt.replace(hour = 0, minute = 0)
            dt = dt + datetime.timedelta(days = 1)

        self.dt = dt
        self.text = text

    def __str__(self):
        return "{}: {}".format(self.dt, self.text)

def update_array(array, last_dt, cur_dt, awake):
    char = '#'
    if awake:
        char = '.'
    day_num = (last_dt - first_date).days
    start_index = last_dt.minute + (day_num * 60)
    end_index = (cur_dt.minute) + (day_num * 60)
    for idx in range(start_index, end_index):
        array[idx] = char
    return array

def update_guard_dict(dict, id, last_dt, cur_dt, awake):
    guard = {}
    if id in dict:
        guard = dict[id]

    # don't need to keep track of awake time
    if not awake:
        day_num = (last_dt - first_date).days
        start_min = last_dt.minute
        end_min = (cur_dt.minute)
        day = []
        if day_num in guard:
            day = guard[day_num]
        day += [x for x in range(start_min, end_min)]
        guard[day_num] = day

    dict[id] = guard
    return dict

first_date = None
last_date = None
lines = []
pattern = re.compile(r'\[(.*)\] (.*)')
with open('input') as f:
    for line in f:
        line = line.rstrip()
        m = re.match(pattern, line)
        dt = datetime.datetime.strptime(m.group(1), '%Y-%m-%d %H:%M')
        if first_date is None or dt < first_date:
            first_date = dt
        if last_date is None or dt > last_date:
            last_date = dt
        lines.append(Line(dt, m.group(2)))

lines.sort(key=lambda x: x.dt)

num_days = (last_date - first_date).days
array = ['.' for x in range(0, 59*num_days*60)]
guard_dict = {}

guard_pattern = re.compile(r'Guard #(\d+).*')
cur_id = None
last_dt = None
awake = True
for line in lines:
    m = re.match(guard_pattern, line.text)
    if m:
        if last_dt:
            array = update_array(array, last_dt, line.dt, awake)
            guard_dict = update_guard_dict(guard_dict, cur_id, last_dt, line.dt, awake)
        cur_id = m.group(1)
        last_dt = line.dt
        awake = True
    else:
        if "falls asleep" in line.text:
            array = update_array(array, last_dt, line.dt, awake)
            guard_dict = update_guard_dict(guard_dict, cur_id, last_dt, line.dt, awake)
            last_dt = line.dt
            awake = False
        elif "wakes up" in line.text:
            array = update_array(array, last_dt, line.dt, awake)
            guard_dict = update_guard_dict(guard_dict, cur_id, last_dt, line.dt, awake)
            last_dt = line.dt
            awake = True
        else:
            print("Error!")
            sys.exit(1)

most_asleep_sum = 0
most_asleep_id = None
for guard, days in guard_dict.iteritems():
    total_asleep = 0
    for day, asleep_times in days.iteritems():
        total_asleep += len(asleep_times)
    if total_asleep > most_asleep_sum:
        most_asleep_sum = total_asleep
        most_asleep_id = guard

minutes_seen = [0 for x in range(0, 59)]
for _, asleep_times in guard_dict[most_asleep_id].iteritems():
    for minute in asleep_times:
        minutes_seen[minute] += 1



#print('      000000000011111111112222222222333333333344444444445555555555')
#print('      012345678901234567890123456789012345678901234567890123456789')
#cur_date = first_date
#for y in range(0, num_days+1):
#    string = "{:02d}-{:02d} ".format(cur_date.month, cur_date.day)
#    for x in range(0, 60):
#        string += "{}".format(array[x + y*60])
#    print(string)
#    cur_date = cur_date + datetime.timedelta(days = 1)

print "Guard asleep the most: {}, max minute: {}".format(most_asleep_id, minutes_seen.index(max(minutes_seen)))
print(int(most_asleep_id) * minutes_seen.index(max(minutes_seen)))
