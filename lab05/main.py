from logstats import parse_event
c_lines = 0
c_errors = 0
c_brokens = 0
path = str(input())
with open (path, 'r', encoding='utf-8') as log:
    for line in log:
        c_lines += 1
        if parse_event(line) == ValueError:
            c_brokens += 1
        else:
            if parse_event(line)['level'] == 'ERROR':
                c_errors += 1
print(c_lines)
print(c_errors)
print(c_brokens)
with open('report.txt', 'w', encoding='utf-8') as f:
    f.write(f'Ввод:           Вывод:\n')
    f.write(f'{path}      {c_lines}\n')
    f.write(f'                {c_errors}\n')
    f.write(f'                {c_brokens}\n')