g='movetime'
d=enumerate
c=Exception
def T(a):print(a,flush=1)
E=abs
import time as U
i=100,320,330,500,900,0;P=0,8,16,24,24,16,8,0
V=(-33,-31,-18,-14,14,18,31,33)
H=(-17,-15,15,17)
I=(-16,-1,1,16)
O=0,0,V,H,I,H+I,H+I
def ev(b,w):
 D=0
 for A,B in d(b):
  if B and A&136==0:
   F=E(B);C=i[F-1]
   if F==2:C+=min(P[A&7],P[A>>4])
   elif F==1:C+=((6-(A>>4),(A>>4)-1)[B<0])*5
   D+=C if(B>0)==w else-C
 return D
def at(b,q,c):
 for S,P in(((17*c,15*c),c),(V,2*c),(H+I,6*c)):
  if any((q+D)&136==0 and b[q+D]==P for D in S):return 1
 for B in H+I:
  A=q+B
  while A&136==0 and not b[A]:A+=B
  if A&136==0 and b[A]//c in((3,5),(4,5))[B in I]:return 1
 return 0
def gm(b,w,ca,ep):
 F=1-2*(not w);C=[]
 for B,L in d(b):
  if B&136 or not L or(L>0)!=(F>0):continue
  J=E(L);N=B>>4
  if J==1:
   D=-16*F;S=6-5*(F<0)
   def P(A):C.extend([(B,A,q)for q in((5,4,3,2),(0,))[N!=7-S]])
   A=B+D
   if A&136==0 and not b[A]:
    P(A)
    if N==S and not b[B+2*D]:C.append((B,B+2*D,0))
   for A in(B+D-1,B+D+1):
    if A&136:continue
    if b[A]and(b[A]>0)!=(F>0)or A==ep:P(A)
  else:
   for D in O[J]:
    A=B+D
    while A&136==0:
     if b[A]:C.append((B,A,0))if(b[A]>0)!=(F>0)else 0;break
     C.append((B,A,0))
     if J in(2,6):break
     A+=D
 G=b.index(6-12*(not w))
 for(S,X,Y,T)in((1,2,3,(1,2)),(2,-2,-4,(-1,-2,-3))):
  S*=1+3*(F<0);Z=G+X;a=G+Y
  if ca&S and b[a]==F*4 and not any(b[G+A]for A in T)and not any(at(b,G+A,-F)for A in(0,)+T[:2]):C.append((G,Z,0))
 return[K for K in C if not at(do(b,w,ca,ep,K)[0],(G,K[1])[K[0]==G],-F)]
def do(b,w,ca,ep,m):
 C,A,F=m;B=b[:];G=1-2*(not w);D=B[C];B[C]=0
 if E(D)==1 and A==ep:B[A+16*G]=0
 if E(D)==6 and E(A-C)==2:S=1-2*(A<C);R=A+S-(S<0);B[A-S]=B[R];B[R]=0
 B[A]=G*F or D;H=ca
 for(I,J)in((116,3),(112,2),(119,1),(4,12),(0,8),(7,4)):
  if C==I or A==I:H&=~J
 K=(C+A)//2 if E(D)==1 and E(A-C)==32 else-1;return B,H,K
Q,X,R=[0],[0],{}
def sr(b,w,ca,ep,d,al,be):
 Q[0]+=1
 if not Q[0]&2047 and U.time()>X[0]:raise c
 if d<=0:return ev(b,w)
 D=tuple(b),w;H=R.get(D);A=gm(b,w,ca,ep)
 if not A:return-99999 if at(b,b.index(6-12*(not w)),-1+2*(not w))else 0
 A.sort(key=lambda m:(m==H,E(b[m[1]])),reverse=1);C=-9e8
 for G in A:
  I,J,K=do(b,w,ca,ep,G);B=-sr(I,not w,J,K,d-1,-be,-al)
  if B>C:C=B;F=G
  al=max(al,B)
  if al>=be:break
 R[D]=F;return C
def pf(f):
 A=f.split();E=[0]*128;B=0
 for C in A[0]:
  if C<'0':B+=8
  elif C<'A':B+=int(C)
  else:D='PNBRQKpnbrqk'.find(C);E[B]=D+1 if D<6 else 5-D;B+=1
 H=sum(1<<B for(B,C)in d('KQkq')if C in A[2]);I=(8-int(A[3][1]))*16+ord(A[3][0])-97 if A[3]!='-'else-1;return E,A[1]=='w',H,I
class Board:
 def __init__(self):self.b,self.t,self.c,self.e=pf('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq -');self.h=[]
 def parse_fen(self,f):self.b,self.t,self.c,self.e=pf(f)
 def generate_moves(self):return gm(self.b,self.t,self.c,self.e)
 def make_move(self,m):
  s=(self.b,self.t,self.c,self.e);self.h.append(s);self.b,self.c,self.e=do(*s,m);self.t=not self.t
 def unmake_move(self):self.b,self.t,self.c,self.e=self.h.pop()
 def is_attacked(self,s,sd):return at(self.b,s,sd)
 def evaluate(self):return ev(self.b,self.t)
class Engine:
 def __init__(self):self.b=Board()
 def go(self,p):
  b=self.b
  J=float(p[g])/1000 if g in p else 1
  Q[0]=0;X[0]=U.time()+(300 if'depth'in p else J);C=0;k=tuple(b.b),b.t
  D=int(p['depth'])if'depth'in p else 99
  for l in range(1,D+1):
   try:sr(b.b,b.t,b.c,b.e,l,-9e8,9e8);C=R[k]
   except c:break
  if not C:m=gm(b.b,b.t,b.c,b.e);C=m[0]if m else 0
  T(f"bestmove {m2u(C)}");return C
def m2u(m):
 if not m:return'0000'
 C,A,F=m;return f"{C%8+97:c}{8-C//16}{A%8+97:c}{8-A//16}{'qrbn'[5-F]if F else''}"
def u2m(u,ms):return{m2u(m):m for m in ms}.get(u,0)
if __name__=='__main__':
 o=Engine()
 for A in map(str.split,open(0)):
  if not A:continue
  K=A[0]
  if K=='uci':T('uciok')
  elif K=='isready':T('readyok')
  elif K=='quit':break
  elif K=='position':
   if A[1]=='startpos':o.b=Board();j=2
   else:o.b.parse_fen(' '.join(A[2:8]));j=8
   if j<len(A)and A[j]=='moves':
    for L in A[j+1:]:o.b.make_move(u2m(L,o.b.generate_moves()))
  elif K=='go':o.go(dict(zip(A[1::2],A[2::2])))