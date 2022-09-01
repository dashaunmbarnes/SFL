

import replit
import time
import random
import math
yg=0
score1=0
score2=0
#stats d players
#tackles,sacks,interceptions,tfl
lb1s=[0,0,0,0]
dl1s=[0,0,0,0]
cb1s=[0,0,0,0]
s1s=[0,0,0,0]
lb2s=[0,0,0,0]
dl2s=[0,0,0,0]
cb2s=[0,0,0,0]
s2s=[0,0,0,0]
#stats wr
#rec,yards
wr11s=[0,0]
wr12s=[0,0]
wr21s=[0,0]
wr22s=[0,0]
#stats rb
#carries,yards
rb1s=[0,0]
rb2s=[0,0]
#stats qb
#attempts,completions,yards
qb1s=[0,0,0]
qb2s=[0,0,0]
#comletions,attmepts,yards, touchdowns,
#position numbering
#QB,OL,RB,WR1,WR2,MLB,DL,CB1,CB2,s
#check if players have drafted positions 1
simp=0
fn=104
ln=102
qbd1=0
old1=0
rbd1=0
wr1d1=0
wr2d1=0
lbd1=0
dld1=0
cb1d1=0
cb2d1=0
sd1=0
#check if players have drafted positions 2
qbd2=0
old2=0
rbd2=0
wr1d2=0
wr2d2=0
lbd2=0
dld2=0
cb1d2=0
cb2d2=0
sd2=0
#attributes for player1
T1A=[]
qb1=[""]
ol1=[""]
rb1=[""]
wr11=[""]
wr12=[""]
lb1=[""]
dl1=[""]
cb11=[""]
cb12=[""]
s1=[""]
#attributes for player2
T2A=[]
qb2=[""]
ol2=[""]
rb2=[""]
wr21=[""]
wr22=[""]
lb2=[""]
dl2=[""]
cb21=[""]
cb22=[""]
s2=[""]

if 0==0:
  LOFN=["Marlon","Derek","Hasaan","Myles","Jimbo","Chris","Devin","Mikal","Cameron","Lebron","Anthony","Malik","Austin","Mac","Dwight","Kevin","Kyrie","Andre","Joe","Ben","Seth","Cam","Goran","Lamelo","Miles","PJ","Kelly","Gordon","Vernon","Mason","Kyle","Jimmy","Tyler","Udonis","Bam","Ja","Jaren","Desmond","Tyus","De'Anthony","Trae","Clint","Cade","Onyeka","Sharife","De'Andre","Lou","Jayson","Jaylen","Robert","Salah","Al","Marus","Juwan","Demar","Zach","Lonzo","Javonte","Ayo","Patrick","Ayo","Devonte","Kira","Zion","Jared","Naji","Keldon","Dontavious","Demarcus","Tredavious","Dashaun","Mekhi","Orlando","Pascal","OG","Khem","Armoni","Malachi","Chris","Donovan","Octavion","Mike","Eric","Xavier","Udoka","Shai","Tre","Isiah","Darius","Lugentz","Derrick","Jeremiah","Theo","RJ","CJ","Bol","ZJ","AJ","Mohamed","Robin","Marquese","Moses","Sterling","Reggie","Jae'Sean","Daquavious"]
  LOLN=["Lawrence","Chase","Sewell","Pitts","Wilson","Smith","Waddle","Lance","Fields","Farley","Surtain","Slater","Tucker","Harris","Darrisaw","Paye","Parsons","Jones","Horn","Ossai","Jenkins","Hamilton","Hutchinson","Ekwonu","Thibodeaux","Neal","Stingley","Booth","Johnson","Williams","Gardner","Walker","Green","Linderbaum","Wyatt","Lloyd","Cross","Hill","Olave","London","Penning","Dean","Young","Burrow","Okudah","Simmons","Wills","Lamb","Jeudy","Brown","Lipkovich","Wirfs","Chaisson","Thomas","Ruggs","Becton","Henderson","Herbert","Mckinney","Dobbins","Fulton","Kinlaw","Queen","Jefferson","Bosa","Allen","Gary","Sweat","Metcalf","Hockenson","Barnes","Ferrell","Oliver","White","Taylor","Murray","Jacobs","Baker","Wilkins","Dillard","Brown","Bush","Burris","Ford","Harry","Murphy","Ferguson","Sanders","Gomez","Tunsil","Buckner","Goff","Stanley","Billings","Newton","Henry","Elliot","Reed","Butler","Coleman","Cook","Garnett","Veluri"]

print("Welcome to The SFL")
print("(Simulated Football League)")
time.sleep(1.5)
print("Hit enter to continue")
pause=input("")
if pause=="Debug Mode":
  simp=1
