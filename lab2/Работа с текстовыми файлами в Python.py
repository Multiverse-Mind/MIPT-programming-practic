import turtle as tl


tl.shape('turtle')
sp = ['', '', '', '', '', '', '', '', '', '']
f = open('Шрифт.txt', 'r')
for j in range(10):
    st = f.readline()
    i, sk = st.split('-')
    i = int(i)
    spk = [(int(k[0]), int(k[2])) for k in sk.split()]
    sp[i] = spk
f.close()
print(sp)
s = '0123456789'
sh = 50
p = 20
po = -350
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