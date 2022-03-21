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
def newScaleByHeight(surface,newHeight):

	scale0=surface.get_height()/surface.get_width()
	newScale = [int(round(newHeight)/scale0)-1,int(round(newHeight))]
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
		person1 = newScaleByWidth(pg.image.load('oimages/bee0.png'),51)
		person2 = newScaleByWidth(pg.image.load('oimages/bee1.png'),51)
		# person3 = newScaleByWidth(pg.image.load('oimages/person.3.png'),51)
		# person4 = newScaleByWidth(pg.image.load('oimages/person.4.png'),51)
		person3=pg.transform.flip(person1,1,0)
		person4=pg.transform.flip(person2,1,0)
		person.ss = [person1.get_width(),person1.get_height()]

		person.surfaces=[person1,person2,person3,person4]
		person.pos = [X/2,-100]
		person.Index = 0;
		person.fallSpeed={'normal':3,'water':1.5}
		person.falling=0;
		person.timer=time.time()
		person.animInterval = 0.05;
		person.speed=3
		person.flyspeed=6;

	def check():
		person.falling=person.gravity()
		#print(person.falling)
		person.move()

		ctime=time.time()
		if ctime - person.timer > person.animInterval:
			#print('yups')
			person.timer = ctime + person.animInterval;

			if 'u' in dircs:
				if 'r' in dircs:
					if person.Index not in [0,1]:
						person.Index=0
				if 'l' in dircs:
					if person.Index not in [2,3]:
						person.Index=2


				if person.Index in [0,1]:
					if person.Index==0:
						person.Index=1
					else:
						person.Index=0
				elif person.Index in [2,3]:
					if person.Index==2:
						person.Index=3
					else:
						person.Index=2

			else:
				if 'r' in dircs:
					if person.Index==0:
						person.Index=1
					elif person.Index==1:
						person.Index=0
					else:
						person.Index=0
				if 'l' in dircs:
					person.Index+=1
					if person.Index==4:
						person.Index=2
			


	def draw():
		pos = [person.pos[0]-viewPort.vp[0],
				person.pos[1]-viewPort.vp[1]]
		screen.blit(person.surfaces[person.Index],pos)


	def move():
		var=0;
		pRect=[person.pos[0],person.pos[1],
				person.ss[0],person.ss[1]]

		prRect=[person.pos[0]+person.ss[0]*0.7+person.speed
				,person.pos[1]+person.ss[1]*0.1,
				person.ss[0]*0.3,person.ss[1]*0.8]

		plRect=[person.pos[0]-person.speed
				,person.pos[1]+person.ss[1]*0.1,
				person.ss[0]*0.3,person.ss[1]*0.8]

		ptRect=[person.pos[0]+person.ss[0]*0.1,
				person.pos[1]-person.flyspeed
				,person.ss[0]*0.8,
					person.ss[1]*0.1]

		rVar=1
		lVar=1
		uVar=1
		scale=1
		for i in Map.rects:
			iRect=pg.Rect(i[0])
			if iRect.colliderect(pRect):
				for c in objects.staticList:
					if c[1] not in Map.pool['s']:
						cRect=pg.Rect(c[0][0],c[0][1],c[1].get_width(),
							c[1].get_height())
						if cRect.colliderect(prRect):
							rVar=0
						if cRect.colliderect(plRect):
							lVar=0
						if cRect.colliderect(ptRect):
							uVar=0
					else:
						cRect=pg.Rect(c[0][0],c[0][1],c[1].get_width(),
							c[1].get_height())
						if cRect.colliderect(prRect):
							scale=0.5
						if cRect.colliderect(plRect):
							scale=0.5
						if cRect.colliderect(ptRect):
							scale=0.5
						
		
		if 'r' in dircs and 'l' not in dircs and rVar:			
			person.pos[0]+=person.speed*scale
			viewPort.vpr[0]+=person.speed*scale*0.2
			viewPort.vp[0]+=person.speed*scale*0.8
				
		if 'l' in dircs and 'r' not in dircs and lVar:
			person.pos[0]-=person.speed*scale
			viewPort.vpr[0]-=person.speed*scale*0.2
			viewPort.vp[0]-=person.speed*scale*0.8

		if 'u' in dircs and 'd' not in dircs and uVar:
			person.pos[1]-=person.flyspeed*scale
			viewPort.vp[1]-=person.flyspeed*scale		

		# if len(dircs)!=0:
			# viewPort.vprRequest()
			


	def gravity():
		
		pRect=[person.pos[0]+person.ss[0]*0.2,
				person.pos[1]+person.ss[1]*0.9+person.fallSpeed['normal']
				,person.ss[0]*0.6,person.ss[1]*0.1]
		colCount=0
		case='normal'
		var=1
		for i in Map.rects:	
			iRect=pg.Rect(i[0])
			if iRect.colliderect(pRect):
				for c in objects.staticList:
					if pg.Rect(c[0][0],c[0][1],51,51).colliderect(pRect):
						if c[1] in Map.pool['s']:
							case='water'
						else:
							var=0


		if var:
			person.pos[1]+=person.fallSpeed[case]
			viewPort.vp[1]+=person.fallSpeed[case]

		return var



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
		for i in objects.dynamicList:
			if i[1]==Map.fires:
				#print('ya')
				ctime=time.time()
				if ctime - i[3] > 0.1:
					i[3] = ctime + 0.1 ;
					i[2]+=1
					if i[2]>len(Map.fires)-1:
						i[2]=0


					

	def draw():
		for i in objects.staticList:
			pos=[i[0][0]-viewPort.vp[0],
				 i[0][1]-viewPort.vp[1]]
			screen.blit(i[1],pos)

		for i in objects.dynamicList:
			#print(i)
			if i[1]==Map.fires:
				pos=[i[0][0]-viewPort.vp[0],
					 i[0][1]-viewPort.vp[1]]
				screen.blit(i[1][i[2]],pos)
			elif i[1] in Map.flowers:
				pos=[i[0][0]-viewPort.vp[0],
					 i[0][1]-viewPort.vp[1]]
				screen.blit(i[1],pos)

	def gravity():
		0

