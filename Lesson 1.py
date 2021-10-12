time = int(input("duration = "))
day = (time // 86400)
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)

if time >= 0 :
  print(seconds, "сек")
if time >= 60:
  print(minutes, "мин")
if time >= 3600:
  print(hours, "час")
if time >= 86400:
  print(day, "день")
