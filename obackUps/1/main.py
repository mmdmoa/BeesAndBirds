import pygame as pg;from pygame.locals import *;
import random,time;
#producing the map generation part is halfly done and it almost killed me
#but is satisfies me now! it worthed it ! 
#let's make a backup for this 

def newScaleByWidth(surface,newWidth):

	scale0=surface.get_width()/surface.get_height()
	newScale = [int(round(newWidth)),int(round(newWidth/scale0))-1]
	nsurface = pg.transform.scale(surface,newScale)
	return nsurface

def fm(Int,Slice):
	return Slice*(Int//Slice)

class character:
	def init():
		0

	def check():
		0

	def draw():
		0

class person:
	
	def init():
		0

	def check():
		0

	def draw():
		0

class bee:
	
	def init():
		0

	def check():
		0

	def draw():
		0

class objects:
	
	def init():
		objects.staticList=[]
		objects.dynamicList=[]


	def check():
		0

	def draw():
		for i in objects.staticList:
			pos=[i[0][0]-viewPort.vp[0],
				 i[0][1]-viewPort.vp[1]]
			screen.blit(i[1],pos)

	def gravity():
		0

class Map:

	def init():
		Map.id = 0;
		dirt0 =newScaleByWidth(pg.image.load('oimages/tile0.png'),51)
		dirt1 =newScaleByWidth(pg.image.load('oimages/tile1.png'),51)
		dirt2 =newScaleByWidth(pg.image.load('oimages/tile2.png'),51)
		Map.dirt3 =newScaleByWidth(pg.image.load('oimages/tile6.png'),51)

		Map.dirts = [dirt0,dirt1,dirt2]

		stone0 =newScaleByWidth(pg.image.load('oimages/tile3.png'),51)
		stone1 =newScaleByWidth(pg.image.load('oimages/tile4.png'),51)

		Map.stones = [stone0,stone1]

		chunk=Map.getChunk(10,10,4)

		fpos=[X/2-chunk[1][0]*50/2,Y/2-chunk[1][1]*50/2]
		for i in chunk[0]: 
			pos=[i[0][0]*50,i[0][1]*50]			
			pos=[pos[0]+fpos[0],pos[1]+fpos[1]]
			objects.staticList.append([pos,i[1],Map.id])

		Map.rects = [[[fpos[0],fpos[1],chunk[1][0]*50,chunk[1][1]*50],Map.id]]
	
	def draw():
		0

	def check():
		Map.removeChunks()
		Map.spawnChunks()

		
	def removeChunks():
		center = [viewPort.vp[0]+X/2,
				viewPort.vp[1]+Y/2]

		for i in Map.rects:
			pos = [i[0][0],i[0][1]]

			if abs(center[0]-pos[0])>3500 or abs(center[1]-pos[1])>3500:
				targetId = i[1]
			else:
				targetId = None;

			if targetId!=None:
				removeList=[]
				for c in objects.staticList:
					if c[2]==targetId:
						removeList.append(c)

				for c in removeList:
					objects.staticList.remove(c)

				Map.rects.remove(i)




	def spawnChunks():
		do=1
		if len(dircs)==0:
			do=0

		if 'r' in dircs and 'l' in dircs :
			do=0
		if 'u' in dircs and 'd' in dircs :
			do=0

		if do:
			if 'r' in dircs and 'l' not in dircs:
				if 'u' in dircs and 'd' not in dircs:
					# print('right up')
					vrr = viewPort.rightUpRect.copy()
				elif 'd' in dircs:
					# print('right down')
					vrr = viewPort.rightDownRect.copy()
				else:
					# print('right')
					vrr = viewPort.rightRect.copy()

			elif 'l' in dircs and 'r' not in dircs:
				if 'u' in dircs and 'd' not in dircs:
					# print('left up')
					vrr = viewPort.leftUpRect.copy()
				elif 'd' in dircs:
					# print('left down')
					vrr = viewPort.leftDownRect.copy()
				else:
					# print('left')
					vrr = viewPort.leftRect.copy()
			elif 'u' in dircs and 'd' not in dircs:
				# print('up')
				vrr = viewPort.upRect.copy()
			elif 'd' in dircs and 'u' not in dircs:
				# print('down')
				vrr = viewPort.downRect.copy()

			
			var = Map.checkPort(vrr)
			if var == 0 :
				width = random.randint(6,18)
				height = random.randint(1,10)
				roosterInit = random.randint(1,8)
				newChunk = Map.getChunk(width,height,roosterInit)
				newPos = [random.randint(vrr[0],vrr[0]+vrr[2]-newChunk[1][0]*50),
							 random.randint(vrr[1],vrr[1]+vrr[3]-newChunk[1][1]*50)]

				Map.rects.append([[newPos[0],newPos[1],newChunk[1][0]*50,
								newChunk[1][1]*50],Map.id])
				Map.id+=1
				for i in newChunk[0]:
					pos=[i[0][0]*50,i[0][1]*50]			
					pos=[pos[0]+newPos[0],pos[1]+newPos[1]]
					objects.staticList.append([pos,i[1],Map.id])
			else:
				viewPort.rectsRequest()
	def checkPort(Port):
		#print(Map.rects)
		for i in Map.rects:
			#print(i)
			iRect=pg.Rect(i[0])

			if iRect.colliderect(Port):
				return 1

		return 0


	def getChunk(width,height,roosterInit):
		reserved=[]
		chunk = []
		maxHeight=0
		main_group0 = [[Map.dirts],[Map.stones],
						[Map.dirts,Map.stones]]
		main_group = random.choice(main_group0)
		for i in range(width):
			group = random.choice(main_group)
			rooster=[1]*roosterInit
			for c in range(height):
				if c==0:
					tile=random.choice(group)
				else:
					if group==Map.dirts:
						tile=Map.dirt3
					else:
						tile=random.choice(group)

				egg=random.choice(rooster)
				#print(rooster)
				if egg:
					chunk.append([[i,c],tile])
					rooster.append(0)
					if c > maxHeight:
						#print(c,maxHeight,'yups')	
						maxHeight = c;

				else:			
					rooster=[0]

		
		return [chunk,[width,maxHeight+1]]



class viewPort:	
	
	def init():
		viewPort.vp = [0,0]
		viewPort.vpr = [0,0]
		viewPort.timer = time.time()
		viewPort.vprInterval = 0.03
		viewPort.initXGrids = [
		i for i in range(-viewPort.vp[0],X-viewPort.vp[0]) if i%50==0]
		viewPort.initYGrids = [
		i for i in range(-viewPort.vp[1],Y-viewPort.vp[1]) if i%50==0]

		viewPort.rectsRequest()

	def check():
		viewPort.vprRequest()




	def draw():
		# viewPort.rect =[viewPort.rightRect[0]-viewPort.vp[0]
		# ,viewPort.rightRect[1]-viewPort.vp[1],viewPort.rightRect[2],
		# 	viewPort.rightRect[3]]

		# pg.draw.rect(screen,[230,230,255],viewPort.rect)
		0

	def rectsRequest():
		viewPort.rightRect = [X+round(viewPort.vp[0]),
						round(viewPort.vp[1]),X,Y]
		viewPort.leftRect = [-X+round(viewPort.vp[0]),
						round(viewPort.vp[1]),X,Y]
		viewPort.upRect = [0+round(viewPort.vp[0]),-Y+round(viewPort.vp[1]),
											X,Y]
		viewPort.downRect = [0+round(viewPort.vp[0]),Y+round(viewPort.vp[1]),
											X,Y]

		viewPort.rightUpRect = [X+round(viewPort.vp[0]),
								-Y+round(viewPort.vp[1]),X,Y]
		viewPort.rightDownRect = [X+round(viewPort.vp[0]),
								Y+round(viewPort.vp[1]),X,Y]

		viewPort.leftUpRect = [-X+round(viewPort.vp[0]),
								-Y+round(viewPort.vp[1]),X,Y]
		viewPort.leftDownRect = [-X+round(viewPort.vp[0]),
								Y+round(viewPort.vp[1]),X,Y]


	def vprRequest():
		

		if len(dircs)!=0:
			if 'u' in dircs:
				viewPort.vpr[1]+=(-Y/100)
			if 'd' in dircs:
				viewPort.vpr[1]+=Y/100
			if 'r' in dircs:
				viewPort.vpr[0]+=X/100
			if 'l' in dircs:
				viewPort.vpr[0]+=(-X/100)
		ctime = time.time()		
		if ctime - viewPort.timer >viewPort.vprInterval:					
			if viewPort.vpr != [0,0]:
				if abs(viewPort.vpr[0])<0.9 and abs(viewPort.vpr[1])<0.9:
					
					viewPort.vp = [viewPort.vp[0]+viewPort.vpr[0],
									viewPort.vp[1]+viewPort.vpr[1]]
					viewPort.vpr = [0,0]
				else:
					move = [i*0.1 for i in viewPort.vpr]
					viewPort.vp[0]+=move[0]
					viewPort.vp[1]+=move[1]
					viewPort.vpr[0] -= move[0]
					viewPort.vpr[1] -= move[1]
					viewPort.timer = ctime

class log:
	def init():
		log.font=pg.font.SysFont('Gabriola',50)
		log.fontCl=(150,130,150)

	def check():
		mfont0 = log.font.render(
			f'dynamic objects:{len(objects.dynamicList)}',1,log.fontCl)
		mfont1 = log.font.render(
			f'static objects:{len(objects.staticList)}',1,log.fontCl)
		mfont2 = log.font.render(
			f'X:{round(viewPort.vp[0])}',1,log.fontCl)
		mfont3 = log.font.render(
			f'Y:{round(viewPort.vp[1])}',1,log.fontCl)
		mfont4 = log.font.render(
			f'Chunks:{len(Map.rects)}',1,log.fontCl)

		log.mfonts=[mfont0,mfont1,mfont2,mfont3,mfont4]

		pos0=[0,0];pos1=[0,mfont0.get_height()]
		pos2=[X-mfont2.get_width(),0]
		pos3=[X-mfont3.get_width(),mfont2.get_height()]
		pos4=[0,mfont0.get_height()+mfont1.get_height()]

		log.poss=[pos0,pos1,pos2,pos3,pos4]

	def draw():
		I=-1
		for i in log.mfonts:
			I+=1
			screen.blit(i,log.poss[I])

dircs = []
def getEvents():
	global run;global dircs

	for i in pg.event.get():
		if i.type==QUIT or i.type==KEYDOWN and i.key==K_ESCAPE:
			run=0

		if i.type==KEYDOWN:
			if i.key in [K_UP,K_w]:
				dircs.append('u')

			if i.key in [K_DOWN,K_s]:
				dircs.append('d')

			if i.key in [K_RIGHT,K_d]:
				dircs.append('r')

			if i.key in [K_LEFT,K_a]:
				dircs.append('l')

		if i.type==KEYUP:
			if i.key in [K_UP,K_w]:
				dircs.remove('u')

			if i.key in [K_DOWN,K_s]:
				dircs.remove('d')

			if i.key in [K_RIGHT,K_d]:
				dircs.remove('r')

			if i.key in [K_LEFT,K_a]:
				dircs.remove('l')

def checkEvents():
	character.check()
	person.check()
	bee.check()
	Map.check()
	viewPort.check()
	log.check()

def upDrawer():
	screen.fill(bg)
	viewPort.draw()
	Map.draw()
	objects.draw()
	character.draw()
	person.draw()
	bee.draw()
	
	
	log.draw()

	pg.display.update()



run=1
X=1200;Y=900;
bg=(150,200,255)

pg.init()
screen=pg.display.set_mode((X,Y))

character.init();person.init();bee.init()
objects.init();viewPort.init();log.init();Map.init()




while run:
	getEvents()
	checkEvents()
	upDrawer()