replit.clear()
if simp==0:
    #Player 1 creates team
    print("Player 1 Enter the city of your team")
    c1=input("")
    T1A.append(c1)
    replit.clear()
    print("Player 1 Enter the name of your team")
    n1=input("")
    T1A.append(n1)
    replit.clear()
    print("Welcome Player 1 and the",T1A[0],T1A[1])
    time.sleep(1)
    print("Hit enter to continue")
    pause=input("")
    replit.clear()
    #Player 2 creates team
    print("Player 2 Enter the city of your team")
    c2=input("")
    T2A.append(c2)
    replit.clear()
    print("Player 2 Enter the name of your team")
    n2=input("")
    T2A.append(n2)
    replit.clear()
    print("Welcome Player 2 and the",T2A[0],T2A[1])
    time.sleep(1)
    print("Hit enter to continue")
    pause=input("")
    replit.clear()
    #Draft Player 1
    #Round 1
    print("Player 1 Welcome to Round 1 of the Draft")
    print("Hit enter to continue")
    pause=input("Say anything to continue")
    replit.clear()
    sfr=3
    #QB randomized stats
    rnq1=random.randint(85,99)
    rnq2=random.randint(85,99)
    rnq3=random.randint(85,99)
    rnq4=random.randint(85,99)
    rnq5=random.randint(85,99)
    rnq6=random.randint(85,99)
    qbo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnq1+rnq2+rnq3)/3),rnq1,rnq2,rnq3,1]
    qbo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnq4+rnq5+rnq6)/3),rnq4,rnq5,rnq6,2]
    #OL randomized stats
    rnol1=random.randint(85,99)
    rnol2=random.randint(85,99)
    rnol3=random.randint(85,99)
    rnol4=random.randint(85,99)
    olo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnol1+rnol2)/2),rnol1,rnol2,3]
    olo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnol3+rnol4)/2),rnol3,rnol4,4]
    #RB randomized stats
    rnrb1=random.randint(85,99)
    rnrb2=random.randint(85,99)
    rnrb3=random.randint(85,99)
    rnrb4=random.randint(85,99)
    rbo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnrb1+rnrb2)/2),rnrb1,rnrb2,5]
    rbo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnrb3+rnrb4)/2),rnrb3,rnrb4,6]
    #WR randomized stats
    rnwr1=random.randint(85,99)
    rnwr2=random.randint(85,99)
    rnwr3=random.randint(85,99)
    rnwr4=random.randint(85,99)
    wro1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnwr1+rnwr2)/2),rnwr1,rnwr2,7]
    wro2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnwr3+rnwr4)/2),rnwr3,rnwr4,8]
    #MLB randomized stats
    rnlb1=random.randint(85,99)
    rnlb2=random.randint(85,99)
    rnlb3=random.randint(85,99)
    rnlb4=random.randint(85,99)
    rnlb5=random.randint(85,99)
    rnlb6=random.randint(85,99)
    lbo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnlb1+rnlb2+rnlb3)/3),rnlb1,rnlb2,rnlb3,9]
    lbo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnlb4+rnlb5+rnlb6)/3),rnlb4,rnlb5,rnlb6,10]
    #DL randomized stats
    rndl1=random.randint(85,99)
    rndl2=random.randint(85,99)
    rndl3=random.randint(85,99)
    rndl4=random.randint(85,99)
    dlo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rndl1+rndl2)/2),rndl1,rndl2,11]
    dlo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rndl3+rndl4)/2),rndl3,rndl4,12]
    #CB randomized stats
    rncb1=random.randint(85,99)
    rncb2=random.randint(85,99)
    rncb3=random.randint(85,99)
    rncb4=random.randint(85,99)
    cbo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rncb1+rncb2)/2),rncb1,rncb2,13]
    cbo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rncb3+rncb4)/2),rncb3,rncb4,14]
    #S randomized stats
    rns1=random.randint(85,99)
    rns2=random.randint(85,99)
    rns3=random.randint(85,99)
    rns4=random.randint(85,99)
    so1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rns1+rns2)/2),rns1,rns2,15]
    so2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rns3+rns4)/2),rns3,rns4,16]
    #list of all prospects
    blanklist=[]
    lop=[blanklist,qbo1,qbo2,olo1,olo2,rbo1,rbo2,wro1,wro2,lbo1,lbo2,dlo1,dlo2,cbo1,cbo2,so1,so2]
    for item in lop:
      item.append(0)
    while sfr>0:
      print("First Round")
      print("")
      print("Selections Remaining:",sfr)
      print("")
      print(qbo1[0],qbo1[1]+"[QB]","|","overall:",qbo1[2],"|","throwing:",qbo1[3],"|","running:",qbo1[4],"|","iq:",qbo1[5],"|","Draft Number:",qbo1[6],"|")
      print("")
      print(qbo2[0],qbo2[1]+"[QB]","|","overall:",qbo2[2],"|","throwing:",qbo2[3],"|","running:",qbo2[4],"|","iq:",qbo2[5],"|","Draft Number:",qbo2[6],"|")
      print("")
      print(olo1[0],olo1[1]+"[OL]","|","overall:",olo1[2],"|","pass-block:",olo1[3],"|","run-block:",olo1[4],"|","Draft Number:",olo1[5],"|")
      print("")
      print(olo2[0],olo2[1]+"[OL]","|","overall:",olo2[2],"|","pass-block:",olo2[3],"|","run-block:",olo2[4],"|","Draft Number:",olo2[5],"|")
      print("")
      print(rbo1[0],rbo1[1]+"[RB]","|","overall:",rbo1[2],"|","speed:",rbo1[3],"|","power:",rbo1[4],"|","Draft Number:",rbo1[5],"|")
      print("")
      print(rbo2[0],rbo2[1]+"[RB]","|","overall:",rbo2[2],"|","speed:",rbo2[3],"|","power:",rbo2[4],"|","Draft Number:",rbo2[5],"|")
      print("")
      print(wro1[0],wro1[1]+"[WR]","|","overall:",wro1[2],"|","route-running:",wro1[3],"|","catching:",wro1[4],"|","Draft Number:",wro1[5],"|")
      print("")
      print(wro2[0],wro2[1]+"[WR]","|","overall:",wro2[2],"|","route-running:",wro2[3],"|","catching:",wro2[4],"|","Draft Number:",wro2[5],"|")
      print("")
      print(lbo1[0],lbo1[1]+"[LB]","|","overall:",lbo1[2],"|","coverage:",lbo1[3],"|","play-rec:",lbo1[4],"|","run-defense:",lbo1[5],"|","Draft Number:",lbo1[6],"|")
      print("")
      print(lbo2[0],lbo2[1]+"[LB]","|","overall:",lbo2[2],"|","coverage:",lbo2[3],"|","play-rec:",lbo2[4],"|","run-defense:",lbo2[5],"|","Draft Number:",lbo2[6],"|")
      print("")
      print(dlo1[0],dlo1[1]+"[DL]","|","overall:",dlo1[2],"|","pass-rush:",dlo1[3],"|","run-stop:",dlo1[4],"|","Draft Number:",dlo1[5],"|")
      print("")
      print(dlo2[0],dlo2[1]+"[DL]","|","overall:",dlo2[2],"|","pass-rush:",dlo2[3],"|","run-stop:",dlo2[4],"|","Draft Number:",dlo2[5],"|")
      print("")
      print(cbo1[0],cbo1[1]+"[CB]","|","overall:",cbo1[2],"|","coverage:",cbo1[3],"|","catching:",cbo1[4],"|","Draft Number:",cbo1[5],"|")
      print("")
      print(cbo2[0],cbo2[1]+"[CB]","|","overall:",cbo2[2],"|","coverage:",cbo2[3],"|","catching:",cbo2[4],"|","Draft Number:",cbo2[5],"|")
      print("")
      print(so1[0],so1[1]+"[S]","|","overall:",so1[2],"|","play-rec:",so1[3],"|","catching:",so1[4],"|","Draft Number:",so1[5],"|")
      print("")
      print(so2[0],so2[1]+"[S]","|","overall:",so2[2],"|","play-rec:",so2[3],"|","catching:",so2[4],"|","Draft Number:",so2[5],"|")
      print("")
      ds=int(input("Select a Player: "))
      
      if ds>0 and ds<3:
        if qbd1==0:
          qb1=lop[ds]
          qbd1=1
          sfr=sfr-1
          (lop[ds])[7]=1
          
      if ds>2 and ds<5:
        if old1==0:
          ol1=lop[ds]
          old1=1
          sfr=sfr-1
          (lop[ds])[6]=1
      if ds>4 and ds<7:
        if rbd1==0:
          rb1=lop[ds]
          rbd1=1
          sfr=sfr-1
          (lop[ds])[6]=1
      if ds>6 and ds<9:
        if wr1d1==0 and (lop[ds])[6]==0:
          wr11=lop[ds]
          wr1d1=1
          sfr=sfr-1
          (lop[ds])[6]=1
        else:
          if wr2d1==0 and(lop[ds])[6]==0:
            wr12=lop[ds]
            wr2d1=1
            sfr=sfr-1
            (lop[ds])[6]=1
      if ds>8 and ds<11:
        if lbd1==0:
          lb1=lop[ds]
          lbd1=1
          sfr=sfr-1
          (lop[ds])[7]=1
      if ds>10 and ds<13:
        if dld1==0:
          dl1=lop[ds]
          dld1=1
          sfr=sfr-1
          (lop[ds])[6]=1
      if ds>12 and ds<15:
        if cb1d1==0 and (lop[ds])[6]==0:
          cb11=lop[ds]
          cb1d1=1
          sfr=sfr-1
          (lop[ds])[6]=1
        else:
          if cb2d1==0 and(lop[ds])[6]==0:
            cb12=lop[ds]
            cb2d1=1
            sfr=sfr-1
            (lop[ds])[6]=1
      if ds>14 and ds<17:
        if sd1==0:
          s1=lop[ds]
          sd1=1
          sfr=sfr-1
          (lop[ds])[6]=1
      replit.clear()
      dp=""
      if ds>0 and ds<3:
        dp="QB"
      if ds>2 and ds<5:
        dp="OL"
      if ds>4 and ds<7:
        dp="RB"
      if ds>6 and ds<9:
        dp="WR"
      if ds>8 and ds<11:
        dp="LB"
      if ds>10 and ds<13:
        dp="DL"
      if ds>12 and ds<15:
        dp="CB"
      if ds>14 and ds<17:
        dp="S"
      print("Youve drafted",dp,(lop[ds])[0],(lop[ds])[1],"Overall:",(lop[ds])[2])
      ds=0
      pause=input("Say anything to continue")
      replit.clear()
    print("Round 1 Has concluded")
    time.sleep(0.5)
    pause=input("Hit enter to view your Big Board")
    replit.clear()
    #Show QB
    if qb1[0]=="":
      print("QB : N/A")
    else:
      print("QB :",qb1[0],qb1[1],"|","overall:",qb1[2],"|")
    #Show OL
    if ol1[0]=="":
      print("OL : N/A")
    else:
      print("OL: ",ol1[0],ol1[1],"|","overall:",ol1[2],"|")
    #Show RB
    if rb1[0]=="":
      print("RB:  N/A")
    else:
      print("RB: ",rb1[0],rb1[1],"|","overall:",rb1[2],"|")
    #Show WR1
    if wr11[0]=="":
      print("WR1: N/A")
    else:
      print("WR1:",wr11[0],wr11[1],"|","overall:",wr11[2],"|")
    #Show WR2
    if wr12[0]=="":
      print("WR2: N/A")
    else:
      print("WR2:",wr12[0],wr12[1],"|","overall:",wr12[2],"|")
    #Show LB
    if lb1[0]=="":
      print("LB : N/A")
    else:
      print("LB: ",lb1[0],lb1[1],"|","overall:",lb1[2],"|")
    #Show DL
    if dl1[0]=="":
      print("DL:  N/A")
    else:
      print("DL: ",dl1[0],dl1[1],"|","overall:",dl1[2],"|")
    #Show CB1
    if cb11[0]=="":
      print("CB1: N/A")
    else:
      print("CB1:",cb11[0],cb11[1],"|","overall:",cb11[2],"|")  
    #Show CB2
    if cb12[0]=="":
      print("CB2: N/A")
    else:
      print("CB2:",cb12[0],cb12[1],"|","overall:",cb12[2],"|") 
    #Show S
    if s1[0]=="":
      print("S:   N/A")
    else:
      print("S:  ",s1[0],s1[1],"|","overall:",s1[2],"|")
    pause=input("Say anything to continue")
    replit.clear()
    #Round 2
    print("Player 1 Welcome to Round 2 of the Draft")
    print("Hit enter to continue")
    pause=input("Say anything to continue")
    replit.clear()
    sfr=3
    #QB randomized stats
    rnq1=random.randint(75,95)
    rnq2=random.randint(75,95)
    rnq3=random.randint(75,95)
    rnq4=random.randint(65,99)
    rnq5=random.randint(65,99)
    rnq6=random.randint(65,99)
    qbo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnq1+rnq2+rnq3)/3),rnq1,rnq2,rnq3,1]
    qbo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnq4+rnq5+rnq6)/3),rnq4,rnq5,rnq6,2]
    #OL randomized stats
    rnol1=random.randint(75,95)
    rnol2=random.randint(75,95)
    rnol3=random.randint(65,99)
    rnol4=random.randint(65,99)
    olo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnol1+rnol2)/2),rnol1,rnol2,3]
    olo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnol3+rnol4)/2),rnol3,rnol4,4]
    #RB randomized stats
    rnrb1=random.randint(75,95)
    rnrb2=random.randint(75,95)
    rnrb3=random.randint(65,99)
    rnrb4=random.randint(65,99)
    rbo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnrb1+rnrb2)/2),rnrb1,rnrb2,5]
    rbo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnrb3+rnrb4)/2),rnrb3,rnrb4,6]
    #WR randomized stats
    rnwr1=random.randint(75,95)
    rnwr2=random.randint(75,95)
    rnwr3=random.randint(65,99)
    rnwr4=random.randint(65,99)
    wro1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnwr1+rnwr2)/2),rnwr1,rnwr2,7]
    wro2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnwr3+rnwr4)/2),rnwr3,rnwr4,8]
    #MLB randomized stats
    rnlb1=random.randint(75,95)
    rnlb2=random.randint(75,95)
    rnlb3=random.randint(75,95)
    rnlb4=random.randint(65,99)
    rnlb5=random.randint(65,99)
    rnlb6=random.randint(65,99)
    lbo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnlb1+rnlb2+rnlb3)/3),rnlb1,rnlb2,rnlb3,9]
    lbo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnlb4+rnlb5+rnlb6)/3),rnlb4,rnlb5,rnlb6,10]
    #DL randomized stats
    rndl1=random.randint(75,95)
    rndl2=random.randint(75,95)
    rndl3=random.randint(65,99)
    rndl4=random.randint(65,99)
    dlo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rndl1+rndl2)/2),rndl1,rndl2,11]
    dlo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rndl3+rndl4)/2),rndl3,rndl4,12]
    #CB randomized stats
    rncb1=random.randint(75,95)
    rncb2=random.randint(75,95)
    rncb3=random.randint(65,99)
    rncb4=random.randint(65,99)
    cbo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rncb1+rncb2)/2),rncb1,rncb2,13]
    cbo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rncb3+rncb4)/2),rncb3,rncb4,14]
    #S randomized stats
    rns1=random.randint(75,95)
    rns2=random.randint(75,95)
    rns3=random.randint(65,99)
    rns4=random.randint(65,99)
    so1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rns1+rns2)/2),rns1,rns2,15]
    so2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rns3+rns4)/2),rns3,rns4,16]
    #list of all prospects
    blanklist=[]
    lop=[blanklist,qbo1,qbo2,olo1,olo2,rbo1,rbo2,wro1,wro2,lbo1,lbo2,dlo1,dlo2,cbo1,cbo2,so1,so2]
    for item in lop:
      item.append(0)
    while sfr>0:
      print("Second Round")
      print("")
      print("Selections Remaining:",sfr)
      print("")
      print(qbo1[0],qbo1[1]+"[QB]","|","overall:",qbo1[2],"|","throwing:",qbo1[3],"|","running:",qbo1[4],"|","iq:",qbo1[5],"|","Draft Number:",qbo1[6],"|")
      print("")
      print(qbo2[0],qbo2[1]+"[QB]","|","overall:","?","|","throwing:","?","|","running:","?","|","iq:","?","|","Draft Number:",qbo2[6],"|")
      print("")
      print(olo1[0],olo1[1]+"[OL]","|","overall:",olo1[2],"|","pass-block:",olo1[3],"|","run-block:",olo1[4],"|","Draft Number:",olo1[5],"|")
      print("")
      print(olo2[0],olo2[1]+"[OL]","|","overall:","?","|","pass-block:","?","|","run-block:","?","|","Draft Number:",olo2[5],"|")
      print("")
      print(rbo1[0],rbo1[1]+"[RB]","|","overall:",rbo1[2],"|","speed:",rbo1[3],"|","power:",rbo1[4],"|","Draft Number:",rbo1[5],"|")
      print("")
      print(rbo2[0],rbo2[1]+"[RB]","|","overall:","?","|","speed:","?","|","power:","?","|","Draft Number:",rbo2[5],"|")
      print("")
      print(wro1[0],wro1[1]+"[WR]","|","overall:",wro1[2],"|","route-running:",wro1[3],"|","catching:",wro1[4],"|","Draft Number:",wro1[5],"|")
      print("")
      print(wro2[0],wro2[1]+"[WR]","|","overall:","?","|","route-running:","?","|","catching:","?","|","Draft Number:",wro2[5],"|")
      print("")
      print(lbo1[0],lbo1[1]+"[LB]","|","overall:",lbo1[2],"|","coverage:",lbo1[3],"|","play-rec:",lbo1[4],"|","run-defense:",lbo1[5],"|","Draft Number:",lbo1[6],"|")
      print("")
      print(lbo2[0],lbo2[1]+"[LB]","|","overall:","?","|","coverage:","?","|","play-rec:","?","|","run-defense:","?","|","Draft Number:",lbo2[6],"|")
      print("")
      print(dlo1[0],dlo1[1]+"[DL]","|","overall:",dlo1[2],"|","pass-rush:",dlo1[3],"|","run-stop:",dlo1[4],"|","Draft Number:",dlo1[5],"|")
      print("")
      print(dlo2[0],dlo2[1]+"[DL]","|","overall:","?","|","pass-rush:","?","|","run-stop:","?","|","Draft Number:",dlo2[5],"|")
      print("")
      print(cbo1[0],cbo1[1]+"[CB]","|","overall:",cbo1[2],"|","coverage:",cbo1[3],"|","catching:",cbo1[4],"|","Draft Number:",cbo1[5],"|")
      print("")
      print(cbo2[0],cbo2[1]+"[CB]","|","overall:","?","|","coverage:","?","|","catching:","?","|","Draft Number:",cbo2[5],"|")
      print("")
      print(so1[0],so1[1]+"[S]","|","overall:",so1[2],"|","play-rec:",so1[3],"|","catching:",so1[4],"|","Draft Number:",so1[5],"|")
      print("")
      print(so2[0],so2[1]+"[S]","|","overall:","?","|","play-rec:","?","|","catching:","?","|","Draft Number:",so2[5],"|")
      print("")
      ds=int(input("Select a Player: "))
      
      if ds>0 and ds<3:
        if qbd1==0:
          qb1=lop[ds]
          qbd1=1
          sfr=sfr-1
          (lop[ds])[7]=1
          
      if ds>2 and ds<5:
        if old1==0:
          ol1=lop[ds]
          old1=1
          sfr=sfr-1
          (lop[ds])[6]=1
      if ds>4 and ds<7:
        if rbd1==0:
          rb1=lop[ds]
          rbd1=1
          sfr=sfr-1
          (lop[ds])[6]=1
      if ds>6 and ds<9:
        if wr1d1==0 and (lop[ds])[6]==0:
          wr11=lop[ds]
          wr1d1=1
          sfr=sfr-1
          (lop[ds])[6]=1
        else:
          if wr2d1==0 and(lop[ds])[6]==0:
            wr12=lop[ds]
            wr2d1=1
            sfr=sfr-1
            (lop[ds])[6]=1
      if ds>8 and ds<11:
        if lbd1==0:
          lb1=lop[ds]
          lbd1=1
          sfr=sfr-1
          (lop[ds])[7]=1
      if ds>10 and ds<13:
        if dld1==0:
          dl1=lop[ds]
          dld1=1
          sfr=sfr-1
          (lop[ds])[6]=1
      if ds>12 and ds<15:
        if cb1d1==0 and (lop[ds])[6]==0:
          cb11=lop[ds]
          cb1d1=1
          sfr=sfr-1
          (lop[ds])[6]=1
        else:
          if cb2d1==0 and(lop[ds])[6]==0:
            cb12=lop[ds]
            cb2d1=1
            sfr=sfr-1
            (lop[ds])[6]=1
      if ds>14 and ds<17:
        if sd1==0:
          s1=lop[ds]
          sd1=1
          sfr=sfr-1
          (lop[ds])[6]=1
      replit.clear()
      dp=""
      if ds>0 and ds<3:
        dp="QB"
      if ds>2 and ds<5:
        dp="OL"
      if ds>4 and ds<7:
        dp="RB"
      if ds>6 and ds<9:
        dp="WR"
      if ds>8 and ds<11:
        dp="LB"
      if ds>10 and ds<13:
        dp="DL"
      if ds>12 and ds<15:
        dp="CB"
      if ds>14 and ds<17:
        dp="S"
      print("Youve drafted",dp,(lop[ds])[0],(lop[ds])[1],"Overall:",(lop[ds])[2])
      ds=0
      pause=input("Say anything to continue")
      replit.clear()
    print("Round 2 Has concluded")
    time.sleep(0.5)
    pause=input("Hit enter to view your Big Board")
    replit.clear()
    #Show QB
    if qb1[0]=="":
      print("QB : N/A")
    else:
      print("QB :",qb1[0],qb1[1],"|","overall:",qb1[2],"|")
    #Show OL
    if ol1[0]=="":
      print("OL : N/A")
    else:
      print("OL: ",ol1[0],ol1[1],"|","overall:",ol1[2],"|")
    #Show RB
    if rb1[0]=="":
      print("RB:  N/A")
    else:
      print("RB: ",rb1[0],rb1[1],"|","overall:",rb1[2],"|")
    #Show WR1
    if wr11[0]=="":
      print("WR1: N/A")
    else:
      print("WR1:",wr11[0],wr11[1],"|","overall:",wr11[2],"|")
    #Show WR2
    if wr12[0]=="":
      print("WR2: N/A")
    else:
      print("WR2:",wr12[0],wr12[1],"|","overall:",wr12[2],"|")
    #Show LB
    if lb1[0]=="":
      print("LB : N/A")
    else:
      print("LB: ",lb1[0],lb1[1],"|","overall:",lb1[2],"|")
    #Show DL
    if dl1[0]=="":
      print("DL:  N/A")
    else:
      print("DL: ",dl1[0],dl1[1],"|","overall:",dl1[2],"|")
    #Show CB1
    if cb11[0]=="":
      print("CB1: N/A")
    else:
      print("CB1:",cb11[0],cb11[1],"|","overall:",cb11[2],"|")  
    #Show CB2
    if cb12[0]=="":
      print("CB2: N/A")
    else:
      print("CB2:",cb12[0],cb12[1],"|","overall:",cb12[2],"|") 
    #Show S
    if s1[0]=="":
      print("S:   N/A")
    else:
      print("S:  ",s1[0],s1[1],"|","overall:",s1[2],"|")
    pause=input("Say anything to continue")
    replit.clear()
    #Round 3
    print("Player 1 Welcome to Round 3 of the Draft")
    print("Hit enter to continue")
    pause=input("Say anything to continue")
    replit.clear()
    sfr=3
    #QB randomized stats
    rnq1=random.randint(65,90)
    rnq2=random.randint(65,90)
    rnq3=random.randint(65,90)
    rnq4=random.randint(60,95)
    rnq5=random.randint(60,95)
    rnq6=random.randint(60,95)
    qbo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnq1+rnq2+rnq3)/3),rnq1,rnq2,rnq3,1]
    qbo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnq4+rnq5+rnq6)/3),rnq4,rnq5,rnq6,2]
    #OL randomized stats
    rnol1=random.randint(65,90)
    rnol2=random.randint(65,90)
    rnol3=random.randint(60,95)
    rnol4=random.randint(60,95)
    olo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnol1+rnol2)/2),rnol1,rnol2,3]
    olo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnol3+rnol4)/2),rnol3,rnol4,4]
    #RB randomized stats
    rnrb1=random.randint(65,90)
    rnrb2=random.randint(65,90)
    rnrb3=random.randint(60,95)
    rnrb4=random.randint(60,95)
    rbo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnrb1+rnrb2)/2),rnrb1,rnrb2,5]
    rbo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnrb3+rnrb4)/2),rnrb3,rnrb4,6]
    #WR randomized stats
    rnwr1=random.randint(65,90)
    rnwr2=random.randint(65,90)
    rnwr3=random.randint(60,95)
    rnwr4=random.randint(60,95)
    wro1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnwr1+rnwr2)/2),rnwr1,rnwr2,7]
    wro2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnwr3+rnwr4)/2),rnwr3,rnwr4,8]
    #MLB randomized stats
    rnlb1=random.randint(65,90)
    rnlb2=random.randint(65,90)
    rnlb3=random.randint(65,90)
    rnlb4=random.randint(60,95)
    rnlb5=random.randint(60,95)
    rnlb6=random.randint(60,95)
    lbo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnlb1+rnlb2+rnlb3)/3),rnlb1,rnlb2,rnlb3,9]
    lbo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnlb4+rnlb5+rnlb6)/3),rnlb4,rnlb5,rnlb6,10]
    #DL randomized stats
    rndl1=random.randint(65,90)
    rndl2=random.randint(65,90)
    rndl3=random.randint(60,95)
    rndl4=random.randint(60,95)
    dlo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rndl1+rndl2)/2),rndl1,rndl2,11]
    dlo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rndl3+rndl4)/2),rndl3,rndl4,12]
    #CB randomized stats
    rncb1=random.randint(65,90)
    rncb2=random.randint(65,90)
    rncb3=random.randint(60,95)
    rncb4=random.randint(60,95)
    cbo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rncb1+rncb2)/2),rncb1,rncb2,13]
    cbo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rncb3+rncb4)/2),rncb3,rncb4,14]
    #S randomized stats
    rns1=random.randint(65,90)
    rns2=random.randint(65,90)
    rns3=random.randint(60,95)
    rns4=random.randint(60,95)
    so1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rns1+rns2)/2),rns1,rns2,15]
    so2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rns3+rns4)/2),rns3,rns4,16]
    #list of all prospects
    blanklist=[]
    lop=[blanklist,qbo1,qbo2,olo1,olo2,rbo1,rbo2,wro1,wro2,lbo1,lbo2,dlo1,dlo2,cbo1,cbo2,so1,so2]
    for item in lop:
      item.append(0)
    while sfr>0:
      print("Third Round")
      print("")
      print("Selections Remaining:",sfr)
      print("")
      print(qbo1[0],qbo1[1]+"[QB]","|","overall:",qbo1[2],"|","throwing:",qbo1[3],"|","running:",qbo1[4],"|","iq:",qbo1[5],"|","Draft Number:",qbo1[6],"|")
      print("")
      print(qbo2[0],qbo2[1]+"[QB]","|","overall:","?","|","throwing:","?","|","running:","?","|","iq:","?","|","Draft Number:",qbo2[6],"|")
      print("")
      print(olo1[0],olo1[1]+"[OL]","|","overall:",olo1[2],"|","pass-block:",olo1[3],"|","run-block:",olo1[4],"|","Draft Number:",olo1[5],"|")
      print("")
      print(olo2[0],olo2[1]+"[OL]","|","overall:","?","|","pass-block:","?","|","run-block:","?","|","Draft Number:",olo2[5],"|")
      print("")
      print(rbo1[0],rbo1[1]+"[RB]","|","overall:",rbo1[2],"|","speed:",rbo1[3],"|","power:",rbo1[4],"|","Draft Number:",rbo1[5],"|")
      print("")
      print(rbo2[0],rbo2[1]+"[RB]","|","overall:","?","|","speed:","?","|","power:","?","|","Draft Number:",rbo2[5],"|")
      print("")
      print(wro1[0],wro1[1]+"[WR]","|","overall:",wro1[2],"|","route-running:",wro1[3],"|","catching:",wro1[4],"|","Draft Number:",wro1[5],"|")
      print("")
      print(wro2[0],wro2[1]+"[WR]","|","overall:","?","|","route-running:","?","|","catching:","?","|","Draft Number:",wro2[5],"|")
      print("")
      print(lbo1[0],lbo1[1]+"[LB]","|","overall:",lbo1[2],"|","coverage:",lbo1[3],"|","play-rec:",lbo1[4],"|","run-defense:",lbo1[5],"|","Draft Number:",lbo1[6],"|")
      print("")
      print(lbo2[0],lbo2[1]+"[LB]","|","overall:","?","|","coverage:","?","|","play-rec:","?","|","run-defense:","?","|","Draft Number:",lbo2[6],"|")
      print("")
      print(dlo1[0],dlo1[1]+"[DL]","|","overall:",dlo1[2],"|","pass-rush:",dlo1[3],"|","run-stop:",dlo1[4],"|","Draft Number:",dlo1[5],"|")
      print("")
      print(dlo2[0],dlo2[1]+"[DL]","|","overall:","?","|","pass-rush:","?","|","run-stop:","?","|","Draft Number:",dlo2[5],"|")
      print("")
      print(cbo1[0],cbo1[1]+"[CB]","|","overall:",cbo1[2],"|","coverage:",cbo1[3],"|","catching:",cbo1[4],"|","Draft Number:",cbo1[5],"|")
      print("")
      print(cbo2[0],cbo2[1]+"[CB]","|","overall:","?","|","coverage:","?","|","catching:","?","|","Draft Number:",cbo2[5],"|")
      print("")
      print(so1[0],so1[1]+"[S]","|","overall:",so1[2],"|","play-rec:",so1[3],"|","catching:",so1[4],"|","Draft Number:",so1[5],"|")
      print("")
      print(so2[0],so2[1]+"[S]","|","overall:","?","|","play-rec:","?","|","catching:","?","|","Draft Number:",so2[5],"|")
      print("")
      ds=int(input("Select a Player: "))
      
      if ds>0 and ds<3:
        if qbd1==0:
          qb1=lop[ds]
          qbd1=1
          sfr=sfr-1
          (lop[ds])[7]=1
          
      if ds>2 and ds<5:
        if old1==0:
          ol1=lop[ds]
          old1=1
          sfr=sfr-1
          (lop[ds])[6]=1
      if ds>4 and ds<7:
        if rbd1==0:
          rb1=lop[ds]
          rbd1=1
          sfr=sfr-1
          (lop[ds])[6]=1
      if ds>6 and ds<9:
        if wr1d1==0 and (lop[ds])[6]==0:
          wr11=lop[ds]
          wr1d1=1
          sfr=sfr-1
          (lop[ds])[6]=1
        else:
          if wr2d1==0 and(lop[ds])[6]==0:
            wr12=lop[ds]
            wr2d1=1
            sfr=sfr-1
            (lop[ds])[6]=1
      if ds>8 and ds<11:
        if lbd1==0:
          lb1=lop[ds]
          lbd1=1
          sfr=sfr-1
          (lop[ds])[7]=1
      if ds>10 and ds<13:
        if dld1==0:
          dl1=lop[ds]
          dld1=1
          sfr=sfr-1
          (lop[ds])[6]=1
      if ds>12 and ds<15:
        if cb1d1==0 and (lop[ds])[6]==0:
          cb11=lop[ds]
          cb1d1=1
          sfr=sfr-1
          (lop[ds])[6]=1
        else:
          if cb2d1==0 and(lop[ds])[6]==0:
            cb12=lop[ds]
            cb2d1=1
            sfr=sfr-1
            (lop[ds])[6]=1
      if ds>14 and ds<17:
        if sd1==0:
          s1=lop[ds]
          sd1=1
          sfr=sfr-1
          (lop[ds])[6]=1
      replit.clear()
      dp=""
      if ds>0 and ds<3:
        dp="QB"
      if ds>2 and ds<5:
        dp="OL"
      if ds>4 and ds<7:
        dp="RB"
      if ds>6 and ds<9:
        dp="WR"
      if ds>8 and ds<11:
        dp="LB"
      if ds>10 and ds<13:
        dp="DL"
      if ds>12 and ds<15:
        dp="CB"
      if ds>14 and ds<17:
        dp="S"
      print("Youve drafted",dp,(lop[ds])[0],(lop[ds])[1],"Overall:",(lop[ds])[2])
      ds=0
      pause=input("Say anything to continue")
      replit.clear()
    print("Round 3 Has concluded")
    time.sleep(0.5)
    pause=input("Hit enter to view your Big Board")
    replit.clear()
    #Show QB
    if qb1[0]=="":
      print("QB : N/A")
    else:
      print("QB :",qb1[0],qb1[1],"|","overall:",qb1[2],"|")
    #Show OL
    if ol1[0]=="":
      print("OL : N/A")
    else:
      print("OL: ",ol1[0],ol1[1],"|","overall:",ol1[2],"|")
    #Show RB
    if rb1[0]=="":
      print("RB:  N/A")
    else:
      print("RB: ",rb1[0],rb1[1],"|","overall:",rb1[2],"|")
    #Show WR1
    if wr11[0]=="":
      print("WR1: N/A")
    else:
      print("WR1:",wr11[0],wr11[1],"|","overall:",wr11[2],"|")
    #Show WR2
    if wr12[0]=="":
      print("WR2: N/A")
    else:
      print("WR2:",wr12[0],wr12[1],"|","overall:",wr12[2],"|")
    #Show LB
    if lb1[0]=="":
      print("LB : N/A")
    else:
      print("LB: ",lb1[0],lb1[1],"|","overall:",lb1[2],"|")
    #Show DL
    if dl1[0]=="":
      print("DL:  N/A")
    else:
      print("DL: ",dl1[0],dl1[1],"|","overall:",dl1[2],"|")
    #Show CB1
    if cb11[0]=="":
      print("CB1: N/A")
    else:
      print("CB1:",cb11[0],cb11[1],"|","overall:",cb11[2],"|")  
    #Show CB2
    if cb12[0]=="":
      print("CB2: N/A")
    else:
      print("CB2:",cb12[0],cb12[1],"|","overall:",cb12[2],"|") 
    #Show S
    if s1[0]=="":
      print("S:   N/A")
    else:
      print("S:  ",s1[0],s1[1],"|","overall:",s1[2],"|")
    pause=input("Say anything to continue")
    replit.clear()
    #Round 4
    print("Player 1 Welcome to Round 4 of the Draft")
    print("Hit enter to continue")
    pause=input("Say anything to continue")
    replit.clear()
    sfr=1
    #QB randomized stats
    rnq1=random.randint(55,95)
    rnq2=random.randint(55,95)
    rnq3=random.randint(55,95)
    rnq4=random.randint(55,95)
    rnq5=random.randint(55,95)
    rnq6=random.randint(55,95)
    qbo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnq1+rnq2+rnq3)/3),rnq1,rnq2,rnq3,1]
    qbo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnq4+rnq5+rnq6)/3),rnq4,rnq5,rnq6,2]
    #OL randomized stats
    rnol1=random.randint(55,95)
    rnol2=random.randint(55,95)
    rnol3=random.randint(55,95)
    rnol4=random.randint(55,95)
    olo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnol1+rnol2)/2),rnol1,rnol2,3]
    olo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnol3+rnol4)/2),rnol3,rnol4,4]
    #RB randomized stats
    rnrb1=random.randint(55,95)
    rnrb2=random.randint(55,95)
    rnrb3=random.randint(55,95)
    rnrb4=random.randint(55,95)
    rbo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnrb1+rnrb2)/2),rnrb1,rnrb2,5]
    rbo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnrb3+rnrb4)/2),rnrb3,rnrb4,6]
    #WR randomized stats
    rnwr1=random.randint(55,90)
    rnwr2=random.randint(55,90)
    rnwr3=random.randint(55,95)
    rnwr4=random.randint(55,95)
    wro1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnwr1+rnwr2)/2),rnwr1,rnwr2,7]
    wro2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnwr3+rnwr4)/2),rnwr3,rnwr4,8]
    #MLB randomized stats
    rnlb1=random.randint(55,95)
    rnlb2=random.randint(55,95)
    rnlb3=random.randint(55,95)
    rnlb4=random.randint(55,95)
    rnlb5=random.randint(55,95)
    rnlb6=random.randint(55,95)
    lbo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnlb1+rnlb2+rnlb3)/3),rnlb1,rnlb2,rnlb3,9]
    lbo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnlb4+rnlb5+rnlb6)/3),rnlb4,rnlb5,rnlb6,10]
    #DL randomized stats
    rndl1=random.randint(55,95)
    rndl2=random.randint(55,95)
    rndl3=random.randint(55,95)
    rndl4=random.randint(55,95)
    dlo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rndl1+rndl2)/2),rndl1,rndl2,11]
    dlo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rndl3+rndl4)/2),rndl3,rndl4,12]
    #CB randomized stats
    rncb1=random.randint(55,95)
    rncb2=random.randint(55,95)
    rncb3=random.randint(55,95)
    rncb4=random.randint(55,95)
    cbo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rncb1+rncb2)/2),rncb1,rncb2,13]
    cbo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rncb3+rncb4)/2),rncb3,rncb4,14]
    #S randomized stats
    rns1=random.randint(55,95)
    rns2=random.randint(55,95)
    rns3=random.randint(55,95)
    rns4=random.randint(55,95)
    so1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rns1+rns2)/2),rns1,rns2,15]
    so2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rns3+rns4)/2),rns3,rns4,16]
    #list of all prospects
    blanklist=[]
    lop=[blanklist,qbo1,qbo2,olo1,olo2,rbo1,rbo2,wro1,wro2,lbo1,lbo2,dlo1,dlo2,cbo1,cbo2,so1,so2]
    for item in lop:
      item.append(0)
    while sfr>0:
      print("Fourth Round")
      print("")
      print("Selections Remaining:",sfr)
      print("")
      print(qbo1[0],qbo1[1]+"[QB]","|","overall:","?","|","throwing:","?","|","running:","?","|","iq:","?","|","Draft Number:",qbo1[6],"|")
      print("")
      print(qbo2[0],qbo2[1]+"[QB]","|","overall:","?","|","throwing:","?","|","running:","?","|","iq:","?","|","Draft Number:",qbo2[6],"|")
      print("")
      print(olo1[0],olo1[1]+"[OL]","|","overall:","?","|","pass-block:","?","|","run-block:","?","|","Draft Number:",olo1[5],"|")
      print("")
      print(olo2[0],olo2[1]+"[OL]","|","overall:","?","|","pass-block:","?","|","run-block:","?","|","Draft Number:",olo2[5],"|")
      print("")
      print(rbo1[0],rbo1[1]+"[RB]","|","overall:","?","|","speed:","?","|","power:","?","|","Draft Number:",rbo1[5],"|")
      print("")
      print(rbo2[0],rbo2[1]+"[RB]","|","overall:","?","|","speed:","?","|","power:","?","|","Draft Number:",rbo2[5],"|")
      print("")
      print(wro1[0],wro1[1]+"[WR]","|","overall:","?","|","route-running:","?","|","catching:","?","|","Draft Number:",wro1[5],"|")
      print("")
      print(wro2[0],wro2[1]+"[WR]","|","overall:","?","|","route-running:","?","|","catching:","?","|","Draft Number:",wro2[5],"|")
      print("")
      print(lbo1[0],lbo1[1]+"[LB]","|","overall:","?","|","coverage:","?","|","play-rec:","?","|","run-defense:","?","|","Draft Number:",lbo1[6],"|")
      print("")
      print(lbo2[0],lbo2[1]+"[LB]","|","overall:","?","|","coverage:","?","|","play-rec:","?","|","run-defense:","?","|","Draft Number:",lbo2[6],"|")
      print("")
      print(dlo1[0],dlo1[1]+"[DL]","|","overall:","?","|","pass-rush:","?","|","run-stop:","?","|","Draft Number:",dlo1[5],"|")
      print("")
      print(dlo2[0],dlo2[1]+"[DL]","|","overall:","?","|","pass-rush:","?","|","run-stop:","?","|","Draft Number:",dlo2[5],"|")
      print("")
      print(cbo1[0],cbo1[1]+"[CB]","|","overall:","?","|","coverage:","?","|","catching:","?","|","Draft Number:",cbo1[5],"|")
      print("")
      print(cbo2[0],cbo2[1]+"[CB]","|","overall:","?","|","coverage:","?","|","catching:","?","|","Draft Number:",cbo2[5],"|")
      print("")
      print(so1[0],so1[1]+"[S]","|","overall:","?","|","play-rec:","?","|","catching:","?","|","Draft Number:",so1[5],"|")
      print("")
      print(so2[0],so2[1]+"[S]","|","overall:","?","|","play-rec:","?","|","catching:","?","|","Draft Number:",so2[5],"|")
      print("")
      ds=int(input("Select a Player: "))
      
      if ds>0 and ds<3:
        if qbd1==0:
          qb1=lop[ds]
          qbd1=1
          sfr=sfr-1
          (lop[ds])[7]=1
          
      if ds>2 and ds<5:
        if old1==0:
          ol1=lop[ds]
          old1=1
          sfr=sfr-1
          (lop[ds])[6]=1
      if ds>4 and ds<7:
        if rbd1==0:
          rb1=lop[ds]
          rbd1=1
          sfr=sfr-1
          (lop[ds])[6]=1
      if ds>6 and ds<9:
        if wr1d1==0 and (lop[ds])[6]==0:
          wr11=lop[ds]
          wr1d1=1
          sfr=sfr-1
          (lop[ds])[6]=1
        else:
          if wr2d1==0 and(lop[ds])[6]==0:
            wr12=lop[ds]
            wr2d1=1
            sfr=sfr-1
            (lop[ds])[6]=1
      if ds>8 and ds<11:
        if lbd1==0:
          lb1=lop[ds]
          lbd1=1
          sfr=sfr-1
          (lop[ds])[7]=1
      if ds>10 and ds<13:
        if dld1==0:
          dl1=lop[ds]
          dld1=1
          sfr=sfr-1
          (lop[ds])[6]=1
      if ds>12 and ds<15:
        if cb1d1==0 and (lop[ds])[6]==0:
          cb11=lop[ds]
          cb1d1=1
          sfr=sfr-1
          (lop[ds])[6]=1
        else:
          if cb2d1==0 and(lop[ds])[6]==0:
            cb12=lop[ds]
            cb2d1=1
            sfr=sfr-1
            (lop[ds])[6]=1
      if ds>14 and ds<17:
        if sd1==0:
          s1=lop[ds]
          sd1=1
          sfr=sfr-1
          (lop[ds])[6]=1
      replit.clear()
      dp=""
      if ds>0 and ds<3:
        dp="QB"
      if ds>2 and ds<5:
        dp="OL"
      if ds>4 and ds<7:
        dp="RB"
      if ds>6 and ds<9:
        dp="WR"
      if ds>8 and ds<11:
        dp="LB"
      if ds>10 and ds<13:
        dp="DL"
      if ds>12 and ds<15:
        dp="CB"
      if ds>14 and ds<17:
        dp="S"
      print("Youve drafted",dp,(lop[ds])[0],(lop[ds])[1],"Overall:",(lop[ds])[2])
      ds=0
      pause=input("Say anything to continue")
      replit.clear()
    print("Round 4 Has concluded")
    time.sleep(0.5)
    pause=input("Hit enter to view your Big Board")
    replit.clear()
    #Show QB
    if qb1[0]=="":
      print("QB : N/A")
    else:
      print("QB :",qb1[0],qb1[1],"|","overall:",qb1[2],"|")
    #Show OL
    if ol1[0]=="":
      print("OL : N/A")
    else:
      print("OL: ",ol1[0],ol1[1],"|","overall:",ol1[2],"|")
    #Show RB
    if rb1[0]=="":
      print("RB:  N/A")
    else:
      print("RB: ",rb1[0],rb1[1],"|","overall:",rb1[2],"|")
    #Show WR1
    if wr11[0]=="":
      print("WR1: N/A")
    else:
      print("WR1:",wr11[0],wr11[1],"|","overall:",wr11[2],"|")
    #Show WR2
    if wr12[0]=="":
      print("WR2: N/A")
    else:
      print("WR2:",wr12[0],wr12[1],"|","overall:",wr12[2],"|")
    #Show LB
    if lb1[0]=="":
      print("LB : N/A")
    else:
      print("LB: ",lb1[0],lb1[1],"|","overall:",lb1[2],"|")
    #Show DL
    if dl1[0]=="":
      print("DL:  N/A")
    else:
      print("DL: ",dl1[0],dl1[1],"|","overall:",dl1[2],"|")
    #Show CB1
    if cb11[0]=="":
      print("CB1: N/A")
    else:
      print("CB1:",cb11[0],cb11[1],"|","overall:",cb11[2],"|")  
    #Show CB2
    if cb12[0]=="":
      print("CB2: N/A")
    else:
      print("CB2:",cb12[0],cb12[1],"|","overall:",cb12[2],"|") 
    #Show S
    if s1[0]=="":
      print("S:   N/A")
    else:
      print("S:  ",s1[0],s1[1],"|","overall:",s1[2],"|")
    pause=input("Say anything to continue")
    replit.clear()
    ##/break
    #Draft Player 2
    #Round 1
    print("Player 2 Welcome to Round 1 of the Draft")
    print("Hit enter to continue")
    pause=input("Say anything to continue")
    replit.clear()
    sfr=3
    #QB randomized stats
    rnq1=random.randint(85,99)
    rnq2=random.randint(85,99)
    rnq3=random.randint(85,99)
    rnq4=random.randint(85,99)
    rnq5=random.randint(85,99)
    rnq6=random.randint(85,99)
    qbo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnq1+rnq2+rnq3)/3),rnq1,rnq2,rnq3,1]
    qbo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnq4+rnq5+rnq6)/3),rnq4,rnq5,rnq6,2]
    #OL randomized stats
    rnol2=random.randint(85,99)
    rnol2=random.randint(85,99)
    rnol3=random.randint(85,99)
    rnol4=random.randint(85,99)
    olo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnol2+rnol2)/2),rnol2,rnol2,3]
    olo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnol3+rnol4)/2),rnol3,rnol4,4]
    #RB randomized stats
    rnrb2=random.randint(85,99)
    rnrb2=random.randint(85,99)
    rnrb3=random.randint(85,99)
    rnrb4=random.randint(85,99)
    rbo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnrb2+rnrb2)/2),rnrb2,rnrb2,5]
    rbo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnrb3+rnrb4)/2),rnrb3,rnrb4,6]
    #WR randomized stats
    rnwr1=random.randint(85,99)
    rnwr2=random.randint(85,99)
    rnwr3=random.randint(85,99)
    rnwr4=random.randint(85,99)
    wro1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnwr1+rnwr2)/2),rnwr1,rnwr2,7]
    wro2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnwr3+rnwr4)/2),rnwr3,rnwr4,8]
    #MLB randomized stats
    rnlb2=random.randint(85,99)
    rnlb2=random.randint(85,99)
    rnlb3=random.randint(85,99)
    rnlb4=random.randint(85,99)
    rnlb5=random.randint(85,99)
    rnlb6=random.randint(85,99)
    lbo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnlb2+rnlb2+rnlb3)/3),rnlb2,rnlb2,rnlb3,9]
    lbo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnlb4+rnlb5+rnlb6)/3),rnlb4,rnlb5,rnlb6,10]
    #DL randomized stats
    rndl2=random.randint(85,99)
    rndl2=random.randint(85,99)
    rndl3=random.randint(85,99)
    rndl4=random.randint(85,99)
    dlo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rndl2+rndl2)/2),rndl2,rndl2,11]
    dlo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rndl3+rndl4)/2),rndl3,rndl4,12]
    #CB randomized stats
    rncb1=random.randint(85,99)
    rncb2=random.randint(85,99)
    rncb3=random.randint(85,99)
    rncb4=random.randint(85,99)
    cbo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rncb1+rncb2)/2),rncb1,rncb2,13]
    cbo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rncb3+rncb4)/2),rncb3,rncb4,14]
    #S randomized stats
    rns2=random.randint(85,99)
    rns2=random.randint(85,99)
    rns3=random.randint(85,99)
    rns4=random.randint(85,99)
    so1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rns2+rns2)/2),rns2,rns2,15]
    so2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rns3+rns4)/2),rns3,rns4,16]
    #list of all prospects
    blanklist=[]
    lop=[blanklist,qbo1,qbo2,olo1,olo2,rbo1,rbo2,wro1,wro2,lbo1,lbo2,dlo1,dlo2,cbo1,cbo2,so1,so2]
    for item in lop:
      item.append(0)
    while sfr>0:
      print("First Round")
      print("")
      print("Selections Remaining:",sfr)
      print("")
      print(qbo1[0],qbo1[1]+"[QB]","|","overall:",qbo1[2],"|","throwing:",qbo1[3],"|","running:",qbo1[4],"|","iq:",qbo1[5],"|","Draft Number:",qbo1[6],"|")
      print("")
      print(qbo2[0],qbo2[1]+"[QB]","|","overall:",qbo2[2],"|","throwing:",qbo2[3],"|","running:",qbo2[4],"|","iq:",qbo2[5],"|","Draft Number:",qbo2[6],"|")
      print("")
      print(olo1[0],olo1[1]+"[OL]","|","overall:",olo1[2],"|","pass-block:",olo1[3],"|","run-block:",olo1[4],"|","Draft Number:",olo1[5],"|")
      print("")
      print(olo2[0],olo2[1]+"[OL]","|","overall:",olo2[2],"|","pass-block:",olo2[3],"|","run-block:",olo2[4],"|","Draft Number:",olo2[5],"|")
      print("")
      print(rbo1[0],rbo1[1]+"[RB]","|","overall:",rbo1[2],"|","speed:",rbo1[3],"|","power:",rbo1[4],"|","Draft Number:",rbo1[5],"|")
      print("")
      print(rbo2[0],rbo2[1]+"[RB]","|","overall:",rbo2[2],"|","speed:",rbo2[3],"|","power:",rbo2[4],"|","Draft Number:",rbo2[5],"|")
      print("")
      print(wro1[0],wro1[1]+"[WR]","|","overall:",wro1[2],"|","route-running:",wro1[3],"|","catching:",wro1[4],"|","Draft Number:",wro1[5],"|")
      print("")
      print(wro2[0],wro2[1]+"[WR]","|","overall:",wro2[2],"|","route-running:",wro2[3],"|","catching:",wro2[4],"|","Draft Number:",wro2[5],"|")
      print("")
      print(lbo1[0],lbo1[1]+"[LB]","|","overall:",lbo1[2],"|","coverage:",lbo1[3],"|","play-rec:",lbo1[4],"|","run-defense:",lbo1[5],"|","Draft Number:",lbo1[6],"|")
      print("")
      print(lbo2[0],lbo2[1]+"[LB]","|","overall:",lbo2[2],"|","coverage:",lbo2[3],"|","play-rec:",lbo2[4],"|","run-defense:",lbo2[5],"|","Draft Number:",lbo2[6],"|")
      print("")
      print(dlo1[0],dlo1[1]+"[DL]","|","overall:",dlo1[2],"|","pass-rush:",dlo1[3],"|","run-stop:",dlo1[4],"|","Draft Number:",dlo1[5],"|")
      print("")
      print(dlo2[0],dlo2[1]+"[DL]","|","overall:",dlo2[2],"|","pass-rush:",dlo2[3],"|","run-stop:",dlo2[4],"|","Draft Number:",dlo2[5],"|")
      print("")
      print(cbo1[0],cbo1[1]+"[CB]","|","overall:",cbo1[2],"|","coverage:",cbo1[3],"|","catching:",cbo1[4],"|","Draft Number:",cbo1[5],"|")
      print("")
      print(cbo2[0],cbo2[1]+"[CB]","|","overall:",cbo2[2],"|","coverage:",cbo2[3],"|","catching:",cbo2[4],"|","Draft Number:",cbo2[5],"|")
      print("")
      print(so1[0],so1[1]+"[S]","|","overall:",so1[2],"|","play-rec:",so1[3],"|","catching:",so1[4],"|","Draft Number:",so1[5],"|")
      print("")
      print(so2[0],so2[1]+"[S]","|","overall:",so2[2],"|","play-rec:",so2[3],"|","catching:",so2[4],"|","Draft Number:",so2[5],"|")
      print("")
      ds=int(input("Select a Player: "))
      
      if ds>0 and ds<3:
        if qbd2==0:
          qb2=lop[ds]
          qbd2=1
          sfr=sfr-1
          (lop[ds])[7]=1
         
      if ds>2 and ds<5:
        if old2==0:
          ol2=lop[ds]
          old2=1
          sfr=sfr-1
          (lop[ds])[6]=1
      if ds>4 and ds<7:
        if rbd2==0:
          rb2=lop[ds]
          rbd2=1
          sfr=sfr-1
          (lop[ds])[6]=1
      if ds>6 and ds<9:
        if wr1d2==0 and (lop[ds])[6]==0:
          wr21=lop[ds]
          wr1d2=1
          sfr=sfr-1
          (lop[ds])[6]=1
        else:
          if wr2d2==0 and(lop[ds])[6]==0:
            wr22=lop[ds]
            wr2d2=1
            sfr=sfr-1
            (lop[ds])[6]=1
      if ds>8 and ds<11:
        if lbd2==0:
          lb2=lop[ds]
          lbd2=1
          sfr=sfr-1
          (lop[ds])[7]=1
      if ds>10 and ds<13:
        if dld2==0:
          dl2=lop[ds]
          dld2=1
          sfr=sfr-1
          (lop[ds])[6]=1
      if ds>12 and ds<15:
        if cb1d2==0 and (lop[ds])[6]==0:
          cb21=lop[ds]
          cb1d2=1
          sfr=sfr-1
          (lop[ds])[6]=1
        else:
          if cb2d2==0 and(lop[ds])[6]==0:
            cb22=lop[ds]
            cb2d2=1
            sfr=sfr-1
            (lop[ds])[6]=1
      if ds>14 and ds<17:
        if sd2==0:
          s2=lop[ds]
          sd2=1
          sfr=sfr-1
          (lop[ds])[6]=1
      replit.clear()
      dp=""
      if ds>0 and ds<3:
        dp="QB"
      if ds>2 and ds<5:
        dp="OL"
      if ds>4 and ds<7:
        dp="RB"
      if ds>6 and ds<9:
        dp="WR"
      if ds>8 and ds<11:
        dp="LB"
      if ds>10 and ds<13:
        dp="DL"
      if ds>12 and ds<15:
        dp="CB"
      if ds>14 and ds<17:
        dp="S"
      print("Youve drafted",dp,(lop[ds])[0],(lop[ds])[1],"Overall:",(lop[ds])[2])
      ds=0
      pause=input("Say anything to continue")
      replit.clear()
    print("Round 1 Has concluded")
    time.sleep(0.5)
    pause=input("Hit enter to view your Big Board")
    replit.clear()
    #Show QB
    if qb2[0]=="":
      print("QB : N/A")
    else:
      print("QB :",qb2[0],qb2[1],"|","overall:",qb2[2],"|")
    #Show OL
    if ol2[0]=="":
      print("OL : N/A")
    else:
      print("OL: ",ol2[0],ol2[1],"|","overall:",ol2[2],"|")
    #Show RB
    if rb2[0]=="":
      print("RB:  N/A")
    else:
      print("RB: ",rb2[0],rb2[1],"|","overall:",rb2[2],"|")
    #Show WR1
    if wr21[0]=="":
      print("WR1: N/A")
    else:
      print("WR1:",wr21[0],wr21[1],"|","overall:",wr21[2],"|")
    #Show WR2
    if wr22[0]=="":
      print("WR2: N/A")
    else:
      print("WR2:",wr22[0],wr22[1],"|","overall:",wr22[2],"|")
    #Show LB
    if lb2[0]=="":
      print("LB : N/A")
    else:
      print("LB: ",lb2[0],lb2[1],"|","overall:",lb2[2],"|")
    #Show DL
    if dl2[0]=="":
      print("DL:  N/A")
    else:
      print("DL: ",dl2[0],dl2[1],"|","overall:",dl2[2],"|")
    #Show CB1
    if cb21[0]=="":
      print("CB1: N/A")
    else:
      print("CB1:",cb21[0],cb21[1],"|","overall:",cb21[2],"|")  
    #Show CB2
    if cb22[0]=="":
      print("CB2: N/A")
    else:
      print("CB2:",cb22[0],cb22[1],"|","overall:",cb22[2],"|") 
    #Show S
    if s2[0]=="":
      print("S:   N/A")
    else:
      print("S:  ",s2[0],s2[1],"|","overall:",s2[2],"|")
    pause=input("Say anything to continue")
    replit.clear()
    #Round 2
    print("Player 2 Welcome to Round 2 of the Draft")
    print("Hit enter to continue")
    pause=input("Say anything to continue")
    replit.clear()
    sfr=3
    #QB randomized stats
    rnq1=random.randint(75,95)
    rnq2=random.randint(75,95)
    rnq3=random.randint(75,95)
    rnq4=random.randint(65,99)
    rnq5=random.randint(65,99)
    rnq6=random.randint(65,99)
    qbo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnq1+rnq2+rnq3)/3),rnq1,rnq2,rnq3,1]
    qbo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnq4+rnq5+rnq6)/3),rnq4,rnq5,rnq6,2]
    #OL randomized stats
    rnol2=random.randint(75,95)
    rnol2=random.randint(75,95)
    rnol3=random.randint(65,99)
    rnol4=random.randint(65,99)
    olo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnol2+rnol2)/2),rnol2,rnol2,3]
    olo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnol3+rnol4)/2),rnol3,rnol4,4]
    #RB randomized stats
    rnrb2=random.randint(75,95)
    rnrb2=random.randint(75,95)
    rnrb3=random.randint(65,99)
    rnrb4=random.randint(65,99)
    rbo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnrb2+rnrb2)/2),rnrb2,rnrb2,5]
    rbo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnrb3+rnrb4)/2),rnrb3,rnrb4,6]
    #WR randomized stats
    rnwr1=random.randint(75,95)
    rnwr2=random.randint(75,95)
    rnwr3=random.randint(65,99)
    rnwr4=random.randint(65,99)
    wro1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnwr1+rnwr2)/2),rnwr1,rnwr2,7]
    wro2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnwr3+rnwr4)/2),rnwr3,rnwr4,8]
    #MLB randomized stats
    rnlb2=random.randint(75,95)
    rnlb2=random.randint(75,95)
    rnlb3=random.randint(75,95)
    rnlb4=random.randint(65,99)
    rnlb5=random.randint(65,99)
    rnlb6=random.randint(65,99)
    lbo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnlb2+rnlb2+rnlb3)/3),rnlb2,rnlb2,rnlb3,9]
    lbo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnlb4+rnlb5+rnlb6)/3),rnlb4,rnlb5,rnlb6,10]
    #DL randomized stats
    rndl2=random.randint(75,95)
    rndl2=random.randint(75,95)
    rndl3=random.randint(65,99)
    rndl4=random.randint(65,99)
    dlo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rndl2+rndl2)/2),rndl2,rndl2,11]
    dlo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rndl3+rndl4)/2),rndl3,rndl4,12]
    #CB randomized stats
    rncb1=random.randint(75,95)
    rncb2=random.randint(75,95)
    rncb3=random.randint(65,99)
    rncb4=random.randint(65,99)
    cbo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rncb1+rncb2)/2),rncb1,rncb2,13]
    cbo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rncb3+rncb4)/2),rncb3,rncb4,14]
    #S randomized stats
    rns2=random.randint(75,95)
    rns2=random.randint(75,95)
    rns3=random.randint(65,99)
    rns4=random.randint(65,99)
    so1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rns2+rns2)/2),rns2,rns2,15]
    so2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rns3+rns4)/2),rns3,rns4,16]
    #list of all prospects
    blanklist=[]
    lop=[blanklist,qbo1,qbo2,olo1,olo2,rbo1,rbo2,wro1,wro2,lbo1,lbo2,dlo1,dlo2,cbo1,cbo2,so1,so2]
    for item in lop:
      item.append(0)
    while sfr>0:
      print("Second Round")
      print("")
      print("Selections Remaining:",sfr)
      print("")
      print(qbo1[0],qbo1[1]+"[QB]","|","overall:",qbo1[2],"|","throwing:",qbo1[3],"|","running:",qbo1[4],"|","iq:",qbo1[5],"|","Draft Number:",qbo1[6],"|")
      print("")
      print(qbo2[0],qbo2[1]+"[QB]","|","overall:","?","|","throwing:","?","|","running:","?","|","iq:","?","|","Draft Number:",qbo2[6],"|")
      print("")
      print(olo1[0],olo1[1]+"[OL]","|","overall:",olo1[2],"|","pass-block:",olo1[3],"|","run-block:",olo1[4],"|","Draft Number:",olo1[5],"|")
      print("")
      print(olo2[0],olo2[1]+"[OL]","|","overall:","?","|","pass-block:","?","|","run-block:","?","|","Draft Number:",olo2[5],"|")
      print("")
      print(rbo1[0],rbo1[1]+"[RB]","|","overall:",rbo1[2],"|","speed:",rbo1[3],"|","power:",rbo1[4],"|","Draft Number:",rbo1[5],"|")
      print("")
      print(rbo2[0],rbo2[1]+"[RB]","|","overall:","?","|","speed:","?","|","power:","?","|","Draft Number:",rbo2[5],"|")
      print("")
      print(wro1[0],wro1[1]+"[WR]","|","overall:",wro1[2],"|","route-running:",wro1[3],"|","catching:",wro1[4],"|","Draft Number:",wro1[5],"|")
      print("")
      print(wro2[0],wro2[1]+"[WR]","|","overall:","?","|","route-running:","?","|","catching:","?","|","Draft Number:",wro2[5],"|")
      print("")
      print(lbo1[0],lbo1[1]+"[LB]","|","overall:",lbo1[2],"|","coverage:",lbo1[3],"|","play-rec:",lbo1[4],"|","run-defense:",lbo1[5],"|","Draft Number:",lbo1[6],"|")
      print("")
      print(lbo2[0],lbo2[1]+"[LB]","|","overall:","?","|","coverage:","?","|","play-rec:","?","|","run-defense:","?","|","Draft Number:",lbo2[6],"|")
      print("")
      print(dlo1[0],dlo1[1]+"[DL]","|","overall:",dlo1[2],"|","pass-rush:",dlo1[3],"|","run-stop:",dlo1[4],"|","Draft Number:",dlo1[5],"|")
      print("")
      print(dlo2[0],dlo2[1]+"[DL]","|","overall:","?","|","pass-rush:","?","|","run-stop:","?","|","Draft Number:",dlo2[5],"|")
      print("")
      print(cbo1[0],cbo1[1]+"[CB]","|","overall:",cbo1[2],"|","coverage:",cbo1[3],"|","catching:",cbo1[4],"|","Draft Number:",cbo1[5],"|")
      print("")
      print(cbo2[0],cbo2[1]+"[CB]","|","overall:","?","|","coverage:","?","|","catching:","?","|","Draft Number:",cbo2[5],"|")
      print("")
      print(so1[0],so1[1]+"[S]","|","overall:",so1[2],"|","play-rec:",so1[3],"|","catching:",so1[4],"|","Draft Number:",so1[5],"|")
      print("")
      print(so2[0],so2[1]+"[S]","|","overall:","?","|","play-rec:","?","|","catching:","?","|","Draft Number:",so2[5],"|")
      print("")
      ds=int(input("Select a Player: "))
      
      if ds>0 and ds<3:
        if qbd2==0:
          qb2=lop[ds]
          qbd2=1
          sfr=sfr-1
          (lop[ds])[7]=1
          
      if ds>2 and ds<5:
        if old2==0:
          ol2=lop[ds]
          old2=1
          sfr=sfr-1
          (lop[ds])[6]=1
      if ds>4 and ds<7:
        if rbd2==0:
          rb2=lop[ds]
          rbd2=1
          sfr=sfr-1
          (lop[ds])[6]=1
      if ds>6 and ds<9:
        if wr1d2==0 and (lop[ds])[6]==0:
          wr21=lop[ds]
          wr1d2=1
          sfr=sfr-1
          (lop[ds])[6]=1
        else:
          if wr2d2==0 and(lop[ds])[6]==0:
            wr22=lop[ds]
            wr2d2=1
            sfr=sfr-1
            (lop[ds])[6]=1
      if ds>8 and ds<11:
        if lbd2==0:
          lb2=lop[ds]
          lbd2=1
          sfr=sfr-1
          (lop[ds])[7]=1
      if ds>10 and ds<13:
        if dld2==0:
          dl2=lop[ds]
          dld2=1
          sfr=sfr-1
          (lop[ds])[6]=1
      if ds>12 and ds<15:
        if cb1d2==0 and (lop[ds])[6]==0:
          cb21=lop[ds]
          cb1d2=1
          sfr=sfr-1
          (lop[ds])[6]=1
        else:
          if cb2d2==0 and(lop[ds])[6]==0:
            cb22=lop[ds]
            cb2d2=1
            sfr=sfr-1
            (lop[ds])[6]=1
      if ds>14 and ds<17:
        if sd2==0:
          s2=lop[ds]
          sd2=1
          sfr=sfr-1
          (lop[ds])[6]=1
      replit.clear()
      dp=""
      if ds>0 and ds<3:
        dp="QB"
      if ds>2 and ds<5:
        dp="OL"
      if ds>4 and ds<7:
        dp="RB"
      if ds>6 and ds<9:
        dp="WR"
      if ds>8 and ds<11:
        dp="LB"
      if ds>10 and ds<13:
        dp="DL"
      if ds>12 and ds<15:
        dp="CB"
      if ds>14 and ds<17:
        dp="S"
      print("Youve drafted",dp,(lop[ds])[0],(lop[ds])[1],"Overall:",(lop[ds])[2])
      ds=0
      pause=input("Say anything to continue")
      replit.clear()
    print("Round 2 Has concluded")
    time.sleep(0.5)
    pause=input("Hit enter to view your Big Board")
    replit.clear()
    #Show QB
    if qb2[0]=="":
      print("QB : N/A")
    else:
      print("QB :",qb2[0],qb2[1],"|","overall:",qb2[2],"|")
    #Show OL
    if ol2[0]=="":
      print("OL : N/A")
    else:
      print("OL: ",ol2[0],ol2[1],"|","overall:",ol2[2],"|")
    #Show RB
    if rb2[0]=="":
      print("RB:  N/A")
    else:
      print("RB: ",rb2[0],rb2[1],"|","overall:",rb2[2],"|")
    #Show WR1
    if wr21[0]=="":
      print("WR1: N/A")
    else:
      print("WR1:",wr21[0],wr21[1],"|","overall:",wr21[2],"|")
    #Show WR2
    if wr22[0]=="":
      print("WR2: N/A")
    else:
      print("WR2:",wr22[0],wr22[1],"|","overall:",wr22[2],"|")
    #Show LB
    if lb2[0]=="":
      print("LB : N/A")
    else:
      print("LB: ",lb2[0],lb2[1],"|","overall:",lb2[2],"|")
    #Show DL
    if dl2[0]=="":
      print("DL:  N/A")
    else:
      print("DL: ",dl2[0],dl2[1],"|","overall:",dl2[2],"|")
    #Show CB1
    if cb21[0]=="":
      print("CB1: N/A")
    else:
      print("CB1:",cb21[0],cb21[1],"|","overall:",cb21[2],"|")  
    #Show CB2
    if cb22[0]=="":
      print("CB2: N/A")
    else:
      print("CB2:",cb22[0],cb22[1],"|","overall:",cb22[2],"|") 
    #Show S
    if s2[0]=="":
      print("S:   N/A")
    else:
      print("S:  ",s2[0],s2[1],"|","overall:",s2[2],"|")
    pause=input("Say anything to continue")
    replit.clear()
    #Round 3
    print("Player 2 Welcome to Round 3 of the Draft")
    print("Hit enter to continue")
    pause=input("Say anything to continue")
    replit.clear()
    sfr=3
    #QB randomized stats
    rnq1=random.randint(65,90)
    rnq2=random.randint(65,90)
    rnq3=random.randint(65,90)
    rnq4=random.randint(60,95)
    rnq5=random.randint(60,95)
    rnq6=random.randint(60,95)
    qbo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnq1+rnq2+rnq3)/3),rnq1,rnq2,rnq3,1]
    qbo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnq4+rnq5+rnq6)/3),rnq4,rnq5,rnq6,2]
    #OL randomized stats
    rnol2=random.randint(65,90)
    rnol2=random.randint(65,90)
    rnol3=random.randint(60,95)
    rnol4=random.randint(60,95)
    olo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnol2+rnol2)/2),rnol2,rnol2,3]
    olo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnol3+rnol4)/2),rnol3,rnol4,4]
    #RB randomized stats
    rnrb2=random.randint(65,90)
    rnrb2=random.randint(65,90)
    rnrb3=random.randint(60,95)
    rnrb4=random.randint(60,95)
    rbo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnrb2+rnrb2)/2),rnrb2,rnrb2,5]
    rbo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnrb3+rnrb4)/2),rnrb3,rnrb4,6]
    #WR randomized stats
    rnwr1=random.randint(65,90)
    rnwr2=random.randint(65,90)
    rnwr3=random.randint(60,95)
    rnwr4=random.randint(60,95)
    wro1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnwr1+rnwr2)/2),rnwr1,rnwr2,7]
    wro2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnwr3+rnwr4)/2),rnwr3,rnwr4,8]
    #MLB randomized stats
    rnlb2=random.randint(65,90)
    rnlb2=random.randint(65,90)
    rnlb3=random.randint(65,90)
    rnlb4=random.randint(60,95)
    rnlb5=random.randint(60,95)
    rnlb6=random.randint(60,95)
    lbo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnlb2+rnlb2+rnlb3)/3),rnlb2,rnlb2,rnlb3,9]
    lbo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnlb4+rnlb5+rnlb6)/3),rnlb4,rnlb5,rnlb6,10]
    #DL randomized stats
    rndl2=random.randint(65,90)
    rndl2=random.randint(65,90)
    rndl3=random.randint(60,95)
    rndl4=random.randint(60,95)
    dlo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rndl2+rndl2)/2),rndl2,rndl2,11]
    dlo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rndl3+rndl4)/2),rndl3,rndl4,12]
    #CB randomized stats
    rncb1=random.randint(65,90)
    rncb2=random.randint(65,90)
    rncb3=random.randint(60,95)
    rncb4=random.randint(60,95)
    cbo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rncb1+rncb2)/2),rncb1,rncb2,13]
    cbo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rncb3+rncb4)/2),rncb3,rncb4,14]
    #S randomized stats
    rns2=random.randint(65,90)
    rns2=random.randint(65,90)
    rns3=random.randint(60,95)
    rns4=random.randint(60,95)
    so1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rns2+rns2)/2),rns2,rns2,15]
    so2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rns3+rns4)/2),rns3,rns4,16]
    #list of all prospects
    blanklist=[]
    lop=[blanklist,qbo1,qbo2,olo1,olo2,rbo1,rbo2,wro1,wro2,lbo1,lbo2,dlo1,dlo2,cbo1,cbo2,so1,so2]
    for item in lop:
      item.append(0)
    while sfr>0:
      print("Third Round")
      print("")
      print("Selections Remaining:",sfr)
      print("")
      print(qbo1[0],qbo1[1]+"[QB]","|","overall:",qbo1[2],"|","throwing:",qbo1[3],"|","running:",qbo1[4],"|","iq:",qbo1[5],"|","Draft Number:",qbo1[6],"|")
      print("")
      print(qbo2[0],qbo2[1]+"[QB]","|","overall:","?","|","throwing:","?","|","running:","?","|","iq:","?","|","Draft Number:",qbo2[6],"|")
      print("")
      print(olo1[0],olo1[1]+"[OL]","|","overall:",olo1[2],"|","pass-block:",olo1[3],"|","run-block:",olo1[4],"|","Draft Number:",olo1[5],"|")
      print("")
      print(olo2[0],olo2[1]+"[OL]","|","overall:","?","|","pass-block:","?","|","run-block:","?","|","Draft Number:",olo2[5],"|")
      print("")
      print(rbo1[0],rbo1[1]+"[RB]","|","overall:",rbo1[2],"|","speed:",rbo1[3],"|","power:",rbo1[4],"|","Draft Number:",rbo1[5],"|")
      print("")
      print(rbo2[0],rbo2[1]+"[RB]","|","overall:","?","|","speed:","?","|","power:","?","|","Draft Number:",rbo2[5],"|")
      print("")
      print(wro1[0],wro1[1]+"[WR]","|","overall:",wro1[2],"|","route-running:",wro1[3],"|","catching:",wro1[4],"|","Draft Number:",wro1[5],"|")
      print("")
      print(wro2[0],wro2[1]+"[WR]","|","overall:","?","|","route-running:","?","|","catching:","?","|","Draft Number:",wro2[5],"|")
      print("")
      print(lbo1[0],lbo1[1]+"[LB]","|","overall:",lbo1[2],"|","coverage:",lbo1[3],"|","play-rec:",lbo1[4],"|","run-defense:",lbo1[5],"|","Draft Number:",lbo1[6],"|")
      print("")
      print(lbo2[0],lbo2[1]+"[LB]","|","overall:","?","|","coverage:","?","|","play-rec:","?","|","run-defense:","?","|","Draft Number:",lbo2[6],"|")
      print("")
      print(dlo1[0],dlo1[1]+"[DL]","|","overall:",dlo1[2],"|","pass-rush:",dlo1[3],"|","run-stop:",dlo1[4],"|","Draft Number:",dlo1[5],"|")
      print("")
      print(dlo2[0],dlo2[1]+"[DL]","|","overall:","?","|","pass-rush:","?","|","run-stop:","?","|","Draft Number:",dlo2[5],"|")
      print("")
      print(cbo1[0],cbo1[1]+"[CB]","|","overall:",cbo1[2],"|","coverage:",cbo1[3],"|","catching:",cbo1[4],"|","Draft Number:",cbo1[5],"|")
      print("")
      print(cbo2[0],cbo2[1]+"[CB]","|","overall:","?","|","coverage:","?","|","catching:","?","|","Draft Number:",cbo2[5],"|")
      print("")
      print(so1[0],so1[1]+"[S]","|","overall:",so1[2],"|","play-rec:",so1[3],"|","catching:",so1[4],"|","Draft Number:",so1[5],"|")
      print("")
      print(so2[0],so2[1]+"[S]","|","overall:","?","|","play-rec:","?","|","catching:","?","|","Draft Number:",so2[5],"|")
      print("")
      ds=int(input("Select a Player: "))
      
      if ds>0 and ds<3:
        if qbd2==0:
          qb2=lop[ds]
          qbd2=1
          sfr=sfr-1
          (lop[ds])[7]=1
          
      if ds>2 and ds<5:
        if old2==0:
          ol2=lop[ds]
          old2=1
          sfr=sfr-1
          (lop[ds])[6]=1
      if ds>4 and ds<7:
        if rbd2==0:
          rb2=lop[ds]
          rbd2=1
          sfr=sfr-1
          (lop[ds])[6]=1
      if ds>6 and ds<9:
        if wr1d2==0 and (lop[ds])[6]==0:
          wr21=lop[ds]
          wr1d2=1
          sfr=sfr-1
          (lop[ds])[6]=1
        else:
          if wr2d2==0 and(lop[ds])[6]==0:
            wr22=lop[ds]
            wr2d2=1
            sfr=sfr-1
            (lop[ds])[6]=1
      if ds>8 and ds<11:
        if lbd2==0:
          lb2=lop[ds]
          lbd2=1
          sfr=sfr-1
          (lop[ds])[7]=1
      if ds>10 and ds<13:
        if dld2==0:
          dl2=lop[ds]
          dld2=1
          sfr=sfr-1
          (lop[ds])[6]=1
      if ds>12 and ds<15:
        if cb1d2==0 and (lop[ds])[6]==0:
          cb21=lop[ds]
          cb1d2=1
          sfr=sfr-1
          (lop[ds])[6]=1
        else:
          if cb2d2==0 and(lop[ds])[6]==0:
            cb22=lop[ds]
            cb2d2=1
            sfr=sfr-1
            (lop[ds])[6]=1
      if ds>14 and ds<17:
        if sd2==0:
          s2=lop[ds]
          sd2=1
          sfr=sfr-1
          (lop[ds])[6]=1
      replit.clear()
      dp=""
      if ds>0 and ds<3:
        dp="QB"
      if ds>2 and ds<5:
        dp="OL"
      if ds>4 and ds<7:
        dp="RB"
      if ds>6 and ds<9:
        dp="WR"
      if ds>8 and ds<11:
        dp="LB"
      if ds>10 and ds<13:
        dp="DL"
      if ds>12 and ds<15:
        dp="CB"
      if ds>14 and ds<17:
        dp="S"
      print("Youve drafted",dp,(lop[ds])[0],(lop[ds])[1],"Overall:",(lop[ds])[2])
      ds=0
      pause=input("Say anything to continue")
      replit.clear()
    print("Round 3 Has concluded")
    time.sleep(0.5)
    pause=input("Hit enter to view your Big Board")
    replit.clear()
    #Show QB
    if qb2[0]=="":
      print("QB : N/A")
    else:
      print("QB :",qb2[0],qb2[1],"|","overall:",qb2[2],"|")
    #Show OL
    if ol2[0]=="":
      print("OL : N/A")
    else:
      print("OL: ",ol2[0],ol2[1],"|","overall:",ol2[2],"|")
    #Show RB
    if rb2[0]=="":
      print("RB:  N/A")
    else:
      print("RB: ",rb2[0],rb2[1],"|","overall:",rb2[2],"|")
    #Show WR1
    if wr21[0]=="":
      print("WR1: N/A")
    else:
      print("WR1:",wr21[0],wr21[1],"|","overall:",wr21[2],"|")
    #Show WR2
    if wr22[0]=="":
      print("WR2: N/A")
    else:
      print("WR2:",wr22[0],wr22[1],"|","overall:",wr22[2],"|")
    #Show LB
    if lb2[0]=="":
      print("LB : N/A")
    else:
      print("LB: ",lb2[0],lb2[1],"|","overall:",lb2[2],"|")
    #Show DL
    if dl2[0]=="":
      print("DL:  N/A")
    else:
      print("DL: ",dl2[0],dl2[1],"|","overall:",dl2[2],"|")
    #Show CB1
    if cb21[0]=="":
      print("CB1: N/A")
    else:
      print("CB1:",cb21[0],cb21[1],"|","overall:",cb21[2],"|")  
    #Show CB2
    if cb22[0]=="":
      print("CB2: N/A")
    else:
      print("CB2:",cb22[0],cb22[1],"|","overall:",cb22[2],"|") 
    #Show S
    if s2[0]=="":
      print("S:   N/A")
    else:
      print("S:  ",s2[0],s2[1],"|","overall:",s2[2],"|")
    pause=input("Say anything to continue")
    replit.clear()
    #Round 4
    print("Player 2 Welcome to Round 4 of the Draft")
    print("Hit enter to continue")
    pause=input("Say anything to continue")
    replit.clear()
    sfr=1
    #QB randomized stats
    rnq1=random.randint(55,95)
    rnq2=random.randint(55,95)
    rnq3=random.randint(55,95)
    rnq4=random.randint(55,95)
    rnq5=random.randint(55,95)
    rnq6=random.randint(55,95)
    qbo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnq1+rnq2+rnq3)/3),rnq1,rnq2,rnq3,1]
    qbo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnq4+rnq5+rnq6)/3),rnq4,rnq5,rnq6,2]
    #OL randomized stats
    rnol2=random.randint(55,95)
    rnol2=random.randint(55,95)
    rnol3=random.randint(55,95)
    rnol4=random.randint(55,95)
    olo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnol2+rnol2)/2),rnol2,rnol2,3]
    olo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnol3+rnol4)/2),rnol3,rnol4,4]
    #RB randomized stats
    rnrb2=random.randint(55,95)
    rnrb2=random.randint(55,95)
    rnrb3=random.randint(55,95)
    rnrb4=random.randint(55,95)
    rbo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnrb2+rnrb2)/2),rnrb2,rnrb2,5]
    rbo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnrb3+rnrb4)/2),rnrb3,rnrb4,6]
    #WR randomized stats
    rnwr1=random.randint(55,90)
    rnwr2=random.randint(55,90)
    rnwr3=random.randint(55,95)
    rnwr4=random.randint(55,95)
    wro1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnwr1+rnwr2)/2),rnwr1,rnwr2,7]
    wro2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnwr3+rnwr4)/2),rnwr3,rnwr4,8]
    #MLB randomized stats
    rnlb2=random.randint(55,95)
    rnlb2=random.randint(55,95)
    rnlb3=random.randint(55,95)
    rnlb4=random.randint(55,95)
    rnlb5=random.randint(55,95)
    rnlb6=random.randint(55,95)
    lbo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnlb2+rnlb2+rnlb3)/3),rnlb2,rnlb2,rnlb3,9]
    lbo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rnlb4+rnlb5+rnlb6)/3),rnlb4,rnlb5,rnlb6,10]
    #DL randomized stats
    rndl2=random.randint(55,95)
    rndl2=random.randint(55,95)
    rndl3=random.randint(55,95)
    rndl4=random.randint(55,95)
    dlo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rndl2+rndl2)/2),rndl2,rndl2,11]
    dlo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rndl3+rndl4)/2),rndl3,rndl4,12]
    #CB randomized stats
    rncb1=random.randint(55,95)
    rncb2=random.randint(55,95)
    rncb3=random.randint(55,95)
    rncb4=random.randint(55,95)
    cbo1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rncb1+rncb2)/2),rncb1,rncb2,13]
    cbo2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rncb3+rncb4)/2),rncb3,rncb4,14]
    #S randomized stats
    rns2=random.randint(55,95)
    rns2=random.randint(55,95)
    rns3=random.randint(55,95)
    rns4=random.randint(55,95)
    so1=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rns2+rns2)/2),rns2,rns2,15]
    so2=[LOFN[random.randint(0,fn)],LOLN[random.randint(0,ln)],math.ceil((rns3+rns4)/2),rns3,rns4,16]
    #list of all prospects
    blanklist=[]
    lop=[blanklist,qbo1,qbo2,olo1,olo2,rbo1,rbo2,wro1,wro2,lbo1,lbo2,dlo1,dlo2,cbo1,cbo2,so1,so2]
    for item in lop:
      item.append(0)
    while sfr>0:
      print("Fourth Round")
      print("")
      print("Selections Remaining:",sfr)
      print("")
      print(qbo1[0],qbo1[1]+"[QB]","|","overall:","?","|","throwing:","?","|","running:","?","|","iq:","?","|","Draft Number:",qbo1[6],"|")
      print("")
      print(qbo2[0],qbo2[1]+"[QB]","|","overall:","?","|","throwing:","?","|","running:","?","|","iq:","?","|","Draft Number:",qbo2[6],"|")
      print("")
      print(olo1[0],olo1[1]+"[OL]","|","overall:","?","|","pass-block:","?","|","run-block:","?","|","Draft Number:",olo1[5],"|")
      print("")
      print(olo2[0],olo2[1]+"[OL]","|","overall:","?","|","pass-block:","?","|","run-block:","?","|","Draft Number:",olo2[5],"|")
      print("")
      print(rbo1[0],rbo1[1]+"[RB]","|","overall:","?","|","speed:","?","|","power:","?","|","Draft Number:",rbo1[5],"|")
      print("")
      print(rbo2[0],rbo2[1]+"[RB]","|","overall:","?","|","speed:","?","|","power:","?","|","Draft Number:",rbo2[5],"|")
      print("")
      print(wro1[0],wro1[1]+"[WR]","|","overall:","?","|","route-running:","?","|","catching:","?","|","Draft Number:",wro1[5],"|")
      print("")
      print(wro2[0],wro2[1]+"[WR]","|","overall:","?","|","route-running:","?","|","catching:","?","|","Draft Number:",wro2[5],"|")
      print("")
      print(lbo1[0],lbo1[1]+"[LB]","|","overall:","?","|","coverage:","?","|","play-rec:","?","|","run-defense:","?","|","Draft Number:",lbo1[6],"|")
      print("")
      print(lbo2[0],lbo2[1]+"[LB]","|","overall:","?","|","coverage:","?","|","play-rec:","?","|","run-defense:","?","|","Draft Number:",lbo2[6],"|")
      print("")
      print(dlo1[0],dlo1[1]+"[DL]","|","overall:","?","|","pass-rush:","?","|","run-stop:","?","|","Draft Number:",dlo1[5],"|")
      print("")
      print(dlo2[0],dlo2[1]+"[DL]","|","overall:","?","|","pass-rush:","?","|","run-stop:","?","|","Draft Number:",dlo2[5],"|")
      print("")
      print(cbo1[0],cbo1[1]+"[CB]","|","overall:","?","|","coverage:","?","|","catching:","?","|","Draft Number:",cbo1[5],"|")
      print("")
      print(cbo2[0],cbo2[1]+"[CB]","|","overall:","?","|","coverage:","?","|","catching:","?","|","Draft Number:",cbo2[5],"|")
      print("")
      print(so1[0],so1[1]+"[S]","|","overall:","?","|","play-rec:","?","|","catching:","?","|","Draft Number:",so1[5],"|")
      print("")
      print(so2[0],so2[1]+"[S]","|","overall:","?","|","play-rec:","?","|","catching:","?","|","Draft Number:",so2[5],"|")
      print("")
      ds=int(input("Select a Player: "))
      
      if ds>0 and ds<3:
        if qbd2==0:
          qb2=lop[ds]
          qbd2=1
          sfr=sfr-1
          (lop[ds])[7]=1
          
      if ds>2 and ds<5:
        if old2==0:
          ol2=lop[ds]
          old2=1
          sfr=sfr-1
          (lop[ds])[6]=1
      if ds>4 and ds<7:
        if rbd2==0:
          rb2=lop[ds]
          rbd2=1
          sfr=sfr-1
          (lop[ds])[6]=1
      if ds>6 and ds<9:
        if wr1d2==0 and (lop[ds])[6]==0:
          wr21=lop[ds]
          wr1d2=1
          sfr=sfr-1
          (lop[ds])[6]=1
        else:
          if wr2d2==0 and(lop[ds])[6]==0:
            wr22=lop[ds]
            wr2d2=1
            sfr=sfr-1
            (lop[ds])[6]=1
      if ds>8 and ds<11:
        if lbd2==0:
          lb2=lop[ds]
          lbd2=1
          sfr=sfr-1
          (lop[ds])[7]=1
      if ds>10 and ds<13:
        if dld2==0:
          dl2=lop[ds]
          dld2=1
          sfr=sfr-1
          (lop[ds])[6]=1
      if ds>12 and ds<15:
        if cb1d2==0 and (lop[ds])[6]==0:
          cb21=lop[ds]
          cb1d2=1
          sfr=sfr-1
          (lop[ds])[6]=1
        else:
          if cb2d2==0 and(lop[ds])[6]==0:
            cb22=lop[ds]
            cb2d2=1
            sfr=sfr-1
            (lop[ds])[6]=1
      if ds>14 and ds<17:
        if sd2==0:
          s2=lop[ds]
          sd2=1
          sfr=sfr-1
          (lop[ds])[6]=1
      replit.clear()
      dp=""
      if ds>0 and ds<3:
        dp="QB"
      if ds>2 and ds<5:
        dp="OL"
      if ds>4 and ds<7:
        dp="RB"
      if ds>6 and ds<9:
        dp="WR"
      if ds>8 and ds<11:
        dp="LB"
      if ds>10 and ds<13:
        dp="DL"
      if ds>12 and ds<15:
        dp="CB"
      if ds>14 and ds<17:
        dp="S"
      print("Youve drafted",dp,(lop[ds])[0],(lop[ds])[1],"Overall:",(lop[ds])[2])
      ds=0
      pause=input("Say anything to continue")
      replit.clear()
    print("Round 4 Has concluded")
    time.sleep(0.5)
    pause=input("Hit enter to view your Big Board")
    replit.clear()
    #Show QB
    if qb2[0]=="":
      print("QB : N/A")
    else:
      print("QB :",qb2[0],qb2[1],"|","overall:",qb2[2],"|")
    #Show OL
    if ol2[0]=="":
      print("OL : N/A")
    else:
      print("OL: ",ol2[0],ol2[1],"|","overall:",ol2[2],"|")
    #Show RB
    if rb2[0]=="":
      print("RB:  N/A")
    else:
      print("RB: ",rb2[0],rb2[1],"|","overall:",rb2[2],"|")
    #Show WR1
    if wr21[0]=="":
      print("WR1: N/A")
    else:
      print("WR1:",wr21[0],wr21[1],"|","overall:",wr21[2],"|")
    #Show WR2
    if wr22[0]=="":
      print("WR2: N/A")
    else:
      print("WR2:",wr22[0],wr22[1],"|","overall:",wr22[2],"|")
    #Show LB
    if lb2[0]=="":
      print("LB : N/A")
    else:
      print("LB: ",lb2[0],lb2[1],"|","overall:",lb2[2],"|")
    #Show DL
    if dl2[0]=="":
      print("DL:  N/A")
    else:
      print("DL: ",dl2[0],dl2[1],"|","overall:",dl2[2],"|")
    #Show CB1
    if cb21[0]=="":
      print("CB1: N/A")
    else:
      print("CB1:",cb21[0],cb21[1],"|","overall:",cb21[2],"|")  
    #Show CB2
    if cb22[0]=="":
      print("CB2: N/A")
    else:
      print("CB2:",cb22[0],cb22[1],"|","overall:",cb22[2],"|") 
    #Shw S
    if s2[0]=="":
      print("S:   N/A")
    else:
      print("S:  ",s2[0],s2[1],"|","overall:",s2[2],"|")
    pause=input("Say anything to continue")
    replit.clear()
