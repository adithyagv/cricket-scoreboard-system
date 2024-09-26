use ipl;
 CREATE TABLE CSK_SQUAD(BATTING_POSITION int,PLAYER_NAME varchar(255),ROLE 
varchar(255),BATTING_STYLE varchar(255));
 INSERT INTO CSK_SQUAD VALUES(1,'RUTURAJ GAIKWAD','BATSMAN','RIGHT HAND'),(2,'FAF DU 
PLESSIS','BATSMAN','RIGHT'),(3,'MOEEN ALI','ALL ROUNDER','LEFT'),(4,'SURESH 
RAINA','BATSMAN','LEFT'),(5,'AMBATI RAYUDU','BATSMAN','RIGHT'),(6,'MS 
DHONI','CAPTAIN/WICKET KEEPER','RIGHT'),(7,'RAVINDRA JADEJA','ALL ROUNDER','LEFT'),(8,'SAM 
CURRAN','ALL ROUNDER','LEFT'),(9,'DWAYNE BRAVO','ALL ROUNDER','RIGHT'),(10,'SHARDUL 
THAKUR','BOWLER','RIGHT'),(11,'DEEPAK CHAHAR','BOWLER','RIGHT');
 select * from csk_squad;
 CREATE TABLE MI_SQUAD(BATTING_POSITION int,PLAYER_NAME varchar(255),ROLE 
varchar(255),BATTING_STYLE varchar(255));
 INSERT INTO MI_SQUAD VALUES(1,'ROHIT SHARMA','CAPTAIN/BATSMAN','RIGHT'),(2,'QUINTON DE 
KOCK','WICKET KEEPER','LEFT'),(3,'SURYAKUMAR YADAV','BATSMAN','RIGHT'),(4,'ISHAN 
KISHAN','BATSMAN','LEFT'),(5,'KIERON POLLARD','ALL ROUNDER','RIGHT'),(6,'HARDIK PANDYA','ALL 
ROUNDER','RIGHT'),(7,'KRUNAL PANDYA','ALL ROUNDER','LEFT'),(8,'COULTER 
NILE','BOWLER','RIGHT'),(9,'TRENT BOULT','BOWLER','RIGHT'),(10,'JASPRIT 
BUMRAH','BOWLER','RIGHT'),(11,'RAHUL CHAHAR','BOWLER','RIGHT');
 select * from mi_squad;
 CREATE TABLE PLAYER_STATS_CSK(MATCHES_PLAYED int,POSITION int,PLAYER_NAME 
varchar(255),NO_OF_RUNS int,HIGH_SCORE int,STRIKE_RATE int,NO_OF_WICKETS 
INT,BEST_BOWLING_FIGURE int,ECONOMY int);
 INSERT INTO PLAYER_STATS_CSK VALUES(22,1,'RUTURAJ 
GAIKWAD',839,101,132.13,0,0,0),(100,2,'FAF DU PLESSIS',2935,96,131.09,0,0/16,16.0),(34,3,'MOEEN 
ALI',666,66,146.37,16,3/7,6.85),(205,4,'SURESH 
RAINA',5528,100,136.73,25,2/0,7.39),(175,5,'AMBATI RAYUDU',3916,100,127.47,0,0,0),(220,6,'MS 
DHONI(C)',4746,84,135.83,0,0,0),(200,7,'RAVINDRA 
JADEJA',2386,62,128.14,127,5/16,7.61),(32,8,'SAM 
CURRAN',337,55,149.78,32,4/11,9.21),(151,9,'DWAYNE 
BRAVO',1537,70,130.25,167,4/22,8.36),(61,10,'SHARDUL 
THAKUR',53,15,112.7,67,3/19,8.89),(63,11,'DEEPAK CHAHAR',79,39,138.6,59,4/13,7.8);
 select * from player_stats_csk;
 INSERT INTO PLAYER_STATS_MI VALUES(213,1,'ROHIT SHARMA',5611,109,130.4,15,0,8.2), 
(77,2,'QUINTON DE KOCK',2256,108,130.6,0,0,0), (115,3,'SURYAKUMAR 
YADAV',2341,82,135.41,0,0,0), (61,4,'ISHAN KISHAN',1452,99,136.34,0,0,0), (178,5,'KIERON 
POLLARD',3268,87,149.89,65,4/44,8.78), (92,6,'HARDIK PANDYA',1476,91,153.91,42,3/20,9.07), 
(84,7,'KRUNAL PANDYA',1143,86,138.55,51,3/14,7.37), (38,8,'COULTER 
NILE',81,24,115.7,48,4/41,7.52), (62,9,'TRENT BOULT',13,6,68.6,76,4/18,8.4), (106,10,'JASPRIT 
BUMRAH',56,16,96.6,130,4/14,7.42), (42,11,'RAHUL CHAHAR',31,10,96.8,43,4/27,7.45);
 SELECT * FROM PLAYER_STATS_MI;
#match preview
 team1=input("enter team name:")
 team2=input("enter team name:")
 print("IPL 2022")
 print(team1 ,'VS', team2)
 print("Date:29/03/2022")
 print("Match number:12")
 print("Venue:Chennai,MAC")
 print("Match timing:7:30pm")
 print("Pitch Report:Its a green grassy pitch.Good wicket to bat upon.Expecting a thrilling match")
 print("Commentator: Harsha Bhogle,Danny Morrison,Ian Bishop")
#Code for toss
 result=int(input("enter result no:"))#if team1 win=0:if team2 wins=1
 toss=int(input("enter the toss no:"))
 if result==0:
    print(team1,"won the toss")
 elif toss==0:
    print("chose to bat")
 else:
    print("chose to field")
 if result==1:
    print(team2,"won the toss")
 elif toss==0:
    print("chose to bat")
 else:
    print("chose to field")
 #Code for csk squad
 print("1st innings")
 print(team1,"batting squad")
 lst=[]
 for i in range(11):
    x=input("Enter The Player Name:")#entering the player's name
    v=input("Enter The Position")#enter the player's role/positon eg: 
batsmen,bowler,allrounder,wicket keeper.etc
    if v=="0":#if player is batsmen enter 0
        v1="Batsmen"
    elif v=="1":#if player is allrounder enter 1
        v1="Allrounder"
    elif v=="2":#if player is bowler enter 2
        v1="Bowler"
    elif v=="3":#if player is wicket keeper enter 3
        v1="Wicket Keeper"
    k=input("Right Hand Or Left Hand")
    if k =="r":
        z="Right Hand"
    else:
        z="Left Hand"
    lst.append(x+"("+v1+","+z+")")
 print(team1,"Playing XI squad:",lst)
 tc=input("Enter the team captain")
 print(team1,"captain :",tc)
 #Code for runs
 import random
 print(" Batting scorecard:")
 print(lst[0],":")#Assuming player 1 has played 3 balls
 x=random.randint(0,6)
 print(x)
 y=random.randint(0,6)
 print(y)
 z=0
 print(z,"Thats OUT!!")
 total=x+y+z
 print(total,"off 3 balls")
 print("strike rate:",total/3*100)
 if total<10:
    print("A short struggling innings comes to an end")
 else:
    print("The batter is gone so quick but has added sufficient runs on the board")
 print(lst[1],":")#Assuming player 2 has played 5 balls
x=random.randint(0,6)
 print(x)
 y=random.randint(0,6)
 print(y)
 z=random.randint(0,6)
 print(z)
 m=random.randint(0,6)
 print(m)
 n=0
 print(n,"Thats OUT!!")
 total1=x+y+z+m+n
 print(total1,"off 5 balls")
 print("strike rate:",total1/5*100)
 if total<10:
    print("A short struggling innings comes to an end")
 elif total>10:
    print("The batter is gone so quick but has added sufficient runs on the board")
 else:
    print("Great innings comes to an end")
 print(lst[2],":")#Assuming player 3 has played 25 balls
 x=random.randint(0,6)
 print(x)
 y=random.randint(0,6)
 print(y)
 z=random.randint(0,6)
 print(z)
 m=random.randint(0,6)
 print(m)
 n=random.randint(0,6)
 print(n)
a=random.randint(0,6)
 print(a)
 b=random.randint(0,6)
 print(b)
 c=random.randint(0,6)
 print(c)
 d=random.randint(0,6)
 print(d)
 e=random.randint(0,6)
 print(e)
 f=random.randint(0,6)
 print(f)
 g=random.randint(0,6)
 print(g)
 h=random.randint(0,6)
 print(h)
 i=random.randint(0,6)
 print(i)
 j=random.randint(0,6)
 print(j)
 k=random.randint(0,6)
 print(k)
 l=random.randint(0,6)
 print(l)
 o=random.randint(0,6)
 print(o)
 p=random.randint(0,6)
 print(p)
 q=random.randint(0,6)
 print(q)
 r=random.randint(0,6)
print(r)
 s=random.randint(0,6)
 print(s)
 t=random.randint(0,6)
 print(t)
 u=random.randint(0,6)
 print(u)
 v=0
 print(v,"Thats OUT")
 total2=x+y+z+m+n+a+b+c+d+e+f+g+h+i+j+k+l+o+p+q+r+s+t+u+v
 print(total2,"off 25 balls")
 print("strike rate:",total2/25*100)
 if total<25:
    print("A short struggling innings comes to an end")
 elif total<50:
    print("The batter is gone so quick but has added sufficient runs on the board")
 else:
    print("Extroadinary innings comes to an end")
 print(lst[3],":")#Assuming player 4 has played 25 balls
 x=random.randint(0,6)
 print(x)
 y=random.randint(0,6)
 print(y)
 z=random.randint(0,6)
 print(z)
 m=random.randint(0,6)
 print(m)
 n=random.randint(0,6)
 print(n)
 a=random.randint(0,6)
print(a)
 b=random.randint(0,6)
 print(b)
 c=random.randint(0,6)
 print(c)
 d=random.randint(0,6)
 print(d)
 e=random.randint(0,6)
 print(e)
 f=random.randint(0,6)
 print(f)
 g=random.randint(0,6)
 print(g)
 h=random.randint(0,6)
 print(h)
 i=random.randint(0,6)
 print(i)
 j=random.randint(0,6)
 print(j)
 k=random.randint(0,6)
 print(k)
 l=random.randint(0,6)
 print(l)
 o=random.randint(0,6)
 print(o)
 p=random.randint(0,6)
 print(p)
 q=random.randint(0,6)
 print(q)
 r=random.randint(0,6)
 print(r)
s=random.randint(0,6)
 print(s)
 t=random.randint(0,6)
 print(t)
 u=random.randint(0,6)
 print(u)
 v=0
 print(v,"Thats OUT!!")
 total3=x+y+z+m+n+a+b+c+d+e+f+g+h+i+j+k+l+o+p+q+r+s+t+u+v
 print(total3,"*off 25 balls")
 print("strike rate:",total3/25*100)
 if total<25:
    print("A short struggling innings comes to an end")
 elif total<50:
    print("The batter is gone so quick but has added sufficient runs on the board")
 else:
    print("Scintillating stuff from the batsman. What a brilliant knock!!")
 print(lst[4],":")#Assuming player 5 has played 25 balls
 x=random.randint(0,6)
 print(x)
 y=random.randint(0,6)
 print(y)
 z=random.randint(0,6)
 print(z)
 m=random.randint(0,6)
 print(m)
 n=random.randint(0,6)
 print(n)
 a=random.randint(0,6)
 print(a)
b=random.randint(0,6)
 print(b)
 c=random.randint(0,6)
 print(c)
 d=random.randint(0,6)
 print(d)
 e=random.randint(0,6)
 print(e)
 f=random.randint(0,6)
 print(f)
 g=random.randint(0,6)
 print(g)
 h=random.randint(0,6)
 print(h)
 i=random.randint(0,6)
 print(i)
 j=random.randint(0,6)
 print(j)
 k=random.randint(0,6)
 print(k)
 l=random.randint(0,6)
 print(l)
 o=random.randint(0,6)
 print(o)
 p=random.randint(0,6)
 print(p)
 q=random.randint(0,6)
 print(q)
 r=random.randint(0,6)
 print(r)
 s=random.randint(0,6)
print(s)
 t=random.randint(0,6)
 print(t)
 u=random.randint(0,6)
 print(u)
 v=0
 print(v,"THats OUT")
 total4=x+y+z+m+n+a+b+c+d+e+f+g+h+i+j+k+l+o+p+q+r+s+t+u+v
 print(total4,"off 25 balls")
 print("strike rate:",total4/25*100)
 if total<25:
    print("A short struggling innings comes to an end")
 elif total<50:
    print("The batter is gone so quick but has added sufficient runs on the board")
 else:
    print("Extroadinary innings comes to an end")
 print(lst[5],":")#Assuming player 6 has played 20 balls
 x=random.randint(0,6)
 print(x)
 y=random.randint(0,6)
 print(y)
 z=random.randint(0,6)
 print(z)
 m=random.randint(0,6)
 print(m)
 n=random.randint(0,6)
 print(n)
 a=random.randint(0,6)
 print(a)
 b=random.randint(0,6)
print(b)
 c=random.randint(0,6)
 print(c)
 d=random.randint(0,6)
 print(d)
 e=random.randint(0,6)
 print(e)
 f=random.randint(0,6)
 print(f)
 g=random.randint(0,6)
 print(g)
 h=random.randint(0,6)
 print(h)
 i=random.randint(0,6)
 print(i)
 j=random.randint(0,6)
 print(j)
 p=random.randint(0,6)
 print(p)
 k=random.randint(0,6)
 print(k)
 l=random.randint(0,6)
 print(l)
 o=random.randint(0,6)
 print(o)
 p=random.randint(0,6)
 print(p)
 q=0
 print(q,"Thats OUT")
 total5=x+y+z+m+n+a+b+c+d+e+f+g+h+i+j+k+l+o+p+q
 print(total5,"off 20 balls")
print("strike rate:",total5/20*100)
 if total<25:
    print("A short struggling innings comes to an end")
 elif total<45:
    print("The batter is gone so quick but has added sufficient runs on the board")
 else:
    print("Extroadinary innings comes to an end")
 print(lst[6],":")#Assuming player 7 has played 17 balls
 a=random.randint(0,6)
 print(a)
 b=random.randint(0,6)
 print(b)
 c=random.randint(0,6)
 print(c)
 d=random.randint(0,6)
 print(d)
 e=random.randint(0,6)
 print(e)
 f=random.randint(0,6)
 print(f)
 g=random.randint(0,6)
 print(g)
 h=random.randint(0,6)
 print(h)
 i=random.randint(0,6)
 print(i)
 j=random.randint(0,6)
 print(j)
 p=random.randint(0,6)
print(p)
 k=random.randint(0,6)
 print(k)
 l=0
 print(l,"Thats OUT")
 total6=x+y+z+m+n+a+b+c+d+e+f+g+h+i+j+k+l
 print(total6,"*off 17 balls")
 print("strike rate:",total6/17*100)
 if total<25:
    print("A short struggling innings comes to an end")
 elif total<50:
    print("The batter is gone so quick but has added sufficient runs on the board")
 else:
    print("That was a run feast at chennai.An extended cameo added sufficient runs on the board for 
csk.")
 target=total+total1+total2+total3+total4+total5+total6
 print(team1,":",target,"-5")
 print("target:",target,"needed from 120 balls")
 #code for bowling
 print(team2,"bowling squad")
 lst1=[]
 for i in range(5):
    x1=input("Enter The Player Name:")#entering the player's name
    v1=input("Enter The Position")#enter the player's role/positon eg:spin or fast bowler
    if v1 =="1":
        z="Spinner"
    else:
        z="Pacer"
    lst1.append(x1+":"+z)
print(team2,lst1)
 #code for wickets       
import random
 print("Bowling scorecard:")
 lst2=[]
 for i in range(5):
    x=input("bowlers name")
    y=input("wickets taken")
    lst2.append(x+"-4-"+y)
 print(lst2)
 #Code for mi squad
 print(team2,"squad")
 lst=[]
 for i in range(11):
    x=input("Enter The Player Name:")#entering the player's name
    v=input("Enter The Position")#enter the player's role/positon eg: 
batsmen,bowler,allrounder,wicket keeper.etc
    if v=="0":#if player is batsmen enter 0
        v1="Batsmen"
    elif v=="1":#if player is allrounder enter 1
        v1="Allrounder"
    elif v=="2":#if player is bowler enter 2
        v1="Bowler"
    elif v=="3":#if player is wicket keeper enter 3
        v1="Wicket Keeper"
    k=input("Right Hand Or Left Hand")
    if k =="r":
        z="Right Hand"
    else:
        z="Left Hand"
    lst.append(x+"("+v1+","+z+")")
 print(team1,"Playing XI squad:",lst)
 tc=input("Enter the team captain")
 print(team1,"captain :",tc)
 #Code for runs
 print("2nd innings")
 import random
 print(" Batting scorecard:")
 print(lst[0],":")#Assuming player 1 has played 3 balls
 x=random.randint(0,6)
 print(x)
 y=random.randint(0,6)
 print(y)
 z=0
 print(z,"Thats OUT!!")
 total=x+y+z
 print(total,"off 3 balls")
 print("strike rate:",total/3*100)
 if total<10:
    print("A short struggling innings comes to an end")
 else:
    print("The batter is gone so quick but has added sufficient runs on the board")
 print(lst[0],"bowled by chahar")
print(lst[1],":")#Assuming player 2 has played 5 balls
 x=random.randint(0,6)
 print(x)
 y=random.randint(0,6)
 print(y)
 z=random.randint(0,6)
 print(z)
 m=random.randint(0,6)
 print(m)
 n=0
 print(n,"Thats OUT!!")
 total1=x+y+z+m+n
 print(total1,"off 5 balls")
 print("strike rate:",total1/5*100)
 if total<10:
    print("A short struggling innings comes to an end")
 else:
    print("The batter is gone so quick but has added sufficient runs on the board")
 print(lst[2],":")#Assuming player 3 has played 10 balls
 x=random.randint(0,6)
 print(x)
 y=random.randint(0,6)
 print(y)
 z=random.randint(0,6)
 print(z)
 m=random.randint(0,6)
 print(m)
 n=random.randint(0,6)
 print(n)
a=random.randint(0,6)
 print(a)
 b=random.randint(0,6)
 print(b)
 c=random.randint(0,6)
 print(c)
 d=random.randint(0,6)
 print(d)
 e=0
 print(e,"Thats OUT!!")
 total2=x+y+z+m+n+a+b+c+d+e
 print(total2,"off 10 balls")
 print("strike rate:",total2/10*100)
 if total<15:
    print("A short struggling innings comes to an end")
 elif total<35:
    print("The batter is gone so quick but has added sufficient runs on the board")
 else:
    print("Extroadinary innings comes to an end")
 print(lst[3],":")#Assuming player 4 has played 20 balls
 x=random.randint(0,6)
 print(x)
 y=random.randint(0,6)
 print(y)
 z=random.randint(0,6)
 print(z)
 m=random.randint(0,6)
 print(m)
 n=random.randint(0,6)
 print(n)
a=random.randint(0,6)
 print(a)
 b=random.randint(0,6)
 print(b)
 c=random.randint(0,6)
 print(c)
 d=random.randint(0,6)
 print(d)
 e=random.randint(0,6)
 print(e)
 f=random.randint(0,6)
 print(f)
 g=random.randint(0,6)
 print(g)
 h=random.randint(0,6)
 print(h)
 i=random.randint(0,6)
 print(i)
 j=random.randint(0,6)
 print(j)
 k=random.randint(0,6)
 print(k)
 l=random.randint(0,6)
 print(l)
 o=random.randint(0,6)
 print(o)
 p=random.randint(0,6)
 print(p)
 q=0
 print(q,"Thats OUT!!")
 total3=x+y+z+m+n+a+b+c+d+e+f+g+h+i+j+k+l+o+p+q
print(total3,"off 20 balls")
 print("strike rate:",total3/20*100)
 if total<25:
    print("A short struggling innings comes to an end")
 elif total<55:
    print("The batter is gone so quick but has added sufficient runs on the board")
 else:
    print("Scintillating stuff from the batsman. What a brilliant knock!!")
 print(lst[4],":")#Assuming player 5 has played 25 balls
 x=random.randint(0,6)
 print(x)
 y=random.randint(0,6)
 print(y)
 z=random.randint(0,6)
 print(z)
 m=random.randint(0,6)
 print(m)
 n=random.randint(0,6)
 print(n)
 a=random.randint(0,6)
 print(a)
 b=random.randint(0,6)
 print(b)
 c=random.randint(0,6)
 print(c)
 d=random.randint(0,6)
 print(d)
 e=random.randint(0,6)
 print(e)
 f=random.randint(0,6)
print(f)
 g=random.randint(0,6)
 print(g)
 h=random.randint(0,6)
 print(h)
 i=random.randint(0,6)
 print(i)
 j=random.randint(0,6)
 print(j)
 k=random.randint(0,6)
 print(k)
 l=random.randint(0,6)
 print(l)
 o=random.randint(0,6)
 print(o)
 p=random.randint(0,6)
 print(p)
 q=random.randint(0,6)
 print(q)
 r=random.randint(0,6)
 print(r)
 s=random.randint(0,6)
 print(s)
 t=random.randint(0,6)
 print(t)
 u=random.randint(0,6)
 print(u)
 v=0
 print(v,"Thats OUT!!")
 total4=x+y+z+m+n+a+b+c+d+e+f+g+h+i+j+k+l+o+p+q+r+s+t+u+v
 print(total4,"off 25 balls")
print("strike rate:",total4/25*100)
 if total<25:
    print("A short struggling innings comes to an end")
 elif total<50:
    print("The batter is gone so quick but has added sufficient runs on the board")
 else:
    print("Extroadinary innings comes to an end")
 print(lst[5],":")#Assuming player 6 has played 15 balls
 x=random.randint(0,6)
 print(x)
 y=random.randint(0,6)
 print(y)
 z=random.randint(0,6)
 print(z)
 m=random.randint(0,6)
 print(m)
 n=random.randint(0,6)
 print(n)
 a=random.randint(0,6)
 print(a)
 b=random.randint(0,6)
 print(b)
 c=random.randint(0,6)
 print(c)
 d=random.randint(0,6)
 print(d)
 e=random.randint(0,6)
 print(e)
 f=random.randint(0,6)
 print(f)
g=random.randint(0,6)
 print(g)
 h=random.randint(0,6)
 print(h)
 i=random.randint(0,6)
 print(i)
 j=0
 print(j,"Thats OUT!!")
 total5=x+y+z+m+n+a+b+c+d+e+f+g+h+i+j
 print(total5,"off 15 balls")
 print("strike rate:",total5/15*100)
 if total<25:
    print("A short struggling innings comes to an end")
 elif total<45:
    print("The batter is gone so quick but has added sufficient runs on the board")
 else:
    print("Extroadinary innings comes to an end")
 print(lst[6],":")#Assuming player 7 has played 10 balls
 a=random.randint(0,6)
 print(a)
 b=random.randint(0,6)
 print(b)
 c=random.randint(0,6)
 print(c)
 d=random.randint(0,6)
 print(d)
 e=random.randint(0,6)
 print(e)
 f=random.randint(0,6)
print(f)
 g=random.randint(0,6)
 print(g)
 h=random.randint(0,6)
 print(h)
 i=random.randint(0,6)
 print(i)
 j=0
 print(j,"Thats OUT!!")
 total6=a+b+c+d+e+f+g+h+i+j
 print(total6,"off 10 balls")
 print("strike rate:",total6/10*100)
 if total<15:
    print("A short struggling innings comes to an end")
 else:
    print("The batter is gone so quick but has added sufficient runs on the board")
 print(lst[7],":")#Assuming player 8 has played 10 balls
 a=random.randint(0,6)
 print(a)
 b=random.randint(0,6)
 print(b)
 c=random.randint(0,6)
 print(c)
 d=random.randint(0,6)
 print(d)
 e=random.randint(0,6)
 print(e)
 f=random.randint(0,6)
 print(f)
 g=random.randint(0,6)
print(g)
 h=random.randint(0,6)
 print(h)
 i=random.randint(0,6)
 print(i)
 j=0
 print(j,"Thats OUT!!")
 total7=a+b+c+d+e+f+g+h+i+j
 print(total7,"off 10 balls")
 print("strike rate:",total6/10*100)
 if total<15:
    print("A short struggling innings comes to an end")
 else:
    print("The batter is gone so quick but has added sufficient runs on the board")
 print(lst[8],":")#Assuming player 9 has played 10 balls
 a=random.randint(0,6)
 print(a)
 b=random.randint(0,6)
 print(b)
 c=random.randint(0,6)
 print(c)
 d=random.randint(0,6)
 print(d)
 e=random.randint(0,6)
 print(e)
 f=random.randint(0,6)
 print(f)
 g=random.randint(0,6)
 print(g)
 h=random.randint(0,6)
print(h)
 i=random.randint(0,6)
 print(i)
 j=0
 print(j,"Thats OUT!!")
 total8=a+b+c+d+e+f+g+h+i+j
 print(total8,"off 10 balls")
 print("strike rate:",total8/10*100)
 if total<15:
    print("A short struggling innings comes to an end")
 else:
    print("The batter is gone so quick but has added sufficient runs on the board")
 print(lst[9],":")#Assuming player 10 has played 5 balls
 a=random.randint(0,6)
 print(a)
 b=random.randint(0,6)
 print(b)
 c=random.randint(0,6)
 print(c)
 d=random.randint(0,6)
 print(d)
 e=0
 print(e,"Thats OUT!!")
 total9=a+b+c+d+e
 print(total9,"*off 5 balls")
 print("strike rate:",total9/5*100)
 if total<15:
    print("A short struggling innings comes to an end")
 else:
    print("The batter is gone so quick but has added sufficient runs on the board")
print(lst[10],":")#Assuming player 11 has played 5 balls
 a=random.randint(0,6)
 print(a)
 b=random.randint(0,6)
 print(b)
 c=random.randint(0,6)
 print(c)
 d=random.randint(0,6)
 print(d)
 e=0
 print(e,"Thats OUT!!")
 total10=a+b+c+d+e
 print(total10,"*off 5 balls")
 print("strike rate:",total10/5*100)
 if total<15:
    print("A short struggling innings comes to an end")
 else:
    print("The batter is gone so quick but has added sufficient runs on the board")
 #code for bowling
 print(team1,"squad")
 lst1=[]
 for i in range(5):
    x1=input("Enter The Player Name:")#entering the player's name
    v1=input("Enter The Position")#enter the player's role/positon eg:spin or fast bowler
    if v1 =="1":
        z="Spinner"
    else:
        z="Pacer"
    lst1.append(x1+":"+z)
 print(team2,lst1)
 #code for wickets       
import random
 print("Bowling scorecard:")
 lst2=[]
 for i in range(5):
    x=input("bowlers name")
    y=input("wickets taken")
    lst2.append(x+"-4-"+y)
 print(lst2)
 #code for post-match presentation
 print('''Rohit Sharma|Losing captain:
 We must have got a partnership.
 You can do a lot of things differently in hindsight.
 Losing by such runs, I think that is the difference.
 Gave too many with the ball at the end.
 Their batters tried to continue the momentum throughout, we didn't do that.
 We could have learnt from their mistake of losing too many wickets in the powerplay.
 We needed one guy to bat deep. We had a couple of soft dismissals. We can't let that happen at this 
level.\n\n''')#losing captain speech
 print('''MS Dhoni | WInning captain:
 I think , you want to get something respectable on the board and Ruturaj and Bravo got us more 
than what we expected.
We had to bat exceptionally to get to desired target on board, but to get to more than expecting was 
tremendous.
 The wicket was slightly two-paced and slow to start off with.
 Most of them got out to the slowness. If you come later and you want to go hard and that's why we 
lost wickets.
 I would have tried to get into the eighth or ninth over and then take it from there.
 You always think you could have gone harder earlier, but with wickets down, it was a risk.
 There's always a catch, one batter played till the end and the others contributed well.
 It's a give and take, you need to see how many fast bowlers have in the armoury and how much time 
they take to bowl their overs.
 If a fast bowler has a long run-up or wastes a lot of time, it is tough for the captains. It depends on 
the situation.\n\n''')#winning captain speech
 print('''Ruturaj Gaikwad | MoM:
 Obviously one of my crucial innings till now.
 With the pressure of early wickets and with the seniors in the dressing room, I just had to grind and 
get the team to possible maximum score.
 When Mahi bhai is around and with the CSK management, once they back you, you don't have to 
think much.
 The SL tour and the preparation coming here did help too.
 Initially the ball was seaming and swinging so I had to take my chance against the spinners and it 
came off well.\n\n''')#man of the match player speech
 print('''Harsha Bhogle:Find yourself a commitment of the magnitude that Mumbai have with losing 
season openers.
 Mind you, this was no opener, but for the sake of history and memes, they've still lost.
 CSK are predominantly a bunch of aged former legends and it clearly doesn't suit their style to play 
on a grassy deck,
 and they have broken out of jail today, but nevertheless, two points are two points.
 So this is me,Harsha Bhogle , signing off on behalf of Danny Morrison,Ian Bishop, Ramakrishnan MS 
and our scorer Siva.
 Until tomorrow, ta ta!\n\n''')#commentator's signing off
