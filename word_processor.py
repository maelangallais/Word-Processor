#Créé le 13 Novembre 2023
from math import pi,radians,cos,sin
from ion import keydown
from kandinsky import draw_string,fill_rect
from time import sleep,monotonic

new,wait=True,True
n,bl=(0,)*3,(255,)*3
color=[(0,0,0),(140,140,140),(230,0,0),(0,230,0),(0,0,230),(255,135,0),(255,235,0),(230,0,230),(0,230,230),(230,170,180),(150,0,0),(0,150,0)]

def d(x,y,r,a,col=n):
  s=int(2*pi*r)+1
  ai=radians(a)
  for i in range(int(s/2)+1):
    ag=i/s*2*pi+ai
    xp=x+r*cos(ag)
    yp=y-r*sin(ag)
    fill_rect(round(xp),round(yp),1,1,col)

alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ",",",".","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," ","?","!","[","]","{","}","<",">","_",":","=","π","√","~","7","8","9","(",")","4","5","6","*","/","1","2","3","+","-","0",".",'"',"\\","^","∞","_","→","%",";","≠","≈","|","°","±","@","#","&"," "," "," "," "," "," "," "," "," "," "," "," "," ","à","â","ä"," "," "," ","é","è","ê","ë"," "," ","î","ï"," "," "," ","ô","ö"," "," "," ","ù","û","ü"," "," ","ÿ","ç"]
keyboard=[18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,42,43,44,45,46,48,49]
text,char,oqp,saco=[" " for i in range(384)],[0 for i in range(12)],[0 for i in range(12)],[0 for i in range(384)]
a,l,aa,ti,ch,lo,coul,ma,col,dc=0,0,0,monotonic(),1,1,color[0],0,color[0],0
lc=0
fill_rect(0,0,320,222,color[dc])

