#Library openCV

import cv2 as cv # นำเข้าไลบรารี OpenCV เป็น cv และ requests
import requests

camera = cv.VideoCapture(0) #เรียกใช้กล้อง(Camera) ใน OpenCV
url='https://notify-api.line.me/api/notify'  # กำหนดURLสำหรับLineNotifyAPI
token='aB08DgPVxb0QIWRfrw4ttZEQKLTREWnHkVM8rdSHn6w' # กำหนดToken
headers={'Content-Type':'application/x-www-form-urlencoded','Authorization': 'Bearer ' + token} # กำหนด(headers)สู่ Line Notify API
msg='ตรวจพบความเคลื่อนไหว' #กำหนดข้อความที่ต้องการส่ง



while camera.isOpened(): # ใช้while สำหรับตรวจสอบกล้องเปิดอยู่หรือไม่
    retry, screen1 = camera.read() # อ่านเฟรมจากกล้องสองครั้ง
    retry, screen2 = camera.read()
    difference = cv.absdiff(screen1,screen2) #คำนวณความแตกต่างระหว่างสองภาพ
    gray = cv.cvtColor(difference,cv.COLOR_RGB2GRAY) #แปลงรูปภาพเป็นขาว-ดำ
    blur = cv.GaussianBlur(gray,(5,5),0)  #ทำการแบลอรูปภาพด้วยกระจาย
    _,threshold=cv.threshold(blur,20,255,cv.THRESH_BINARY) #ใช้ค่าที่กำหนดในการแบ่งสีขาวและดำ
    dilation=cv.dilate(threshold,None,iterations=5) # ทำการขยายข้อมูลในรูปภาพเพื่อกำจัดสัญญาณรบกว
    contours, _,=cv.findContours(dilation,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE) # ค้นหาเส้นขอบในรูปภาพ
    cv.drawContours(screen1,contours,-1,(0,225,0),2)  # วาดกรอบลงบน(screen1) สีเขียว

    for movement in contours: #วนลูปผ่านรายการเส้นขอบที่ค้นหาได้
        if cv.contourArea(movement)<8000: # ถ้าพื้นที่ของเส้นขอบน้อยกว่า 8000พิกเซล ข้ามไป
            continue
        x,y, height,width,= cv.boundingRect(movement) #คำนวณพิกัดของกล่องล้อมวัตถุ
        cv.rectangle(screen1, (x, y), (x + width, y + height), (0, 225, 0), 2)#วาดกรอบวัตถุบนเฟรมหลัก (screen1) ด้วยสีเขียว
        # ส่งข้อความไปที่Line Notify API
        notify = requests.post(url, headers=headers, params={'message': msg})
        print(notify.text)


    if cv.waitKey(10) == ord('q'): #รับinput จากผู้ใช้ ถ้าผู้ใช้กดปุ่ม 'q' ในระหว่างที่แสดงภาพ
        break
    cv.imshow('pyCCTV',screen1) # แสดงภาพบนหน้าต่างชื่อ 'pyCCTV'