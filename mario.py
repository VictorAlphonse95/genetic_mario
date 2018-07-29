
import gym
import gym_pull
import random
import time
import pygame
import sys
import csv
import numpy
#import json
#gym_pull.pull('github.com/ppaquette/gym-super-mario')
env = gym.make('ppaquette/SuperMarioBros-1-1-v0')

up, down, left, right, a, b = [0,0,0,0,0,0]

pygame.init()
pygame.display.init()
pygame.display.set_mode((200,200))

with open('mar1.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    for i_episode in range(1):
        observation = env.reset()
        distance=0
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

            action = [up,left,down,right,a,b]

            old_observation = observation
            #print old_observation
            observation, reward, done, info = env.step(action)
            if action != [0,0,0,0,0,0] and info['distance'] > distance:
                spamwriter.writerow(numpy.append(old_observation,action))
                distance = info['distance']
            if done:
                break
