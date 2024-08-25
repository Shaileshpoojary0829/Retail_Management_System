from tkinter import *
from tkinter import messagebox
from datetime import *
import random
billno=random.randint(1000,9999)
date=date.today().strftime('%d-%b-%Y')
time=datetime.now().strftime('%H:%M:%S')
global Flag 
global Generate
Flag=Generate=False
total_price = 0
#functionality

def savefile():
  global Generate
  bill_content=textarea.get(1.0,END)
  bill=messagebox.askyesno("CONFIRM","Do you really want to save the bill?")
  if(bill):
    file=open(f"{billno}.pdf",'w')
    file.write(bill_content)
    messagebox.showinfo("Success","Your Bill saved successfully")
def generate():
  if not Generate:
     messagebox.showerror('ERROR','Please calculate total.')
  else:
     savebtn.configure(state="normal")
     gbill=messagebox.askyesno("CONFIRM","Do you really want to sumarize the bill")
     if gbill:
        textarea.config(state="normal")
        textarea.insert(END,"===============================================\n")
        gst=(total_price*10)/100
        total_amount=total_price+gst
        textarea.insert(END,f"Total Amount :                  {total_price} Rs\n")
        textarea.insert(END,f"GST:                            {gst} Rs\n")
        textarea.insert(END,f"Grand Total :                   {total_amount} Rs\n")
        textarea.insert(END,"----------------------------------------------\n")
        textarea.insert(END,"\t  **** THANK YOU VISIT AGAIN ****\n")
        li=g_entry+c_entry+co_entry
        for entry in li:
          entry.delete(0,END)
          entry.insert(0,0)
        root.focus()
        addbtn.configure(state="disabled")
        totalbtn.configure(state="disabled")
        generatebtn.configure(state="disabled")      
        textarea.config(state="disabled")            
def totalbutton():
  global Flag
  global Generate
  global total_price

  phno=phone_no.get()
  if cus_text.get()=='' or phone_no.get()=='':
    messagebox.showerror('ERROR','Please fill customer details')
    return
  if phno.isnumeric()==False or len(phno)!=10:
    messagebox.showerror('ERROR','Please enter valid phone number')
    return
  try:
      all_entry=g_entry+c_entry+co_entry
      selected_item=any(int(entry.get())>0 for entry in all_entry)
      print(selected_item)
      if not selected_item:
          messagebox.showerror("ERROR","No Products selected")
          return
      #caculation
      item_entries = g_label + c_label + co_label
      item_values = g_entry + c_entry + co_entry
      selected_items = {}
      for label, entry in zip(item_entries, item_values):# multiple iteration
            value = int(entry.get())
            if value > 0:
                item_name = label.cget("text") #returns label_name
                selected_items[item_name]=value
  except ValueError:
      messagebox.showerror("ERROR","Please enter correct value")
      return
  #bill_area
  textarea.config(state="normal")
  Generate=True
  if Flag==False:
   textarea.insert(END,"\t          RETAIL STORE  \n")
   textarea.insert(END,"\t       **** CASH BILL ****\n")
   textarea.insert(END,"-----------------------------------------------\n")
   textarea.insert(END,f"Bill Number: {billno}           ")
   textarea.insert(END,f"Date: {date}\n")
   textarea.insert(END,f"Customer Name: {cus_text.get()}      ")
   textarea.insert(END,f"Time: {time}\n")
   textarea.insert(END,f"Phone Number: {phone_no.get()}\n")
   textarea.insert(END,"===============================================\n")
   textarea.insert(END,"Product\t\t Rate\t Quantity\t  Price\n")
   textarea.insert(END,"===============================================\n")
   Flag=True  
  prices = {
        'Sugar': 50, 'Rice': 80, 'Oil': 120, 'Daal': 90, 'Wheat': 60,
        'Mazza': 40, 'Fanta': 40, 'Sprite': 40, 'Sting': 20, 'RedBull': 100,
        'Soap': 30, 'Shampoo': 5, 'Perfume': 200, 'Cream': 40, 'Powder': 50
    }
  for item, qty in selected_items.items():
        price = prices.get(item, 0)
        item_total = price * qty
        total_price+=item_total #total amt
        textarea.insert(END, f"{item}\t\t {prices.get(item,1)}\t  {qty}\t     {item_total}\n")
        li=g_entry+c_entry+co_entry
        for entry in li:
           entry.delete(0,END)
           entry.insert(0,0)
  root.focus()
  textarea.config(state="disabled")
  
