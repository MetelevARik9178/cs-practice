def count_by_extension(paths):
    expansions = {}
    for path in paths:
        cut_path = path.split('.')
        if len(cut_path) > 1:
            expansion = cut_path[-1].lower()
            expansions[expansion] = expansions.get(expansion, 0) + 1
        else:
            expansions[''] = expansions.get('', 0) + 1
    return(expansions)

def deepest_path(paths):
    return 0

def human_size(n_bytes):
    return 0

paths = ["docs/report.PDF", "notes.txt", "docs/img/logo.png", "Makefile"]

print(count_by_extension(paths))   # {"pdf": 1, "txt": 1, "png": 1, "": 1}
print(deepest_path(paths))         # "docs/img/logo.png"

print(human_size(900))           # "900 Б"
print(human_size(1536))            # "1.5 КБ"
print(human_size(5 * 1024 * 1024)) # "5.0 МБ"
        