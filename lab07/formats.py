def csv_to_records(text):
    data = []
    head, *lines = text.split('\n')
    head = head.split(',')
    for line in lines:
        line = line.split(',')
        record = {}
        for i in range(len(line)):
            record[head[i]] = line[i]
        data.append(record)
    return data

def parse_settings(lines):
    return 0

def merge_by_key(rows, extra, key):
    return 0

def records_to_json(records):
    return 0

print(csv_to_records("id,город\n1,Азов\n2,Шахты"))