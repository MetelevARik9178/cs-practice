def count_by_extension(paths):
    expansions = {}
    for path in paths:
        cut_path = path.split('.')
        if len(cut_path) > 1 and path[0] != '.':
            expansion = cut_path[-1].lower()
            expansions[expansion] = expansions.get(expansion, 0) + 1
        else:
            expansions[''] = expansions.get('', 0) + 1
    return(expansions)

def deepest_path(paths):
    answer_path = ""
    for path in paths:
        cut_path = path.split('.')
        if len(cut_path) > 1:
            if answer_path == "" or who_bigger(answer_path, path):
                answer_path = path
    return(answer_path)

def human_size(n_bytes):
    what_bites = {1: 'Б', 2: 'КБ', 3: 'МБ', 4: 'ГБ', 5: 'ТБ'}
    i_1024_i = 1024
    that_number = 1
    flag = True
    while flag:
        if n_bytes < i_1024_i:
            flag = False
        else:
            that_number += 1
            i_1024_i *= 1024
    if that_number == 1:
        return f"{n_bytes} {what_bites[that_number]}"
    else:
        good_n_bytes = n_bytes * 1024 / i_1024_i
        return f"{good_n_bytes:.1f} {what_bites[that_number]}"

def who_bigger(path1, path2):
    cut_path1 = heavy_cut(path1)
    cut_path2 = heavy_cut(path2)
    if len(cut_path2) > len(cut_path1):
        return True
    elif len(cut_path2) < len(cut_path1):
        return False
    else:
        for i in range(min(len(cut_path1[0]), len(cut_path2[0]))):
            if cut_path1[0][i] > cut_path2[0][i]:
                return True
                break
            elif cut_path1[0][i] < cut_path2[0][i]:
                return False
                break
    return False

def heavy_cut(path):
    cut_path = path.split('.')
    if len(cut_path) > 1:
        if len(cut_path) > 2:
            our_must = ".".join(cut_path)
        else:
            our_must = cut_path[0]
        cut_our_must = our_must.split('/')
        return(cut_our_must)
    else:
        return("")