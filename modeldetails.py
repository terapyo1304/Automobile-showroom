# PROJECT (Models Choice menu)
print("MODELS AND DISTINCT COMPANIES WE'VE PARTNERED WITH")
import mysql.connector
def totaldetails():
  bname=input("enter the brand")
  mydb=mysql.connector.connect(host="localhost",user="root",passwd="Novosibirskschalke@123")
  mycs=mydb.cursor()
  mycs.execute("create database if not exists PROJ;")
  mycs.execute("USE PROJ;")
  #print ("Connection to our server is ",mydb.is_connected)
  mycs.execute("create table if not exists models_available(S_no integer,company varchar(30), Model_name varchar(30), Distance_travelled varchar(30),Model_year integer, Year_of_addition datetime,Price integer)")
  mycs.execute("insert into models_available values(1,'Mercedes_Benz','S450','10000km',2018,'2019-04-19 00:00:00',10000000)")
  mycs.execute("insert into models_available values(2,'Mercedes_Benz','AMG GT','2500km',2019,'2020-04-28 00:00:00',25000000)")
  mycs.execute("insert into models_available values(3,'Mercedes_Benz','G63 AMG','15000km',2019,'2020-06-21 00:00:00',15000000)")
  mycs.execute("insert into models_available values(4,'BMW','7series','20000km',2019,'2018-08-21 00:00:00',9000000)")
  mycs.execute("insert into models_available values(5,'BMW','M5','2800km',2019,'2019-12-30 00:00:00',9500000)")
  mycs.execute("insert into models_available values(6,'BMW','320d','30000km',2014,'2016-04-30 00:00:00',9500000)")
  mycs.execute("insert into models_available values(7,'Jaguar','XJ','25000km',2018,'2020-02-21 00:00:00',8500000)")
  mycs.execute("insert into models_available values(8,'Jaguar','XF','35000km',2018,'2019-03-31 00:00:00',8500000)")
  mycs.execute("insert into models_available values(9,'Jaguar','XE','35000km',2018,'2020-02-21 00:00:00',8500000)")
  mycs.execute("insert into models_available values(10,'Audi','R8','10000km',2016,'2018-04-21 00:00:00',9700000)")
  mycs.execute("insert into models_available values(11,'Audi','A4','10000km',2012,'2018-04-21 00:00:00',5000000)")
  mycs.execute("insert into models_available values(12,'Audi','A6','10000km',2018,'2020-04-21 00:00:00',6700000)")
  mycs.execute("insert into models_available values(13,'Aston Martin','DB9','20000km',2016,'2018-09-27 00:00:00',9200000)")
  mycs.execute("insert into models_available values(14,'Rolls Royce','Ghost VI','20000km',2012,'2016-04-21 00:00:00',45000000)")
  mycs.execute("insert into models_available values(15,'Rolls Royce','Cullinun','200000km',2019,'2020-03-24 00:00:00',55000000)")
  mycs.execute("insert into models_available values(16,'Lamborghini','Avantador','20000km',2014,'2017-08-17 00:00:00',15000000)")
  mycs.execute("insert into models_available values(17,'Bugatti','Veyron','1000km',2012,'2016-04-21 00:00:00',90000000)")
  mycs.execute("insert into models_available values(18,'Lamborghini','Huracan_Evo','50000km',2020,'2020-04-21 00:00:00',35000000)")
  mycs.execute("insert into models_available values(19,'Lamborghini','URUS','45000km',2019,'2019-08-11 00:00:00',4000000)")
  mycs.execute("insert into models_available values(20,'Hyundai','SantaFe','340000km',2018,'2020-04-21 00:00:00',1500000)")
  
  
  
  
  
  
  
  mycs.execute("select Company, Model_name,Model_year,Year_of_addition, Price from models_available where Company='"+bname+"'")#+"' and model_name='"+mname+"' ")
  print("Details for the car you chose are: ")
  print("Company\tModel\tYear\tDate of addition\t\tPrice")
  for x in mycs:
    print(x[0],end="\t")
    print(x[1],end="\t")
    print(x[2], end="\t")
    print(x[3], end="\t")
    print(x[4])
  mydb.commit()
  mycs.close()
  mydb.close()


def get_company_names():
  mydb=mysql.connector.connect(host="localhost",user="root",passwd="Novosibirskschalke@123")
  
  mycs=mydb.cursor()
  mycs.execute("use PROJ;")
  mycs.execute("select distinct(company),Model_name from models_available order by company")
  
  for i in mycs:
    print(i)
  mydb.commit()
  mycs.close()
  mydb.close()
  




def history():
  file = open("history.txt","r")
  print(file.read())
  file.close()

'''history()
c='y'
while c=='y' or c=='Y':
  print("Choose from our range of luxury car brands to see the models available in them: ")
  c_list=get_company_names()
  i=1
  print("0 . History")
  for comp in c_list:
    print(i,". ",comp)
    i+=1
  ch=int(input("Enter your choice: "))
  if ch>=i or ch<0:
    print("Invalid choice!!")
  elif ch==0:
    history()
  else:
    totaldetails(c_list[ch-1])
  c=input("Do you want to continue? (y/n) ")'''











    
