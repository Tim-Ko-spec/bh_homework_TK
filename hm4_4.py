
s = "имя: Андрей, фамилия: Зубов, возраст: 29"

parts = s.split(',')

name = parts[0].split(':')[1].strip()
surname = parts[1].split(':')[1].strip()
age = parts[2].split(':')[1].strip()

print(f"- {name}\n- {surname}\n- {age}")