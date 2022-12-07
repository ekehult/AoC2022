with open('input.txt') as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]
    
    all_sizes = {}
    open_directories = []

    for line in lines:
        row = line.split(' ')
        dir_name = row[-1]
        file_size = row[0]

        if ('cd' in row):
            if ('..' in row):
                open_directories.pop(-1)
            else:
                name = ''.join(open_directories) + dir_name
                open_directories.append(name)
                all_sizes[name] = 0

        elif file_size.isdigit():
            size_dir = int(file_size)
            for directory in open_directories:
                all_sizes[directory] = all_sizes[directory] + size_dir  

  
    left = 70000000-all_sizes['/']
    need = 30000000 - left

    candidate = 70000000
    for directory in all_sizes:
        if all_sizes[directory] >= need and all_sizes[directory] < candidate:
            print(all_sizes[directory])
