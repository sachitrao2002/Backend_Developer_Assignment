from django.http import JsonResponse
from .models import user_data
from .serializers import user_dataSerilizater
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,viewsets
import psycopg2 
import json
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import user_dataSerilizater
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
import re

class userviewset(viewsets.ModelViewSet):
    permission_classes=(IsAuthenticated,)
    serializer_class=user_dataSerilizater
    queryset=get_user_model().objects.all()

#connection to postgreSQL database
hostname='localhost'
database='data'
username='postgres'
pwd='Sensational@5'
port_id=5432
conn=None
cur=None


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

#error thrown if database fails to connect               
except Exception as error:
    print(error)    


    
#the post reques takes multiple paragraphs as input from the user and is saved in the database
@api_view(['POST',])
@permission_classes([IsAuthenticated])
def user_data_list(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        input=data['paragraph']
        input=input.lower()
        create_script='''CREATE TABLE IF NOT EXISTS user_data (paragraph varchar(40))'''
        cur.execute(create_script)
        conn.commit()
        paragraphs = re.split(r'  ', input)
        for paragraph in paragraphs:
            insert_script='INSERT INTO user_data (paragraph) VALUES (%s)'
            insert_value=(paragraph,)
            cur.execute(insert_script,insert_value)
            conn.commit()
        return Response(status=status.HTTP_201_CREATED)

#the GET request takes in the text that needs to be searched and outputs a list of paragraphs where the text was found
@api_view(['GET',])
@permission_classes([IsAuthenticated])
def user_data_search(request):
    if request.method == 'GET':
        data=json.loads(request.body)
        value=data.get('text')
        if value==None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        input=data['text']
        input=input.lower()
        cur.execute('SELECT * FROM user_data')
        user_list=list(cur.fetchall())
        result=[]
        output=[]
        for i in user_list:
            string = ''.join(i)
            result.append(string)

        #return Response(result[0],status=status.HTTP_201_CREATED)
        for i in range(0,len(result)):
            if input in str(result[i]) and len(str(result[i]))==len(input):
                output.append("paragraph"+ " "+str(i+1))
            else:
                var=result[i].split()
                for word in var:
                    if word==input:
                        output.append("paragraph"+ " " +str(i+1))
        output= sorted(output, key=lambda x: int(x.split()[-1]))  
        for i in output:
            if output.count(i)>1:
                output.remove(i)              
        if len(output)>10:
            return Response(output[0:10],status=status.HTTP_201_CREATED) 
        else:       
            return Response(output,status=status.HTTP_201_CREATED)    
        

        
    

