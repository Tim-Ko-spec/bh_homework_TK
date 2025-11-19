seconds = int(input("Введите количество секунд: "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds_remaining = seconds % 60

hours_str = str(hours).zfill(2)
minutes_str = str(minutes).zfill(2)
seconds_str = str(seconds_remaining).zfill(2)

print(hours_str + ":" + minutes_str + ":" + seconds_str)

seconds = int(input("Введите количество секунд: "))


seconds = int(input("Введите количество секунд: "))


#hours = seconds // 3600
#minutes = (seconds % 3600) // 60
#seconds_remaining = seconds % 60

#time_formatted = f"{hours:02d}:{minutes:02d}:{seconds_remaining:02d}"

#print(time_formatted)