class Map:

	def init():
		Map.id = 0;

		dirt0 =newScaleByWidth(pg.image.load('oimages/dirt0.png'),51)
		dirt1 =newScaleByWidth(pg.image.load('oimages/dirt1.png'),51)
		dirt2 =newScaleByWidth(pg.image.load('oimages/dirt2.png'),51)
		dirt3 =newScaleByWidth(pg.image.load('oimages/dirt3.png'),51)
		dirt4 =newScaleByWidth(pg.image.load('oimages/dirt4.png'),51)
		dirt5 =newScaleByWidth(pg.image.load('oimages/dirt5.png'),51)

		Map.dirts = 		{'s':[dirt0,dirt1],
						'm':[dirt2,dirt3],
						'e':[dirt4,dirt5]}

		stone0 =newScaleByWidth(pg.image.load('oimages/stone0.png'),51)
		stone1 =newScaleByWidth(pg.image.load('oimages/stone1.png'),51)
		stone2 =newScaleByWidth(pg.image.load('oimages/stone2.png'),51)
		stone3 =newScaleByWidth(pg.image.load('oimages/stone3.png'),51)
		stone4 =newScaleByWidth(pg.image.load('oimages/stone4.png'),51)
		stone5 =newScaleByWidth(pg.image.load('oimages/stone5.png'),51)

		Map.stones = {'s':[stone2,stone3],
						'm':[stone0,stone1],
						'e':[stone4,stone5]}

		water0 =newScaleByWidth(pg.image.load('oimages/water0.png'),51)
		water1 =newScaleByWidth(pg.image.load('oimages/water1.png'),51)
		water2 =newScaleByWidth(pg.image.load('oimages/water2.png'),51)
		water3 =newScaleByWidth(pg.image.load('oimages/water3.png'),51)
		water4 =newScaleByWidth(pg.image.load('oimages/water4.png'),51)
		water5 =newScaleByWidth(pg.image.load('oimages/water5.png'),51)

		waters = [water0,water1,water2,
					water3,water4,water5]

		Map.pool = {'s':waters.copy(),
						'm':waters.copy(),
						'e':[stone4,stone5]}

		fire0 =newScaleByWidth(pg.image.load('oimages/fire0.png'),51)
		fire1 =newScaleByWidth(pg.image.load('oimages/fire1.png'),51)
		fire2 =newScaleByWidth(pg.image.load('oimages/fire2.png'),51)
		fire3 =newScaleByWidth(pg.image.load('oimages/fire3.png'),51)
		fire4 =newScaleByWidth(pg.image.load('oimages/fire4.png'),51)
		fire5 =newScaleByWidth(pg.image.load('oimages/fire5.png'),51)

		Map.fires = [fire0,fire1,fire2,
					fire3,fire4,fire5]


		flower0 =newScaleByHeight(pg.image.load('oimages/flower0.png'),51)
		flower1 =newScaleByHeight(pg.image.load('oimages/flower1.png'),51)

		Map.flowers=[flower0,flower1]

		chunk=Map.getChunk(10,10,[3,2])

		#print(chunk)
		fpos=[X/2-chunk[1][0]*50/2,Y/2-chunk[1][1]*50/2]
		for i in chunk[0]: 
			pos=[i[0][0]*50,i[0][1]*50]			
			pos=[pos[0]+fpos[0],pos[1]+fpos[1]]
			objects.staticList.append([pos,i[1],Map.id])

		Map.rects = [[[fpos[0],fpos[1],chunk[1][0]*50,chunk[1][1]*50],Map.id]]
	
	def draw():
		# for i in Map.rects:
		# 	rect=[i[0][0]-viewPort.vp[0],
		# 		i[0][1]-viewPort.vp[1],i[0][2],i[0][3]]
		# 	pg.draw.rect(screen,[0,0,0],rect)
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
				removeList1=[]
				for c in objects.staticList:
					if c[2]==targetId:
						removeList.append(c)

				for c in objects.dynamicList:
					if c[1]==Map.fires:
						if c[4]==targetId:
							removeList1.append(c)
					if c[1] in Map.flowers:
						if c[2]==targetId:
							removeList1.append(c)

				for c in removeList:
					objects.staticList.remove(c)
				for c in removeList1:
					objects.dynamicList.remove(c)

				Map.rects.remove(i)




	def spawnChunks():
		do=1

		if len(dircs)==0:
			do=0
		else:
			viewPort.rectsRequest()
		if 'r' in dircs and 'l' in dircs :
			do=0
		if 'u' in dircs and 'd' in dircs :
			do=0

		if person.falling==1:
			do=1

		if do:
			vrr=None;
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
					if person.falling==1:
						vrr = viewPort.rightDownRect.copy()

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
					if person.falling==1:
						vrr = viewPort.leftDownRect.copy()
			elif 'u' in dircs and 'd' not in dircs:
				# print('up')
				vrr = viewPort.upRect.copy()
			elif 'd' in dircs and 'u' not in dircs or (
				person.falling==1):
				# print('down')
				vrr = viewPort.downRect.copy()


			# if vrr==None:
			# 	if person.falling==1:
			# 		vrr = viewPort.downRect.copy()
			# 		print('falling')

			
			var = Map.checkPort(vrr)

			
			#print(var)
			if var == 0 :
				egg=random.choice([1,0,0])
				width = random.randint(3,23)

				height = random.randint(3,15)
				roosterInit = [random.randint(1,8),random.randint(0,10)]
				if egg:
					width = random.randint(3,5)
					height = random.randint(2,9)
					roosterInit[1]=0;
				
				newChunk = Map.getChunk(width,height,roosterInit)
				newPos = [random.randint(vrr[0],vrr[0]+vrr[2]-newChunk[1][0]*50),
							 random.randint(vrr[1],vrr[1]+vrr[3]-newChunk[1][1]*50)]

				Map.rects.append([[newPos[0],newPos[1],newChunk[1][0]*50,
								newChunk[1][1]*50],Map.id])
				#print(newChunk)
				if len(newChunk)==3:
					#print(newChunk)
					for i in newChunk[2]:
						#print(i)
						#print(i)
						if i[1]==Map.fires:
							pos=[i[0][0]*50,i[0][1]*50+50]			
							pos=[pos[0]+newPos[0],pos[1]+newPos[1]]
							objects.dynamicList.append([pos,i[1],i[2],i[3]
								,Map.id])
						elif i[1] in Map.flowers:

							pos=[i[0][0]*50,i[0][1]*50+50]
							pos=[pos[0]+newPos[0],pos[1]+newPos[1]]	
							objects.dynamicList.append([pos,i[1]
								,Map.id])

				
				for i in newChunk[0]:
					pos=[i[0][0]*50,i[0][1]*50 + 50]			
					pos=[pos[0]+newPos[0],pos[1]+newPos[1]]
					objects.staticList.append([pos,i[1],Map.id])

				Map.id+=1
			
				
	def checkPort(Port):
		#print(Map.rects)
		for i in Map.rects:
			#print(i)
			iRect=pg.Rect(i[0])

			if iRect.colliderect(Port):
				return 1

		return 0


	def getChunk(width,height,roosterInit):
		chunkRects=[]
		#chunkTypes = 's','m','e','n';
		end = []
		none = []
		middle = []
		rooster = [1]*roosterInit[0]
		rooster.extend([0]*roosterInit[1])
		pos=[0,0];Type='s';
		maxHeight=0
		for i in range(width):
			for c in range(height):
				
				pos=[i,c]
				upperRect=[i,c-1]
				if c==0:
					Type='s'					
				else:
					if c==height-1:
						if upperRect not in end+none:
							Type='e'
						else:
							Type='n'
					else:
						egg = random.choice(rooster);
						if egg:
							Type='m'
						else:
							Type='e'

						if upperRect in end+none:
							Type='n'
						
				rect = [pos,Type]	
				if Type=='e':
					end.append(pos)
				elif Type=='n':
					none.append(pos)
				elif Type=='m':
					middle.append(pos)

				chunkRects.append(rect)

				if pos not in end+none:
					if maxHeight<c:
						maxHeight=c;

	

		#print(maxHeight,c)

		c=chunk;
		chunks = [c.stone,c.dirt,c.dirtStone,
					c.waterStone,c.waterDirt
				]
		#rooster = random.choice([0,1,2,3,4])
		rooster1 = random.choice([0,1,2]);
		if roosterInit[1]==0:
			rooster1=3;
		#print(len(chunks[rooster1](chunkRects,width,maxHeight)))
		return chunks[rooster1](chunkRects,width,maxHeight+1)


