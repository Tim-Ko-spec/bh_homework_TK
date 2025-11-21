
s = "Это тестовая <start>строка для изучения<end> строковых операций"

start_tag = "<start>"
end_tag = "<end>"

text_between = s.split(start_tag)[1].split(end_tag)[0]

print(text_between)