import os

def get_entry(name):
    f = open('entries/{}.txt'.format(name), 'rt')
    title = f.readline()
    content = f.read()
    f.close()
    entry = {
        'title': title,
        'content': content,
        'name': name
    }
    return entry

def get_all_entries():
    entries = []
    for filename in os.listdir('entries'):
        f = open('entries/' + filename, 'rt')
        title = f.readline()
        f.close()
        entries.append({'title': title, 'name': filename.replace('.txt', '')})
    return entries

def save_entry(name, title, content):
    f = open('entries/{}.txt'.format(name), 'wt')
    f.write(title)
    f.write('\n')
    f.write(content)
    f.close()

def delete_file_entry(name):
    os.remove('entries/{}.txt'.format(name))