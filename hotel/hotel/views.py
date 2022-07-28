from django.http import HttpResponse
from django.shortcuts import render
from sqlalchemy import create_engine

def list(request):
     categoryno=""
     if request.GET:
        categoryno = request.GET["categoryno"]
     sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/hotelbook')
     result=sqlEngine.execute("SELECT * FROM `rooms` WHERE room_category='{0}'".format(categoryno))
     
     names = result.keys()
     return render(request, "listbook.html",
                  {'result': result,'names':names})

def roombook(request):
     
     sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/hotelbook')
     result=sqlEngine.execute("SELECT category_no,category_name,description,charge  FROM `room_category`")
     #result=list(result)
     names = result.keys()
     return render(request, "Room_booking.html",
                  {'result': result,'names':names})
      
def page(request):
    return render(request, "Page.html")

def loginpage (request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(user)
            return render(request, 'rough.html', {})
        else:
            return render(request, 'rough.html', {'message':'the acount is not active'})
    else:
        return render(request, 'rough.html', {'message':'username and password is incorrect'})


def all_checkout(request):
     id = ""
     name = ""
     email = ""
     phone = ""
     city = ""
     postcode = ""
     country = ""
     people = ""
     room = ""
     bedding = ""
     arrive = ""
     depart = ""
     comment = ""
    
     if request.GET:
        id = request.GET["id"]
     sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/hotelbook')
     result=sqlEngine.execute("SELECT * FROM `checkout`")
     #result=list(result)
     names = result.keys()
     return render(request, "AllCheckoutRoom.html",
                  {"result":result,"id":id,"name": name, "email": email, "phone":phone, "city": city,"postcode":postcode ,"country":country, "people":people, "room":room, "bedding":bedding, "arrive":arrive, "depart":depart, "comment":comment})



def docheckout(request):
    id=[]
    result=[]
    
    if request.POST:
        id = request.POST["id"]
        print("Id",id)
    sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/hotelbook')
    # print("SELECT * FROM `hotelbook` WHERE id = '{0}'".format(id))
    
    result=sqlEngine.execute("SELECT * FROM `hotelbook` WHERE id = '{0}'".format(id))
    row =result.fetchone()
    if row==None:
        return HttpResponse("Not Found")
    name=row[1]
    email=row[2]
    phone=row[3]
    city=row[4]
    postcode=row[5]
    country=row[6]
    people=row[7]
    room=row[8]
    bedding=row[9]
    arrive=row[10]
    depart=row[11]
    comment=row[12]
    sqlEngine.execute(
                 "INSERT INTO `checkout`  VALUES ('{0}', '{1}','{2}', '{3}','{4}', '{5}','{6}', '{7}','{8}', '{9}','{10}','{11}','{12}');".format(id,name, email,phone,city,postcode,country,people,room,bedding,arrive,depart,
                                                                              comment))
        
    sqlEngine.execute("DELETE FROM `hotelbook` WHERE id='{0}'".format(id))

   

    return render(request, "docheckout.html",
                  {"result":result,"id":id,"name": name, "email": email, "phone":phone, "city": city,"postcode":postcode ,"country":country, "people":people, "room":room, "bedding":bedding, "arrive":arrive, "depart":depart, "comment":comment})






def check(request):
    result = ""
    id= ""
    if request.GET:
     id=request.GET["id"]
        
     sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/hotelbook')
     result=sqlEngine.execute("SELECT * FROM `hotelbook` WHERE id = '{0}'".format(id))
    return render(request, "Check.html",
                   { "result":result,"id":id })




def all_Check(request):
    id=[]
    result=[]
    name=[]
    email=[]
    phone=[]
    city=[]
    postcode=[]
    country=[]
    people=[]
    room=[]
    bedding=[]
    arrive=[]
    depart=[]
    comment=[]

    
    if request.POST:
        id = request.POST["id"]
        print("Id",id)
    sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/hotelbook')
    print("SELECT * FROM `hotelbook` WHERE id = '{0}'".format(id))
    result=sqlEngine.execute("SELECT * FROM `hotelbook` WHERE id = '{0}'".format(id))
    #result=list(result)
    # names = result.keys()
    
    row =result.fetchone()
    if row==None:
        return HttpResponse("Not Found")
    name=row[1]
    email=row[2]
    phone=row[3]
    city=row[4]
    postcode=row[5]
    country=row[6]
    people=row[7]
    room=row[8]
    bedding=row[9]
    arrive=row[10]
    depart=row[11]
    comment=row[12]
    print("name ",name)

    return render(request, "Check_All.html",
                  {"result":result,"id":id,"name": name, "email": email, "phone":phone, "city": city,"postcode":postcode ,"country":country, "people":people, "room":room, "bedding":bedding, "arrive":arrive, "depart":depart, "comment":comment})


# def check(request):
#     return render(request, "Check.html")



def all_guest(request):
    guest_id=""
    result="" 
    name = ""
    age = ""
    address = ""
    aadhaar = ""
    pan = ""
    comment = ""
    
    if request.GET:
        guest_id = request.GET["guest_id"]
    sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/hotelbook')
    result=sqlEngine.execute("SELECT * FROM `guest`")
     #result=list(result)
    names = result.keys()
    return render(request, "all_guest_Entry.html",
                  {"result":result,"name": name, "age": age, "address":address, "aadhaar": aadhaar,"pan":pan ,"comment":comment, "guest_id":guest_id})



def editguest(request):
    guest_id=[]
    result= []
    name = []
    age = []
    address = []
    aadhaar = []
    pan = []
    comment = []
        
    
    if request.GET:
      guest_id = request.GET["guest_id"] 
    
    
    sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/hotelbook')
    result = sqlEngine.execute("SELECT * FROM `guest` WHERE guest_id = '{0}'".format(guest_id))
    row = result.fetchone()
    name = row[0]
    age = row[1]
    address = row[2]
    aadhaar = row[3]
    pan = row[4]
    comment = row[5]
    print("Age ",age)
   
    return render(request, "editguest.html",
                  {"result": result, "name": name, "age": age, "address": address, "aadhaar": aadhaar, "pan":pan,
                   "comment": comment, "guest_id":guest_id})

def guestupdate(request):
    name = ""
    age = ""
    address = ""
    aadhaar = ""
    pan = ""
    comment = ""
    guest_id = ""
    cmd="Solve"
    
    if request.POST:
        cmd=request.POST["cmd"]
        if cmd=="update":
            print("updating")
            guest_id=request.POST["guest_id"]
            name = request.POST["name"]
            age = request.POST["age"]
            address = request.POST["address"]
            aadhaar = request.POST["aadhaar"]
            pan = request.POST["pan"]
            comment=request.POST["comment"]
            
           # print("UPDATE `rooms` SET `guest`='{0}',`floar_no`='{1}',`no_bads`='{2}',`comment`='{3}' WHERE room_id='{4}'".format(room_no, floar_no, no_bads, comment, room_id)) 
    
            sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/hotelbook')
            sqlEngine.execute("UPDATE `guest` SET `name`='{0}',`age`='{1}',`address`='{2}',`aadhaar`='{3}',`pan`='{4}',`comment`='{5}' WHERE guest_id='{6}'".format(name,age,address,aadhaar,pan,comment,guest_id)) 
                
                
                
              
            
            
        if cmd=="delete":
            if cmd=="delete":
             print("delete")
             
            guest_id=request.POST["guest_id"]
            name = request.POST["name"]
            age = request.POST["age"]
            address = request.POST["address"]
            aadhaar = request.POST["aadhaar"]
            pan = request.POST["pan"]
            comment=request.POST["comment"]

            
            sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/hotelbook')
            sqlEngine.execute("DELETE FROM `guest` WHERE guest_id='{0}'".format(guest_id))
                
            
   
            
    return render(request, "editguest.html",{"name": name, "age": age, "address":address, "aadhaar": aadhaar,"pan": pan, "comment":comment ,"guest_id": guest_id })
    
  
def guestinsert(request):
    
    # if request.GET:
    #     categoryno=request.GET["categoryno"]
        
    name = ""
    age = ""
    address = ""
    aadhaar = ""
    pan = ""
    comment = ""
    guest_id = ""
    
    if request.POST:
        name = request.POST["name"]
        age = request.POST["age"]
        address = request.POST["address"]
        aadhaar = request.POST["aadhaar"]
        pan = request.POST["pan"]
        comment = request.POST["comment"]
        


        
        sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/hotelbook')
        sqlEngine.execute(
                "INSERT INTO `guest`  VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}',null);".format( name, age, address, aadhaar, pan, comment))

        
        
    return render(request, "guestEntry.html",{"name": name, "age": age, "address":address, "aadhaar": aadhaar,"pan":pan ,"comment":comment, "guest_id":guest_id})

    






def all_tableroom(request):
     categoryno=""
     if request.GET:
        categoryno = request.GET["categoryno"]
     sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/hotelbook')
     result=sqlEngine.execute("SELECT * FROM `rooms` WHERE room_category='{0}'".format(categoryno))
     
     names = result.keys()
     return render(request, "allroom.html",
                  {'result': result,'names':names})


def editroom(request):
    result = ""
    room_id = ""
    room_no = ""
    floar_no = ""
    no_bads = ""
    comment = ""
    if request.GET:
     room_id=request.GET["room_no"]
        
     sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/hotelbook')
     result=sqlEngine.execute("SELECT * FROM `rooms` WHERE room_id = '{0}'".format(room_id))
     row =result.fetchone()
     room_no=row[1]
     floar_no=row[3]
     no_bads=row[4]
     comment=row[5]
     
    return render(request, "Editroom.html",
                   { "result":result,"room_id":room_id, "room_no": room_no, "floar_no":floar_no, "no_bads": no_bads, "comment":comment })





def roomupdate(request):
    room_id=""
    room_no = ""
    floar_no = ""
    no_bads = ""
    comment = ""
    
    cmd="Solve"
    
    if request.GET:
        categoryno=request.GET["room_id"]
        
    if request.POST:
        cmd=request.POST["cmd"]
        if cmd=="update":
            print("updating")
            room_id=request.POST["room_id"]
            room_no = request.POST["room_no"]
            floar_no = request.POST["floar_no"]
            no_bads = request.POST["no_bads"]
            comment=request.POST["comment"]
            print("UPDATE `rooms` SET `room_no`='{0}',`floar_no`='{1}',`no_bads`='{2}',`comment`='{3}' WHERE room_id='{4}'".format(room_no, floar_no, no_bads, comment, room_id)) 
    
            sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/hotelbook')
            sqlEngine.execute("UPDATE `rooms` SET `room_no`='{0}',`floar_no`='{1}',`no_bads`='{2}',`comment`='{3}' WHERE room_id='{4}'".format(room_no, floar_no, no_bads, comment, room_id)) 
                
                
                
              
            
            
        if cmd=="delete":
            room_id=request.POST["room_id"]
            room_no = request.POST["room_no"]
            floar_no = request.POST["floar_no"]
            no_bads = request.POST["no_bads"]
            comment=request.POST["comment"]
                
            sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/hotelbook')
            sqlEngine.execute("DELETE FROM `rooms` WHERE room_id='{0}'".format(room_id))
                
            
   
            
    return render(request, "Editroom.html",{"room_id": room_id, "room_no": room_no, "floar_no":floar_no, "no_bads": no_bads, "comment":comment })
    
  
def rooms(request):
    categoryno = ""
    
    if request.GET:
        categoryno=request.GET["categoryno"]
        
    room_no = ""
    floar_no = ""
    no_bads = ""
    comment = ""
    
    if request.POST:
        categoryno=request.POST["categoryno"]
        room_no = request.POST["room_no"]
        floar_no = request.POST["floar_no"]
        no_bads = request.POST["no_bads"]
        comment=request.POST["comment"]
        
        sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/hotelbook')
        sqlEngine.execute(
                "INSERT INTO `rooms`  VALUES (null,'{0}', '{1}', '{2}', '{3}', '{4}');".format( room_no, categoryno, floar_no, no_bads, comment))
        result = "Success"

        
        
    return render(request, "Rooms.html",{"categoryno": categoryno, "room_no": room_no, "floar_no":floar_no, "no_bads": no_bads, "comment":comment})

    
    
    
#     result = ""
#     category_name = ""
#     rooms_no = ""
#     floar_no = ""
#     no_bads = ""
#     comment = ""
#     try:
#         if request.GET:
            
#             categoryno = request.GET["categoryno"]
            
#             rooms_no = request.GET["rooms_no"]

#             floar_no = request.GET["floar_no"]
            
#             sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/hotelbook')
#             sqlEngine.execute(
#                 "INSERT INTO `rooms`  VALUES (null,null,'{0}', '{1}','{2}','{3}');".format(categoryno, rooms_no, floar_no, no_bads, comment))
#             result = "Success"
            
#     except ex as Exception:
#         result = str(ex)
#     return render(request, "Rooms.html",
#                   {"result": result, "room_id":rooms_id,"categoryno": categoryno, "room_no": rooms_no, "floar":floar_no, "no_bads":no_bads, "comment":comment})
     

# # def sum(request):
# #     num1=0
# #     num2=0
# #     result=0
# #     cmd="Solve"
# #     if request.POST:
# #         cmd=request.POST["cmd"]
# #         num1=int(request.POST["num1"])
# #         num2=int(request.POST["num2"])
# #         if cmd=="add":
#             result=int(num1) + int(num2)
#             print("Add code here")
#         if cmd=="sub":
#             result=int(num1) - int(num2)
#             print("Sub code here")
#         print(cmd)
#     return render(request,"AddAndSub.html",{'cmd':cmd,'num1':num1,'num2':num2,'result':result})
  
  
  
  
def login(request):
    return render(request, "login.html")

def index(request):
    return render(request, "form.html")

def rough(request):
    return render(request, "Start_Hotel_1.html")




def book(request):
    id = ""
    name = ""
    email = ""
    phone = ""
    city = ""
    postcode = ""
    country = ""
    people = ""
    room = ""
    bedding = ""
    arrive = ""
    depart = ""
    comment = ""
    
    if request.POST:
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        city = request.POST["city"]
        postcode = request.POST["postcode"]
        country = request.POST["country"]
        people = request.POST["people"]
        room = request.POST["room"]
        bedding = request.POST["bedding"]
        arrive = request.POST["arrive"]
        depart = request.POST["depart"]
        comment = request.POST["comment"]

        
        sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/hotelbook')
        sqlEngine.execute(
                "INSERT INTO `hotelbook`  VALUES (null,'{0}', '{1}','{2}', '{3}','{4}', '{5}','{6}', '{7}','{8}', '{9}','{10}','{11}');".format(name, email,phone,city,postcode,country,people,room,bedding,arrive,depart,
                                                                              comment))
        result = "Success"

        
        
    return render(request, "BokkingHotel.html",{"name": name, "email": email, "phone":phone, "city": city,"postcode":postcode ,"country":country, "people":people, "room":room, "bedding":bedding, "arrive":arrive, "depart":depart, "comment":comment})
 
    # guest id or room id 
    
def all_booking(request):
    id = ""
    name = ""
    email = ""
    phone = ""
    city = ""
    postcode = ""
    country = ""
    people = ""
    room = ""
    bedding = ""
    arrive = ""
    depart = ""
    comment = ""
    
    if request.GET:
        id = request.GET["id"]
    sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/hotelbook')
    result=sqlEngine.execute("SELECT * FROM `hotelbook`")
     #result=list(result)
    names = result.keys()
    return render(request, "all_booking.html",
                  {"result":result,"id":id,"name": name, "email": email, "phone":phone, "city": city,"postcode":postcode ,"country":country, "people":people, "room":room, "bedding":bedding, "arrive":arrive, "depart":depart, "comment":comment})





        
def update_booking(request):
    id = ""
    name = ""
    email = ""
    phone = ""
    city = ""
    postcode = ""
    country = ""
    people = ""
    room = ""
    bedding = ""
    arrive = ""
    depart = ""
    comment = ""
    cmd="Solve"
    
    if request.POST:
        cmd=request.POST["cmd"]
        if cmd=="update":
            print("updating")
            id = request.POST["id"]
            name = request.POST["name"]
            email = request.POST["email"]
            phone = request.POST["phone"]
            city = request.POST["city"]
            postcode = request.POST["postcode"]
            country = request.POST["country"]
            people = request.POST["people"]
            room = request.POST["room"]
            bedding = request.POST["bedding"]
            arrive = request.POST["arrive"]
            depart = request.POST["depart"]
            comment = request.POST["comment"]
            
            
    
            sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/hotelbook')
            update="UPDATE `hotelbook` SET `name`='{0}',`email`='{1}',`phone`='{2}',`city`='{3}',`postcode`='{4}',`country`='{5}',`people`='{6}',`room`='{7}',`bedding`='{8}',`arrive`='{9}',`depart`='{10}',`comment`='{11}' WHERE id = '{12}' ".format(name, email,phone,city,postcode,country,people,room,bedding,arrive,depart,comment,id)
            print("Update",update)
            sqlEngine.execute("UPDATE `hotelbook` SET `name`='{0}',`email`='{1}',`phone`='{2}',`city`='{3}',`postcode`='{4}',`country`='{5}',`people`='{6}',`room`='{7}',`bedding`='{8}',`arrive`='{9}',`depart`='{10}',`comment`='{11}' WHERE id = '{12}' ".format(name, email,phone,city,postcode,country,people,room,bedding,arrive,depart,comment,id))
            # print("uppppp")
            
                
              
            
            
        if cmd=="delete":
            if cmd=="delete":
             print("delete")
             id = request.POST["id"]
             name = request.POST["name"]
             email = request.POST["email"]
             phone = request.POST["phone"]
             city = request.POST["city"]
             postcode = request.POST["postcode"]
             country = request.POST["country"]
             people = request.POST["people"]
             room = request.POST["room"]
             bedding = request.POST["bedding"]
             arrive = request.POST["arrive"]
             depart = request.POST["depart"]
             comment = request.POST["comment"]
            
             
            

            
            sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/hotelbook')
            sqlEngine.execute("DELETE FROM `hotelbook` WHERE id='{0}'".format(id))
                
            
   
            
    return render(request, "edit_booking.html",{"name": name, "email": email, "phone":phone, "city": city,"postcode":postcode ,"country":country, "people":people, "room":room, "bedding":bedding, "arrive":arrive, "depart":depart, "comment":comment, "id":id})
    
  
def guestinsert(request):
    
    # if request.GET:
    #     categoryno=request.GET["categoryno"]
        
    name = ""
    age = ""
    address = ""
    aadhaar = ""
    pan = ""
    comment = ""
    guest_id = ""
    
    if request.POST:
        name = request.POST["name"]
        age = request.POST["age"]
        address = request.POST["address"]
        aadhaar = request.POST["aadhaar"]
        pan = request.POST["pan"]
        comment = request.POST["comment"]
        


        
        sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/hotelbook')
        sqlEngine.execute(
                "INSERT INTO `guest`  VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}',null);".format( name, age, address, aadhaar, pan, comment))

        
        
    return render(request, "guestEntry.html",{"name": name, "age": age, "address":address, "aadhaar": aadhaar,"pan":pan ,"comment":comment, "guest_id":guest_id})

    
    
            
    


def edit_booking(request):
    result=[]
    name=[]
    email=[]
    phone=[]
    city=[]
    postcode=[]
    country=[]
    people=[]
    room=[]
    bedding=[]
    arrive=[]
    depart=[]
    comment=[]

    if request.GET:
     id = request.GET["id"]
     
     sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/hotelbook')
     result=sqlEngine.execute("SELECT * FROM `hotelbook` WHERE id ='{0}'".format(id))
     row =result.fetchone()
     name=row[1]
     email=row[2]
     phone=row[3]
     city=row[4]
     postcode=row[5]
     country=row[6]
     people=row[7]
     room=row[8]
     bedding=row[9]
     arrive=row[10]
     depart=row[11]
     comment=row[12]

    return render(request, "edit_booking.html",
                   {"result": result,"name": name, "email": email, "phone":phone, "city": city,"postcode":postcode ,"country":country, "people":people, "room":room, "bedding":bedding, "arrive":arrive, "depart":depart, "comment":comment, "id":id})
        
    
    
    
    



def insert(request):
    result = ""
    category_name = ""
    description = ""
    charge = ""
    try:
        if request.GET:
            category_name = request.GET["category_name"]
            # print(category_name)
            description = request.GET["discription"]
            # print(description)
            charge = request.GET["charge"]
            # print(charge)
            sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/hotelbook')
            sqlEngine.execute(
                "INSERT INTO `room_category`  VALUES (null,'{0}', '{1}','{2}');".format(category_name, description,
                                                                              charge))
            result = "Success"
    except ex as Exception:
        result = str(ex)
    return render(request, "insert.html",
                  {"result": result, "categoryname": category_name, "description": description, "charge": charge})
    
    
def update(request):
    result = ""
    category_name = ""
    description = ""
    charge = ""
    categoryno=0
    cmd="Solve"
    try:
        if request.POST:
            cmd=request.POST["cmd"]
            if cmd=="update":
                categoryno=request.POST["categoryno"]
                category_name = request.POST["category_name"]
                # print(category_name)
                description = request.POST["discription"]
                # print(description)
                charge = request.POST["charge"]
                # print(charge)
                sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/hotelbook')
                sqlEngine.execute("UPDATE `room_category` SET `category_name`='{0}',`description`='{1}',`charge`='{2}' WHERE category_no='{3}'".format(category_name,description,charge,categoryno)) 
                print("sagar")
                result = "Updated"
                #except:
                result ="" # str(ex)
            
            
            if cmd=="delete":
                print("Deleting")
                categoryno=request.POST["categoryno"]
                print("category no",categoryno)
                
                category_name = request.POST["category_name"]
            
                description = request.POST["discription"]
                
                charge = request.POST["charge"]
                print("DELETE FROM `room_category` WHERE category_no='{0}'".format(categoryno))
                sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/hotelbook')
                sqlEngine.execute("DELETE FROM `room_category` WHERE category_no='{0}'".format(categoryno))
                result = "Deleted"
                print("Deleted")
    except Exception as ex:
                result ="" # str(ex)
                print("error")
            
    return render(request, "editcategories.html",{"result": result, "categoryname": category_name, "description": description, "charge": charge,"categoryno":categoryno})
    

# def delete(request):
#     result = ""
#     category_name = ""
#     description = ""
#     charge = ""
#     try:
#         if request.GET:
#             category_name = request.GET["category_name"]
        
#             description = request.GET["discription"]
            
#             charge = request.GET["charge"]
            
#             sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/hotelbook')
#             sqlEngine.execute("DELETE FROM `room_category` WHERE category_no='{3}'".format(category_no))
#             result = "Success"
#     except:
#         result ="" # str(ex)
#     return render(request, ".html",
#                   {"result": result})
    
    
    
    
# def all_table(request):
            
#     sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/hotelbook')
#     sqlEngine.execute("SELECT * FROM `room_category`;".format(category_name,description,charge,40)) 
    
#     return render(request, "all_table.html",
#                   {"result": result})
    
    
    
def all_table(request):
     if request.GET:
        category_no = request.GET["category_no"]
     sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/hotelbook')
     result=sqlEngine.execute("SELECT * FROM `room_category`")
     #result=list(result)
     names = result.keys()
     return render(request, "all_table.html",
                  {'result': result,'names':names})
     
     
     
def editcategories(request):
    result=""
    category_no=""
    categoryname=""
    description=""
    charge=""
    if request.GET:
     category_no = request.GET["categoryno"]
     
     sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/hotelbook')
     result=sqlEngine.execute("SELECT * FROM `room_category` WHERE category_no ='{0}'".format(category_no))
     row =result.fetchone()
     categoryname=row[1]
     description=row[2]
     charge=row[3]
    return render(request, "editcategories.html",
                   {"result": result,"categoryno":category_no, "categoryname": categoryname,"description":description,"charge":charge})
            
            
def board(request):
    return render(request, "DashBoard.html")
    
     
