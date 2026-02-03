import warnings
warnings.filterwarnings('ignore')


import mysql.connector as sqltor
import pandas as pd
s=sqltor.connect(host='localhost',user='root',passwd='987654321',database='starters')

m=sqltor.connect(host='localhost',user='root',passwd='987654321',database='main_course')

s.autocommit=True
c1=s.cursor()
    
#importing data from database mysql
            ################################################################
starters_nveg=pd.read_sql("select Rpad(Name,60,' ')as Name,Price from non_vegetarian",s)
starters_veg = pd.read_sql("select Rpad(Name,60,' ')as Name,Price from vegetarian",s)
starters_soup=pd.read_sql("select Rpad(Name,120,' ')as Name,Price from soup",s)



main_sea=pd.read_sql("select Rpad(Name,60,' ')as Name,Price from Seafood",m)
main_pol=pd.read_sql("select Rpad(Name,120,' ')as Name,Price from Poultry",m)
main_lamb=pd.read_sql("select Rpad(Name,120,' ')as Name,Price from Lamb",m)
main_veg=pd.read_sql("select Rpad(Name,120,' ')as Name,Price from Vegetarian",m)
main_rice=pd.read_sql("select Rpad(Name,120,' ')as Name,Price from Rice_and_Noodles",m)

main_desserts=pd.read_sql("select Rpad(Name,120,' ')as Name,Price from Desserts",m)


           #################################################################

def def_main():
    while True:
        print("*" * 24 + "RESTRAUNT FOOD ORDERING SYSTEM" + "*" * 18 + "\n\n") 
        print("*" * 31 + "MAIN MENU" + "*" * 32 + "\n"     
              "\t(O) ORDER\n"                              
              "\t(P) PAYMENT\n"
              "\t(E) EXIT\n" +
              "_" * 72)

        input_1 = str(input("Please Select Your Operation: ")).upper()    
        if (len(input_1) == 1):                                           
            if (input_1 == 'O'):                                          
                print("\n" * 10)                                        
                def_order_menu()                                          
                break                                                                                                          
            elif (input_1 == 'P'):                                        
                print("\n" * 10)                                         
                def_payment()                                             
                break                                                     
            elif (input_1 == 'E'):                                        
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")           
                break                                                     
            else:                                                                                 
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")     
        else:                                                                                     
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

def def_order_menu():                                                                               
    while True:                                             
        print("*" * 31 + "ORDER PAGE" + "*" * 31 + "\n"    
              "\t(S) STARTERS\n"
              "\t(C) MAIN COURSE\n"
              "\t(D) DESSERTS\n"
              "\t(M) MAIN MENU\n"
              "\t(E) EXIT\n" +
              "_" * 72)

        input_1 = str(input("Please Select Your Operation: ")).upper() 
        if len(input_1) == 1:
            if (input_1 == 'S'):  
                print("\n" * 10)
                def_starters()
                break
            elif (input_1 == 'C'):
                print("\n" * 10)
                def_main_course() 
                break
            elif (input_1 == 'D'):
                print("\n" * 10)
                def_desserts() 
                break
            elif (input_1 == 'M'):
                print("\n" * 10)
                def_main() 
                break
            elif (input_1 == 'E'):
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                break
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!") 
        else:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")


def def_starters():
    while True:                                             
        print("*" * 31 + "ORDER PAGE" + "*" * 31 + "\n"    
              "\t(V) VEGETARIAN\n"
              "\t(N) NON VEGETARIAN\n"
              "\t(S) SOUP\n"
              "\t(O) ORDER MENU\n"
              "\t(M) MAIN MENU\n" +
              "_" * 72)

        input_1 = str(input("Please Select Your Operation: ")).upper() 
        if len(input_1) == 1:
            if (input_1 == 'V'):  
                print("\n" * 10)
                s_v()                  
                break
            elif (input_1 == 'N'):
                print("\n" * 10)
                s_nveg()
                break
            elif (input_1 == 'S'):
                print("\n" * 10)
                s_soup()
                break
            elif (input_1 == 'M'):
                print("\n" * 10)
                def_main() 
                break
            elif (input_1 == 'O'):
                print("\n" * 10)
                def_order_menu()
                break
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!") 
        else:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")


