import pygame 
from PIL import Image
from time import sleep
import datetime
from random import randint 

br=Image.open("traffic_runner_background2.png")

game=True 

decalage_mv_du_bck=0
pygame.init()
bck_im=br.crop((0,br.size[1]-(800)+decalage_mv_du_bck,br.size[0],br.size[1]-decalage_mv_du_bck))
bck_im.save("bck_im.png")

fenetre=pygame.display.set_mode((bck_im.size[0],bck_im.size[1]))
pygame.display.set_caption("traffic runner")
   
#les positions des voix 
position_voix_gd=(300,-2000)
position_voix_dg=(450,-500)
position_voix_dd=(565,-500)
position_voix_gg=(180,-2000)

#seconde
pre_seconde=0
00000
#selection de la voiture    
i_voiture_ai=0
i_voiture_a=0


#deceleration  et acceleration progressive 
elan=0
acceleration=7/40 # 7/40
#limite vitesse
l_v_m_c=60		# 30km + par 10  //start= 60
#vitesse_bck
vitesse_bck=20
#freinage 
freinage=3/4    # 3/4
#score
score=0
#voiture et pos
image_voiture= pygame.image.load("car bird view 3.png")
image_voiture = pygame.transform.scale(image_voiture, (100,150))
position_voiture=(position_voix_dd[0],600)


image_voiture_a2= pygame.image.load("car bird view a2.jpg")
image_voiture_a2 = pygame.transform.scale(image_voiture_a2, (100,150))
position_voiture_a2=[[-100,0]for i in range(50)]


image_voiture_ai1= pygame.image.load("car bird view.jfif")
image_voiture_ai1 = pygame.transform.scale(image_voiture_ai1, (100,175))
position_voiture_ai1=[[-100,0]for i in range (50) ]

#image game over 
im_gm=pygame.image.load("game over car.png")

#image explosion
explosion=pygame.image.load("explosion_voi.png")
explosion = pygame.transform.scale(explosion, (200,200))


def dessin_road():
	bck_im=br.crop((0,br.size[1]-(800+decalage_mv_du_bck),br.size[0],br.size[1]-decalage_mv_du_bck))
	bck_im.save("bck_im.png")
	background_image=pygame.image.load("bck_im.png")
	fenetre.blit(background_image,(0,0))
	pygame.display.flip()
def dessin_voitures():
	fenetre.blit(image_voiture, position_voiture)#affiche la voiture 

	for i in range(len(position_voiture_a2)):
		fenetre.blit(image_voiture_a2,(position_voiture_a2[i][0],position_voiture_a2[i][1]))

	for i in range(len(position_voiture_ai1)):
		fenetre.blit(image_voiture_ai1,(position_voiture_ai1[i][0],position_voiture_ai1[i][1] ))

	pygame.display.flip()#rafraichissement de l'ecran 
def gerer_le_fond():
	global decalage_mv_du_bck ,elan , vitesse_bck , touchesPressees
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
				pygame.quit()
	touchesPressees = pygame.key.get_pressed() 
	if touchesPressees[pygame.K_UP]==True  or touchesPressees[pygame.K_w] == True or touchesPressees[pygame.K_SPACE] == True:
	

		decalage_mv_du_bck+=elan
		
		
		if decalage_mv_du_bck>=br.size[1]-800:
			decalage_mv_du_bck=0

		if elan < l_v_m_c:

			elan+=acceleration
		
	if elan>0  and (touchesPressees[pygame.K_UP]==False  and touchesPressees[pygame.K_w] == False and touchesPressees[pygame.K_SPACE] == False):
		
		elan-=7/80
		decalage_mv_du_bck+=elan
	
	
		if elan <(0.09):
			elan=0
		

		
	if touchesPressees[pygame.K_DOWN] == False and touchesPressees[pygame.K_s] == False: 
		if vitesse_bck>=7 and vitesse_bck<=19:
			vitesse_bck+=1			
		else:
			vitesse_bck=20

	elif  touchesPressees[pygame.K_DOWN] == True or touchesPressees[pygame.K_s] == True:
		if vitesse_bck>=8:
			vitesse_bck-=1
	decalage_mv_du_bck+=vitesse_bck
	
	#if elan>0  and (touchesPressees[pygame.K_UP]==False  and touchesPressees[pygame.K_w] == False and touchesPressees[pygame.K_SPACE] == False):
	#	decalage_mv_du_bck+=elan



	if decalage_mv_du_bck>=br.size[1]-800:
		decalage_mv_du_bck=0
	if touchesPressees[pygame.K_DOWN]==True:
		if elan>=freinage:
			elan-=freinage

