def mouseclick(pos):
    global state, matched1, match1_index, matched2, match2_index
    if state == 0: # state of my program, first click
        match1_index = int(pos[0] / 50) # this number tells me the card index that was clicked
        print match1_index # This prints that card index
        if exposed[int(pos[0] / 50)] == True: # deck and exposed indexes are ==, THis test to see if the card has been flipped. If true it's face up.
            pass
        else:
            exposed[int(pos[0] / 50)] = True # if it was false it's been switch to true which flippes the card face up
            matched1 = deck[int(pos[0] / 50)] #This assignd the value in this card to matched
            print matched1
            state = 1
    elif state == 1: # this is the second click
        match2_index = int(pos[0] / 50) # this tells me the card index that was clicked. Not the card value. 
        if exposed[int(pos[0] / 50)] == True:
            pass
        else:
            exposed[int(pos[0] / 50)] = True
            matched2 = deck[int(pos[0] / 50)]
            print matched2
            state = 2

    else:
        match1_index = int(pos[0] / 50)
        
        if matched1 != matched2: # do the values of the cards match
            exposed[match1_index] = False
            exposed[match2_index] = False
            
        match1_index = int(pos[0] / 50)
        
        if exposed[int(pos[0] / 50)] == True:
            pass
        else:
            exposed[int(pos[0] / 50)] = True
            matched1 = deck[int(pos[0] / 50)]
            state = 1   