else:
  T1A=["Default","Team One"]
  T2A=["Default","Team Two"]
  qb1=["Default","QB1",75,75,75,75]
  ol1=["Default","OL1",75,75,75]
  rb1=["Default","RB1",75,75,75]
  wr11=["Default","WR11",75,75,75]
  wr12=["Default","WR12",75,75,75]
  lb1=["Default","LB1",75,75,75,75]
  dl1=["Default","DL1",75,75,75]
  cb11=["Default","CB11",75,75,75]
  cb12=["Default","CB12",75,75,75]
  s1=["Default","S1",75,75,75]
  #break
  qb2=["Default","QB2",75,75,75,75]
  ol2=["Default","OL2",75,75,75]
  rb2=["Default","RB2",75,75,75]
  wr21=["Default","WR21",75,75,75]
  wr22=["Default","WR22",75,75,75]
  lb2=["Default","LB2",75,75,75,75]
  dl2=["Default","DL2",75,75,75]
  cb21=["Default","CB21",75,75,75]
  cb22=["Default","CB22",75,75,75]
  s2=["Default","S2",75,75,75]
print("Welcome to the SFL Super Bowl")
time.sleep(1.2)
print("The home team is")
time.sleep(1)
print("The",T1A[0])
time.sleep(0.8)
replit.clear()
print("The",T1A[0],T1A[1].upper())
time.sleep(3)
replit.clear()
print("The away team is")
time.sleep(1)
print("The",T2A[0])
time.sleep(0.8)
replit.clear()
print("The",T2A[0],T2A[1].upper())
time.sleep(3)
replit.clear()
print("Its time for the coin toss")