def s_v():
    v=0
    while True:
        print(starters_veg)
        print()
        print()
        print(" Press The No of order item else press\n"
              "\t(O) for ORDER MENU\n"
              "\t(M) for MAIN MENU\n"
              "\t(P) for PAYMENT\n")
        print()
        input_3 = (input("Please Select Your Input : "))
        if input_3.strip().isdigit():
            input_4=int(input("How many of it you want ? : "))
            input_3=int(input_3)
            for i in starters_veg.index:
                x=int(i)
                if x == input_3:
                    item=starters_veg.iloc[input_3,0]
                    price=starters_veg.iloc[input_3,1]
                    print()
                    t_price=price*input_4
                    print()
                    print('You have ordered :',item)
                    print('you have make of total =', price,'X',input_4,'=',t_price)
                    c1.execute("insert into oder(Name,price,total_Price) values ('%s',%s,%s)"%(item,price,t_price))
                    s.commit()
                    break
            v=v+t_price
        else:
            input_3=(input_3).upper()
            if (input_3 == 'M'):
                print("\n" * 10)
                def_main() 
                break
            elif (input_3 == 'O'):
                print("\n" * 10)
                def_order_menu()
                break
            elif (input_3 == 'P'):
                print("\n" * 10)
                def_payment()
                break
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_3) + "). Try again!")
            
def s_nveg():
    nv=0
    while True:
        print(starters_nveg)
        print()
        print()
        print(" Press The No of order item else press\n"
              "\t(O) for ORDER MENU\n"
              "\t(M) for MAIN MENU\n"
              "\t(P) for PAYMENT\n")
        print()
        input_3 = (input("Please Select Your Input : "))
        if input_3.strip().isdigit():
            input_4=int(input("How many of it you want ? : "))
            input_3=int(input_3)
            for i in starters_nveg.index:
                x=int(i)
                if x == input_3:
                     item=starters_nveg.iloc[input_3,0]
                     price=starters_nveg.iloc[input_3,1]
                     print()
                     t_price=price*input_4
                     print()
                     print('You have ordered :',item)
                     print('you have make of total =', price,'X',input_4,'=',t_price)
                     c1.execute("insert into oder(Name,price,total_Price) values ('%s',%s,%s)"%(item,price,t_price))
                     s.commit()
                     break
            nv=nv+t_price
        else:
            input_3=(input_3).upper()
            if (input_3 == 'M'):
                print("\n" * 10)
                def_main() 
                break
            elif (input_3 == 'O'):
                print("\n" * 10)
                def_order_menu()
                break
            elif (input_3 == 'P'):
                print("\n" * 10)
                def_payment()
                break
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_3) + "). Try again!")
                        
def s_soup():
    soup=0
    while True:
        print(starters_soup)
        print()
        print()
        print(" Press The No of order item else press\n"
              "\t(O) for ORDER MENU\n"
              "\t(M) for MAIN MENU\n"
              "\t(P) for PAYMENT\n")
        print()
        input_3 =input("Please Select Your Input : ")
        if input_3.strip().isdigit():
            input_4=int(input("How many of it you want ? : "))
            input_3=int(input_3)
            for i in starters_soup.index:
                x=int(i)
                if x == input_3:
                    item=starters_soup.iloc[input_3,0]
                    price=starters_soup.iloc[input_3,1]
                    print()
                    t_price=0
                    t_price=price*input_4
                    print()
                    print('You have ordered :',item)
                    print('you have make of total =', price,'X',input_4,'=',t_price)
                    c1.execute("insert into oder(Name,price,total_Price) values ('%s',%s,%s)"%(item,price,t_price))
                    s.commit()
                    soup=soup+t_price
                    break
                
        else:
            input_3=(input_3).upper()
            if (input_3 == 'M'):
                print("\n" * 10)
                def_main() 
                break
            elif (input_3 == 'O'):
                print("\n" * 10)
                def_order_menu()
                break
            elif (input_3 == 'P'):
                print("\n" * 10)
                def_payment()
                break
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_3) + "). Try again!")
            

