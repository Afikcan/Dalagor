import turtle
import math
import random
import system
import os 


#Değişkenler
score1=0
score2=0
renktutucu=0
size1=1.5
size2=1.5
goalspeed1=15
goalspeed2=15
 
#Fontu ayarlama
FONTSIZE =7
FONT = ('Arial', FONTSIZE, 'normal')
FONTSIZE2 =8
FONTFINISH = ('Arial', FONTSIZE2, 'normal')
 
 
#Ekran yaratma
ekran = turtle.Screen()
ekran.bgcolor("lightblue")
 
#scoreboard yaratma
scoreboard=turtle.Turtle()
scoreboard.penup()
scoreboard.setposition(-85,0)
scoreboard.pencolor("white")
scoreboard.hideturtle()
scoreboard.write("Score P1:{}   Score P2:{}".format(score1,score2),font=FONT)
 
#Bilgi yazısını yaratma
info=turtle.Turtle()
info.penup()
info.setposition(-85,150)
info.pencolor("black")
info.hideturtle()
info.write("Kontrol:\nYeşil karakter(P1) Sağ-Sol\nSarı karakter(P2) A-D\n\nYem bilgileri:\nP1->Siyah(+) Kırmızı(SÜRPİZ)\nP2->Beyaz(+) Turuncu(SÜRPİZ)",font=FONT)
 
 
#Ekrana sınır çizme1
borderpen = turtle.Turtle()
borderpen.speed(700)
borderpen.pensize(3)
borderpen.color("darkblue")
borderpen.penup() 
borderpen.setposition(+100,-350)
borderpen.pendown()
for i in range(2):
    borderpen.forward(+400)
    borderpen.left(90)
    borderpen.forward(+700)
    borderpen.left(90)
borderpen.hideturtle()
 
#Ekrana sınır çizme 2
borderpen2 = turtle.Turtle()
borderpen2.speed(700)
borderpen2.pensize(3)
borderpen2.color("darkblue")
borderpen2.penup() 
borderpen2.setposition(-500,-350)
borderpen2.pendown()
for i in range(2):
    borderpen2.forward(+400)
    borderpen2.left(90)
    borderpen2.forward(+700)
    borderpen2.left(90)
borderpen2.hideturtle()
 
#Player 1 oluşturulması
player1 = turtle.Turtle()
player1.penup()
player1.color("darkgreen")
player1.shape("turtle")
player1.turtlesize(size1)
player1.setposition(+300,0)
player1.speed()
player1.penup() 
player1.seth(90)
 
#Player 2 oluşturulması
player2 = turtle.Turtle()
player2.penup()
player2.color("yellow")
player2.shape("turtle")
player2.setposition(-300,0)
player2.turtlesize(size2)
player2.speed()
player2.penup()
player2.seth(90)
 
#Player1-Player2 hareket fonksiyonları
def moverightp1():
    player1.setposition(player1.xcor()+30,player1.ycor())
    
def moveleftp1():
    player1.setposition(player1.xcor()-30,player1.ycor())
#player2 hareket fonksiyonları
def moverightp2():
    player2.setposition(player2.xcor()+30,player2.ycor())
     
def moveleftp2():
    player2.setposition(player2.xcor()-30,player2.ycor())    
 
 
#Yem yaratma 
bobstacle = turtle.Turtle()
bobstacle.shape("square")
bobstacle.color("lightblue")
bobstacle.penup()
bobstacle.hideturtle()
bobstacle.setposition(random.randint(-200,200),+410)
bobstacle.showturtle()
bobstacle.setheading(270)
 
bobstacle2 = turtle.Turtle()
bobstacle2.shape("square")
bobstacle2.color("lightblue")
bobstacle2.penup()
bobstacle2.hideturtle()
bobstacle2.setposition(random.randint(-200,200),+410)
bobstacle2.showturtle()
bobstacle2.setheading(270)


 
 
 
#Klavyeyi ayarlamak için.Burada bir tuşa bastığımızda o fonksyonun gerçekleşmesini sağlıyoruz.
turtle.listen()
turtle.onkey(moveleftp1, "Left")
turtle.onkey(moverightp1, "Right")
turtle.onkey(moveleftp2,"a")
turtle.onkey(moveleftp2,"A")
turtle.onkey(moverightp2,"d")
turtle.onkey(moverightp2,"D")

