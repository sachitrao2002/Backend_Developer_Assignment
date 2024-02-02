
import psycopg2 
from flask import Flask,request,jsonify
app=Flask(__name__)

hostname='localhost'
database='data'
username='postgres'
pwd='Sensational@5'
port_id=5432
conn=None
cur=None
input='he'

def close():
    if cur is not None:
        cur.close()
    if conn is not None:    
        conn.close() 
    return "data base connection closed succesfully"



try:
    conn=psycopg2.connect(host=hostname,
    dbname=database,
    user=username,
    password=pwd,
    port=port_id)

    cur=conn.cursor() 
                

except Exception as error:
    print(error)    


@app.route('/insert',methods=["POST"])  
def insert():
    input=request.json['paragraph']
    create_script='''CREATE TABLE IF NOT EXISTS user_data (paragraph varchar(40))'''
    cur.execute(create_script)
    conn.commit()

    insert_script='INSERT INTO user_data (paragraph) VALUES (%s)'
    insert_value=(input,)
    cur.execute(insert_script,insert_value)
    conn.commit()
    return "insertion succesfull"

@app.route('/search',methods=["GET"])
def search():
    cur.execute('SELECT * FROM user_data')
    l1=list(cur.fetchall())
    l2=res=[]
    for i in l1:
        res.append(list(i))
    print(res)
    for i in range(0,len(res)):
        if input in str(res[i]):
            l2.append("para"+str(i))
    return l2      
        

if __name__=="__main__":
    app.run(debug=True)            