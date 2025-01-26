note = []

# получаем данные от пользователя
username = input('Введите имя пользователя: ')
title = input('Введите главный заголовок для заметки: ')
content = input('Введите описание для заметки: ')
status = input('Введите актуальный статус заметки: ')
created_date = input('Введите дату создания заметки в виде ДД-ММ-ГГГГ: ')
issue_date = input('Введите дату истечения заметки (дедлайн) в виде ДД-ММ-ГГГГ: ')

# получаем заголовки и добавляем их во вложенный список
titles = []
while True:
    title = input("Введите заголовок (или 'стоп' для завершения): ")
    if title.lower() == "стоп":
        break
    titles.append(title)

# добавляем данные в список заметки
note.append(username)
note.append(content)
note.append(status)
note.append(created_date)
note.append(issue_date)
note.append(titles) # добавляем список заголовков


# выводим информацию о заметке
print("Имя пользователя:", note[0])
print("Содержание заметки:", note[1])
print("Статус:", note[2])
print("Дата создания:", note[3])
print("Дата изменения:", note[4])
print("Заголовки:", note[5])

