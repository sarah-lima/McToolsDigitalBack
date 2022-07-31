import database.db as db
from request_data import get
from datetime import datetime
import download_file

def create_data():
    connection = db.connection_db()
    cursor = connection.cursor()
    data = get()
    format_data = data.get("data")
    insert_value = ''
    for i, value in enumerate(format_data):
        datas = (datetime.strptime(value.get('data'), "%d/%m/%Y"))
        insert_value+=f"('{datas.strftime('%Y-%m-%d %H:%M:%S')}', {float(value.get('valor'))})" if i+1 == len(format_data) else f"('{datas.strftime('%Y-%m-%d %H:%M:%S')}', {float(value.get('valor'))}),"  
    query = f"INSERT INTO bcb (data, valor) VALUES {insert_value}"
    print(query)
    if insert_value != '':
        cursor.execute(query)
        db.connection.commit()
    db.close_connection()
    return 'Success'
    
    
def get_data(init_data='', terminal_data='', file_type=''):
    connection = db.connection_db()
    cursor = connection.cursor()
    if init_data!=None and terminal_data!=None:
        init_data = datetime.strptime(init_data, "%d/%m/%Y")
        terminal_data = datetime.strptime(terminal_data, "%d/%m/%Y")
        interval = terminal_data-init_data
        if interval.days > 365:
            return 'Intervalo de datas deve ser de no máximo 1 ano'
        query = f"SELECT data, valor FROM bcb WHERE data between '{init_data.strftime('%Y-%m-%d %H:%M:%S')}' and '{terminal_data.strftime('%Y-%m-%d %H:%M:%S')}'"
        cursor.execute(query)
        myresult = cursor.fetchall()
        if file_type!=None:
            if file_type == 'JSON':
                download_file.create_file_json(myresult)
            if file_type == 'EXCEL':
                download_file.create_file_excel(myresult)
        
        query_sum = f"SELECT SUM(valor) FROM bcb WHERE data between '{init_data.strftime('%Y-%m-%d %H:%M:%S')}' and '{terminal_data.strftime('%Y-%m-%d %H:%M:%S')}'"
        cursor.execute(query_sum)
        sum = cursor.fetchone()
    else:
        cursor.execute("SELECT data, valor FROM bcb")
        myresult = cursor.fetchall()
        cursor.execute("SELECT SUM(valor) FROM bcb")
        sum = cursor.fetchone()
    return dict(data=myresult, sum=sum[0])    
   