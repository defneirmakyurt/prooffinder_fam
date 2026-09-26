"""Typesetting-fidelity check (stdlib): every inline/display math segment of submission/proof.md
occurs (whitespace-normalised) in submission.tex; every step label and section number is preserved;
the appendix listing equals submission/code/check_c1.py. Run from out/."""
import re
md=open('submission/proof.md').read(); tx=open('submission.tex').read()
norm=lambda s: re.sub(r'\s+','',s); T=norm(tx)
segs=re.findall(r'\$\$(.+?)\$\$',md,re.S)+re.findall(r'(?<!\$)\$([^$]+?)\$(?!\$)',md)
print('math segments:',len(segs),'missing in tex:',sum(norm(s) not in T for s in segs))
labs=re.findall(r'\*\*(\d+\.\d+)\.\*\*',md)
print('step labels:',len(labs),'missing:',[l for l in labs if '\\paragraph{%s.}'%l not in tx])
heads=re.findall(r'^## (\d+)\. ',md,re.M)
print('sections:',len(heads),'missing:',[h for h in heads if '\\subsection*{%s. '%h not in tx])
s=open('submission/code/check_c1.py').read()
a=tx.index('\\begin{verbatim}\n"""')+len('\\begin{verbatim}\n'); b=tx.index('\\end{verbatim}\n\\endgroup')
print('appendix listing identical to script:', tx[a:b]==s)
