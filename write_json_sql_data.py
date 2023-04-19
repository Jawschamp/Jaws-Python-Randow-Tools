import json

def generate_sql_from_json(json_file_path, table_name):
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    
    if isinstance(data, dict):
        data = [data]
    
    columns = tuple(data[0].keys())
    values_template = ', '.join(['%s'] * len(columns))
    sql_insert_template = f"INSERT INTO {table_name} {columns} VALUES ({values_template});"
    
    sql_queries = []
    for item in data:
        values = tuple(item.values())
        sql_queries.append(sql_insert_template % values)
        
    return '\n'.join(sql_queries)