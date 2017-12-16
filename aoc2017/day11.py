"""
Cheers to
http://keekerdc.com/2011/03/hexagon-grids-coordinate-systems-and-distance-calculations/
for providing some insight into hex grids!
"""
DATA = "se,ne,ne,n,n,n,n,n,n,nw,nw,nw,se,nw,nw,sw,se,nw,sw,nw,se,sw,s,sw,s,s,sw,s,sw,sw,ne,sw,s,sw,s,sw,nw,s,s,s,s,s,s,sw,s,s,n,nw,s,s,se,se,se,s,nw,se,s,se,nw,se,se,n,se,se,se,se,se,se,se,ne,sw,nw,ne,n,se,sw,nw,ne,se,se,ne,sw,se,ne,ne,se,n,ne,ne,ne,ne,ne,ne,sw,ne,ne,ne,ne,ne,ne,sw,ne,nw,s,se,ne,ne,ne,nw,ne,sw,ne,ne,ne,ne,ne,ne,nw,sw,sw,ne,ne,ne,n,s,ne,n,s,n,ne,n,n,n,n,n,n,n,ne,n,n,s,s,ne,n,n,sw,n,sw,n,n,se,n,n,n,n,n,n,n,n,s,sw,ne,nw,nw,n,n,se,se,s,n,nw,n,n,n,nw,n,nw,n,n,nw,se,ne,nw,nw,n,nw,n,nw,s,n,nw,n,ne,n,n,nw,n,nw,se,se,nw,nw,nw,nw,n,nw,ne,ne,n,s,nw,nw,nw,nw,n,nw,sw,se,nw,nw,nw,sw,nw,s,nw,nw,nw,nw,nw,se,n,ne,nw,ne,sw,sw,nw,sw,s,nw,nw,ne,nw,sw,nw,sw,nw,n,n,sw,nw,nw,n,ne,s,ne,sw,ne,nw,nw,sw,nw,nw,s,nw,nw,nw,nw,nw,nw,sw,sw,nw,nw,se,nw,sw,nw,ne,sw,sw,nw,nw,nw,nw,nw,s,sw,nw,sw,sw,nw,nw,sw,sw,sw,sw,sw,sw,sw,ne,sw,nw,sw,sw,nw,sw,ne,ne,sw,se,se,sw,sw,sw,sw,sw,n,n,sw,nw,n,sw,sw,n,se,sw,sw,sw,sw,sw,sw,sw,sw,sw,se,sw,ne,sw,n,sw,sw,s,nw,s,s,sw,sw,sw,s,sw,sw,sw,ne,nw,s,sw,s,sw,s,ne,s,ne,sw,sw,sw,s,sw,s,sw,s,s,sw,sw,sw,n,sw,s,sw,sw,s,sw,sw,sw,sw,s,sw,sw,sw,se,sw,ne,sw,sw,se,sw,sw,sw,sw,s,s,s,s,sw,s,s,sw,sw,s,nw,n,s,s,sw,s,s,n,se,s,sw,sw,se,se,s,s,sw,sw,nw,s,nw,s,s,s,s,s,s,sw,sw,s,s,s,n,sw,s,sw,s,s,s,s,s,n,s,se,s,ne,ne,s,s,ne,s,s,sw,s,s,s,s,s,s,se,s,n,s,s,s,s,s,se,s,se,s,se,ne,s,s,s,sw,se,se,se,s,s,se,nw,s,s,s,sw,se,s,s,se,s,ne,s,s,se,s,s,s,s,s,s,s,se,se,nw,s,s,se,n,s,se,ne,s,s,s,ne,s,se,nw,s,s,s,s,n,ne,s,se,se,s,s,ne,s,sw,s,s,s,se,s,s,s,se,ne,s,s,s,s,se,s,s,s,se,s,s,s,se,s,s,nw,s,s,nw,s,se,sw,s,s,se,s,s,se,se,s,se,se,s,s,se,sw,se,se,se,se,se,s,s,s,s,se,se,ne,se,s,ne,nw,se,se,s,se,nw,se,se,n,se,s,n,se,n,s,se,se,se,sw,ne,se,se,s,n,s,se,se,se,s,se,s,se,n,se,se,sw,se,se,s,nw,sw,se,nw,se,se,se,se,s,se,se,se,se,se,se,se,se,se,se,n,s,se,se,se,se,ne,nw,se,se,nw,se,se,n,s,se,se,se,s,se,se,se,se,se,se,ne,se,se,ne,se,se,nw,se,ne,se,se,se,se,s,se,ne,se,se,se,ne,se,nw,ne,se,s,se,se,se,se,se,nw,se,se,sw,sw,se,se,se,sw,se,ne,s,se,nw,ne,se,ne,nw,se,se,se,se,se,se,sw,se,ne,se,se,se,se,se,se,se,ne,se,se,se,se,se,s,se,ne,sw,se,s,se,ne,s,se,se,se,se,sw,sw,se,se,ne,ne,se,se,nw,ne,ne,ne,se,se,se,se,se,s,ne,se,ne,ne,se,ne,ne,s,n,ne,ne,se,ne,ne,se,se,se,se,nw,se,se,ne,se,ne,se,se,s,se,se,ne,se,sw,se,se,se,ne,ne,se,se,sw,se,ne,ne,se,se,n,ne,ne,ne,se,ne,ne,ne,se,ne,ne,ne,ne,ne,ne,se,se,se,ne,se,ne,ne,ne,ne,nw,ne,nw,se,ne,ne,ne,se,ne,ne,ne,se,ne,ne,se,n,n,ne,nw,se,se,ne,ne,se,ne,n,ne,ne,ne,se,se,se,nw,nw,se,ne,ne,ne,ne,nw,ne,ne,ne,ne,ne,se,ne,ne,ne,ne,ne,ne,ne,ne,se,ne,s,sw,ne,ne,n,se,ne,ne,se,ne,ne,ne,ne,ne,ne,se,ne,sw,ne,ne,ne,s,ne,ne,ne,ne,ne,ne,ne,ne,sw,ne,ne,ne,ne,ne,nw,sw,se,nw,ne,ne,ne,ne,se,ne,s,ne,ne,ne,ne,ne,s,ne,ne,ne,ne,ne,n,ne,n,ne,ne,ne,nw,se,ne,ne,ne,ne,n,nw,ne,ne,ne,ne,sw,ne,n,n,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,n,ne,n,ne,ne,se,n,n,nw,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,se,ne,n,n,ne,ne,se,ne,n,s,ne,ne,ne,s,n,ne,s,n,ne,s,n,n,s,n,ne,ne,ne,nw,n,n,n,ne,nw,s,ne,n,ne,ne,n,ne,ne,n,n,n,ne,ne,n,ne,n,ne,ne,sw,ne,ne,ne,ne,ne,n,n,ne,ne,se,ne,se,nw,ne,sw,ne,ne,s,ne,n,ne,n,nw,s,s,ne,ne,nw,ne,se,se,ne,ne,se,ne,n,n,n,sw,ne,s,n,ne,n,n,n,ne,sw,n,ne,ne,ne,n,ne,ne,n,ne,ne,nw,n,n,nw,ne,n,n,se,ne,n,ne,ne,n,n,ne,n,se,ne,nw,ne,n,sw,se,ne,n,n,se,nw,sw,n,ne,s,n,n,ne,n,ne,se,ne,n,n,ne,n,n,n,n,n,ne,ne,sw,ne,se,ne,ne,n,n,ne,ne,ne,n,ne,ne,ne,n,se,n,ne,se,sw,sw,n,ne,n,n,n,n,n,n,ne,n,n,ne,ne,n,n,sw,nw,nw,ne,n,ne,n,se,se,ne,n,ne,n,ne,ne,ne,ne,n,n,n,n,ne,n,n,n,ne,n,ne,n,n,n,se,ne,ne,nw,n,ne,ne,nw,n,ne,n,n,n,n,ne,n,n,n,ne,n,n,n,ne,nw,n,ne,n,n,n,n,sw,ne,n,sw,n,n,ne,n,n,ne,n,ne,nw,n,n,n,ne,n,n,n,sw,n,n,n,n,n,n,n,n,n,nw,n,n,n,sw,n,n,n,n,n,n,n,n,se,ne,n,n,n,n,nw,n,ne,n,se,se,n,n,s,ne,n,n,n,n,n,sw,s,n,n,n,n,n,n,ne,sw,n,s,n,n,n,nw,n,n,n,n,n,n,n,ne,n,n,n,n,n,se,n,n,n,nw,n,n,n,n,sw,n,n,n,n,se,n,n,nw,n,n,n,n,n,n,s,n,n,n,n,n,se,n,nw,n,n,n,n,n,n,nw,n,n,n,n,n,n,ne,nw,n,nw,n,n,n,n,n,n,n,n,se,nw,n,n,n,n,nw,n,nw,n,se,n,n,n,n,s,ne,sw,n,n,se,se,n,n,n,sw,n,n,n,nw,n,n,ne,n,nw,n,nw,n,n,nw,n,n,n,n,n,n,nw,n,se,nw,s,nw,n,se,se,n,n,n,n,n,n,ne,ne,n,n,n,n,n,n,n,se,n,n,n,sw,n,sw,n,nw,nw,s,nw,n,nw,n,n,n,nw,n,n,s,n,n,n,nw,nw,se,n,nw,nw,n,nw,n,nw,n,n,se,nw,n,n,n,n,n,n,n,ne,nw,n,nw,nw,n,nw,ne,n,n,n,n,s,se,s,n,n,n,n,n,n,se,n,s,n,nw,nw,nw,nw,n,n,n,sw,se,s,n,nw,n,n,nw,n,n,n,n,n,nw,n,s,n,se,n,ne,n,nw,nw,nw,nw,n,n,n,n,n,se,nw,sw,nw,n,nw,n,n,n,n,nw,nw,se,nw,n,nw,n,nw,nw,sw,n,n,n,n,nw,n,n,nw,nw,sw,n,s,n,nw,n,n,n,nw,n,nw,se,nw,n,nw,ne,ne,s,nw,se,nw,nw,n,nw,nw,n,nw,nw,n,n,ne,s,nw,nw,nw,n,nw,n,n,nw,n,nw,sw,se,se,nw,n,ne,n,n,se,nw,n,s,ne,sw,nw,n,nw,nw,n,sw,nw,se,n,se,n,n,nw,ne,nw,nw,nw,nw,nw,s,nw,nw,nw,nw,nw,ne,n,nw,nw,nw,nw,n,n,n,n,n,sw,nw,n,n,n,nw,nw,s,nw,n,se,nw,n,se,n,n,nw,nw,nw,nw,n,nw,nw,nw,nw,nw,nw,n,nw,n,s,nw,nw,nw,nw,n,nw,n,se,nw,n,ne,nw,n,nw,n,se,n,n,nw,nw,nw,nw,nw,sw,nw,nw,sw,nw,nw,nw,ne,nw,n,s,s,nw,ne,nw,n,nw,n,ne,nw,n,nw,nw,ne,nw,n,nw,nw,se,nw,n,nw,n,sw,se,n,n,nw,ne,nw,nw,n,nw,nw,nw,nw,nw,se,se,se,ne,nw,n,nw,nw,s,nw,nw,nw,se,n,nw,nw,se,n,nw,nw,nw,n,nw,sw,nw,se,n,nw,nw,nw,n,nw,ne,nw,n,nw,nw,sw,nw,nw,n,nw,nw,n,nw,ne,sw,nw,n,n,nw,sw,nw,se,nw,nw,nw,s,nw,nw,n,n,sw,n,s,ne,sw,s,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,n,n,nw,nw,nw,ne,n,nw,nw,s,nw,ne,s,ne,nw,nw,nw,nw,s,nw,nw,nw,nw,se,s,nw,nw,sw,nw,nw,nw,nw,nw,nw,nw,nw,n,s,s,nw,ne,nw,se,nw,se,nw,nw,nw,ne,se,nw,ne,nw,nw,nw,nw,n,se,nw,nw,nw,ne,nw,nw,s,nw,nw,sw,ne,s,nw,nw,nw,sw,n,nw,nw,nw,nw,sw,s,se,nw,nw,nw,se,ne,nw,nw,n,nw,sw,nw,sw,nw,nw,n,nw,nw,nw,n,nw,nw,nw,nw,nw,nw,sw,nw,sw,nw,nw,nw,n,nw,s,sw,nw,sw,nw,nw,nw,nw,sw,nw,nw,nw,nw,n,nw,sw,nw,nw,sw,nw,s,nw,s,nw,sw,sw,nw,nw,se,nw,nw,nw,sw,nw,nw,sw,nw,nw,n,s,ne,nw,nw,nw,nw,se,nw,n,nw,nw,sw,nw,nw,nw,nw,nw,nw,nw,sw,nw,nw,nw,nw,sw,nw,se,nw,s,nw,nw,sw,nw,nw,sw,sw,nw,nw,nw,nw,nw,nw,nw,nw,s,nw,nw,nw,nw,s,nw,nw,nw,sw,nw,nw,s,nw,nw,nw,nw,nw,nw,nw,nw,nw,sw,nw,nw,ne,nw,s,sw,nw,nw,nw,sw,nw,ne,se,sw,nw,nw,nw,se,nw,sw,nw,nw,sw,nw,sw,sw,sw,nw,nw,sw,nw,nw,nw,sw,ne,nw,nw,n,nw,nw,sw,nw,sw,nw,nw,sw,sw,nw,ne,sw,nw,sw,se,sw,n,sw,n,ne,nw,nw,n,s,nw,nw,nw,ne,nw,nw,nw,nw,s,nw,s,nw,nw,sw,sw,nw,nw,nw,nw,nw,nw,nw,nw,n,nw,nw,se,nw,n,nw,n,ne,n,nw,sw,sw,sw,nw,nw,ne,nw,nw,nw,ne,n,nw,sw,sw,nw,sw,nw,sw,nw,sw,n,sw,nw,nw,sw,nw,nw,ne,nw,nw,nw,nw,sw,sw,nw,nw,sw,nw,sw,nw,nw,s,ne,s,sw,nw,nw,nw,sw,sw,nw,nw,sw,nw,s,sw,sw,nw,se,nw,nw,sw,nw,nw,sw,sw,nw,sw,sw,nw,s,nw,nw,nw,sw,sw,nw,nw,nw,se,sw,s,nw,nw,nw,nw,nw,nw,sw,n,s,nw,sw,nw,se,n,sw,ne,se,sw,nw,nw,ne,sw,nw,sw,sw,nw,ne,ne,sw,sw,nw,se,sw,nw,nw,sw,sw,sw,sw,se,sw,n,nw,nw,sw,sw,sw,sw,sw,nw,sw,nw,nw,sw,sw,nw,n,sw,sw,sw,nw,nw,nw,nw,sw,s,sw,nw,sw,sw,nw,sw,nw,n,nw,s,nw,sw,nw,se,sw,nw,ne,ne,sw,n,nw,nw,nw,nw,nw,nw,nw,sw,sw,sw,nw,nw,nw,nw,nw,nw,sw,nw,nw,nw,nw,sw,nw,sw,se,sw,nw,sw,nw,ne,nw,sw,sw,sw,s,nw,sw,nw,nw,nw,nw,sw,sw,s,n,s,sw,sw,se,sw,nw,ne,nw,sw,nw,sw,sw,nw,nw,s,sw,sw,ne,sw,se,n,sw,sw,nw,nw,sw,se,n,nw,sw,nw,sw,n,nw,n,sw,sw,sw,sw,nw,s,sw,nw,sw,nw,sw,sw,s,nw,sw,sw,sw,sw,sw,sw,se,sw,ne,nw,sw,se,sw,sw,nw,sw,sw,sw,se,n,sw,nw,sw,se,sw,se,s,nw,sw,nw,sw,sw,nw,n,s,nw,nw,sw,sw,nw,sw,sw,sw,n,nw,n,ne,se,s,se,s,sw,sw,se,n,sw,sw,sw,sw,sw,sw,sw,nw,sw,sw,sw,nw,sw,sw,sw,nw,sw,nw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,nw,sw,sw,nw,sw,nw,sw,nw,sw,sw,sw,s,nw,nw,n,sw,sw,nw,nw,sw,sw,ne,s,sw,nw,s,sw,nw,s,nw,se,sw,sw,sw,n,sw,n,sw,ne,n,sw,sw,ne,sw,sw,sw,se,sw,sw,sw,se,sw,sw,sw,sw,sw,sw,nw,sw,ne,ne,sw,sw,sw,nw,sw,sw,sw,sw,sw,ne,nw,sw,nw,sw,sw,se,sw,sw,sw,sw,ne,sw,sw,sw,sw,sw,sw,sw,se,sw,sw,nw,sw,sw,sw,nw,nw,sw,sw,se,nw,sw,n,sw,sw,sw,sw,sw,sw,sw,sw,s,sw,sw,se,sw,s,s,sw,n,sw,sw,sw,sw,sw,sw,sw,sw,n,sw,sw,sw,sw,sw,nw,nw,nw,s,se,sw,sw,sw,s,s,se,sw,sw,sw,se,sw,n,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,ne,sw,sw,sw,sw,sw,n,n,sw,sw,sw,sw,nw,n,sw,n,sw,sw,sw,sw,sw,sw,sw,nw,sw,sw,sw,ne,sw,sw,sw,ne,n,se,s,sw,sw,sw,sw,ne,sw,sw,ne,sw,sw,sw,sw,nw,sw,s,se,se,sw,sw,sw,s,sw,sw,sw,sw,sw,s,n,sw,sw,sw,sw,sw,sw,sw,sw,sw,nw,sw,sw,sw,sw,sw,se,sw,sw,sw,ne,s,sw,sw,sw,sw,sw,s,sw,sw,sw,ne,sw,sw,s,sw,sw,s,sw,sw,sw,sw,sw,sw,sw,sw,se,sw,sw,sw,sw,sw,sw,sw,nw,sw,sw,sw,sw,sw,sw,sw,s,sw,sw,nw,sw,sw,sw,ne,ne,sw,n,sw,sw,s,sw,sw,sw,sw,s,sw,sw,sw,s,sw,sw,sw,sw,nw,sw,sw,sw,ne,sw,sw,s,sw,sw,sw,s,sw,sw,sw,sw,nw,sw,sw,sw,sw,s,sw,sw,sw,s,sw,sw,sw,s,sw,n,nw,sw,nw,s,nw,sw,sw,sw,s,sw,sw,sw,s,s,ne,ne,sw,sw,sw,s,sw,sw,sw,sw,sw,nw,s,sw,sw,sw,sw,sw,sw,sw,s,sw,sw,sw,s,sw,n,sw,nw,sw,nw,sw,s,sw,sw,s,sw,n,sw,sw,s,sw,s,s,n,sw,sw,sw,sw,se,ne,s,s,sw,s,sw,sw,sw,ne,sw,ne,sw,se,sw,sw,s,sw,sw,nw,s,s,sw,ne,s,sw,sw,nw,n,s,ne,s,s,s,n,se,sw,s,s,sw,sw,s,ne,sw,n,s,sw,s,n,se,sw,sw,sw,sw,sw,sw,s,sw,s,nw,s,sw,s,sw,n,sw,s,sw,sw,s,sw,sw,ne,sw,se,sw,sw,nw,ne,sw,sw,s,ne,sw,sw,sw,sw,sw,sw,sw,ne,sw,ne,s,ne,sw,s,s,s,n,n,nw,sw,sw,se,se,sw,ne,n,n,sw,ne,sw,se,sw,sw,s,sw,sw,nw,sw,sw,sw,s,sw,s,sw,s,sw,s,sw,sw,s,sw,sw,s,sw,nw,s,sw,sw,s,sw,sw,sw,s,s,sw,s,sw,sw,n,s,sw,s,sw,s,sw,s,s,sw,sw,sw,sw,nw,s,sw,s,sw,sw,ne,sw,sw,s,s,nw,sw,sw,sw,sw,sw,sw,sw,sw,nw,sw,s,s,sw,sw,sw,s,sw,sw,nw,sw,sw,sw,sw,ne,sw,sw,sw,s,s,ne,s,sw,s,sw,sw,sw,sw,sw,sw,s,s,s,nw,se,se,ne,s,s,sw,ne,s,n,s,nw,sw,sw,s,sw,sw,n,sw,s,s,n,sw,ne,s,s,s,nw,s,sw,sw,ne,sw,sw,sw,s,se,sw,sw,sw,ne,s,n,s,se,se,n,sw,n,sw,s,s,sw,s,s,n,s,sw,sw,se,s,sw,s,sw,s,s,s,s,sw,s,s,sw,sw,s,sw,s,sw,sw,s,sw,s,s,sw,sw,sw,s,s,sw,s,nw,sw,ne,s,sw,sw,sw,s,sw,sw,s,sw,sw,s,ne,s,s,sw,s,s,sw,sw,sw,ne,s,s,sw,sw,sw,ne,n,s,s,s,sw,nw,s,s,sw,sw,n,s,s,se,s,s,sw,s,s,s,sw,sw,sw,s,sw,s,s,nw,s,s,sw,s,s,sw,ne,sw,s,s,s,ne,sw,sw,s,n,sw,s,s,s,sw,ne,s,ne,sw,sw,s,sw,s,sw,s,s,ne,sw,nw,sw,s,s,sw,s,n,sw,sw,s,sw,sw,ne,sw,ne,s,se,s,sw,sw,s,se,sw,sw,s,sw,sw,sw,s,sw,sw,sw,s,s,s,se,nw,sw,s,sw,s,s,nw,s,sw,sw,sw,s,s,ne,s,sw,ne,ne,s,sw,ne,sw,sw,s,ne,sw,sw,se,s,s,s,n,sw,s,nw,s,sw,s,s,s,s,s,s,n,s,s,s,ne,s,s,s,s,s,se,sw,s,s,s,s,sw,s,s,s,sw,n,sw,sw,nw,se,s,n,sw,s,ne,n,sw,nw,sw,sw,ne,sw,s,s,nw,sw,ne,nw,sw,s,se,se,sw,s,sw,n,s,s,s,s,ne,s,s,se,s,sw,s,ne,s,se,s,s,sw,s,s,s,s,ne,s,s,s,s,s,s,sw,s,sw,s,se,nw,nw,sw,s,s,s,s,s,s,s,s,s,s,s,sw,s,sw,se,s,s,s,sw,se,s,se,s,s,nw,s,sw,n,sw,sw,sw,s,s,ne,s,se,sw,s,s,nw,s,s,s,s,s,s,s,sw,sw,s,s,sw,s,sw,s,s,sw,s,s,se,s,se,sw,n,sw,s,s,s,s,sw,s,s,s,sw,nw,sw,s,s,s,se,s,s,s,s,sw,se,ne,s,s,sw,s,s,sw,sw,sw,s,s,s,se,s,s,s,s,s,ne,ne,s,sw,sw,s,se,n,ne,sw,sw,s,nw,n,n,s,sw,s,n,s,s,n,n,s,s,s,n,s,ne,s,s,sw,s,sw,s,s,s,s,s,se,sw,se,s,sw,s,n,s,s,ne,s,s,s,s,ne,sw,sw,s,sw,s,s,s,se,s,s,se,nw,nw,s,s,s,s,s,ne,s,s,se,sw,s,s,s,nw,s,n,ne,s,s,s,nw,s,ne,s,sw,nw,nw,sw,s,s,s,s,sw,n,s,s,sw,s,s,se,se,s,sw,s,s,s,s,sw,s,sw,n,s,sw,s,s,s,n,s,s,s,s,s,s,s,s,s,s,s,s,sw,s,s,s,s,s,s,s,s,se,sw,s,n,s,nw,s,s,s,s,s,s,se,s,s,s,s,ne,s,s,s,s,s,s,s,s,s,se,ne,s,s,s,s,s,s,s,s,s,s,nw,s,s,s,s,s,s,s,ne,s,s,nw,s,s,s,sw,s,s,s,n,n,s,s,s,s,s,s,s,s,n,ne,se,s,s,se,s,sw,nw,s,ne,s,s,s,s,s,n,sw,s,s,s,sw,s,s,se,s,n,s,s,ne,s,s,se,s,s,s,se,s,s,s,s,ne,se,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,sw,s,s,s,sw,sw,s,sw,n,n,s,s,s,s,s,s,s,s,s,ne,se,s,ne,s,se,s,se,s,s,s,s,s,se,s,ne,s,n,s,s,ne,sw,s,s,nw,s,se,s,s,s,se,s,s,s,ne,s,s,nw,s,s,s,s,n,s,s,n,s,s,s,s,s,s,s,s,se,s,nw,s,s,se,s,ne,s,s,s,s,s,s,s,s,s,s,s,s,s,ne,s,s,s,s,s,s,sw,s,s,se,s,nw,se,s,s,s,s,s,s,s,se,s,s,se,s,s,s,s,s,s,s,s,s,s,ne,s,s,s,s,s,s,s,s,sw,s,se,s,se,s,s,s,se,se,s,nw,s,s,s,s,nw,s,ne,s,s,s,nw,se,sw,sw,s,s,se,s,ne,nw,s,s,se,s,s,se,n,s,s,se,s,s,s,sw,s,s,ne,s,s,s,se,s,s,s,sw,se,ne,se,n,s,s,se,s,se,n,s,s,nw,s,s,sw,ne,s,s,se,s,se,s,s,s,sw,n,s,s,nw,s,ne,s,se,nw,n,s,n,s,s,s,sw,s,s,s,n,s,se,ne,s,s,s,s,s,s,se,s,s,s,s,se,se,s,s,s,s,se,s,s,s,s,n,s,s,s,s,s,s,se,s,nw,s,nw,se,nw,sw,s,s,ne,s,se,s,nw,s,s,s,s,s,s,se,s,se,n,se,se,s,s,ne,s,s,n,se,s,s,s,sw,sw,s,nw,s,s,se,s,sw,s,s,s,sw,s,s,s,s,se,n,se,s,nw,s,se,se,se,s,nw,s,s,s,s,n,s,s,se,nw,s,s,sw,se,s,s,sw,s,s,s,se,ne,ne,s,se,s,s,s,s,se,s,s,s,s,s,se,s,s,s,s,n,s,s,s,s,se,se,sw,s,s,s,s,s,s,s,s,ne,se,s,s,se,nw,s,se,se,se,se,s,se,s,s,se,s,s,sw,s,nw,se,s,s,s,nw,s,s,s,s,ne,se,s,s,n,se,sw,se,nw,ne,s,s,s,se,s,se,se,s,se,se,s,se,s,se,s,nw,s,sw,nw,s,s,s,s,s,s,s,sw,se,se,s,s,s,s,s,sw,se,se,s,s,se,nw,ne,s,s,s,s,s,s,s,s,s,se,n,se,s,s,n,se,se,se,s,s,s,s,ne,se,s,s,s,s,s,sw,s,s,sw,s,s,s,s,s,sw,se,s,s,se,se,se,se,s,s,s,s,sw,s,nw,sw,s,se,nw,se,s,se,s,s,se,se,s,s,s,se,sw,n,nw,se,s,se,s,se,se,s,se,s,se,ne,s,s,s,s,s,s,se,se,se,s,s,sw,s,se,s,s,s,s,se,s,se,se,se,s,se,se,n,s,s,se,se,s,se,s,s,sw,s,se,s,se,s,se,s,se,se,se,se,sw,s,s,se,se,se,s,s,sw,s,s,ne,se,nw,s,s,s,s,s,s,s,nw,se,s,se,s,s,s,se,nw,se,s,ne,s,s,nw,s,s,sw,s,s,se,s,se,s,s,s,n,se,se,se,se,s,s,sw,s,se,s,s,n,s,s,s,se,s,s,se,s,s,ne,se,se,se,se,se,se,se,s,s,se,se,s,se,se,se,s,s,s,se,s,s,se,ne,se,s,s,se,s,se,s,se,se,s,se,s,se,se,se,n,s,sw,s,ne,se,se,se,ne,se,s,s,se,s,se,s,se,sw,se,se,s,se,s,s,s,s,s,s,s,s,se,s,s,s,se,se,se,s,se,nw,se,n,se,se,se,se,s,se,n,s,s,s,se,s,s,se,s,ne,s,se,se,se,s,s,se,se,s,s,s,se,s,n,sw,s,s,s,ne,s,se,s,s,s,s,nw,se,s,s,s,se,sw,s,ne,s,se,se,se,s,se,se,s,se,se,s,ne,s,s,s,se,nw,nw,nw,ne,s,se,se,ne,se,se,se,se,n,ne,se,s,s,se,s,se,se,se,se,se,s,se,s,s,se,s,se,se,s,se,se,s,se,sw,s,sw,s,se,se,se,se,ne,se,se,se,se,se,se,n,se,sw,se,se,se,sw,s,n,s,nw,s,sw,sw,se,se,s,ne,se,se,se,se,ne,s,se,s,se,se,se,sw,se,se,se,s,se,s,se,nw,se,se,se,se,s,se,s,se,se,se,se,ne,se,se,s,s,se,s,se,se,s,nw,se,s,se,se,se,s,se,sw,nw,sw,se,s,s,ne,sw,se,se,nw,s,se,se,sw,s,s,se,s,s,s,se,se,n,n,se,se,s,se,nw,se,s,nw,se,se,s,ne,s,se,se,s,s,se,s,s,ne,se,se,se,se,nw,nw,nw,ne,se,ne,se,sw,se,n,se,s,s,se,s,s,se,s,n,se,se,se,se,se,se,s,se,nw,sw,se,se,se,se,s,s,s,ne,s,se,se,se,s,se,s,se,ne,sw,se,n,se,se,se,se,se,s,se,s,se,s,s,nw,s,se,se,se,se,se,s,nw,se,s,se,s,se,se,s,se,se,n,s,s,se,se,sw,se,s,ne,s,se,se,ne,ne,se,se,se,se,s,se,se,se,se,se,s,se,s,nw,se,sw,s,sw,nw,ne,s,se,s,s,s,se,se,se,se,se,ne,n,se,se,nw,se,se,s,se,se,se,se,se,se,se,s,se,se,se,ne,se,s,nw,se,se,nw,ne,nw,s,se,se,se,se,s,se,s,nw,se,sw,nw,se,s,s,se,se,se,se,se,n,s,se,se,s,se,nw,se,se,s,se,se,s,se,se,se,se,s,se,se,se,s,se,ne,se,se,se,se,se,se,se,se,s,se,nw,s,n,ne,se,s,se,sw,se,se,se,s,ne,n,se,se,se,ne,se,nw,se,ne,ne,se,se,se,se,se,se,se,n,se,se,se,se,se,s,se,n,se,se,se,se,n,se,se,n,se,ne,se,nw,se,se,se,se,se,s,nw,se,s,se,s,s,se,se,se,sw,s,se,se,se,se,nw,s,sw,se,se,nw,se,se,se,se,se,s,se,se,se,se,ne,se,nw,se,sw,sw,ne,se,se,n,nw,sw,sw,nw,se,s,n,se,se,se,sw,se,sw,s,se,sw,se,ne,se,se,s,se,se,se,se,nw,se,se,se,se,se,se,se,ne,sw,se,nw,se,se,se,se,s,s,se,se,n,nw,se,nw,se,se,se,ne,se,se,se,se,se,nw,se,se,se,se,n,se,se,se,se,s,se,n,se,s,s,se,se,se,se,sw,ne,se,se,se,sw,s,se,se,se,se,se,se,se,se,se,se,se,sw,se,se,s,se,s,sw,se,se,se,se,se,se,sw,se,se,se,se,se,se,se,se,se,se,s,se,s,se,se,se,sw,se,se,se,se,nw,se,se,sw,se,nw,se,se,se,s,se,se,se,se,se,se,se,se,s,se,ne,se,se,se,se,sw,se,se,se,ne,se,se,se,sw,se,se,se,se,se,se,se,se,se,se,se,se,se,se,se,se,se,se,se,se,se,se,se,se,se,se,se,se,se,nw,se,se,se,se,se,n,se,se,se,s,se,se,se,se,se,se,se,se,se,se,se,se,se,se,se,se,se,se,se,se,sw,se,se,se,se,se,se,s,se,ne,se,se,se,n,s,sw,sw,sw,nw,nw,nw,nw,nw,n,n,ne,n,n,n,ne,ne,n,ne,n,ne,ne,se,se,n,se,se,se,ne,se,se,se,sw,se,se,se,se,nw,se,se,se,se,se,se,s,n,se,s,s,s,n,s,s,n,s,se,se,n,s,s,s,ne,s,se,ne,ne,s,sw,s,s,s,s,sw,se,s,sw,sw,se,sw,nw,sw,s,s,sw,sw,sw,s,sw,sw,sw,sw,sw,ne,sw,s,sw,sw,sw,s,sw,n,sw,sw,se,sw,sw,sw,n,sw,nw,nw,nw,sw,sw,sw,nw,se,nw,nw,nw,se,sw,sw,nw,nw,sw,nw,nw,nw,nw,sw,se,nw,nw,sw,ne,nw,nw,nw,nw,nw,n,nw,nw,nw,ne,nw,s,sw,nw,nw,n,ne,nw,nw,sw,nw,nw,nw,n,n,se,s,ne,nw,sw,nw,s,n,nw,s,nw,n,nw,n,sw,n,n,nw,n,nw,n,n,n,n,n,n,n,n,nw,n,n,nw,n,n,n,n,n,sw,n,n,nw,n,ne,s,n,n,n,se,n,sw,n,nw,n,n,sw,n,n,nw,sw,se,se,n,n,n,n,n,n,s,ne,n,n,n,ne,nw,nw,n,n,nw,n,ne,s,nw,n,n,ne,n,n,ne,se,n,n,nw,ne,n,n,n,ne,nw,n,n,ne,n,nw,ne,n,ne,n,ne,nw,ne,se,ne,n,sw,ne,ne,ne,n,ne,n,ne,n,sw,ne,ne,ne,nw,ne,nw,n,nw,ne,ne,ne,n,ne,se,ne,s,ne,nw,n,n,ne,s,ne,ne,s,s,ne,nw,ne,n,ne,ne,ne,ne,nw,ne,ne,ne,ne,ne,se,ne,ne,s,ne,sw,ne,ne,ne,se,ne,ne,ne,n,n,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,se,se,ne,ne,ne,se,sw,ne,ne,nw,se,ne,se,ne,ne,se,ne,s,se,ne,sw,ne,ne,se,se,se,se,ne,se,se,se,ne,se,nw,se,se,ne,n,ne,se,se,n,s,ne,ne,se,se,se,ne,ne,se,ne,ne,se,se,s,ne,se,s,ne,ne,ne,s,se,se,s,ne,se,n,ne,se,ne,se,se,ne,se,s,se,ne,se,se,ne,ne,se,ne,se,ne,se,nw,se,s,ne,ne,se,se,ne,nw,se,ne,se,se,se,se,n,se,ne,se,se,se,nw,se,se,se,s,se,se,se,se,se,se,se,se,se,sw,se,ne,se,n,se,se,s,s,se,se,se,se,se,se,sw,s,se,ne,se,s,se,se,se,se,se,se,se,se,s,s,se,se,se,se,nw,se,se,se,se,se,se,nw,ne,s,ne,se,se,nw,s,se,se,se,se,s,sw,s,ne,n,se,s,se,se,s,se,s,s,se,nw,sw,s,s,se,se,se,sw,se,se,s,se,ne,se,se,se,n,s,s,s,s,ne,n,s,se,s,nw,se,se,s,se,se,s,s,s,s,n,s,nw,n,se,se,s,s,se,se,s,se,s,s,se,s,s,se,s,s,se,s,s,s,n,se,ne,nw,s,se,s,nw,n,se,s,se,n,s,ne,s,nw,s,s,s,s,s,se,nw,s,s,se,ne,s,se,s,s,se,s,ne,se,s,se,s,s,se,s,s,se,s,ne,se,s,n,se,nw,s,s,s,se,s,s,s,n,s,s,s,s,s,s,s,s,s,s,s,s,nw,s,s,s,se,s,s,s,s,n,ne,s,s,s,s,nw,s,s,sw,s,s,s,n,sw,s,s,s,s,s,s,s,s,s,ne,s,s,nw,sw,s,nw,s,s,s,s,s,s,s,se,nw,s,s,s,sw,s,sw,n,s,s,s,s,s,nw,ne,sw,s,nw,sw,s,sw,s,n,s,s,s,s,s,s,nw,s,s,sw,sw,s,sw,s,nw,sw,sw,s,s,s,s,s,nw,s,n,s,sw,sw,s,sw,sw,sw,sw,s,s,s,s,s,sw,sw,nw,sw,sw,s,n,s,sw,s,s,s,nw,se,s,se,s,ne,s,s,s,s,ne,s,sw,s,ne,sw,s,s,sw,ne,s,s,sw,s,sw,n,se,s,s,se,s,nw,s,sw,s,s,sw,s,sw,sw,s,s,s,n,sw,sw,sw,n,nw,sw,s,sw,s,sw,s,ne,se,s,sw,sw,sw,sw,sw,s,n,sw,s,sw,s,s,sw,s,s,nw,s,s,s,s,sw,nw,sw,s,sw,sw,s,sw,se,s,se,sw,sw,sw,sw,ne,sw,sw,s,sw,ne,sw,sw,s,sw,s,s,sw,sw,se,sw,ne,sw,sw,sw,sw,s,sw,s,sw,sw,sw,sw,sw,sw,ne,sw,s,sw,se,nw,se,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,nw,sw,sw,sw,sw,s,sw,sw,nw,sw,se,sw,se,sw,sw,sw,se,sw,sw,ne,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,s,nw,sw,s,sw,sw,sw,s,sw,sw,sw,sw,nw,sw,sw,s,sw,sw,sw,nw,sw,sw,sw,n,sw,sw,n,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,nw,sw,sw,sw,sw,nw,se,nw,sw,sw,sw,sw,n,sw,sw,sw,sw,sw,se,sw,sw,s,ne,s,se,n,nw,ne,n,sw,sw,s,ne,ne,sw,s,sw,se,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,nw,s,sw,sw,n,se,sw,sw,nw,sw,sw,nw,ne,sw,sw,sw,sw,sw,nw,se,s,nw,sw,nw,nw,sw,sw,sw,sw,nw,sw,nw,nw,se,sw,sw,s,se,sw,nw,sw,nw,sw,nw,se,sw,nw,nw,nw,sw,sw,sw,se,nw,ne,sw,sw,nw,s,sw,nw,nw,sw,nw,ne,sw,nw,nw,nw,sw,se,nw,nw,sw,nw,se,sw,s,sw,se,sw,nw,sw,sw,sw,sw,sw,nw,ne,nw,nw,nw,nw,nw,nw,sw,nw,sw,sw,nw,sw,se,nw,se,sw,nw,sw,nw,nw,s,sw,sw,s,se,sw,nw,nw,sw,sw,nw,nw,nw,nw,nw,s,nw,nw,nw,nw,nw,ne,sw,nw,n,ne,nw,nw,sw,nw,nw,sw,sw,s,s,sw,sw,nw,nw,ne,sw,sw,nw,nw,nw,nw,nw,sw,sw,nw,sw,nw,nw,nw,n,s,nw,sw,nw,nw,nw,ne,sw,sw,nw,nw,sw,sw,nw,nw,sw,nw,sw,nw,nw,s,nw,sw,n,nw,nw,sw,sw,n,sw,nw,sw,ne,sw,nw,nw,n,s,nw,nw,sw,nw,nw,nw,sw,sw,nw,nw,nw,nw,sw,nw,sw,sw,sw,ne,nw,nw,sw,nw,s,sw,se,nw,nw,nw,nw,ne,nw,nw,nw,nw,se,nw,nw,nw,nw,nw,nw,nw,nw,nw,se,nw,s,nw,nw,s,sw,sw,ne,nw,nw,nw,nw,n,nw,nw,se,nw,s,nw,se,nw,ne,nw,nw,nw,se,s,n,nw,nw,n,nw,nw,sw,nw,nw,se,s,nw,nw,n,nw,nw,sw,nw,nw,nw,nw,nw,sw,nw,nw,nw,nw,nw,nw,n,sw,nw,nw,n,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,s,nw,nw,nw,sw,n,ne,se,ne,nw,nw,nw,se,n,nw,nw,nw,nw,nw,ne,nw,nw,nw,nw,nw,nw,s,se,nw,se,nw,n,sw,nw,nw,nw,nw,sw,nw,nw,nw,nw,nw,s,n,nw,n,nw,nw,nw,n,nw,ne,n,nw,n,nw,nw,s,nw,nw,nw,nw,n,nw,ne,nw,s,nw,nw,nw,sw,nw,se,n,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,n,nw,sw,nw,n,nw,nw,nw,nw,nw,n,n,nw,n,ne,nw,ne,nw,nw,nw,nw,s,nw,nw,nw,n,sw,n,nw,nw,se,nw,nw,nw,nw,nw,nw,n,nw,sw,nw,nw,nw,nw,nw,se,nw,nw,nw,nw,s,nw,n,nw,n,nw,s,nw,n,nw,nw,nw,nw,nw,ne,nw,nw,nw,nw,nw,nw,n,nw,s,nw,nw,sw,nw,nw,n,nw,s,nw,sw,ne,n,nw,nw,nw,se,nw,nw,nw,nw,n,ne,n,n,s,nw,n,n,s,nw,n,nw,n,nw,nw,s,n,nw,nw,nw,n,nw,n,nw,sw,nw,s,n,n,nw,nw,nw,n,nw,n,nw,nw,s,nw,n,nw,nw,nw,n,nw,n,nw,sw,sw,n,n,nw,nw,nw,s,nw,nw,nw,n,nw,n,se,nw,nw,nw,nw,n,nw,n,n,se,n,nw,sw,n,nw,nw,n,n,n,se,se,n,n,nw,nw,n,nw,nw,n,se,nw,sw,se,n,n,nw,se,n,nw,s,n,n,n,nw,nw,nw,nw,n,sw,nw,se,nw,ne,nw,nw,nw,nw,n,n,n,n,n,n,nw,n,n,n,n,n,se,sw,n,nw,n,n,n,n,nw,n,n,ne,n,ne,nw,n,nw,nw,sw,n,nw,n,n,nw,n,nw,n,n,sw,nw,s,nw,n,nw,n,s,n,sw,nw,n,nw,n,n,ne,n,nw,n,n,s,n,n,n,ne,nw,n,n,nw,ne,n,se,n,n,n,nw,s,n,ne,nw,n,nw,nw,nw,n,n,s,se,sw,nw,s,n,n,se,nw,n,nw,se,n,n,sw,n,n,n,n,n,sw,nw,sw,sw,n,n,nw,ne,n,n,ne,n,n,n,s,n,n,se,n,nw,s,n,nw,n,ne,n,nw,n,ne,n,nw,nw,n,nw,n,sw,n,ne,n,n,nw,n,n,n,n,s,n,n,nw,sw,nw,sw,n,n,n,n,sw,n,nw,n,n,ne,n,n,n,ne,ne,n,sw,n,nw,n,nw,n,n,n,s,sw,n,n,sw,ne,se,n,se,n,n,n,n,n,sw,n,n,n,n,sw,se,n,n,nw,s,n,n,n,n,se,n,n,n,se,n,s,n,n,n,n,n,n,n,sw,n,n,n,n,n,sw,n,nw,n,n,n,n,s,ne,n,n,n,n,n,n,se,nw,n,s,n,n,n,se,sw,n,n,n,n,n,n,n,s,n,n,nw,sw,s,n,n,n,n,n,ne,se,n,nw,n,sw,se,n,n,s,n,n,ne,n,n,n,s,sw,n,n,n,se,n,n,n,n,n,n,n,n,n,n,n,sw,n,ne,ne,ne,se,n,ne,n,n,n,n,n,sw,n,n,n,n,n,n,ne,n,ne,n,n,se,s,s,n,n,sw,n,n,n,s,n,n,n,ne,nw,n,n,n,n,n,s,n,ne,n,n,n,n,n,n,n,n,n,n,sw,n,s,n,n,n,n,n,ne,n,n,n,n,n,n,n,s,sw,n,n,n,ne,sw,ne,n,n,n,s,se,n,n,n,n,n,n,n,n,n,ne,sw,sw,se,s,n,n,n,nw,sw,ne,n,n,ne,n,n,ne,s,n,ne,n,ne,n,n,n,n,n,ne,n,ne,sw,n,n,ne,n,n,n,n,ne,n,s,ne,n,sw,n,n,n,n,ne,n,ne,se,n,n,n,n,n,ne,sw,n,n,n,n,s,ne,nw,n,n,n,n,n,se,n,ne,se,n,n,n,n,n,ne,n,n,n,ne,n,ne,n,n,n,ne,n,ne,n,n,s,n,n,n,ne,n,n,n,ne,ne,ne,n,n,n,ne,ne,ne,n,n,n,n,n,n,ne,ne,sw,ne,ne,n,nw,ne,n,n,n,se,n,ne,ne,n,ne,nw,ne,n,n,ne,n,s,ne,ne,sw,sw,n,n,ne,se,n,ne,ne,ne,ne,nw,ne,sw,ne,sw,n,n,n,ne,sw,n,n,n,ne,ne,ne,n,ne,n,n,nw,ne,n,n,n,n,ne,s,ne,ne,ne,n,sw,ne,s,n,n,ne,nw,sw,n,n,n,n,n,ne,ne,n,n,n,n,n,n,n,n,s,ne,n,n,n,n,n,n,ne,n,n,ne,s,se,n,ne,se,n,ne,sw,ne,n,ne,ne,ne,ne,n,n,n,s,s,ne,ne,n,ne,n,nw,n,ne,nw,se,ne,ne,ne,n,n,n,s,sw,se,s,n,n,nw,nw,ne,ne,ne,n,ne,ne,ne,ne,ne,sw,ne,ne,ne,n,ne,ne,ne,n,ne,ne,ne,ne,nw,ne,ne,ne,n,n,n,ne,n,ne,n,ne,n,ne,n,n,nw,ne,nw,n,n,n,ne,n,ne,ne,n,ne,nw,ne,n,ne,ne,n,ne,ne,ne,ne,ne,ne,ne,ne,n,n,ne,ne,ne,n,ne,ne,s,ne,ne,n,ne,ne,ne,n,n,ne,n,n,nw,s,n,ne,ne,n,ne,ne,ne,ne,n,ne,ne,n,n,n,ne,ne,n,n,nw,n,ne,ne,nw,n,ne,ne,ne,n,ne,n,ne,se,ne,ne,n,ne,ne,n,ne,ne,ne,ne,ne,ne,n,ne,ne,ne,sw,ne,ne,n,ne,ne,s,ne,n,se,sw,ne,ne,ne,s,ne,ne,s,ne,sw,ne,n,n,sw,ne,ne,ne,n,n,n,s,n,ne,ne,ne,ne,ne,n,ne,n,n,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,se,ne,nw,ne,ne,nw,nw,n,n,nw,ne,ne,ne,ne,n,n,ne,ne,n,ne,ne,s,ne,n,s,ne,ne,n,ne,ne,ne,ne,ne,ne,ne,n,nw,ne,n,n,ne,n,nw,ne,n,ne,ne,n,ne,ne,nw,ne,n,ne,ne,sw,sw,ne,ne,nw,ne,ne,ne,nw,ne,ne,s,ne,ne,ne,ne,ne,sw,n,ne,nw,ne,ne,nw,ne,ne,nw,n,se,ne,s,ne,ne,ne,ne,s,n,ne,ne,n,ne,ne,ne,ne,ne,nw,ne,ne,ne,ne,n,ne,ne,nw,s,ne,nw,ne,ne,ne,ne,ne,sw,sw,ne,n,ne,ne,ne,ne,ne,n,ne,ne,ne,ne,ne,se,ne,se,ne,ne,ne,sw,n,sw,ne,ne,ne,ne,ne,ne,nw,s,nw,se,ne,nw,n,nw,ne,ne,ne,ne,ne,ne,s,ne,ne,ne,ne,ne,ne,ne,ne,se,se,ne,ne,ne,s,ne,n,ne,s,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,s,ne,ne,ne,ne,s,se,ne,nw,ne,sw,se,ne,ne,se"

DIRS = {
    'n': (0, 1),
    's': (0, -1),
    'ne': (1, 0),
    'se': (1, -1),
    'nw': (-1, 1),
    'sw': (-1, 0),
}

GLOBAL_MAX = 0


def hex_dist(x1, y1, x2=0, y2=0):
    z1 = -x1 - y1
    z2 = -x2 - y2

    return max(abs(x2 - x1), abs(y2 - y1), abs(z2 - z1))


def part1():
    global GLOBAL_MAX
    x = 0
    y = 0
    for d in DATA.split(','):
        dx, dy = DIRS[d]
        x += dx
        y += dy
        dist = hex_dist(x, y)
        if dist > GLOBAL_MAX:
            GLOBAL_MAX = dist

    return hex_dist(x, y)


if __name__ == '__main__':
    print("Part 1: {}".format(part1()))
    print("Part 2: {}".format(GLOBAL_MAX))