pm=0
fhp=0
shp=0
h=1
mlh=30
slh=0
ct=10
pos=0
ytt=75
ytf=10
down=1
t=20
oot=random.randint(1,2)
if oot==1:
  print("Player 1 would you like to kick or receive")
  kor=input("[K or R]").upper()
  replit.clear()
  if kor=="R":
    pos=1
    shp=2
  else:
    pos=2
    shp=1
if oot==2:
  print("Player 2 would you like to kick or receive")
  kor=input("[K or R]").upper()
  replit.clear()
  if kor=="K":
    pos=1
    shp=2
  else:
    pos=2
    shp=1
while score1<21 and score2<21:
  
  if mlh<1 and slh<0:
    h=2
  if pos==1:
    if down<5:
      if down==1:
        dstring="First Down"
      if down==2:
        dstring="Second Down"
      if down==3:
        dstring="Third Down"
      if down==4:
        dstring="Fourth Down"
      print(T1A[1]+":",score1,"    ",T2A[1]+":",score2)
      print(T1A[1],"have possesion,",dstring)
      print(ytt,"yards from the endzone and",ytf,"yards from a first")
      pause=input("Say anything to continue")
      replit.clear()
      print("Run[1],Pass[2]")
      rpfp=int(input(""))
      replit.clear()
      if rpfp==1:
        play=1
      if rpfp==2:
        print("Short[1],Medium[2],Long[3]")
        wop=int(input(""))
        replit.clear()
        play=wop+1
        if play==2:
          pm=1.2
          ming=2
          maxg=8
        if play==3:
          pm=1
          ming=10
          maxg=25
        if play==4:
          pm=0.8
          ming=math.floor(ytt/3)
          maxg=ytt
      if rpfp<3:
        print("Player 2 Select a defense")
        print("Zone[Z],Man[M],Blitz[B]")
        zmb=input("").upper()
        replit.clear()
        time.sleep(0.5)
        if zmb=="Z":
          rd=1.2
          lbzd=(lb2[3]+lb2[4])/2
          md=1.3*(s2[3]/100)*(lbzd/100)
          rush=0.4
        if zmb=="M":
          rd=0.8
          md=1.6
          rush=0.5
        if zmb=="B":
          rd=1.6
          md=0.6
          rush=1
      #Running The ball
          
      if play==1:
        yg=0
        print(qb1[1],"takes the snap")
        time.sleep(0.8)
        print("Looks like the",T1A[1],"are gonna run the ball")
        time.sleep(0.8)
        print(rb1[1],"takes the handoff")
        time.sleep(1)
        olr=ol1[4]*random.randint(50,99)
        dlr=(dl2[4]*random.randint(50,99))*rd
        if olr>dlr:
          yg=yg+random.randint(1,5)
          print("He gets past",dl2[1])
          time.sleep(0.8)
          rbr=(rb1[2]*random.randint(50,99))*0.85
      
          if lb2[4]*random.randint(50,99)>50*random.randint(50,99):
          
            lbr=(lb2[5]*random.randint(50,99))*rd
            print("Here comes",lb2[1],"trying to stop the run")
            time.sleep(0.8)
          if lb2[4]*random.randint(50,99)<50*random.randint(50,99):
            lbr=0
            print(lb2[1],"appears to be lost on the field")
            print("There goes",rb1[1])
          if rbr>lbr:
            jot=random.randint(1,2)
            if jot==1:
              print("Wow, what a juke by",rb1[1])
              rfg=random.randint(1,3)
              if rfg==1:
                yg=yg+random.randint(5,10)
              if rfg==2:
                yg=yg+random.randint(9,20)
              if rfg==3:
                yg=yg+random.randint(20,ytt)
              time.sleep(0.8)
            if jot==2:
              print(rb1[1],"muscles through",lb2[1])
              rfg=random.randint(1,3)
              if rfg==1:
                yg=yg+random.randint(5,10)
              if rfg==2:
                yg=yg+random.randint(9,20)
              if rfg==3:
                yg=yg+random.randint(7,7+ytt)
              time.sleep(0.8)
          else:
            print(lb2[1],"with a great tackle")
          
        else:
          print(dl2[1],"with a smothering tackle")
          time.sleep(0.8)
          loy=random.randint(0,4)
          if loy==0:
            print("The play goes nowhere",rb1[1],"spotted at the line of scrimmage")
            time.sleep(0.8)
          else:
            print("Great play by",dl2[1])
            time.sleep(0.8)
            print("Its a loss of",loy,"yards")
            
            time.sleep(0.8)
            ytf=ytf+loy
            ytt=ytt+loy
        
                
          
      #Passing
      if play>1 and play<5:
        print(qb1[1],"takes the snap and drops back to pass")
        time.sleep(0.8)
        olr=ol1[3]*random.randint(50,99)
        dlr=(dl2[3]*random.randint(50,99))*rush
        if olr>dlr:
          if play== 3 or 4:
            print("The line is holding up well giving",qb1[1],"lots of time to make a play")
            time.sleep(0.8)
          if zmb=="M" or "B" or "Z":
            if (wr11[3]*random.randint(50,99))*pm>(cb12[3]*random.randint(50,99))*md:
              print(wr11[1],"breaks the coverage")
              time.sleep(0.8)
              if qb1[3]*random.randint(50,99)>50*random.randint(50,99):
                print(qb1[1],"rips the ball in")
                time.sleep(0.8)
                if wr11[4]*random.randint(50,99)>50*random.randint(50,99):
                  yg=random.randint(ming,maxg)
                  print(wr11[1],"makes the grab")
                  time.sleep(0.8)
            
                else:
                  print(wr11[1],"cant reel it in")
                  time.sleep(0.8)
              else:
                print(qb1[1],"cant make the pass")
                time.sleep(0.8)
                
            else:
              print(cb21[1],"with great defense",wr11[1],"not able to get open")
              time.sleep(1.5)
              if (wr12[3]*random.randint(50,99))*pm>(cb22[3]*random.randint(50,99))*md:
                print(wr12[1],"breaks the coverage")
                time.sleep(0.8)
                if qb1[3]*random.randint(50,99)>50*random.randint(50,99):
                  print(qb1[1],"rips the ball in")
                  time.sleep(0.8)
                  if wr12[4]*random.randint(50,99)>50*random.randint(50,99):
                    yg=random.randint(ming,maxg)
                    print(wr12[1],"makes the grab")
                    time.sleep(0.8)
                  else:
                    print(wr12[1],"cant reel it in")
                    time.sleep(0.8)
                else:
                  print(qb1[1],"cant make the throw")
                  time.sleep(0.8)
              
                 
              
                    
              else:
                print(wr12[1],"also cant get open great defense by",T2A[1])
                time.sleep(0.8)
                nop=random.randint(1,3)
                if nop==1:
                  print(qb1[1],"sees nothing and throws the ball away")
                  yg=0
                  time.sleep(0.8)
                if nop==2:
                  print(qb1[1],"is gonna try to run for a gain")
                  time.sleep(0.8)
                  if qb1[5]*random.randint(50,99)>50*random.randint(50,99):
                    if qb1[4]*random.randint(50,99)>dl1[4]*(random.randint(50,99))*rd:
                      print(qb1[1],"with a dazzling move able to get past",dl2[1])
                      time.sleep(0.8)
                      if lb2[4]*random.randint(50,99)>50*random.randint(50,99):
                        print("here comes",lb2[1],"trying to stop",qb1[1])
                        time.sleep(0.8)
                        if (qb1[4]*random.randint(50,99)+qb1[5]*random.randint(50,99))/2>lb2[5]*random.randint(50,99):
                          print(qb1[1],"is too much for this defense")
                          time.sleep(0.8)
                          print("but here comes",s2[1])
                          time.sleep(0.8)
                          if (qb1[4]*random.randint(50,99)+qb1[5]*random.randint(50,99))/2>s2[3]*random.randint(50,99):
                            yg=ytt
                          else:
                            print("Theres",s2[1],"there to prevent a huge gain")
                            yg=random.randint(math.floor(ytt/10),math.ceil(ytt/2))
                        else:
                          print("Great play by",lb2[1],"great tackle")
                          yg=random.randint(1,6)
                      else:
                        if (qb1[4]*random.randint(50,99)+qb1[5]*random.randint(50,99))/2>s2[3]*random.randint(50,99):
                          yg=ytt
                    else:
                      print(dl2[1],"big tackle forcing a loss")
                      yl=random.randint(1,5)
                      time.sleep(0.8)
                      print("what a play for a loss of",yl)
                      ytf=ytf+yl
                      ytt=ytt+yl
                      time.sleep(0.8)
                  else:
                    print(dl2[1],"big tackle forcing a loss")
                    yl=random.randint(1,5)
                    time.sleep(0.8)
                    print("what a play for a loss of",yl)
                    ytf=ytf+yl
                    ytt=ytt+yl
                    time.sleep(0.8)
                if nop==3:
                  if qb1[5]*random.randint(50,99)>50*random.randint(50,99):
                    print(qb1[1],"sees nothing and throws the ball away")
                    yg=0
                    time.sleep(0.8)
                  else:
                    print(qb1[1],"is gonna heave one up")
                    time.sleep(0.8)
                    pot=random.randint(1,3)
                    wtt=random.randint(1,2)
                    wttl=[]
                    wg=random.randint(1,2)
                    wgl=[]
                    wtbt=""
                    if pot==1:
                      wtbt="left side"
                    if pot==2:
                      wtbt="center"
                    if pot==3:
                      wtbt="right side"
                    if wtt==1:
                      wttl=wr11
                    if wtt==2:
                      wttl=wr12
                    if wg==1:
                      wgl=cb21
                    if wg==2:
                      wgl=cb22
                          
                    print("Hes gonna throw it to the",wtbt,"of the field")
                    time.sleep(1)
                    print("Its a one on one ball between",wttl[1],"and",wgl[1])
                    time.sleep(1)
                    boc=random.randint(1,2)
                    if boc==1:
                      print("The ball is batted away by",wgl[1])
                      yg=0
                      time.sleep(0.8)
                    if boc==2:
                      print("it looks like...")
                      time.sleep(1.2)
                      cot=0
                      if wttl[4]*random.randint(50,99)>wgl[4]*random.randint(50,99):
                        cot=1
                      else:
                        cot=2
                      if cot==1:
                        print("Its caught")
                        time.sleep(0.8)
                        print("What a catch by",wttl[1])
                        yg=random.randint(10,ytt+10)
                        time.sleep(0.8)
                      if cot==2:
                        print("Its intercepted by",wgl[1])
                        time.sleep(0.8)
                        pos=2
                        down=1
                        ytt=100-ytt
                        ytf=10    
                  
              
            
              
        else:
          #not the problem
          print(qb1[1],"is starting to feel the pressure")
          time.sleep(1)
          print("Here comes",dl2[1])
          time.sleep(1)
          nop=random.randint(1,3)
          if nop==1:
            print(qb1[1],"sees nothing and throws the ball away")
            yg=0
            time.sleep(0.8)
          if nop==2:
            print(qb1[1],"is gonna try to run for a gain")
            time.sleep(0.8)
            if qb1[5]*random.randint(50,99)>50*random.randint(50,99):
              if qb1[4]*random.randint(50,99)>dl1[4]*(random.randint(50,99))*rd:
                print(qb1[1],"with a dazzling move able to get past",dl2[1])
                if lb2[4]*random.randint(50,99)>50*random.randint(50,99):
                  if (qb1[4]*random.randint(50,99)+qb1[5]*random.randint(50,99))/2>lb2[5]*random.randint(50,99):
                    if (qb1[4]*random.randint(50,99)+qb1[5]*random.randint(50,99))/2>s2[3]*random.randint(50,99):
                      yg=ytt
                    else:
                      print("Theres",s2[1],"there to prevent a huge gain")
                      yg=random.randint((ytt/10).floor(),(ytt/2).ceiling())
                  else:
                    print("Great play by",lb2[1],"great tackle")
                    yg=random.randint(1,6)
                else:
                  if (qb1[4]*random.randint(50,99)+qb1[5]*random.randint(50,99))/2>s2[3]*random.randint(50,99):
                    yg=ytt
              else:
                print(dl2[1],"big tackle forcing a loss")
                yg=0
                yl=random.randint(1,5)
                time.sleep(0.8)
                print("what a play for a loss of",yl)
                ytf=ytf+yl
                ytt=ytt+yl
                time.sleep(0.8)
            else:
              print(dl2[1],"big tackle forcing a loss")
              yl=random.randint(1,5)
              time.sleep(0.8)
              print("what a play for a loss of",yl)
              ytf=ytf+yl
              ytt=ytt+yl
              time.sleep(0.8)
          if nop==3:
            if qb1[5]*random.randint(50,99)>50*random.randint(50,99):
              print(qb1[1],"sees nothing and throws the ball away")
              yg=0
              time.sleep(0.8)
            else:
              print(qb1[1],"is gonna heave one up")
              time.sleep(0.8)
              pot=random.randint(1,3)
              wtt=random.randint(1,2)
              wttl=[]
              wg=random.randint(1,2)
              wgl=[]
              wtbt=""
              if pot==1:
                wtbt="left side"
              if pot==2:
                wtbt="center"
              if pot==3:
                wtbt="right side"
              if wtt==1:
                wttl=wr11
              if wtt==2:
                wttl=wr12
              if wg==1:
                wgl=cb21
              if wg==2:
                wgl=cb22
                    
              print("Hes gonna throw it to the",wtbt,"of the field")
              time.sleep(1)
              print("Its a one on one ball between",wttl[1],"and",wgl[1])
              time.sleep(1)
              boc=random.randint(1,2)
              if boc==1:
                print("The ball is batted away by",wgl[1])
                yg=0
                time.sleep(0.8)
              if boc==2:
                print("it looks like...")
                time.sleep(1.2)
                cot=0
                if wttl[4]*random.randint(50,99)>wgl[4]*random.randint(50,99):
                  cot=1
                else:
                  cot=2
                if cot==1:
                  print("Its caught")
                  time.sleep(0.8)
                  print("What a catch by",wttl[1])
                  yg=random.randint(10,ytt+10)
                  time.sleep(0.8)
                if cot==2:
                  print("Its intercepted by",wgl[1])
                  time.sleep(0.8)
                  pos=2
                  ytt=100-ytt
                  down=1
                  ytf=10
                        
                    
                      
                    
                    
                    
          
          
      ytt=ytt-yg   
      ytf=ytf-yg
      down=down+1
      if ytt<1:
        print("Touchdown!!!!")
        print(T1A[1])
        pause=input("Say anything to continue")
        replit.clear()
        down=1
        score1=score1+7
        pos=2
        ytt=75
        ytf=10
      else:
        if yg>ytt:
            print("The gain is",yg,"yards")
        else:
          if yg>0:
            print("The gain is",yg,"yards")
          else:
            pass
        
        
          
          
          
        if ytf<0:
          ytf=10
          down=1
        pause=input("Say anything to continue")
        replit.clear()            
        yg=0
                
              
    else:
      down=1
      pos=2
      ytt=100-ytt
      ytf=10
  if pos==2:
    if down<5:
      if down==1:
        dstring="First Down"
      if down==2:
        dstring="Second Down"
      if down==3:
        dstring="Third Down"
      if down==4:
        dstring="Fourth Down"
      print(T1A[1]+":",score1,"    ",T2A[1]+":",score2)
      print(T2A[1],"have possesion,",dstring)
      print(ytt,"yards from the endzone and",ytf,"yards from a first")
      pause=input("Say anything to continue")
      replit.clear()
      print("Run[1],Pass[2]")
      rpfp=int(input(""))
      replit.clear()
      if rpfp==1:
        play=1
      if rpfp==2:
        print("Short[1],Medium[2],Long[3]")
        wop=int(input(""))
        replit.clear()
        play=wop+1
        if play==2:
          pm=1.2
          ming=2
          maxg=8
        if play==3:
          pm=1
          ming=10
          maxg=25
        if play==4:
          pm=0.8
          ming=math.floor(ytt/3)
          maxg=ytt
      if rpfp<3:
        print("Player 1 Select a defense")
        print("Zone[Z],Man[M],Blitz[B]")
        zmb=input("").upper()
        replit.clear()
        time.sleep(0.5)
        if zmb=="Z":
          rd=1.2
          lbzd=(lb1[3]+lb1[4])/2
          md=1.3*(s1[3]/100)*(lbzd/100)
          rush=0.4
        if zmb=="M":
          rd=0.8
          md=1.6
          rush=0.7
        if zmb=="B":
          rd=1.6
          md=0.6
          rush=1.2
      #Running The ball
          
      if play==1:
        yg=0
        print(qb2[1],"takes the snap")
        time.sleep(0.8)
        print("Looks like the",T2A[1],"are gonna run the ball")
        time.sleep(0.8)
        print(rb2[1],"takes the handoff")
        time.sleep(1)
        olr=ol2[4]*random.randint(50,99)
        dlr=(dl1[4]*random.randint(50,99))*rd
        if olr>dlr:
          yg=yg+random.randint(1,5)
          print("He gets past",dl1[1])
          time.sleep(0.8)
          rbr=(rb2[2]*random.randint(50,99))*0.85
      
          if lb1[4]*random.randint(50,99)>50*random.randint(50,99):
          
            lbr=(lb1[5]*random.randint(50,99))*rd
            print("Here comes",lb2[1],"trying to stop the run")
            time.sleep(0.8)
          if lb1[4]*random.randint(50,99)<50*random.randint(50,99):
            lbr=0
            print(lb2[1],"appears to be lost on the field")
            print("There goes",rb2[1])
          if rbr>lbr:
            jot=random.randint(1,2)
            if jot==1:
              print("Wow, what a juke by",rb2[1])
              rfg=random.randint(1,3)
              if rfg==1:
                yg=yg+random.randint(5,10)
              if rfg==2:
                yg=yg+random.randint(9,20)
              if rfg==3:
                yg=yg+random.randint(20,ytt)
              time.sleep(0.8)
            if jot==2:
              print(rb2[1],"muscles through",lb1[1])
              rfg=random.randint(1,3)
              if rfg==1:
                yg=yg+random.randint(5,10)
              if rfg==2:
                yg=yg+random.randint(9,20)
              if rfg==3:
                yg=yg+random.randint(7,7+ytt)
              time.sleep(0.8)
          else:
            print(lb1[1],"with a great tackle")
          
        else:
          print(dl1[1],"with a smothering tackle")
          time.sleep(0.8)
          loy=random.randint(0,4)
          if loy==0:
            print("The play goes nowhere",rb2[1],"spotted at the line of scrimmage")
            time.sleep(0.8)
          else:
            print("Great play by",dl1[1])
            time.sleep(0.8)
            print("Its a loss of",loy,"yards")
            
            time.sleep(0.8)
            ytf=ytf+loy
            ytt=ytt+loy
        
                
          
      #Passing
      if play>1 and play<5:
        print(qb2[1],"takes the snap and drops back to pass")
        time.sleep(0.8)
        olr=ol2[3]*random.randint(50,99)
        dlr=(dl1[3]*random.randint(50,99))*rush
        if olr>dlr:
          if play== 3 or 4:
            print("The line is holding up well giving",qb2[1],"lots of time to make a play")
            time.sleep(0.8)
          if zmb=="M" or "B" or "Z":
            if (wr21[3]*random.randint(50,99))*pm>(cb11[3]*random.randint(50,99))*md:
                print(wr21[1],"breaks the coverage")
                time.sleep(0.8)
                
                if qb2[3]*random.randint(50,99)>50*random.randint(50,99):
                  print(qb2[1],"rips the ball in")
                  time.sleep(0.8)
                  if wr21[4]*random.randint(50,99)>50*random.randint(50,99):
                    yg=random.randint(ming,maxg)
                    print(wr21[1],"makes the grab")
                    time.sleep(0.8)
                  else:
                    print(wr21[1],"cant reel it in")
                    time.sleep(0.8)
                else:
                  print(qb2[1],"cant make the throw")
                  
            else:
              print(wr21[1],"unable to get open great defense by",cb11[1])
              time.sleep(1.5)
              if (wr22[3]*random.randint(50,99))*pm>(cb12[3]*random.randint(50,99))*md:
                print(wr22[1],"breaks the coverage")
                time.sleep(0.8)
                
                if qb2[3]*random.randint(50,99)>50*random.randint(50,99):
                  print(qb2[1],"rips the ball in")
                  time.sleep(0.8)
                  if wr22[4]*random.randint(50,99)>50*random.randint(50,99):
                    yg=random.randint(ming,maxg)
                    print(wr22[1],"makes the grab")
                    time.sleep(0.8 )
                  else:
                    print(wr22[1],"cant reel it in")
                    time.sleep(0.8)
                else:
                  print(qb2[1],"cant make the throw")
                  
              
                    
              else:
                print(wr22[1],"also cant get open great defense by",T2A[1])
                time.sleep(0.8)
                nop=random.randint(1,3)
                if nop==1:
                  print(qb2[1],"sees nothing and throws the ball away")
                  yg=0
                  time.sleep(0.8)
                if nop==2:
                  print(qb2[1],"is gonna try to run for a gain")
                  time.sleep(0.8)
                  if qb2[5]*random.randint(50,99)>50*random.randint(50,99):
                    if qb2[4]*random.randint(50,99)>dl1[4]*(random.randint(50,99))*rd:
                      print(qb2[1],"with a dazzling move able to get past",dl2[1])
                      time.sleep(0.8)
                      if lb1[4]*random.randint(50,99)>50*random.randint(50,99):
                        print("here comes",lb1[1],"trying to stop",qb1[1])
                        time.sleep(0.8)
                        if (qb2[4]*random.randint(50,99)+qb1[5]*random.randint(50,99))/2>lb1[5]*random.randint(50,99):
                          print(qb2[1],"is too much for this defense")
                          time.sleep(0.8)
                          print("but here comes",s1[1])
                          time.sleep(0.8)
                          if (qb2[4]*random.randint(50,99)+qb2[5]*random.randint(50,99))/2>s1[3]*random.randint(50,99):
                            yg=ytt
                          else:
                            print("Theres",s1[1],"there to prevent a huge gain")
                            yg=random.randint(math.floor(ytt/10),math.ceil(ytt/2))
                        else:
                          print("Great play by",lb1[1],"great tackle")
                          yg=random.randint(1,6)
                      else:
                        if (qb1[4]*random.randint(50,99)+qb1[5]*random.randint(50,99))/2>s2[3]*random.randint(50,99):
                          yg=ytt
                    else:
                      print(dl1[1],"big tackle forcing a loss")
                      yl=random.randint(1,5)
                      time.sleep(0.8)
                      print("what a play for a loss of",yl)
                      ytf=ytf+yl
                      ytt=ytt+yl
                      time.sleep(0.8)
                  else:
                    print(dl1[1],"big tackle forcing a loss")
                    yl=random.randint(1,5)
                    time.sleep(0.8)
                    print("what a play for a loss of",yl)
                    ytf=ytf+yl
                    ytt=ytt+yl
                    time.sleep(0.8)
                if nop==3:
                  if qb2[5]*random.randint(50,99)>50*random.randint(50,99):
                    print(qb2[1],"sees nothing and throws the ball away")
                    yg=0
                    time.sleep(0.8)
                  else:
                    print(qb2[1],"is gonna heave one up")
                    time.sleep(0.8)
                    pot=random.randint(1,3)
                    wtt=random.randint(1,2)
                    wttl=[]
                    wg=random.randint(1,2)
                    wgl=[]
                    wtbt=""
                    if pot==1:
                      wtbt="left side"
                    if pot==2:
                      wtbt="center"
                    if pot==3:
                      wtbt="right side"
                    if wtt==1:
                      wttl=wr21
                    if wtt==2:
                      wttl=wr22
                    if wg==1:
                      wgl=cb11
                    if wg==2:
                      wgl=cb12
                          
                    print("Hes gonna throw it to the",wtbt,"of the field")
                    time.sleep(1)
                    print("Its a one on one ball between",wttl[1],"and",wgl[1])
                    time.sleep(1)
                    boc=random.randint(1,2)
                    if boc==1:
                      print("The ball is batted away by",wgl[1])
                      yg=0
                      time.sleep(0.8)
                    if boc==2:
                      print("it looks like...")
                      time.sleep(1.2)
                      cot=0
                      if wttl[4]*random.randint(50,99)>wgl[4]*random.randint(50,99):
                        cot=1
                      else:
                        cot=2
                      if cot==1:
                        print("Its caught")
                        time.sleep(0.8)
                        print("What a catch by",wttl[1])
                        yg=random.randint(10,ytt+10)
                        time.sleep(0.8)
                      if cot==2:
                        print("Its intercepted by",wgl[1])
                        time.sleep(0.8)
                        pos=1
                        ytt=100-ytt
                        down=1
                        ytf=10    
        else:
          print(qb2[1],"is starting to feel the pressure")
          time.sleep(1)
          print("Here comes",dl1[1])
          time.sleep(1)
          nop=random.randint(1,3)
          if nop==1:
            print(qb2[1],"sees nothing and throws the ball away")
            yg=0
            time.sleep(0.8)
          if nop==2:
            print(qb2[1],"is gonna try to run for a gain")
            time.sleep(0.8)
            if qb2[5]*random.randint(50,99)>50*random.randint(50,99):
              if qb2[4]*random.randint(50,99)>dl1[4]*(random.randint(50,99))*rd:
                print(qb2[1],"with a dazzling move able to get past",dl2[1])
                time.sleep(0.8)
                if lb1[4]*random.randint(50,99)>50*random.randint(50,99):
                  print("here comes",lb1[1],"trying to stop",qb1[1])
                  time.sleep(0.8)
                  if (qb2[4]*random.randint(50,99)+qb1[5]*random.randint(50,99))/2>lb1[5]*random.randint(50,99):
                    print(qb2[1],"is too much for this defense")
                    time.sleep(0.8)
                    print("but here comes",s1[1])
                    time.sleep(0.8)
                    if (qb2[4]*random.randint(50,99)+qb2[5]*random.randint(50,99))/2>s1[3]*random.randint(50,99):
                      yg=ytt
                    else:
                      print("Theres",s1[1],"there to prevent a huge gain")
                      yg=random.randint(math.floor(ytt/10),math.ceil(ytt/2))
                  else:
                    print("Great play by",lb1[1],"great tackle")
                    yg=random.randint(1,6)
                else:
                  if (qb1[4]*random.randint(50,99)+qb1[5]*random.randint(50,99))/2>s2[3]*random.randint(50,99):
                    yg=ytt
              else:
                print(dl1[1],"big tackle forcing a loss")
                yl=random.randint(1,5)
                time.sleep(0.8)
                print("what a play for a loss of",yl)
                ytf=ytf+yl
                ytt=ytt+yl
                time.sleep(0.8)
            else:
              print(dl1[1],"big tackle forcing a loss")
              yl=random.randint(1,5)
              time.sleep(0.8)
              print("what a play for a loss of",yl)
              ytf=ytf+yl
              ytt=ytt+yl
              time.sleep(0.8)
          if nop==3:
            if qb2[5]*random.randint(50,99)>50*random.randint(50,99):
              print(qb2[1],"sees nothing and throws the ball away")
              yg=0
              time.sleep(0.8)
            else:
              print(qb2[1],"is gonna heave one up")
              time.sleep(0.8)
              pot=random.randint(1,3)
              wtt=random.randint(1,2)
              wttl=[]
              wg=random.randint(1,2)
              wgl=[]
              wtbt=""
              if pot==1:
                wtbt="left side"
              if pot==2:
                wtbt="center"
              if pot==3:
                wtbt="right side"
              if wtt==1:
                wttl=wr21
              if wtt==2:
                wttl=wr22
              if wg==1:
                wgl=cb11
              if wg==2:
                wgl=cb12
                          
              print("Hes gonna throw it to the",wtbt,"of the field")
              time.sleep(1)
              print("Its a one on one ball between",wttl[1],"and",wgl[1])
              time.sleep(1)
              boc=random.randint(1,2)
              if boc==1:
                print("The ball is batted away by",wgl[1])
                yg=0
                time.sleep(0.8)
              if boc==2:
                print("it looks like...")
                time.sleep(1.2)
                cot=0
                if wttl[4]*random.randint(50,99)>wgl[4]*random.randint(50,99):
                  cot=1
                else:
                  cot=2
                if cot==1:
                  print("Its caught")
                  time.sleep(0.8)
                  print("What a catch by",wttl[1])
                  yg=random.randint(10,ytt+10)
                  time.sleep(0.8)
                if cot==2:
                  print("Its intercepted by",wgl[1])
                  time.sleep(0.8)
                  pos=1
                  ytt=100-ytt
                  down=1
                  ytf=10 
              
            
              
        
                        
                    
                      
                    
                    
                    
          
      ytt=ytt-yg   
      ytf=ytf-yg
      down=down+1
      if ytt<1:
        print("Touchdown!!!!")
        print(T2A[1])
        pause=input("Say anything to continue")
        replit.clear()
        down=1
        score2=score2+7
        pos=1
        ytt=75
        ytf=10
      else:
        if yg>ytt:
            print("The gain is",yg,"yards")
        else:
          if yg>0:
            print("The gain is",yg,"yards")
          else:
            pass
        
        
          
          
          
        if ytf<0:
          ytf=10
          down=1
        pause=input("Say anything to continue")
        replit.clear()            
        yg=0
                
              
    else:
      down=1
      pos=1
      ytt=100-ytt  
      ytf=10
    
    
    
    
  
  



if score1>20:
	print("In the end",T1A[1],"comes out on top")
	print("The final score being")
	print(T1A+":",score1)
	print(T2A+":",score2)