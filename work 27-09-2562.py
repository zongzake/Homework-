#!/usr/bin/env python
# coding: utf-8

# In[2]:


#ข้อที่ 1 ให้นักศึกษากำหนดค่าตัวเลขมา 1 จำนวน ตั้งแต่ 15-60 เป็นตัวแปร A จากนั้นให้เลือกตัวเลขตั้งแต่ 2-15 มา 1 จำนวน เป็นตัวแปร B แล้วให้หาว่า ตัวแปร B สามารถหารจำนวนในช่วงที่ 15-A ใดแล้วมีเศษเป็น 0 บ้าง จงแสดงจำนวนทั้งหมดนั้น

A = int(input("Enter A in range 15-60 :   "))
B = int(input("Enter B in range 2-15 :   "))
for C in range(15,A+1):
    if C%B == 0:
        print(C,end='   ')


# In[5]:


#ข้อที่ 2 กำหนดข้อมูลมา 1 จำนวน และจงคำนวณหาผลรวมของจำนวนเต็มบวกทุกจำนวนที่มี 2 4 6 และ 8 เป็นตัวประกอบ และมีค่าน้อยกว่าข้อมูลที่กำหนด

nums = [2, 4, 6, 8]
max = int(input("Count: "))
result = 0
for x in range(0,max):
    if x%2 == 0 or x%4 == 0 or x%6 == 0 or x%8 == 0:
        result += x
print("Answer is ",result)


# In[6]:


#ข้อที่ 3 จงแปลงอุณภูมิจากองศาเซลเซียสเป็นองศาฟาเรนไฮ และจากองศาเซลเซียสเป็นองศาเคลวิน

temperature = float(input("temp ํC :" ))
temperature_convert_ํC_to_ํF = (9/5*temperature)+32
temperature_convert_ํC_to_ํK = (temperature + 273.15)
print("temp ํF = ", temperature_convert_ํC_to_ํF,"      " "temp ํK = " ,temperature_convert_ํC_to_ํK)


# In[7]:


#ข้อที่ 4 หนอนตัวหนึ่ง พยายามปีนต้นไม้ที่มีความสูง T เมตร หนอนพยายามจะไต่ให้ถึงยอดต้นไม้ ในเวลากลางวันหนอนไต่ขึ้นไปได้ W เมตร เวลากลางคืนหนอนนอนหลับจึงไม่ได้ไต่แต่กลับไถลลงมาเป็นระยะทาง F เมตร จงหาว่าหนอนจะใช้เวลากี่วันในการไต่ไปถึงยอดไม้ (กำหนดให้หนอนทากเริ่มไต่ในเวลากลางวัน)
T = int(input("T: ")) 
W = int(input("W: ")) 
F = int(input("F: ")) 
s = 0 
day = 1 
while True:    
    s = s+W    
    if s>=T:       
        break    
    s = s-F    
    day = day+1 
print(day,"day(s).")


# In[8]:


#ข้อที่ 5 จงทำการตรวจสอบความถูกต้องของ ISBN จะใช้ตัวเลขหลักสุดท้ายเป็น check digit ในการตรวจสอบความถูกต้องของตัวเลขอื่น ๆ โดยวิธีที่ใช้ตรวจสอบคือ10n1+ 9n2+ 8n3+ 7n4+ 6n5+ 5n6+ 4n7+ 3n8+ 2n9+ n10 จะต้องหารด้วย 11 ลงตัวหากกำหนดตัวเลขหลักที่ 1-9 มาให้ จงคำนวณหา ISBN ทั้งสิบหลัก
n1 = int(input("n1 :"))
n2 = int(input("n2 :"))
n3 = int(input("n3 :"))
n4 = int(input("n4 :"))
n5 = int(input("n5 :"))
n6 = int(input("n6 :"))
n7 = int(input("n7 :"))
n8 = int(input("n8 :"))
n9 = int(input("n9 :"))
print(str(n1) + str(n2) + str(n3) + str(n4) + str(n5) + str(n6) + str(n7) + str(n8) + str(n9))
ISBN1to9 = ((10 * n1) + (9 * n2) + (8 * n3) + (7 * n4) + (6 * n5) + (5 * n6) + (4 * n7) + (3 * n8) + (2 * n9))
if (ISBN1to9 + 1) % 11 == 0:
    print(str(n1) + str(n2) + str(n3) + str(n4) + str(n5) + str(n6) + str(n7) + str(n8) + str(n9) + "1")
elif (ISBN1to9 + 2) % 11 == 0:
    print(str(n1) + str(n2) + str(n3) + str(n4) + str(n5) + str(n6) + str(n7) + str(n8) + str(n9) + "2")