def def_main_course():
    while True:                                             
        print("*" * 31 + "ORDER PAGE" + "*" * 31 + "\n"    
              "\t(S) SEAFOOD\n"
              "\t(P) POULTRY\n"
              "\t(L) LAMB\n"
              "\t(V) VEGETARIAN\n"
              "\t(R) RICE AND NOODLES"
              "\t(O) ORDER MENU\n"
              "\t(M) MAIN MENU\n" +
              "_" * 72)

        input_1 = str(input("Please Select Your Operation: ")).upper() 
        if len(input_1) == 1:
            if (input_1 == 'S'):  
                print("\n" * 10)
                main_seafood()                  
                break
            elif (input_1 == 'P'):
                print("\n" * 10)
                main_polt()
                break
            elif (input_1 == 'L'):
                print("\n" * 10)
                def_main_lamb()
                break
            elif (input_1 == 'V'):
                print("\n" * 10)
                def_main_veg()
                break
            elif (input_1 == 'R'):
                print("\n" * 10)
                def_main_rice()
                break
            elif (input_1 == 'M'):
                print("\n" * 10)
                def_main() 
                break
            elif (input_1 == 'O'):
                print("\n" * 10)
                def_order_menu()
                break
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!") 
        else:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")
def main_seafood():
    sea=0
    while True:
        print(main_sea)
        print()
        print()
        print(" Press The No of order item else press\n"
              "\t(O) for ORDER MENU\n"
              "\t(M) for MAIN MENU\n"
              "\t(P) for PAYMENT\n")
        print()
        input_3 =input("Please Select Your Input : ")
        if input_3.strip().isdigit():
            input_4=int(input("How many of it you want ? : "))
            input_3=int(input_3)
            for i in main_sea.index:
                x=int(i)
                if x == input_3:
                    item=main_sea.iloc[input_3,0]
                    price=main_sea.iloc[input_3,1]
                    print()
                    t_price=price*input_4
                    print()
                    print('You have ordered :',item)
                    print('you have make of total =', price,'X',input_4,'=',t_price)
                    c1.execute("insert into oder(Name,price,total_Price) values ('%s',%s,%s)"%(item,price,t_price))
                    s.commit()
                    break
            sea=sea+t_price
        else:

            input_3=(input_3).upper()
            if (input_3 == 'M'):
                print("\n" * 10)
                def_main() 
                break
            elif (input_3 == 'O'):
                print("\n" * 10)
                def_order_menu()
                break
            elif (input_3 == 'P'):
                print("\n" * 10)
                def_payment()
                break
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_3) + "). Try again!")

            
def main_polt():
    pol=0
    while True:
        print(main_pol)
        print()
        print()
        print(" Press The No of order item else press\n"
              "\t(O) for ORDER MENU\n"
              "\t(M) for MAIN MENU\n"
              "\t(P) for PAYMENT\n")
        print()
        input_3 = (input("Please Select Your Input : "))
        if input_3.strip().isdigit():
            input_4=int(input("How many of it you want ? : "))
            input_3=int(input_3)
            for i in main_pol.index:
                x=int(i)
                if x == input_3:
                    item=main_pol.iloc[input_3,0]
                    price=main_pol.iloc[input_3,1]
                    print()
                    t_price=price*input_4
                    print()
                    print('You have ordered :',item)
                    print('you have make of total =', price,'X',input_4,'=',t_price)
                    c1.execute("insert into oder(Name,price,total_Price) values ('%s',%s,%s)"%(item,price,t_price))
                    s.commit()
                    break
            pol=pol+t_price
        else:
            input_3=(input_3).upper()
            if (input_3 == 'M'):
                print("\n" * 10)
                def_main() 
                break
            elif (input_3 == 'O'):
                print("\n" * 10)
                def_order_menu()
                break
            elif (input_3 == 'P'):
                print("\n" * 10)
                def_payment()
                break
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_3) + "). Try again!")
            
        
def def_main_lamb():
    lamb=0
    while True:
        print(main_lamb)
        print()
        print()
        print(" Press The No of order item else press\n"
              "\t(O) for ORDER MENU\n"
              "\t(M) for MAIN MENU\n"
              "\t(P) for PAYMENT\n")
        print()
        input_3 = (input("Please Select Your Input : "))
        if input_3.strip().isdigit():
            input_4=int(input("How many of it you want ? : "))
            input_3=int(input_3)
            for i in main_lamb.index:
                x=int(i)
                if x == input_3:
                    item=main_lamb.iloc[input_3,0]
                    price=main_lamb.iloc[input_3,1]
                    print()
                    t_price=price*input_4
                    print()
                    print('You have ordered :',item)
                    print('you have make of total =', price,'X',input_4,'=',t_price)
                    c1.execute("insert into oder(Name,price,total_Price) values ('%s',%s,%s)"%(item,price,t_price))
                    s.commit()
                    break
            lamb=lamb+t_price
        else:
            input_3=(input_3).upper()
            if (input_3 == 'M'):
                print("\n" * 10)
                def_main() 
                break
            elif (input_3 == 'O'):
                print("\n" * 10)
                def_order_menu()
                break
            elif (input_3 == 'P'):
                print("\n" * 10)
                def_payment()
                break
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_3) + "). Try again!")
            
    
def def_main_veg():
    veg=0
    while True:
        print(main_veg)
        print()
        print()
        print(" Press The No of order item else press\n"
              "\t(O) for ORDER MENU\n"
              "\t(M) for MAIN MENU\n"
              "\t(P) for PAYMENT\n")
        print()
        input_3 = (input("Please Select Your Input : "))
        if input_3.strip().isdigit():
            input_4=int(input("How many of it you want ? : "))
            input_3=int(input_3)
            for i in main_veg.index:
                x=int(i)
                if x == input_3:
                    item=main_veg.iloc[input_3,0]
                    price=main_veg.iloc[input_3,1]
                    print()
                    t_price=price*input_4
                    print()
                    print('You have ordered :',item)
                    print('you have make of total =', price,'X',input_4,'=',t_price)
                    c1.execute("insert into oder(Name,price,total_Price) values ('%s',%s,%s)"%(item,price,t_price))
                    s.commit()
                    break
            veg=veg+t_price
        else:
            input_3=(input_3).upper()
            if (input_3 == 'M'):
                print("\n" * 10)
                def_main() 
                break
            elif (input_3 == 'O'):
                print("\n" * 10)
                def_order_menu()
                break
            elif (input_3 == 'P'):
                print("\n" * 10)
                def_payment()
                break
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_3) + "). Try again!")
        
