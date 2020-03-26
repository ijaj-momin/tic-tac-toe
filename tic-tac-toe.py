def mark(pos,player_mark):
    box[pos[0]-1][pos[1]-1] = player_mark
    draw(box)

def draw(box):
    for row in box:
        print('|',end='')
        
        for col in row:
            if col == '*':
                print('   ',end='|')
                
            elif col == 'X':
                print(' X ',end='|')
            
            else:
                print(' O ',end='|')
        print()


box = [['*' for _ in range(3)] for _ in range(3)]
while(1):
    pos1 = [int(i) for i in input()]
    mark(pos1,'X')
    pos2 = [int(i) for i in input()]
    mark(pos2,'O')

