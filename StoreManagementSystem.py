import mysql.connector
db1 = mysql.connector.connect(host="localhost",user="root",
password="1234")
c1 = db1.cursor(buffered=True)
try:
    c1.execute("use Mystore")
except:
    c1.execute("create database Mystore")
#c1.execute("drop database Mystore")
try:
    c1.execute("select * from users")
except:
    c1.execute("create table users (username varchar(30), passw varchar(30))")
    c1.execute("insert into users values('Anjali','abc123')")
    c1.execute("insert into users values('Rahul','xyz123')")
    c1.execute("insert into users values('Vinayak','pqr123')")
    db1.commit()
'''try:
c1.execute("select * from stock")
except:
c1.execute("create table stock(pName varchar(30) primary key,pid
varchar(20),Quantity int(3),brand varchar(20),Price int(4))")
try:
c1.execute("select * from bill")
except:
Lotus Valley International School Page 13 of 31
Sohum Chandra Srivastava Session 2022-23
c1.execute("create table bill(oid varchar(30) primary key, CustomerName
varchar(20),PhoneNumber char(10) unique key,pname varchar(30),Quantity
int(100),Price int(4),foreign key (pname) references stock(pname))")
db1.commit()'''
def login():
    print("-" * 50)
    print("\t MY STORE")
    print("-" * 50)
    print("\t LOGIN")
    un = input("Enter User Name : ")
    pw = str(input("Enter Password : "))
    q = "select * from users where username = %s and passw = %s"
    val = (un,pw)
    c1.execute(q,val)
    res = c1.fetchall()
    print("-" * 50)
    if len(res) == 0:
        print("Invalid User Name or Password ")
        print("-" * 50)
        q=input("New to MYSTORE?(y/n)")
        if q=="y":
            username=input("Enter name:")
            pw=input("Enter Password:")
            c1.execute("insert into users values('"+username+"','"+pw+"')")
            print("-" * 25,"SUCCESSFUL","-" * 25)
            db1.commit()
            return False
        else:
            print("Access Granted !!!")
            print("-" * 50)
            return True
def add_stock():
    print("All information prompted are mandatory to be filled")
    prod=str(input("Enter Product Name:"))
    p_id=input("product id:")
    quantity=int(input("Enter quantity:"))
    br=str(input("Enter Brand name:"))
    price=int(input("Enter the price:"))
    c1.execute("select * from Stock where pname='"+prod+"")
    row=c1.fetchone()
    if row is not None:
        c1.execute("update Stock set quantity=quantity+'"+str(quantity)+"'where pname='"+prod+"'")
        db1.commit()
        print("""++++++++++++++++++++++++SUCCESSFULLY ADDED++++++++++++++++++++++++""")
    else:
        c1.execute("insert into Stock(pname,pid,quantity,brand,price")
        values('"+prod+"','"+p_id+"','"+str(quantity)+"','"+br+"','"+str(price)+"')
        db1.commit()
        print("""++++++++++++++++++++++++SUCCESSFULLY ADDED++++++++++++++++++++++++""")
def billing():
    print("AVAILABLE ITEMS...")
    c1.execute("select * from Stock ")
    for x in c1:
        print(x)
        cusname=str(input("Enter customer name:"))
        phno=int(input("Enter phone number:"))
        prod=str(input("Enter Product Name:"))
        price=int(input("Enter the price:"))
        n=int(input("Enter quantity:"))
        c1.execute("select quantity from stock where pname='"+prod+"'")
        lk=c1.fetchone()
        if max(lk)<n:
            print(n,"Items are not available!!!!")
        else:
            c1.execute("select pname from stock where pname='"+prod+"'")
            log=c1.fetchone()
            if log is not None:
                c1.execute("insert into Bill values('"+cusname+"','"+str(phno)+"','"+prod+"','"+str(n)+"','"+str(price)+"')")
                c1.execute("update Stock set quantity=quantity-'"+str(n)+"' where pame='"+prod+"'")
                db1.commit()
                print("++++++++++++++++++++++++ITEM HAS BEEN SOLD++++++++++++++++++++++++")
            else:
                print("ITEM IS NOT AVAILABLE!!!!!!!")