def def_main_rice():
    rice=0
    while True:
        print(main_rice)
        print()
        print()
        print(" Press The No of order item else press\n"
              "\t(O) for ORDER MENU\n"
              "\t(M) for MAIN MENU\n"
              "\t(P) for PAYMENT\n")
        print()
        input_3 = (input("Please Select Your Input : "))
        if input_3.strip().isdigit():
            input_4=int(input("How many of it you want ? : "))
            input_3=int(input_3)
            for i in main_rice.index:
                x=int(i)
                if x == input_3:
                    item=main_rice.iloc[input_3,0]
                    price=main_rice.iloc[input_3,1]
                    print()
                    t_price=price*input_4
                    print()
                    print('You have ordered :',item)
                    print('you have make of total =', price,'X',input_4,'=',t_price)
                    c1.execute("insert into oder(Name,price,total_Price) values ('%s',%s,%s)"%(item,price,t_price))
                    s.commit()
                    break
            rice=nv=rice+t_price
        else:
            input_3=(input_3).upper()
            if (input_3 == 'M'):
                print("\n" * 10)
                def_main() 
                break
            elif (input_3 == 'O'):
                print("\n" * 10)
                def_order_menu()
                break
            elif (input_3 == 'P'):
                print("\n" * 10)
                def_payment()
                break
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_3) + "). Try again!")
            


    
def def_desserts():
    while True:                                             
        print("*" * 31 + "ORDER PAGE" + "*" * 31 + "\n"    
              "\t(D) DESSERTS\n"
              "\t(O) ORDER MENU\n"
              "\t(M) MAIN MENU\n" +
              "_" * 72)

        input_1 = str(input("Please Select Your Operation: ")).upper() 
        if len(input_1) == 1:
            if (input_1 == 'D'):  
                print("\n" * 10)
                def_dessert()
                break
            elif (input_1 == 'M'):
                print("\n" * 10)
                def_main() 
                break
            elif (input_1 == 'O'):
                print("\n" * 10)
                def_order_menu()
                break
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!") 
        else:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")



