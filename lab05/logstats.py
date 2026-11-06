def parse_event(line):
    line = line.split(' ')
    data = line[0].split('-')
    if len(line) >= 3 and if_int(data[0]) and if_level(line[1]):
        time, level, *message = line
        message = ' '.join(message).strip()
        return {
            'time':time,
            'level':level,
            'message':message
        }
    else:
        return ValueError

def count_levels(lines):
    dictionary = {
    }
    for line in lines:
        if if_VE(line):
            good_line = parse_event(line)
            if if_KE(dictionary, good_line['level']):
                dictionary[good_line['level']] += 1
            else:
                dictionary[good_line['level']] = 1
        else:
            if if_KE(dictionary, 'BROKEN'):
                dictionary['BROKEN'] += 1
            else:
                dictionary['BROKEN'] = 1
    pairs = dictionary
    return pairs
    
def top_errors(lines, n):
    dictionary = {
    }
    sch = 0
    for line in lines:
        good_line = parse_event(line)
        if if_VE(line) and good_line['level'] == 'ERROR':
            if if_KE(dictionary, good_line['message']):
                dictionary[good_line['message']] += 1
            else:
                dictionary[good_line['message']] = 1
                sch += 1
    pairs = list(dictionary.items())
    max_pairs = []
    if sch < n:
        n = sch
    for i in range(n):
        maxi = find_max(pairs)
        pairs.remove(maxi)
        max_pairs.append(maxi)
    return max_pairs

def format_report(counts, errors):
    counts1 = list(counts.items())
    what_return = f"Отчёт по журналу\n\n"
    for i in range(len(counts1)):
        what_return += f"{counts1[i][0]}: {counts1[i][1]}\n"
    what_return += f"\nЧастые ошибки:\n"
    for j in range(len(errors)):
        what_return += f"- {errors[j][0]} — {errors[j][1]}\n"
    return what_return

def if_VE(line):
    if parse_event(line) == ValueError:
        return False
    else:
        return True

def if_level(level):
    match level:
        case "DEBUG" | "INFO" | "WARNING" | "ERROR":
            return True
        case _:
            return False
     
def if_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def if_KE(dictionary, key):
    try:
        dictionary[key]
        return True
    except KeyError:
        return False

def find_max(pairs):
    maxi = ('', 0)
    for i in range(len(pairs)):
        if maxi[1] < pairs[i][1]:
            maxi = pairs[i]
        elif maxi[1] == pairs[i]:
            if maxi[0].line.split('')[0] < pairs[i].line.split('')[0]:
                maxi = pairs[i]
    return maxi