def search():
    print("""1:Search by name
    2:Search by brand
    3:Search by price""")
    l=int(input("Search by?:"))
    if l==1:
        o=input("Enter product name to search:")
        q=c1.execute("select pname from stock where pname='"+o+"'")
        tree=c1.fetchone()
        if tree!=None:
            print("""++++++++++++++++++++++ITEM IS IN STOCK++++++++++++++++++++++""")
            c1.execute("select * from stock where pname='"+o+"'")
            for y in c1:
                print(y)
        else:
            print("ITEM IS NOT IN STOCK!!!!!!!")
            print("*"*40)
    elif l==2:
        b=input("Enter brand to search:")
        c1.execute("select brand from stock where brand='"+b+"'")
        poll=c1.fetchall()
        if poll is not None:
            print("""++++++++++++++++++++++ITEMIS IN STOCK++++++++++++++++++++++""")
            c1.execute("select * from stock where brand='"+b+"'")
            for y in c1:
                print(y)
        else:
            print("ITEMS OF THIS BRAND ARE NOT AVAILABLE!!!!!!!!!")
            print("*"*40)
    elif l==3:
        p=int(input("Enter price to search:"))
        c1.execute("select price from stock where price='"+p+"'")
        home=c1.fetchall()
        if home is not None:
            print("""++++++++++++++++++++++ITEM IS IN STOCK++++++++++++++++++++++""")
            c1.execute("select * from stock where price='"+p+"'")
            for z in c1:
                print(z)
        else:
            print("ITEMS OF THIS RANGE ARE NOT AVAILABLE!!!!!!!")
            print("*"*40)
    db1.commit()
def staff():
    print("1:New staff entry")
    print("2:Remove staff")
    print("3:Existing staff details")
    ch=int(input("Enter your choice:"))
    if ch==1:
        fname=str(input("Enter Fullname:"))
        gender=str(input("Gender(M/F/O):"))
        age=int(input("Age:"))
        phno=int(input("Staff phone no.:"))
        add=str(input("Address:"))
        c1.execute("insert into Users(fname,gender,age,phno,add) values('"+fname+"','"+gender+"','"+str(age)+"','"+str(phno)+"','"+add+"')")
        print("""++++++++++++++++++++++++++++++STAFF IS SUCCESSFULLY ADDED++++++++++++++++++++++++++++++""")
        db1.commit()
    elif ch==2:
        nm=str(input("Enter staff name to remove:"))
        c1.execute("select name from users where username='"+nm+"'")
        toy=c1.fetchone()
        if toy is not None:
            c1.execute("delete from users where username='"+nm+"'")
            print("""+++++++++++++++++++++++++++++++++++STAFF IS SUCCESSFULLY REMOVED+++++++++++++++++++++++++++++++++++""")
            db1.commit()
        else:
            print("STAFF DOESNOT EXIST!!!!!!")
    elif ch==3:
        c1.execute("select * from Users")
        run=c1.fetchone()
        for t in c1:
            print(t)
        if run is not None:
            print("EXISTING STAFF DETAILS...")
            for t in c1:
                print(t)
            else:
                print("NO STAFF EXISTS!!!!!!!")
        db1.commit()
def sell_r():
    print("1:Sell history details")
    print("2:Reset Sell history")
    ty=int(input("Enter your choice:"))
    if ty==1:
        c1.execute("select * from bill")
        for u in c1:
            print(u)
    elif ty==2:
        bb=input("Are you sure(Y/N):")
        if bb=="Y":
            c1.execute("delete from bill")
            db1.commit()
        elif bb=="N":
            pass
print("Connected!!!")
if login():
    while True:
        print("-" * 50)
        print("\t CHOOSE AN OPERATION ")
        print("-" * 50)
        print("Press 1 - Add a Stock")
        print("Press 2 - Add a Bill")
        print("Press 3 - Search Item")
        print("Press 4 - To Manage Staff")
        print("Press 5 - Show Sell bill")
        print("Press 6 - Show total Sales")
        print("Press 7 - To Show Total sales")
        print("Press 8 - Quit")
        ch = int(input("Enter Your Choice : "))
        if ch == 1:
            add_stock()
        elif ch == 2:
            billing()
        elif ch == 3:
            search()
        elif ch == 4:
            staff()
        elif ch==5:
            sell_r()
        elif ch==6:
            c1.execute("select * from stock order by pname")
            for v in c1:
                print(v)
        elif ch==7:
            c1.execute("select sum(price) from bill")
            for x in c1:
                print(x)
        elif ch == 8:
            print("THANKS FOR VISITING!!")
            break
        else:
            print("-"*25,"THANK YOU","-"*25)
