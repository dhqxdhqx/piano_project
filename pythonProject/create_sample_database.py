import pickle
from datetime import date, timedelta

# username = "Test"
# username = "x"

this_week = []
a_week = 7
today = date.today()
today_day = today.weekday()

for i in range(7):
    this_week.append(today - timedelta(days=today_day))
    today_day -= 1

d = { "Test" : ["Test123", 75, [['Wed, June 15', 'Mary had a little lamb', 20],
                     [this_week[0].strftime("%a, %B %d"), 'Twinkle, Twinkle', 15],
                     [this_week[1].strftime("%a, %B %d"), 'Mary had a little lamb', 15],
                     ['Fri, June 24', 'Twinkle, Twinkle', 15]]],
      "x" : ["x", 120, [[this_week[0].strftime("%a, %B %d"), 'mud', 17],
                   [this_week[1].strftime("%a, %B %d"), 'jerry', 10],
                   [this_week[2].strftime("%a, %B %d"), 'grapevine', 20],
                   ['Fri, June 24', 'grapevine', 15]  ] ]}

print(d)

# filename = f"{username}_data"
filename = "user_data"
output_file = open(filename, 'wb')
pickle.dump(d, output_file)
output_file.close()

output_file = open(filename, 'rb')
data = pickle.load(output_file)
print(data)