def mouvement_voiture():
	global position_voiture  ,touchesPressees
	
	
	boost_lateral=0.5*elan

	
	if position_voiture [0]>=120:  #gauche si la position ne depasse pas une limite 
		if touchesPressees[pygame.K_LEFT]==True or touchesPressees[pygame.K_a] == True:
			position_voiture=(position_voiture[0]-(10+boost_lateral) , position_voiture[1])

	if position_voiture [0]<610:
		if touchesPressees[pygame.K_RIGHT]==True or touchesPressees[pygame.K_d]  == True:
			position_voiture=(position_voiture[0]+(10+boost_lateral), position_voiture[1])
 	

def gerer_other_cars():
	global position_voiture_a2 , position_voiture_ai1 ,touchesPressees
	
	if touchesPressees[pygame.K_UP]==True  or touchesPressees[pygame.K_w] == True or touchesPressees[pygame.K_SPACE] == True:
		for i in range (len(position_voiture_a2)):
			position_voiture_a2[i]=(position_voiture_a2[i][0],position_voiture_a2[i][1]+elan)
		for i in range(len(position_voiture_ai1)):	
			position_voiture_ai1[i]=(position_voiture_ai1[i][0],position_voiture_ai1[i][1]+elan)
	for i in range(len(position_voiture_ai1)):	
		position_voiture_ai1[i]=(position_voiture_ai1[i][0],position_voiture_ai1[i][1]+20)		

	
	if touchesPressees[pygame.K_DOWN] == True or touchesPressees[pygame.K_s] == True:
		for i in range (len(position_voiture_a2)):
			position_voiture_a2[i]=(position_voiture_a2[i][0],position_voiture_a2[i][1]-7)
		for i in range(len(position_voiture_ai1)):
			position_voiture_ai1[i]=(position_voiture_ai1[i][0],position_voiture_ai1[i][1]-7)
	if elan>0  and (touchesPressees[pygame.K_UP]==False  and touchesPressees[pygame.K_w] == False and touchesPressees[pygame.K_SPACE] == False):
		for i in range (len(position_voiture_a2)):
			position_voiture_a2[i]=(position_voiture_a2[i][0],position_voiture_a2[i][1]+elan)
		for i in range(len(position_voiture_ai1)):
			position_voiture_ai1[i]=(position_voiture_ai1[i][0],position_voiture_ai1[i][1]+elan)

	#for i in range (len(position_voiture_a2)):
	#	if position_voiture_a2[i][1]<=-500 :
	#		position_voiture_a2[i]=position_voiture_a2[i][0],position_voiture_a2[i][1]+10

def traffic():
	global pre_seconde , position_voix_gg,position_voix_gd,position_voix_dg, position_voix_dd,i_voiture_ai,i_voiture_a , touchesPressees , vitesse
	t=datetime.datetime.today()
	temps=[t.strftime("%A,%B %d,%Y")[:2],t.second]
	seconde=temps[1]
	
	if seconde%4==0 and  seconde!=pre_seconde :
		voix_ch_l=[]
		voix_ch_r=[]
		for i in range (2):

			voix_chl=randint(1,2)#hasard dans la voix choisit /gauche
			voix_ch_l.append(voix_chl)

			voix_chr=randint(1,2)#hasard dans la voix choisit /droite 
			voix_ch_r.append(voix_chr)

		if i_voiture_ai==50:
			i_voiture_ai=0

		if i_voiture_a==50:
			i_voiture_a=0	

		if voix_ch_l[0]==1 :
			position_voiture_ai1[i_voiture_ai]=(position_voix_gg)
			i_voiture_ai+=1

		if  voix_ch_l[1]==1:
			position_voiture_ai1[i_voiture_ai]=(position_voix_gg[0],position_voix_gg[1]-randint(180,400))
			i_voiture_ai+=1

		if voix_ch_l[0]==2 :
			position_voiture_ai1[i_voiture_ai]=(position_voix_gd)
			i_voiture_ai+=1

		if voix_ch_l[1]==2:
			position_voiture_ai1[i_voiture_ai]=(position_voix_gd[0],position_voix_gd[1]-randint(180,400))
			i_voiture_ai+=1



		if ((touchesPressees[pygame.K_UP]==True  or touchesPressees[pygame.K_w] == True or touchesPressees[pygame.K_SPACE] == True)and vitesse>=100) or vitesse>=100:
			if voix_ch_r[0]==1 :
				position_voiture_a2[i_voiture_a]=(position_voix_dg)
				i_voiture_a+=1
				

			if  voix_ch_r[1]==1:
				position_voiture_a2[i_voiture_a]=(position_voix_dg[0],position_voix_dg[1]-randint(160,400))
				i_voiture_a+=1
				

			if voix_ch_r[0]==2 :
				position_voiture_a2[i_voiture_a]=(position_voix_dd)
				i_voiture_a+=1
				
			if voix_ch_r[1]==2:
				position_voiture_a2[i_voiture_a]=(position_voix_dd[0],position_voix_dd[1]-randint(160,400))
				i_voiture_a+=1
				
		 
		pre_seconde=seconde

