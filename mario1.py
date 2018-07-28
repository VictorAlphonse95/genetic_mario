import gym
import gym_pull
import random
import time
import pygame
import sys
import csv
#import json
#gym_pull.pull('github.com/ppaquette/gym-super-mario')
env = gym.make('ppaquette/SuperMarioBros-1-1-v0')

up=0
down=0
left=0
right=0
a=0
b=0
file
dic = {}
pygame.init()
pygame.display.init()
pygame.display.set_mode((200,200))
writer = csv.writer(open('mariodat.csv','w'))
for i_episode in range(100):
    observation = env.reset()
    while True:
	env.render()
	for event in pygame.event.get():
	   if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_a:
		    	a=1
		if event.key == pygame.K_s:
		    	b=1
		if event.key == pygame.K_RIGHT:
		    	right=1
		if event.key == pygame.K_LEFT:
		    	left=1
		if event.key == pygame.K_UP:
		    	up=1
		if event.key == pygame.K_DOWN:
		    	down=1
		if event.key == pygame.K_ESCAPE:
		   	pygame.display.quit()
		   	break			

	   if event.type == pygame.KEYUP:
	    	if event.key == pygame.K_a:	
			a=0 
		if event.key == pygame.K_s:	
			b=0 		
		if event.key == pygame.K_RIGHT:	
			right=0  
		if event.key == pygame.K_LEFT:
		    	left=0
		if event.key == pygame.K_UP:
		    	up=0
		if event.key == pygame.K_DOWN:
		    	down=0
		
	   if event.type == pygame.MOUSEBUTTONDOWN:
		   pygame.display.quit()
		   break

	#[  ,atras,  ,adelante,a,b] - mi analisis
	#[up,down,left,right,a,b] - el que trae el programa

        action = [up,left,down,right,a,b]
	#print action

      	observation, reward, done, info = env.step(action)
	
	#print observation
	
	#with open('mariodata.json','w') as outfile:
	writer.writerow(observation)
        #{'observation' :  [[252, 188, 176],[200,  76,  12],[200,  76,  12],[252, 188, 176],[252, 188, 176],[  0,   0,   0]], 'action' : [up,left,down,right,a,b]}	
    if done:
      break	