elif (ISBN1to9 + 3) % 11 == 0:
    print(str(n1) + str(n2) + str(n3) + str(n4) + str(n5) + str(n6) + str(n7) + str(n8) + str(n9) + "3")
elif (ISBN1to9 + 4) % 11 == 0:
    print(str(n1) + str(n2) + str(n3) + str(n4) + str(n5) + str(n6) + str(n7) + str(n8) + str(n9) + "4")
elif (ISBN1to9 + 5) % 11 == 0:
    print(str(n1) + str(n2) + str(n3) + str(n4) + str(n5) + str(n6) + str(n7) + str(n8) + str(n9) + "5")
elif (ISBN1to9 + 6) % 11 == 0:
    print(str(n1) + str(n2) + str(n3) + str(n4) + str(n5) + str(n6) + str(n7) + str(n8) + str(n9) + "6")
elif (ISBN1to9 + 7) % 11 == 0:
    print(str(n1) + str(n2) + str(n3) + str(n4) + str(n5) + str(n6) + str(n7) + str(n8) + str(n9) + "7")
elif (ISBN1to9 + 8) % 11 == 0:
    print(str(n1) + str(n2) + str(n3) + str(n4) + str(n5) + str(n6) + str(n7) + str(n8) + str(n9) + "8")
elif (ISBN1to9 + 9) % 11 == 0:
    print(str(n1) + str(n2) + str(n3) + str(n4) + str(n5) + str(n6) + str(n7) + str(n8) + str(n9) + "9")
else:
    print("ERROR")


# In[9]:


#ข้อที่ 6 ให้กำหนดข้อมูลใดก็ได้ที่เป็นจำนวนจริงจนกว่าจะพบค่า -1 เพื่อหาค่าเฉลี่ยของจำนวนเหล่านั้นทั้งหมด (ไม่รวม -1)

sum = 0
count = 0
n = float(input("enter number"))
while n != -1:
    sum += n
    count = count + 1
    n = float(input("enter number"))
avg = sum / count
print(avg)


# In[10]:


#ข้อที่ 7 จงเขียนคำนวณหาความยาวของด้านที่สามของสามเหลี่ยม เมื่อเราทราบความยาวด้านสองด้าน (a กับ b)และมุมระหว่างด้านสองด้านนั้น (C) ซึ่งคำนวณได้จาก Law of Cosines

import math
A=float(input("A SIDE LENGTH : "))
B=float(input("B SIDE LENGTH :"))
D=float(input("CORNER C :"))
C=D*math.pi/180
c=math.sqrt((A**2)+(B**2)-(2*A*B*math.cos(C)))
print("c = ",c, "cm.")


# In[12]:


#ข้อที่ 8 ให้ทำการกำหนดคะแนนเพื่อตัดเกรดตามเกณฑ์ที่ระบุ โดย 100-80=A  79-75=B+  74-70=B  69-65=C+  64-60=C  59-55=D+  54-50=D >50=F โดยในกรณีที่คะแนนมีข้อผิดพลาด ให้แสดงผลว่า ERROR
x = int(input("score:"))
if 100>=x>=80:
    print("A")
elif 80>x>=75:
    print("B+")
elif 75>x>=70:
    print("B")
elif 70>x>=65:
    print("C+")
elif 65>x>=60:
    print("C")
elif 60>x>=55:
    print("D+")
elif 55>x>=50:
    print("D")
elif 50>x:
    print("F")
else:
    print("error")


# In[11]:


#ข้อที่ 9 ร้านขายโต๊ะร้านหนึ่ง พยายามเพิ่มยอดขายโดยการเสนอโปรโมชั่นพิเศษ ถ้าคุณซื้อโต๊ะมากกว่า 5 ตัว ที่มีมูลค่ารวมเกิน 18000 บาท คุณจะได้ส่วนลด 20%   ให้คำนวณจำนวนโต๊ะที่ซื้อและราคารวม จากนั้นคำนวณราคาที่ต้องจ่าย
Count = int(input("How many table: ")) 
money = int(input("How much: ")) 
if Count > 5 and money > 18000:    
    s = money-money*0.2 
else:    
    s = money 
print("You have to pay",int(s),"bath.")


# In[13]:


#ข้อที่ 10 จงคำนวณหาค่าโอห์มรวมของวงจรแบบขนาน ตามสูตร RT = (R1 x R2)/(R1 + R2) โดยกำหนดให้ R1 = 250 Ohm. และ R2 = 870 Ohm.

print("R1 = 250 Ohm.")
print("")
print("R2 = 870 Ohm.")
print("")
print("RT = (R1 x R2)/(R1 + R2)")
print("")
print("RT = " ,(250*870)/(250+870),"Ohm.")


# In[ ]:




