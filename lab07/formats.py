def csv_to_records(text):
    data = []
    head, *lines = text.split('\n')
    head = head.split(',')
    for q in range(len(lines) - 1):
        line = lines[q]
        line = line.split(',')
        record = {}
        for i in range(len(line)):
            record[head[i].strip()] = line[i].strip()
        data.append(record)
    return data

def parse_settings(lines):
    records = {}
    flag = True
    data = []
    for line in lines:
        if flag:
            if line[0] == '#':
                continue
            key, value = line.split(':')
            value = value.strip()
            if value == "":
                flag = False
                break
            if if_int(value):
                value = int(value)
            else:
                if if_bool(value):
                    value = bool(value)
            records[key] = value
        else:
            data.append(line[4:])
    if data != []:
        records[key] = data
    return records

def if_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def if_bool(string):
    if string == "true" or string == "false":
        return True
    else:
        False

def merge_by_key(rows, extra, key):
    return 0

def records_to_json(records):
    return 0

print(csv_to_records("id, город \n1, Азов \n2,Шахты\n"))
print(parse_settings(["# отчёт", "title: Отчёт за март", "decimals: 1", "active: true", "columns:"]))
#, "  - город", "  - цена"