hsp,vsp=11,7
fbh,lbh=20,25
fbw,lbw=41,52
def dcmp(): #Display Character Map Preview
  def dss(x,y,w=10,h=4):  #Draw Space Symbol
    fill_rect(x,y-h,1,h,n)
    fill_rect(x,y,w,1,n)
    fill_rect(x+w-1,y-h,1,h,n)
  def dbs(x,y):  #Draw Backspace Symbol
    fill_rect(x+1,y+6,7,1,n)
    fill_rect(x+2,y+5,1,3,n)
    fill_rect(x+3,y+4,1,5,n)
  def des(x,y):  #Draw Enter Symbol
    fill_rect(x+7,y+2,1,5,n)
    fill_rect(x+1,y+6,7,1,n)
    fill_rect(x+2,y+5,1,3,n)
    fill_rect(x+3,y+4,1,5,n)
  fill_rect(0,0,320,222,bl)
  fcr,lcr=fbh//2,lbh//2
  fbth,lbth=vsp+fbh,vsp+lbh
  fbtw,lbtw=hsp+fbw,hsp+lbw
  fls,lls=fbw-fbh,lbw-lbh
  for y in range(1,4):
    #cy=vsp+(fbh+vsp)*y+fbh/2
    #  =vsp*(y+1)+fbh*(y+1/2)
    #Si on commence à y=1 :
    #cy=vsp*y+fbh*(y-1/2)
    #  =(vsp+fbh)*y-fbh/2
    #cy=fbth*y-fcr
    ycc=fbth*y-fcr
    for x in range(1,7):
      #cx=hsp+(fbw+hsp)*x+fcr
      xcc=fbtw*x-fbw+fcr
      d(xcc,ycc,fcr,90)
      d(xcc+fls,ycc,fcr,270)
      fill_rect(xcc,ycc-fcr,fls,1,n)
      fill_rect(xcc,ycc+fcr,fls,1,n)
      sx,sy=xcc+fls//2-4,ycc-8
      if y==1:
        sx=xcc+fls//2-14
        if x==1:draw_string("A-Z",sx,sy)
        elif x==2:draw_string("1-9",sx,sy)
        elif x==3:draw_string("@&#",sx,sy)
        elif x==4:draw_string("à-é",sx,sy)
        elif x==5:draw_string("col",sx,sy,color[(dc+1)%len(color)])
        elif x==6:dbs(sx+10,sy+2)
      else:
        i=(y-2)*6+(x-1)+ma
        draw_string(alphabet[i],sx,sy)
  for y in range(1,5):
    #cy=vsp+(fbh+vsp)*3+(lbh+vsp)*y+lbh/2
    #  =vsp*4+fbh*3+vsp*y+lbh*(y+1/2)
    #  =vsp*(y+4)+fbh*3+lbh*(y+1/2)
    #Si on commence à 1 :
    #cy=fbth*3+lbth*y-lcr
    ycc=fbth*3+lbth*y-lcr
    for x in range(1,6):
      xcc=lbtw*x-lbw+lcr
      d(xcc,ycc,lcr,90)
      d(xcc+lls,ycc,lcr,270)
      fill_rect(xcc,ycc-lcr,lls,1,n)
      fill_rect(xcc,ycc+lcr,lls,1,n)
      sx,sy=xcc+lls//2-4,ycc-8
      if y==4 and x>2:
        if x==3:draw_string("map",xcc+lls//2-14,sy)
        elif x==4:draw_string("last",xcc+lls//2-19,sy)
        elif x==5:des(sx,sy+3)
      else:
        i=12+(y-1)*5+(x-1)+ma
        if i==26 or i==55:dss(sx,sy+14)
        else:draw_string(alphabet[i],sx,sy)

while not keydown(5):
  if new:   #actualisation de l'écran
    new,t=False,monotonic()
    for b in range(12):
      for c in range(32):
        draw_string(text[b*32+c],c*10,b*18,color[saco[b*32+c]])
    fill_rect(a,l,lo,18,coul)
    if wait:
      for i in range(53):
        if keydown(i):
          te=i
          while keydown(i):
            if monotonic()-t>0.5:
              wait=False
              break
            else:sleep(0.1-(monotonic()-t))
    else:
      if not keydown(te):wait,te=True,0
  for i in range(29):   #clavier
    if keydown(keyboard[i]):
      lc=i+ma
      saco[l//18*32+a//10]=dc
      draw_string(str(alphabet[i+ma]),a,l,color[dc])
      char[l//18]+=1
      if a<310:a+=10
      else:
        if l<198:
          l+=18
          a=0
      text[l//18*32+a//10-1]=alphabet[i+ma]
      fill_rect(a,l,lo,18,coul),sleep(0.1)
      new,aa=True,a//10
      break
  if keydown(17):   #backspace
    if a>0 or l>0:
      char[l//18]-=1
      if a==0 and l>0:oqp[l//18]=0
      if a>0:a-=10
      else:
        if l>0:
          l-=18
          a=char[l//18]*10
      fill_rect(a,l,11,18,bl),fill_rect(a,l,lo,18,coul),sleep(0.05)
      text[l//18*32+a//10]=alphabet[26]
    new,aa=True,a//10
  elif keydown(52):   #retour à la ligne
    if l//18<11:
      l+=18
      new,a,aa,oqp[l//18]=True,0,0,1
  elif keydown(12):   #shift
    if ma==58:ma,lo,coul=0,1,color[0]
    else:ma,lo,coul=58,10,color[2]
    new=True
  elif keydown(13):  #alpha
    if ma==29:ma,lo,coul=0,1,color[0]
    else:ma,lo,coul=29,10,color[3]
    new=True
  elif keydown(14):   #cut
    if ma==87:ma,lo,coul=0,1,color[0]
    else:ma,lo,coul=87,10,color[4]
    new=True
  elif keydown(15):   #copy
    if ma==116:ma,lo,coul=0,1,color[0]
    else:ma,lo,coul=116,10,color[5]
    new=True
  elif keydown(16):   #couleur
    if dc<len(color)-1:dc+=1
    else:dc=0
    fill_rect(0,216,320,6,color[dc])
    new=True
  elif keydown(0):  #gauche
    if a>0:a-=10
    else:
      if l>0:
        l-=18
        a=char[l//18]*10
    new,aa=True,a//10
  elif keydown(3):  #droite
    if a<310 and char[l//18]>a//10:a+=10
    else:
      if l<216 and oqp[l//18+1]==1:
        l+=18
        a=0
    new,aa=True,a//10
  elif keydown(1):  #haut
    if l>0:l-=18
    if char[l//18]>=aa:a=aa*10
    elif char[l//18]<a//10:a=char[l//18]*10
    else:a=char[l//18]*10
    new=True
  elif keydown(2):  #bas
    if char[l//18+1]!=0 and char[l//18+1]>=a//10 or char[l//18]==32 or oqp[l//18+1]==1:
      if l<198:l+=18
    if char[l//18]>=aa:a=aa*10
    elif char[l//18]<a//10:a=char[l//18]*10
    else:a=char[l//18]*10
    new=True
  elif keydown(50):  #x10^
    dcmp()
    while not keydown(50):
      pass
    fill_rect(0,216,320,6,color[dc])
    new=True
  elif keydown(51):  #ANS
    saco[l//18*32+a//10]=dc
    draw_string(str(alphabet[lc]),a,l,color[dc])
    char[l//18]+=1
    if a<310:a+=10
    else:
      if l<198:
        l+=18
        a=0
    text[l//18*32+a//10-1]=alphabet[lc]
    fill_rect(a,l,lo,18,coul),sleep(0.1)
    new,aa=True,a//10
  elif monotonic()-ti>0.5: #curseur
    ti=monotonic()
    if ch==1:
      fill_rect(a,l,lo,18,coul)
      ch=2
    else:
      fill_rect(a,l,lo,18,bl)
      ch=1
