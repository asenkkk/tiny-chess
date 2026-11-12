h='wtime'
g='movetime'
f='qrbn'
d=enumerate
e=tuple
c=Exception
T=print
N=int
M=range
E=abs
import sys,time as U
i=100,320,330,500,900,0
V=[-33,-31,-18,-14,14,18,31,33]
H=[-17,-15,15,17]
I=[-16,-1,1,16]
def j(b,w):
	D=0
	for A in M(128):
		if A&136:continue
		B=b[A]
		if not B:continue
		F=E(B);H=A&7;G=A>>4;C=i[F-1]
		if F==2:C+=(7-max(E(2*H-7),E(2*G-7)))*4
		elif F==1:I=6-G if B>0 else G-1;C+=I*5
		D+=C if B>0 else-C
	return D if w else-D
def O(b,q,c):
	for B in(17,15):
		A=q+B*c
		if not A&136 and b[A]==c:return 1
	for B in V:
		A=q+B
		if not A&136 and b[A]==c*2:return 1
	for B in H+I:
		A=q+B
		if not A&136 and b[A]==c*6:return 1
	for B in H+I:
		A=q+B
		while not A&136:
			C=b[A]
			if C:
				if B in H and C in(c*3,c*5)or B in I and C in(c*4,c*5):return 1
				break
			A+=B
	return 0
def W(b,w,ca,ep):
	F=1 if w else-1;C=[];G=-1
	for B in M(128):
		if B&136:continue
		L=b[B]
		if not L or(L>0)!=(F>0):continue
		J=E(L);N=B>>4
		if J==6:G=B
		if J==1:
			D=-16*F;R=0 if F>0 else 7;A=B+D
			if not A&136 and not b[A]:
				if N+D//16==R:
					for Q in(5,4,3,2):C.append((B,A,Q))
				else:C.append((B,A,0))
				if N==(6 if F>0 else 1)and not b[B+2*D]:C.append((B,B+2*D,0))
			for W in(D-1,D+1):
				A=B+W
				if A&136:continue
				if b[A]and(b[A]>0)!=(F>0):
					if N+D//16==R:
						for Q in(5,4,3,2):C.append((B,A,Q))
					else:C.append((B,A,0))
				elif A==ep:C.append((B,A,0))
		elif J in(2,6):
			for D in V if J==2 else H+I:
				A=B+D
				if A&136:continue
				if not b[A]:C.append((B,A,0))
				elif(b[A]>0)!=(F>0):C.append((B,A,0))
		else:
			for D in(H,I,H+I)[J-3]:
				A=B+D
				while not A&136:
					if b[A]:
						if(b[A]>0)!=(F>0):C.append((B,A,0))
						break
					C.append((B,A,0));A+=D
	if G>=0:
		for(S,X,Y,T)in((1,2,3,(1,2)),(2,-2,-4,(-1,-2,-3))):
			S*=4 if F<0 else 1;Z=G+X;a=G+Y
			if ca&S and b[a]==F*4 and all(not b[G+A]for A in T)and all(not O(b,G+A,-F)for A in(0,)+T[:2]):C.append((G,Z,0))
	U=[]
	for K in C:
		c,e,f=P(b,w,ca,ep,K);d=K[1]if E(b[K[0]])==6 else G
		if not O(c,d,-F):U.append(K)
	return U
def P(b,w,ca,ep,m):
	C,A,F=m;B=b[:];G=1 if w else-1;D=B[C];B[C]=0
	if E(D)==1 and A==ep and not b[A]:B[A+16*G]=0
	if E(D)==6 and E(A-C)==2:
		if A>C:B[A-1]=B[A+1];B[A+1]=0
		else:B[A+1]=B[A-2];B[A-2]=0
	B[A]=G*F if F else D;H=ca
	for(I,J)in((116,3),(112,2),(119,1),(4,12),(0,8),(7,4)):
		if C==I or A==I:H&=~J
	K=(C+A)//2 if E(D)==1 and E(A-C)==32 else-1;return B,H,K
Q=[0]
X=[0]
R={}
def Y(b,w,ca,ep,d,al,be,pl):
	Q[0]+=1
	if Q[0]%2048==0 and U.time()>X[0]:raise c
	if d<=0:return j(b,w)
	D=e(b),w;H=R.get(D);A=W(b,w,ca,ep)
	if not A:return-99999+pl if O(b,[A for A in M(128)if b[A]==(6 if w else-6)][0],-1 if w else 1)else 0
	A.sort(key=lambda m:(m==H,E(b[m[1]])),reverse=True);C=-9e8;F=A[0]
	for G in A:
		I,J,K=P(b,w,ca,ep,G);B=-Y(I,not w,J,K,d-1,-be,-al,pl+1)
		if B>C:C=B;F=G
		if B>al:al=B
		if al>=be:break
	R[D]=F;return C
def S(s):return(8-N(s[1]))*16+ord(s[0])-97
def Z(f):
	A=f.split();E=[0]*128
	for(F,G)in d(A[0].split('/')):
		B=0
		for C in G:
			if C.isdigit():B+=N(C)
			else:D='PNBRQKpnbrqk'.find(C);E[F*16+B]=D+1 if D<6 else 5-D;B+=1
	H=sum(1<<B for(B,C)in d('KQkq')if C in A[2]);I=S(A[3])if A[3]!='-'else-1;return E,A[1]=='w',H,I
def a():return Z('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
D,B,F,G=a()
for A in map(str.split,sys.stdin):
	if not A:continue
	if A[0]=='uci':T('uciok',flush=1)
	elif A[0]=='isready':T('readyok',flush=1)
	elif A[0]=='quit':break
	elif A[0]=='position':
		if A[1]=='startpos':D,B,F,G=a();K=2
		else:D,B,F,G=Z(' '.join(A[2:8]));K=8
		if K<len(A)and A[K]=='moves':
			for L in A[K+1:]:D,F,G=P(D,B,F,G,(S(L[:2]),S(L[2:4]),5-f.find(L[4])if len(L)>4 else 0));B=not B
	elif A[0]=='go':
		J=1
		if g in A:J=N(A[A.index(g)+1])/1000
		elif h in A:J=N(A[A.index(h if B else'btime')+1])/30000
		J=min(5,J);Q[0]=0;X[0]=U.time()+J;C=None;k=e(D),B
		try:
			for l in M(1,100):Y(D,B,F,G,l,-9e8,9e8,0);C=R[k]
		except c:0
		if C is None:b=W(D,B,F,G);C=b[0]if b else(0,0,0)
		T(f"bestmove {chr(97+(C[0]&7))}{8-(C[0]>>4)}{chr(97+(C[1]&7))}{8-(C[1]>>4)}{f[5-C[2]]if C[2]else""}",flush=1)