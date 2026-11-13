from ion import keydown
from kandinsky import draw_string,fill_rect
from time import sleep,monotonic

new,wait=True,True
n,bl=(0,)*3,(255,)*3
color=[(0,0,0),(140,140,140),(230,0,0),(0,230,0),(0,0,230),(255,135,0),(255,235,0),(230,0,230),(0,230,230),(230,170,180),(150,0,0),(0,150,0)]
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ",",",".","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," ","?","!","[","]","{","}","<",">","_",":","=","π","√","~","7","8","9","(",")","4","5","6","*","/","1","2","3","+","-","0",".",'"',"\\","^","∞","_","→","%",";","≠","≈","|","°","±","@","#","&"," "," "," "," "," "," "," "," "," "," "," "," "," "]
keyboard=[18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,42,43,44,45,46,48,49]
text,char,oqp,saco=[" " for i in range(384)],[0 for i in range(12)],[0 for i in range(12)],[0 for i in range(384)]
a,l,aa,ti,ch,lo,coul,ma,col,dc=0,0,0,monotonic(),1,1,color[0],0,color[0],0
fill_rect(0,0,320,222,color[dc])

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
  elif monotonic()-ti>0.5: #curseur
    ti=monotonic()
    if ch==1:
      fill_rect(a,l,lo,18,coul)
      ch=2
    else:
      fill_rect(a,l,lo,18,bl)
      ch=1
