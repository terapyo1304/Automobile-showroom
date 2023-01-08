# Computer Science Project
# Functions
import mysql.connector
l=("Huracan_Evo", "Aventador_S", "Urus", "Centenario", "Huracan_Evo_Spyder", "Aventador_SVJ", "Sian_FK7_Roadster")
name=input("Enter your name: ")
print("Welcome to Lamborghini Mr./Ms.",name," !")
def showlineup(l):
  cnt=0
  for i in l:
    print (i)
    cnt+=1
  print ("These is our lineup of ",cnt," best super and hyper cars in the world!")
showlineup(l)

def details():
  mydb=mysql.connector.connect(host='localhost',user='abhishek',passwd='India@123')
  print(' You are now connected to our database')
  mycsr=mydb.cursor()
  mydb.close()

def showcolours(l):
  cc=input("Enter the car's name to view its colour options: ")
  for cc in l:
     if cc=="Huracan_Evo" or cc=="Huracan_Evo_Spyder":
      print ("Colour options are: Green, Orange, Formula Red, Opulant Purple, Race Yellow and Pearl White")
     elif cc=="Avantador_S" or cc=="Avantador_SVJ":
      print ("Colour options are: Formula Red, Orange, Orange Speciale Italia finish, Pearl White, White Speciale Italia Finish, Race Yellow")
     elif cc=="Centenario" or cc=="Sian_FK7_Roadster":
      print("Colour options are: Black-Yellow, Black-Orange, Grey-Yellow, Grey-Orange, Pure Black")
     elif cc=="Urus":
      print("Colour options are: Formula Red, Orange, Orange Speciale Italia finish, Pearl White, White Speciale Italia Finish, Race Yellow")
     else:
      print("That car doesn't belongs to our lineup. Please enter a valid car name...")

showcolours(l)      
  
      
    

















    