def addbutton():
  global Flag
  global Generate
  global total_price
  if(itmtxt.get()=='' or pricetxt.get()=='' or qtytxt==''):
    messagebox.showerror("ERROR!!!","Enter all three entries")
  else:
    try:
      item_name=itmtxt.get()
      price=int(pricetxt.get())
      qty=int(qtytxt.get())
      item_total=price*qty
      total_price+=item_total
      textarea.config(state="normal")
      Generate=True
      if Flag==False:
        textarea.insert(END,"\t          RETAIL STORE  \n")
        textarea.insert(END,"\t      **** CASH BILL ****\n")
        textarea.insert(END,"---------------------------------------------\n")
        textarea.insert(END,f"Bill Number: {billno}           ")
        textarea.insert(END,f"Date: {date}\n")
        textarea.insert(END,f"Customer Name: {cus_text.get()}      ")
        textarea.insert(END,f"Time: {time}\n")
        textarea.insert(END,f"Phone Number: {phone_no.get()}\n")
        textarea.insert(END,"=============================================\n")
        textarea.insert(END,"Product\t\t Rate\t Quantity\t  Value\n")
        textarea.insert(END,"=============================================\n")
        Flag=True
      textarea.insert(END, f"{item_name}\t\t {price}\t  {qty}\t     {item_total}\n")
      subclear()
      textarea.config(state="disabled")
    except ValueError:
      messagebox.showerror("ERROR!!!","Qty and Price must be number")
  


def mainclear():
    all_entry=g_entry+c_entry+co_entry
    selected_item=any(int(entry.get())>0 for entry in all_entry)
    if not selected_item and cus_text.get()=='' or phone_no.get()=='':
      messagebox.showerror("ERROR","Nothing to clear ")
    else:
      global Flag
      global Generate
      global total_price
      cus_text.delete(0,END)
      phone_no.delete(0,END)
      li=g_entry+c_entry+co_entry
      for entry in li:
        entry.delete(0,END)
        entry.insert(0,0)
      itmtxt.delete(0,END)
      qtytxt.delete(0,END)
      pricetxt.delete(0,END)
      textarea.config(state="normal")
      textarea.delete(1.0,END)
      textarea.config(state="disabled")
      cus_text.focus_set()
      Flag=Generate=False
      total_price = 0
      addbtn.configure(state="normal")
      totalbtn.configure(state="normal")
      generatebtn.configure(state="normal")   

def subclear():
   if(itmtxt.get()=='' or pricetxt.get()=='' or qtytxt==''):
    messagebox.showerror("ERROR!!!","Nothing to clear ")
   else:
     itmtxt.delete(0,END)
     qtytxt.delete(0,END)
     pricetxt.delete(0,END)
     itmtxt.focus_set()

#GUI Part
root=Tk()
root.configure(background="white")
root.title("𝗕𝗶𝗹𝗹𝗶𝗻𝗴 𝗦𝘆𝘀𝘁𝗲𝗺")
#root.iconbitmap("bill_icon.ico")
root.geometry("1270x625+1+1")
root.resizable(False,False)

head_label=Label(root,text="Retail Billing System",font=('times new roman','30','bold'),bg="black",fg="Yellow",width=100,bd=12,relief=GROOVE)

#cus_details_Frame
customer_frame=LabelFrame(root,text="Customer Details",font=('times new roman','17','bold'),bg="black",fg="Yellow",bd=12,relief=GROOVE)
cus_name=Label(customer_frame,text='Name',font=('times new roman',16,'bold'),bg='black',fg='white')
cus_name.grid(row=0,column=1,padx=20,pady=4)

cus_text=Entry(customer_frame,font=('arial',15),bd=8,width=20)
cus_text.grid(row=0,column=2,padx=9,pady=8)

phone=Label(customer_frame,text='Phone Number',font=('times new roman',16,'bold'),bg='black',fg='white')
phone.grid(row=0,column=3,padx=20,pady=4)

phone_no=Entry(customer_frame,font=('arial',15),bd=8,width=20)
phone_no.grid(row=0,column=4,padx=9,pady=8)

bill=Label(customer_frame,text='Bill No',font=('times new roman',16,'bold'),bg='black',fg='white')
bill.grid(row=0,column=5,padx=20,pady=4)
bill_no=Entry(customer_frame,font=('arial',15),bd=8,width=20,state="readonly",textvariable=StringVar(value=billno))
bill_no.grid(row=0,column=6,padx=9,pady=8)


head_label.pack(fill=X,padx=3)
customer_frame.pack(fill=X,pady=5,padx=3)

#Product_frame
product_frame=Frame(root)
#grocery_section
Grocery_details=LabelFrame(product_frame,text="Grocery",font=('times new roman','17','bold'),bg="black",fg="Yellow",bd=12,relief=GROOVE)
grocery_items={
'Sugar':0,
'Rice':1,
'Oil':2,
'Daal':3,
'Wheat':4
}
g_label=[]
g_entry=[]
for name,row in grocery_items.items():
  label=Label(Grocery_details,text=name,font=('times new roman',16,'bold'),bg='black',fg='white')
  label.grid(row=row,column=0,pady=5,padx=5)
  g_label.append(label)    #glabel
  entry=Entry(Grocery_details,font=('arial',15),bd=8,width=8)
  entry.insert(0,0)
  entry.grid(row=row,column=1,padx=30,pady=5)
  g_entry.append(entry)    #gentry

Grocery_details.grid(row=0,column=0,padx=3)