def def_dessert():
    d=0
    while True:
        print(main_desserts)
        print()
        print()
        print(" Press The No of order item else press\n"
              "\t(O) for ORDER MENU\n"
              "\t(M) for MAIN MENU\n"
              "\t(P) for PAYMENT\n")
        print()
        input_3 =input("Please Select Your Input : ")
        if input_3.strip().isdigit():
            input_4=int(input("How many of it you want ? : "))
            input_3=int(input_3)
            for i in main_desserts.index:
                x=int(i)
                if x == input_3:
                    item=main_desserts.iloc[input_3,0]
                    price=main_desserts.iloc[input_3,1]
                    print()
                    t_price=0
                    t_price=price*input_4
                    print()
                    print('You have ordered :',item)
                    print('you have make of total =', price,'X',input_4,'=',t_price)
                    c1.execute("insert into oder(Name,price,total_Price) values ('%s',%s,%s)"%(item,price,t_price))
                    s.commit()
                    d=d+t_price
                    break
                
        else:
            input_3=(input_3).upper()
            if (input_3 == 'M'):
                print("\n" * 10)
                def_main() 
                break
            elif (input_3 == 'O'):
                print("\n" * 10)
                def_order_menu()
                break
            elif (input_3 == 'P'):
                print("\n" * 10)
                def_payment()
                break
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_3) + "). Try again!")
            
    

def def_payment():
    while True:
        order=pd.read_sql("select Rpad(Name,120,' ')as Name,Price,Total_price from oder",s)
        print("*" * 31 + "ORDERED ITEMS" + "*" * 31 + "\n")
        print(order)
        print("*" * 76 + "\n")
        x=pd.read_sql("select sum(total_price) as NET_PRICE from oder",s)
        print(x)
        print('************************************************'+ "\n")
        b=pd.read_sql("select sum(total_price)*0.05 as GST_APPLIED from oder",s)
        print(b)
        print('************************************************'+ "\n")
        f=pd.read_sql("select sum(total_price)*1.05 as TOTAL_AMOUNT_TO_BE_PAID from oder",s)
        print(f)
        print('************************************************'+ "\n")
        print(" Press\n"
              "\t(O) for going ORDER MENU\n"
              "\t(M) for going MAIN MENU\n"
              "\t(P) for  Final PAYMENT\n")
        input_5=input("Please Select Your Input : ").upper()
        if (input_5 == 'M'):
                print("\n" * 10)
                def_main() 
                break
        elif (input_5 == 'O'):
                print("\n" * 10)
                def_order_menu()
                break
        elif (input_5 == 'P'):
                print()
                print("YOUR ORDER WILL BE ARRIVING SOON")
                print("\n" * 10)
                print("*" * 28 +"YOU HAVE PAID THE BILL" + "*" * 28 + "\n")
                print("*" * 32 + "THANK YOU" + "*" * 37 + "\n")
                c1.execute("delete from oder")
                s.commit()
                break
        else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_5) + "). Try again!")


##############FINAL EXECUTION #################################
def_main()

