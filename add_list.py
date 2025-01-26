username = input('Введите имя пользователя: ')

title = input('Введите главный заголовок для заметки: ')
title1 = input("Введите первый заголовок: ")
title2 = input("Введите второй заголовок: ")
title3 = input("Введите третий заголовок: ")
titles = [title1, title2, title3]

content = input('Введите описание для заметки: ')

status = input('Введите актуальный статус заметки: ')

created_date = input('Введите дату создания заметки в виде ДД-ММ-ГГГГ: ')

issue_date = input('Введите дату истечения заметки (дедлайн) в виде ДД-ММ-ГГГГ: ')

print('Имя пользователя: ', username)
print('Заголовок заметки: ', title)
print("Заголовки заметки:")
for i, title in enumerate(titles):
    print(f"{i+1}. {title}")
print('Описание заметки: ', content)
print('Статус заметки: ', status)
print('Дата создания заметки: ', created_date[0:5])
print('Дата истечения заметки (дедлайн): ', issue_date[0:5])