while True:
    
    bobstacle.forward(goalspeed1)
    bobstacle2.forward(goalspeed2)

    #P1-P2 için yemlerin sürekli akması    
    if bobstacle.ycor()<-350:
        bobstacle.speed(500)
        bobstacle.color("lightblue")
        kontrol=random.randint(0,10)
        if(kontrol<=5):
            bobstacle.color("black")
            bobstacle.speed(goalspeed1)
            renktutucu=1
        else:
            bobstacle.color("red")
            bobstacle.speed(goalspeed1)
            renktutucu=2
        bobstacle.setposition(random.randint(100,500),+360)   
            
    if bobstacle2.ycor()<-350:
        bobstacle2.speed(500)
        bobstacle2.color("lightblue")
        
        kontrol2=random.randint(0,10)
        if(kontrol2<=7):
            bobstacle2.color("white")
            bobstacle2.speed(goalspeed2)
            renktutucu2=1
        else:
            bobstacle2.color("orange")
            bobstacle2.speed(goalspeed2)
            renktutucu2=2
        bobstacle2.setposition(random.randint(-500,-100),+360)
        
    #Player1'in sınırları geçmesini engelleme
    uzaklık1= math.hypot(player1.xcor()-bobstacle.xcor() ,player1.ycor()-bobstacle.ycor() )
    
    if player1.xcor() > 500 :
        player1.setposition(player1.xcor()-20,player1.ycor())
    if player1.xcor() <100 :
        player1.setposition(player1.xcor()+20,player1.ycor())

        
        
    #Player1'in yemi yeme durumu   
    if(uzaklık1 <20):
            scoreboard.hideturtle()  
            bobstacle.hideturtle()
            if(renktutucu==1):
                system.play("siyahyem.wav")
                score1=score1+1
            elif(renktutucu==2):
               luck1 = random.randint(0,13)
               if(luck1<4):
                   system.play("eksiyem.wav")
                   score1=score1 - 1
               if(luck1<7 and 3<luck1):
                   system.play("kucultme.wav")
                   if(size2 <= 0.5):
                       goalspeed2 = goalspeed2 + 1
                       bobstacle2.speed(goalspeed2)
                   else: 
                       size2 = size2 - 0.25
                       player2.turtlesize(size2)
               if(luck1<10 and 6<luck1):
                   system.play("kuculme.wav")
                   if(size1 <= 0.5):
                       goalspeed1 = goalspeed1 + 1
                       bobstacle.speed(goalspeed1)
                   else: 
                       size1 = size1 - 0.25
                       player1.turtlesize(size1)
               if(luck1<13 and 9<luck1):
                   system.play("ikiyem.wav")
                   score1 = score1 + 2
            bobstacle.speed(500)
            bobstacle.color("lightblue")
            bobstacle.setposition(random.randint(100,500),-399)
            bobstacle.showturtle()
            scoreboard.clear()
            scoreboard.write("Score P1:{}   Score P2:{}".format(score1,score2),font=FONT)
               
    
    #Player2'nin sınırları geçmesinin engellenmesi
    uzaklık2= math.hypot(player2.xcor()-bobstacle2.xcor() ,player2.ycor()-bobstacle2.ycor() )
    
    if player2.xcor() > -100 :
        player2.setposition(player2.xcor()-20,player2.ycor())
    if player2.xcor() <-500 :
        player2.setposition(player2.xcor()+20,player2.ycor())
    
    
    
    
    #Player2'nin yemi yeme durumu
    if(uzaklık2<20):
        scoreboard.hideturtle()
        bobstacle2.hideturtle()
        if(renktutucu2==1):
            system.play("beyazyem.wav")
            score2=score2+1
        elif(renktutucu2==2):
           luck2 = random.randint(0,13)
           if(luck2<4):
               system.play("eksiyem.wav")
               score2=score2 - 1
           if(luck2<7 and 3<luck2):
               system.play("kucultme.wav")
               if(size1 <= 0.5):
                   goalspeed1 = goalspeed1 + 1
                   bobstacle.speed(goalspeed1)
               else: 
                   size1 = size1 - 0.25
                   player1.turtlesize(size1)
           if(luck2<10 and 6<luck2):
               system.play("kuculme.wav")
               if(size2 <= 0.5):
                   goalspeed2 = goalspeed2 + 1
                   bobstacle2.speed(golaspeed2)
               else:
                   size2 = size2 - 0.25
                   player2.turtlesize(size2)
           if(luck2<13 and 9<luck2):
               system.play("ikiyem.wav")
               score2 = score2 + 2
        bobstacle2.speed(500)
        bobstacle2.color("lightblue")
        bobstacle2.setposition(random.randint(-500,-100),-399)
        bobstacle2.showturtle()    
        scoreboard.clear()
        scoreboard.write("Score P1:{}   Score P2:{}".format(score1,score2),font=FONT)
        
    #Oyunun bitme durumu    
    if(score1>=20):
        system.play("oyunbitis.wav")
        info.clear()
        info.write("   OYUN BİTTİ",font=FONTFINISH)
        scoreboard.clear()
        scoreboard.write("Score P1:{}   Score P2:{}\nP1 KAZANDI\nMÜKEMMELSİN!!".format(score1,score2),font=FONTFINISH)
        break
    if(score2>=20):
        system.play("oyunbitis.wav")
        info.clear()
        info.write("   OYUN BİTTİ",font=FONTFINISH)
        scoreboard.clear()
        scoreboard.write("Score P1:{}   Score P2:{}\nP2 KAZANDI\nMÜKEMMELSİN!!".format(score1,score2),font=FONTFINISH)
        break