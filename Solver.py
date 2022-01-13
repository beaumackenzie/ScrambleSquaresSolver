#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 16:08:25 2021

@author: beau
"""



import itertools


# Top bag = tb
# Bottom bag = bb
# Top orange = to
# Bottom orange = bo
# top blue = tbl
# bottom blue = bbl
# top club = tc
# bottom club = bc




#All of the cards in order
#[top, right, bottom, left]

sq0 = ['bb', 'bc', 'to', 'bbl']
sq1 = ['to', 'bc', 'tb', 'bbl']
sq2 = ['bbl', 'bo', 'tbl', 'tc']
sq3 = ['bbl', 'tb', 'bc', 'to']
sq4 = ['bb', 'tbl', 'bo', 'bc']
sq5 = ['bb', 'to', 'tbl', 'bbl']
sq6 = ['tb', 'tc', 'to', 'bb']
sq7 = ['tb', 'to', 'bc', 'tc']
sq8 = ['bb', 'tc', 'bo', 'tbl']


#Create a function that returns a list of every rotation of the specifc card

def getallrotations(square):
    allrotations = []
    
    for i in range(0,4):        
        allrotations.append((square[i:]+square[:i]))
        
    return(allrotations)


sq0rotations = getallrotations(sq0)
sq1rotations = getallrotations(sq1)
sq2rotations = getallrotations(sq2)
sq3rotations = getallrotations(sq3)
sq4rotations = getallrotations(sq4)
sq5rotations = getallrotations(sq5)
sq6rotations = getallrotations(sq6)
sq7rotations = getallrotations(sq7)
sq8rotations = getallrotations(sq8)







## ALGO WALKTHROUGH ##

# Lets assume there are two tiles only and you want to figure out how many matches
# Also assume each integer 0 through 3 represents a rotation of the tile
# We can walk through each possible match by going [0,0], [0,1], [0,2], [0,3], [1,0] ... And so on.

# If we were to add a third tile, we would then see that there would be an extra four rotations for each pair of rotations
# Thus, adding another tile increases the possible combinations exponentially, or it would be 4^n number of tiles
# Moreover, we would have to try each combination for each order, so for three tiles there would be 3! * 4^3 (or 384) total combinations


# For the function, we first pass in every rotation of each card
# We then apply itertools.permutations to find every permutation of each card, which is represented by a list containing each of
#its four rotations
# We are then able to go through the permutations by lining up the nine cards, rotating the last card four times,
#and then rotating the second to last card once, rotating the last card four times again for each of those rotations... and so on.

# However, we are able to significantly eliminate the number of rotations we need to try
# We know that when lining up the cards for the permutation, if there is no match when we try to line it up, we need to rotate it
# Thereby if no rotations of the second card match the first, we need to rotate the first card
# Once we have rotated the first card four times and we do not have a match on the second card (for example), we know we
#need to try a different permutation, and the first loop goes into a different permutation of each card, which is represented by their rotations




#Calculate all possible twobytwo solutions given four tiles

def twobytwo(rotations1, rotations2, rotations3, rotations4):
     
    possiblematch = [['bb', 'tb'], ['tb', 'bb'], ['to', 'bo'], ['bo', 'to'], ['tbl', 'bbl'], ['bbl', 'tbl'], ['tc', 'bc'], ['bc', 'tc']]

    
    allrotations = [rotations1, rotations2, rotations3, rotations4]
    
    permsallrotations = list(itertools.permutations(allrotations))
    
    totalnum = 0
    
    for l in range(0,len(permsallrotations)):
        
        # Chooses the order the cards are in
        
        rotationorder = permsallrotations[l]
        
        
        order = []
        
        
        
        for i in range(0,4):
            
            for j in range(0,4):
                
                # This references which rotation each card is in. i determines the rotation of the first card, j the second, and so on.
                
                order = [rotationorder[0][i], rotationorder[1][j]]
                
                # In this case [0] refers to the specific rotation of the specific card that was placed in the list order
                # The [1] in [0][1] grabs the item facing the right of that card's rotation
                # This checks if the top left and top middle cards have a match
                
                if [order[0][1], order[1][3]] in possiblematch:
                
                    for k in range(0,4):
                        
                        order = [rotationorder[0][i], rotationorder[1][j], rotationorder[2][k]]
                        
                        if [order[0][1], order[1][3]] in possiblematch and [order[0][2], order[2][0]] in possiblematch:
                        
                            for m in range(0,4):
                                
                                
                                order = [rotationorder[0][i], rotationorder[1][j], rotationorder[2][k], rotationorder[3][m]]
        
        
                                if [order[0][1], order[1][3]] in possiblematch and [order[1][2], order[3][0]] in possiblematch and [order[2][1], order[3][3]] in possiblematch:        
                                    print("partial success")
                                    
                                    # If only these three match
        
                                if [order[0][1], order[1][3]] in possiblematch and [order[0][2], order[2][0]] in possiblematch and [order[1][2], order[3][0]] in possiblematch and [order[2][1], order[3][3]] in possiblematch:
                                    
                                    # If everything is a match
                                    
                                    print("success")
                                    
                                    print(order)
                                    
                                totalnum +=1
                        
    print(totalnum)
                            
                            
                        
                        
# If you want to run the algorithm with four cards
            
    
#twobytwo(sq1rotations, sq2rotations, sq3rotations, sq8rotations)




def threebythree(r0,r1,r2,r3,r4,r5,r6,r7,r8):
    
    possiblematch = [['bb', 'tb'], ['tb', 'bb'], ['to', 'bo'], ['bo', 'to'], ['tbl', 'bbl'], ['bbl', 'tbl'], ['tc', 'bc'], ['bc', 'tc']]
    
    
    allrs = [r0,r1,r2,r3,r4,r5,r6,r7,r8]
    
    permsallrs = list(itertools.permutations(allrs))
    
    
    for l in range(0,len(permsallrs)):
        
        rsorders = permsallrs[l]
        
        order2 = []
        
        for a in range(0,4):
            
            for b in range(0,4):
                
                order2 = [rsorders[0][a], rsorders[1][b]]
                
                if [order2[0][1], order2[1][3]] in possiblematch:
                
                    for c in range(0,4):
                        
                        order2 = [rsorders[0][a], rsorders[1][b], rsorders[2][c]]
                        
                        if [order2[0][1], order2[1][3]] in possiblematch and [order2[1][1], order2[2][3]] in possiblematch:
                        
                            for d in range(0,4):
                                
                                order2 = [rsorders[0][a], rsorders[1][b], rsorders[2][c], rsorders[3][d]]
                                
                                if [order2[0][1], order2[1][3]] in possiblematch and [order2[1][1], order2[2][3]] in possiblematch and [order2[3][0], order2[0][2]] in possiblematch:
                                
                                    for e in range(0,4):
                                        
                                        order2 = [rsorders[0][a], rsorders[1][b], rsorders[2][c], rsorders[3][d], rsorders[4][e]]
                                        
                                        if [order2[0][1], order2[1][3]] in possiblematch and [order2[1][1], order2[2][3]] in possiblematch and [order2[3][0], order2[0][2]] in possiblematch and [order2[1][2], order2[4][0]] in possiblematch:
                                        
                                            for f in range(0,4):
                                                
                                                order2 = [rsorders[0][a], rsorders[1][b], rsorders[2][c], rsorders[3][d], rsorders[4][e], rsorders[5][f]]
                                                
                                                if [order2[0][1], order2[1][3]] in possiblematch and [order2[1][1], order2[2][3]] in possiblematch and [order2[3][0], order2[0][2]] in possiblematch and [order2[1][2], order2[4][0]] in possiblematch and [order2[2][2], order2[5][0]] in possiblematch and [order2[3][1], order2[4][3]] in possiblematch and [order2[4][1], order2[5][3]] in possiblematch:
                                                
                                                    for g in range(0,4):
                                                        
                                                        order2 = [rsorders[0][a], rsorders[1][b], rsorders[2][c], rsorders[3][d], rsorders[4][e], rsorders[5][f], rsorders[6][g]]
                                                        
                                                        if [order2[0][1], order2[1][3]] in possiblematch and [order2[1][1], order2[2][3]] in possiblematch and [order2[3][0], order2[0][2]] in possiblematch and [order2[1][2], order2[4][0]] in possiblematch and [order2[2][2], order2[5][0]] in possiblematch and [order2[3][1], order2[4][3]] in possiblematch and [order2[4][1], order2[5][3]] in possiblematch and [order2[3][2], order2[6][0]] in possiblematch:
                                                            
                                                            for h in range(0,4):                                                    
                                                                
                                                                order2 = [rsorders[0][a], rsorders[1][b], rsorders[2][c], rsorders[3][d], rsorders[4][e], rsorders[5][f], rsorders[6][g], rsorders[7][h]]
                                                                
                                                                if [order2[0][1], order2[1][3]] in possiblematch and [order2[1][1], order2[2][3]] in possiblematch and [order2[3][0], order2[0][2]] in possiblematch and [order2[1][2], order2[4][0]] in possiblematch and [order2[2][2], order2[5][0]] in possiblematch and [order2[3][1], order2[4][3]] in possiblematch and [order2[4][1], order2[5][3]] in possiblematch and [order2[3][2], order2[6][0]] in possiblematch and [order2[4][2], order2[7][0]] in possiblematch:                                                               
                                                                    
                                                                    for i in range(0,4):
                                                                        
                                                                        order2 = [rsorders[0][a], rsorders[1][b], rsorders[2][c], rsorders[3][d], rsorders[4][e], rsorders[5][f], rsorders[6][g], rsorders[7][h], rsorders[8][i]]
                                                                        
                                                                        if [order2[0][1], order2[1][3]] in possiblematch and [order2[1][1], order2[2][3]] in possiblematch and [order2[3][0], order2[0][2]] in possiblematch and [order2[1][2], order2[4][0]] in possiblematch and [order2[2][2], order2[5][0]] in possiblematch and [order2[3][1], order2[4][3]] in possiblematch and [order2[4][1], order2[5][3]] in possiblematch and [order2[3][2], order2[6][0]] in possiblematch and [order2[4][2], order2[7][0]] in possiblematch and [order2[5][2], order2[8][0]] in possiblematch and [order2[6][1], order2[7][3]] in possiblematch and [order2[7][1], order2[8][3]] in possiblematch:
    
                                                                            print("success")
                                                                            
                                                                            print(order2)

#    print(numtrials)
                
             
                
# Three cards

threebythree(sq0rotations,sq1rotations,sq2rotations,sq3rotations,sq4rotations,sq5rotations,sq6rotations,sq7rotations,sq8rotations)
             
                
             
## Spoiler ##

# There seems to be two unique solutions
# 8 total solutions, but just four rotations of two solutions   

             
      
             
                                                                        
#   if [order2[0][1], order2[1][3]] in possiblematch and [order2[1][1], order2[2][3]] in possiblematch and [order2[3][0], order2[0][2]] in possiblematch and [order2[1][2], order2[4][0]] in possiblematch
#and [order2[2][2], order2[5][0]] in possiblematch and [order2[3][1]], order2[4][3]] in possiblematch
#    and [order2[4][1], order2[5][3]] in possiblematch and [order2[3][2], order2[6][0]] in possiblematch
#    and [order2[4][2]], order2[7][0]] in possiblematch and [order2[5][2]], order2[8][0]] in possiblematch
#    and [order2[6][1], order2[7][3]] in possiblematch and [order2[7][1]], order2[8][3]] in possiblematch


    
    
    
    