#ColdDrinks_section
coldDrinks_details=LabelFrame(product_frame,text="Cold Items",font=('times new roman','17','bold'),bg="black",fg="Yellow",bd=12,relief=GROOVE)
cold_items={
'Mazza':0,
'Fanta':1,
'Sprite':2,
'Sting':3,
'RedBull':4
}
c_label=[]
c_entry=[]
for name,row in cold_items.items():
  label=Label(coldDrinks_details,text=name,font=('times new roman',16,'bold'),bg='black',fg='white')
  label.grid(row=row,column=0,pady=5,padx=5)
  c_label.append(label)
  entry=Entry(coldDrinks_details,font=('arial',15),bd=8,width=8)
  entry.insert(0,0)
  c_entry.append(entry)
  entry.grid(row=row,column=1,padx=30,pady=5)
coldDrinks_details.grid(row=0,column=1,padx=3)

#cosmetics_section
cosmetics_details=LabelFrame(product_frame,text="Cosmetics",font=('times new roman','17','bold'),bg="black",fg="Yellow",bd=12,relief=GROOVE)
cosmetics_items={
'Soap':0,
'Shampoo':1,
'Perfume':2,
'Cream':3,
'Powder':4
}
co_label=[]
co_entry=[]
for name,row in cosmetics_items.items():
  label=Label(cosmetics_details,text=name,font=('times new roman',16,'bold'),bg='black',fg='white')
  label.grid(row=row,column=0,pady=5,padx=5)
  co_label.append(label)
  entry=Entry(cosmetics_details,font=('arial',15),bd=8,width=8)
  entry.insert(0,0)
  co_entry.append(entry)
  entry.grid(row=row,column=1,padx=30,pady=5)
cosmetics_details.grid(row=0,column=2,padx=3)

product_frame.pack(fill=X,padx=3)
#billSection
bill_frame=Frame(product_frame,bd=8,relief='groove')
bill_label=Label(bill_frame,text="Bill Area",font=('times new roman',15,'bold'),fg='black',bd=7,relief='groove')
bill_label.pack(fill=X)
scrollbar=Scrollbar(bill_frame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(bill_frame,height=15,width=47,state="disabled",yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

bill_frame.grid(row=0,column=3)
#additional
moreitm=LabelFrame(root,text="Other Items",font=('times new roman','17','bold'),bg="black",fg="Yellow",bd=12,relief=GROOVE)

itmname=Label(moreitm,text="Item Name",font=('times new roman',16,'bold'),bg='black',fg='white')
itmname.grid(row=0,column=0,pady=5,padx=5)
itmtxt=Entry(moreitm,font=('arial',15),bd=8,width=8)
itmtxt.grid(row=0,column=1,padx=10,pady=5)

qtyname=Label(moreitm,text="Quantity",font=('times new roman',16,'bold'),bg='black',fg='white')
qtyname.grid(row=1,column=0,pady=5,padx=5)
qtytxt=Entry(moreitm,font=('arial',15),bd=8,width=8)
qtytxt.grid(row=1,column=1,padx=10,pady=5)

pricename=Label(moreitm,text="Price",font=('times new roman',16,'bold'),bg='black',fg='white')
pricename.grid(row=0,column=2,pady=5,padx=5)
pricetxt=Entry(moreitm,font=('arial',15),bd=8,width=8)
pricetxt.grid(row=0,column=3,padx=10,pady=5)

addbtn=Button(moreitm,text="Add",font=('times new roman',15,'bold'),width=8,command=addbutton)
addbtn.grid(row=1,column=2,padx=3)
clrbtn=Button(moreitm,text="Clear",font=('times new roman',15,'bold'),width=8,command=subclear)
clrbtn.grid(row=1,column=3)


btnFrame=Frame(moreitm,bd=8,relief=GROOVE,bg='white')

totalbtn=Button(btnFrame,text='Total',bg='black',fg='white',font=('arial',15,'bold'),width=10,command=totalbutton)
totalbtn.grid(row=0,column=0,padx=5,pady=14)
generatebtn=Button(btnFrame,text='Generate',bg='black',fg='white',font=('arial',15,'bold'),width=10,command=generate)
generatebtn.grid(row=0,column=1,padx=5,pady=14)
savebtn=Button(btnFrame,text='Save',bg='black',fg='white',font=('arial',15,'bold'),width=10,state='disabled',command=savefile)
savebtn.grid(row=0,column=2,padx=5,pady=14)
clearbtn=Button(btnFrame,text='Clear',bg='black',fg='white',font=('arial',15,'bold'),width=10,command=mainclear)
clearbtn.grid(row=0,column=3,padx=5,pady=14)
exitbtn=Button(btnFrame,text='Exit',bg='black',fg='white',font=('arial',15,'bold'),width=10,command=lambda:root.destroy())
exitbtn.grid(row=0,column=4,padx=5,pady=14)

btnFrame.grid(row=0,column=5,rowspan=3,padx=30)
moreitm.pack(fill=X,padx=4)
root.mainloop()


