

def find_line(file_path, search_text):
    file1 = open(file_path, 'r')
    lines = file1.readlines()
    for line in lines:
        line = line.strip()
        line = " ".join(line.split())
        if line != '':
            if line.startswith(search_text):
                return line.split() 

def find_lines(file_path, search_text):
    file1 = open(file_path, 'r')
    lines = file1.readlines()
    results = []
    for line in lines:
        line = line.strip()
        line = " ".join(line.split())
        if line != '':
            if line.startswith(search_text):
                results.append(line.split()) 
    return results