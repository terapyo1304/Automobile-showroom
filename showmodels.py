#Project (Show car linup)
import mysql.connector
def showmodels():
  mydb=mysql.connector.connect(host="localhost",user="root",passwd="Novosibirskschalke@123",database="PROJ")
  mycs=mydb.cursor()
  mycs.execute("select company,Model_name from models_available order by company")
  print("These are the luxury cars in our collection: ")
  print("Company\t\tModel")
  for x in mycs:
    print(x[0],end="\t")
    print(x[1],end="\t\n")
  mycs.close
  mydb.close()
#showmodels()
