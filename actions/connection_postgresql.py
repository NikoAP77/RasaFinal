import psycopg2

def DataUpdate(FirstName, LastName, Feedback):
   conn = psycopg2.connect(
      database="chat_rasabot", user='postgres', password='cuenca', host='127.0.0.1', port= '5432'
   )
   cursor = conn.cursor()
   cursor.execute("select version()")

   data = cursor.fetchone()
   print("Connection established to: ",data)

   postgresql='''INSERT INTO datos (firstname, lastname, feedback) VALUES ('{0}','{1}', '{2}');'''.format(FirstName,LastName,Feedback)
   cursor.execute(postgresql)
   conn.commit()

#if __name__ == "__main__":
#   DataUpdate('malki', 'yupanki', 'jdk')