def affichage_v_s():
	global vitesse_bck , vitesse ,touchesPressees , score, font , elan , l_v_m_c
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
				pygame.quit()
	touchesPressees = pygame.key.get_pressed() 

	

	vitesse=int((vitesse_bck+elan)*(6/2))
	if vitesse<=255:
		couleur_vit=(vitesse,0,0)
	else:
		couleur_vit=(255,0,0)
	if touchesPressees[pygame.K_DOWN] == True or touchesPressees[pygame.K_s] == True:
		couleur_vit=(0,100,0)
	
	if int(elan)==l_v_m_c:
		score+=(25/30)*l_v_m_c
	if 20<elan<l_v_m_c:
		score+=(1/10)*vitesse
	

	font = pygame.font.SysFont("comicsansms",25) #font 
	texte_score= font.render("Score:"+str(int(score)),True ,(0,0,0))
	texte_vitesse= font.render(str(vitesse)+":Vitesse",True ,(couleur_vit))

	fenetre.blit(texte_score,(0,0))
	fenetre.blit(texte_vitesse,(705,0))




def collision():
	global game , accident , vitesse 
	accident=[]
	
	for i in range(len(position_voiture_a2)):
		if(position_voiture_a2[i][1]+137>position_voiture[1]>position_voiture_a2[i][1] or position_voiture_a2[i][1]+137>position_voiture[1]+140>position_voiture_a2[i][1] ) and (position_voiture_a2[i][0]-10<position_voiture[0]<position_voiture_a2[i][0]+60 or position_voiture_a2[i][0]-10<position_voiture[0]+60<position_voiture_a2[i][0]+60  ) :
			#game=False
			accident.append(position_voiture_a2[i])
			fenetre.blit(explosion,(accident[0]))
			
			game=False
				

	for i in range(len(position_voiture_ai1)):
		if(position_voiture_ai1[i][1]+167>position_voiture[1]>position_voiture_ai1[i][1] or position_voiture_ai1[i][1]+167>position_voiture[1]+140>position_voiture_ai1[i][1] ) and (position_voiture_ai1[i][0]-10<position_voiture[0]<position_voiture_ai1[i][0]+60 or position_voiture_ai1[i][0]-10<position_voiture[0]+60<position_voiture_ai1[i][0]+60  ) :
			
			accident.append(position_voiture_ai1[i])
			fenetre.blit(explosion,(accident[0]))
			
			game=False

	pygame.display.flip()
def game_over():
	global font , score 
	fenetre.blit(im_gm,(210,200))
	texte_score= font.render("Score:"+str(int(score)),True ,(0,0,0))
	fenetre.blit(texte_score,(0,0))
	pygame.display.flip()


clock = pygame.time.Clock()

while game==True:
	clock.tick(140)

	dessin_road()
	affichage_v_s()
	gerer_le_fond()
	dessin_voitures()
	mouvement_voiture()
	gerer_other_cars()
	traffic()
	collision()


while game ==False:
	dessin_road()
	gerer_le_fond()
	game_over()
	

pygame.quit()
