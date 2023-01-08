#Queries
import mysql.connector
def colouroptions():
  mydb=mysql.connector.connect(host="localhost",user="root",passwd="Novosibirskschalke@123",database="PROJ")
  mycs=mydb.cursor()
  mycs.execute("create table if not exists colours_available(S_no integer,Car_company varchar(30), Colours_available varchar(30), Custom_colours_available varchar(30))")
  mycs.execute("insert into colours_available values(1,'Mercedes_Benz','Silver and Black','Yes')")
  mycs.execute("insert into colours_available values(2,'BMW','blue,black and white','No')")
  mycs.execute("insert into colours_available values(3,'Lamborghini','White,red and orange','Yes')")
  mycs.execute("insert into colours_available values(4,'Aston Martin','Grey,black,white','No')")
  mycs.execute("insert into colours_available values(5,'Audi','Red,Black and White','Yes')")
  
  bname=input("Enter name of the car company: ")
  mycs.execute("select Colours_available from Colours_available where Car_company='"+bname+"' ")
  for x in mycs:
    print("Colours available are: ",x)
  mydb.commit()
  mycs.close()
  mydb.close()
colouroptions()
def totaldetails():
  mydb=mysql.connector.connect(host="localhost",user="root",passwd="India@123",database="aa_premium_automobiles")
  mycs=mydb.cursor()
  bname=input("Enter name of the car company: ")
  #mname=input("Enter name of the model: ")
  mycs.execute("select Company, Model_name,Model_year,Year_of_addition, Price from models_available where Company='"+bname+"'")#+"' and model_name='"+mname+"' ")
  print("Details for the car you chose are: ")
  print("Company\t\tModel\tYear\tDate of addition\tPrice")
  for x in mycs:
    print(x[0],end="\t")
    print(x[1],end="\t")
    print(x[2], end="\t")
    print(x[3], end="\t")
    print(x[4])
  mycs.close()
  mydb.close()
#totaldetails()
