# memPY v1.0.0
# Licensed under MIT

slot = []
reg = []

def setSize(size):
    global slot
    global reg
    i = 0
    while i < size:
        slot.append(' ')
        reg.append(0)
        i += 1

def alloc(sl):
    global slot
    global reg
    try:
        if reg[sl] == 0:
            slot[sl] = 0
            reg[sl] = 1
        else:
            print('Error: slot not free')
            exit()
    except IndexError:
        print('Error: slot does not exist')
        exit()

def free(sl):
    global slot
    global reg
    try:
        if reg[sl] == 1:
            reg[sl] = 0
            slot[sl] = ' '
        else:
            print('Error: slot not allocated')
            exit()
    except IndexError:
        print('Error: slot does not exist')
        exit()

def mSet(sl,vl):
    global slot
    global reg
    try:
        if reg[sl] == 1:
            slot[sl] = vl
        else:
            print('Error: tried to modify unallocated memory')
            exit()
    except IndexError:
        print('Error: slot does not exist')
        exit()