class chunk:

	def stone(chunkRects,width,maxHeight):
		mapRect=[width,maxHeight+2]

		source = Map.stones

		newChunk=[]
		egg=random.choice([1])

		for i in chunkRects:
			if i[1]!='n':
				tile = [i[0].copy(),random.choice(source[i[1]])]
				newChunk.append(tile)
		if egg:
			pos = [random.randint(0,width-1),-1]
			dynamicRequest = [[pos,Map.fires,0,time.time()]]
			#print(pos)
			return newChunk,mapRect,dynamicRequest

		

		return newChunk,mapRect

		

	def dirt(chunkRects,width,maxHeight):
		mapRect=[width,maxHeight+2]
		reserved = []
		source = Map.dirts

		newChunk=[]

		egg=random.choice([1])
		egg2=random.choice([1])
		for i in chunkRects:
			if i[1]!='n':
				tile = [i[0].copy(),random.choice(source[i[1]])]
				newChunk.append(tile)

		if egg:
			pos = [random.randint(0,width-1),-1]
			dynamicRequest = [[pos,Map.fires,0,time.time()]]
			#print(pos)
			reserved.append(pos)
			
			if egg2:
				epoint=round(width/6)
				if epoint<1:
					epoint=1
				count=random.randint(1,epoint)
				
				for i in range(count):
					while 1:
						pos = [random.randint(0,width-1),-1]
						if pos not in reserved:
							reserved.append(pos)
							break

					dynamicObject = [pos,random.choice(Map.flowers)]
					
					dynamicRequest.append(dynamicObject)

			return newChunk,mapRect,dynamicRequest


		return newChunk,mapRect

	def dirtStone(chunkRects,width,maxHeight):
		mapRect=[width,maxHeight+2]

		source = Map.dirts
		source0 = Map.stones
		newChunk=[]

		for i in chunkRects:
			sourcex=source
			egg=random.choice([1,0,0,0,0,0,0])
			if egg and i[1]=='m':
				sourcex=source0
			if i[1]!='n':
				tile = [i[0].copy(),random.choice(sourcex[i[1]])]
				newChunk.append(tile)

		return newChunk,mapRect

	def waterStone(chunkRects,width,maxHeight):
		mapRect=[width,maxHeight+2]

		source = Map.pool
		source0 = Map.stones
		newChunk=[]
		egg=random.choice([1,0,0])
		for i in chunkRects:
			if i[1]!='n':
				
				if i[0][0]==0 or i[0][0]==width-1:
					tile = [i[0].copy(),random.choice(source0[i[1]])]
				else:
					tile = [i[0].copy(),random.choice(source[i[1]])]
				newChunk.append(tile)

		if egg:
			pos = [random.choice([0,width-1]),-1]
			dynamicRequest = [[pos,Map.fires,0,time.time()]]
			#print(pos)
			return newChunk,mapRect,dynamicRequest

		return newChunk,mapRect

	def waterDirt(chunkRects,width,maxHeight):
		0




class viewPort:	
	
	def init():
		viewPort.vp = [0,round(-Y/2-100)]
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
		if person.falling==1:
			viewPort.rectsRequest()





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
		# if len(dircs)!=0:
		# 	if 'u' in dircs:
		# 		viewPort.vpr[1]+=(-Y/100)
		# 	if 'd' in dircs:
		# 		viewPort.vpr[1]+=Y/100
		# 	if 'r' in dircs:
		# 		viewPort.vpr[0]+=X/100
		# 	if 'l' in dircs:
		# 		viewPort.vpr[0]+=(-X/100)

		ctime = time.time()		
		if ctime - viewPort.timer >viewPort.vprInterval:					
			if viewPort.vpr != [0,0]:
				if abs(viewPort.vpr[0])<0.9 and abs(viewPort.vpr[1])<0.9:
					
					viewPort.vp = [viewPort.vp[0]+viewPort.vpr[0],
									viewPort.vp[1]+viewPort.vpr[1]]
					viewPort.vpr = [0,0]
				else:
					move = [i*0.3 for i in viewPort.vpr]
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
	objects.check()
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
objects.init();
viewPort.init();
log.init();
Map.init()




while run:
	getEvents()
	checkEvents()
	upDrawer()
