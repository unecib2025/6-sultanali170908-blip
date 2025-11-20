#1

users = ['admin', 'operator']
new_user = "mike"
users.append(new_user)
print(users)

#2

users = ['root', 'security']
admin_name = "superuser"
users.insert(0, admin_name)
print(users)

#3

active_users = ['bob', 'alice', 'charlie']
active_users.remove("alice")
print(active_users)

#4

logs = ['Access granted', 'Login failed', 'Connection lost']
last_record = logs.pop()
print("Последняя запись:", last_record)
print("Оставшиеся логи:", logs)

#5

attempts = ['ok', 'error', 'ok', 'error', 'error']
errors_count = attempts.count("error")
print("Количество ошибок входа:", errors_count)

#6

logs = ['Access ok', 'Breach detected', 'System reboot', 'Breach detected']
idx = logs.index('Breach detected')
print("Первое обнаружение вторжения на позиции:", idx)

#7

levels = [3, 1, 2, 3, 1, 2]
levels.sort()
print(levels)

#8

reports = ['2025-10-01', '2025-10-02', '2025-10-03']
reports.reverse()
print(reports)

#9

log = ["alert", "spam", "login", "error", "spam", "alert"]
while "spam" in log:
    log.remove("spam")
log.append("END_LOG")
log.reverse()
print("Журнал после очистки:", log)
print("Количество 'alert':", log.count("alert"))

#10

whitelist = []
whitelist.append('192.168.0.1')
whitelist.append('192.168.0.2')
whitelist.append('192.168.0.3')
whitelist.append('192.168.0.4')
whitelist.append('192.168.0.5')
to_delete = "192.168.0.2"
new_ip = "192.168.0.10"
whitelist.remove(to_delete)
whitelist.insert(2, new_ip)
print("Обновлённый белый список:", whitelist)
print("Индекс нового IP:", whitelist.index(new_ip))

#11

attempts = ['ok', 'fail', 'fail', 'ok', 'fail']
fails = attempts.count('fail')
print("Количество неудачных входов:", fails)
while 'fail' in attempts:
    attempts.remove('fail')
attempts.append('audit_completed')
attempts.reverse()
idx = attempts.index('ok')
print("Итоговый список:", attempts)
print("Первый индекс 'ok':", idx)