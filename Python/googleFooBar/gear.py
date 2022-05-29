def solution(pegs):
    totalLen=pegs[-1]

solution([4,14,15])

'''
pegs[0]+x+y=pegs[1]
x+y=pegs[1]-pegs[0]
x/y=2  =>  x=2y
3y=pegs[1]-pegs[0]
x=2*(pegs[1]-pegs[0])/3
return [20,3]
'''

'''
pegs[0]+x+y=pegs[1]
pegs[1]+y+z=pegs[2]
x=2z

3z+2y=pegs[2]-pegs[0]
2y+2z=(pegs[2]-pegs[1])*2
z=2*pegs[1]-pegs[0]
x=4*pegs[1]-2*pegs[0]
'''

'''
pegs[0]+x+y=pegs[1]
pegs[1]+y+z=pegs[2]
pegs[2]+z+w=pegs[3]
x=2w

pegs[1]-pegs[2]+y-w=pegs[2]-pegs[3]
pegs[0]+x+y=pegs[1]
pegs[1]-pegs[2]-pegs[0]-w-x=pegs[2]-pegs[3]-pegs[1]

3x=2*pegs[1]-2*pegs[2]-pegs[0]+pegs[3]
'''