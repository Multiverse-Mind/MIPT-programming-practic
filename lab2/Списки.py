import turtle as tl


tl.shape('turtle')
sp0 = [(0, 0), (0, 2), (1, 2), (1, 0), (0, 0)]
sp1 = [(0, 1), (1, 0), (1, 2)]
sp4 = [(0, 0), (0, 1), (1, 1), (1, 2), (1, 0)]
sp7 = [(0, 0), (1, 0), (0, 1), (0, 2)]
sp = [sp0, sp1, '', '', sp4, '', '', sp7, '', '']
s = '141700'
sh = 50
p = 20
po = -200
for i in range(len(s)):
    tl.penup()
    tl.goto(po, 0)
    f = True
    for c in sp[int(s[i])]:
        tl.goto(po + c[0] * sh, -c[1] * sh)
        if f:
            tl.pendown()
            f = False
    po += sh + p