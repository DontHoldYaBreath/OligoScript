#Insert all amino acids at all positions
pos1 = ['L', 'F', 'Y', 'M', 'A', 'G', 'S', 'T', 'N', 'Q', 'D', 'E', 'K', 'R']
pos2 = ['S', 'W', 'M', 'I', 'V', 'A', 'G', 'T', 'N', 'Q', 'D', 'E', 'K']
pos3 = ['T', 'L', 'K']
pos4 = ['I']
pos5 = ['K', 'W']
pos6 = ['F', 'M', 'A', 'N', 'Q', 'E', 'R']
pos7 = ['I', 'F', 'W', 'Y', 'M', 'L', 'T', 'E', 'H', 'K', 'R']
pos8 = ['D', 'F', 'W', 'L', 'V', 'T', 'N', 'E']
pos9 = ['M', 'T', 'R']
pos10 = ['E', 'A', 'T']
pos11 = ['L']
pos12 = ['V', 'M', 'A', 'Q', 'H', 'K']
pos13 = ['K', 'M', 'I', 'V', 'A', 'S', 'Q', 'E', 'R']
pos14 = ['R', 'F', 'W', 'Y', 'M', 'I', 'L','V','A','G','S','T','N','E','K']
pos15 = ['K','M','N','R']
pos16 = ['R']
pos17 = ['I','V','A','K','R']
pos18 = ['E','F','Y','M','A','S','N','Q','H','K','R']
pos19 = ['A','S','N']
pos20 = ['I','L','V','N']
pos21 = ['R','M','A','S','N']
pos22 = ['G','M','L','A','S','N','D','E']
pos23 = ['Q','A','G','S','E']
pos24 = ['I','V']
pos25 = ['L','P','A','G','S','T','N','Q','D','E']
pos26 = ['S']
pos27 = ['K']
pos28 = ['L', 'M','V','A','G','S','T','N','Q','D','E','H','K']
pos29 = ['R','M','A','G','S','T','N','Q','D','E','K']
pos30 = ['L','M','G','S','T','N','K','R']
pos31 = ['A','F','Y','M','L','G','S','T','Q','D','N','H','K']
pos32 = ['S','L','A','E','R']
pos33 = ['P','M','I','L','V','A','G','S','T','N','Q','D','E','K','R']
pos34 = ['P','F','W','M','I','L','V','A','G','S','T','N','Q','D','E','H','K','R']
pos35 = ['S']
pos36 = ['G','S','N','H']
pos37 = ['L','G','S','N','D','K','R']
pos38 = ['T','N','Q','E','H']
pos39 = ['M','V','A','S','K']
pos40 = ['P','F','W','Y','M','I','L','V','A','G','S','T','N','Q','D','E','H','K','R']
pos41 = ['P','F','W','Y','M','I','L','V','A','G','S','T','N','Q','D','E','H','K','R']
pos42 = ['G']
pos43 = ['P','S','T','D']
pos44 = ['L','A','G','S']
pos45 = ['P'] 
pos46 = ['V','A','N','E']
pos47 = ['F','A','S','N','D','E','H','K']
pos48 = ['V']
pos49 = ['M','I','L','V','N','Q','E','R']
pos50 = ['A']
pos51 = ['L']
pos52 = ['Y','F','W','M','A','S','D','H']
pos53 = ['W','M','L','A','S','N','Q','E','H','R']
pos54 = ['A','S','N']
pos55 = ['A','I','G','S','T','E','R']
pos56 = ['F','W','Y','M','L','A','G','S','T','N','Q','D','E','H','K','R']
 

#codon optimization reference for sac. cerev. yeast
import random
#     .59   .41
subf = ['TTT ', 'TTC ']
#     .28   .29   .13   .06    .14    .11
subl = ['TTA ', 'TTG ', 'CTT ', 'CTC ', 'CTA ', 'CTG ']
#     .56   .44
suby = ['TAT ', 'TAC ']
#     .64   .36
subh = ['CAT ', 'CAC ']
#     .69   .31
subq = ['CAA ', 'CAG ']
#     .46   .26   .27
subi = ['ATT ', 'ATC ', 'ATA ']
#     1
subm = ['ATG ']
#     .59   .41
subn = ['AAT ', 'AAC ']
#     .58   .42
subk = ['AAA ', 'AAG ']
#     .39   .21   .21   .19
subv = ['GTT ', 'GTC ', 'GTA ', 'GTG ']
#     .65   .35
subd = ['GAT ', 'GAC ']
#     .7   .3
sube = ['GAA ', 'GAG ']
#     .26   .16     .21      .1      .13    .11
subs = ['TCT ', 'TCC ', 'TCA ', 'TCG ', 'AGT ', 'AGC ']
#     .63   .37
subc = ['TGT ', 'TGC ']
#     1
subw = ['TGG ']
#     .31   .15   .42   .12
subp = ['CCT ', 'CCC ', 'CCA ', 'CCG ']
#     .14   .06   .07   .04     .48   .21
subr = ['CGT ', 'CGC ', 'CGA ', 'CGG ', 'AGA ', 'AGG ']
#     .35   .22   .3   .14
subt = ['ACT ', 'ACC ', 'ACA ', 'ACG ']
#     .38   .22   .29   .11
suba = ['GCT ', 'GCC ', 'GCA ', 'GCG ']
#     .47   .19   .22   .12
subg = ['GGT ', 'GGC ', 'GGA ', 'GGG ']

#Reset count to get total number
count = 0
#Iterate through positions
for a in range(0, len(pos1)):
    for b in range(0, len(pos2)):
        for c in range(0, len(pos3)):
            for d in range(0, len(pos4)):
                for e in range(0, len(pos5)):
                    for f in range (0,len(pos6)):
                        for g in range (0,len(pos7)):
                            for h in range (0,len(pos8)):
                                for i in range (0,len(pos9)):
                                    for j in range (0,len(pos10)):
                                        for k in range (0,len(pos11)):
                                            for l in range (0,len(pos12)):
                                                for m in range (0,len(pos13)):
                                                    for n in range (0,len(pos14)):
                                                        for o in range (0,len(pos15)):
                                                            for p in range (0,len(pos16)):
                                                                for q in range (0,len(pos17)):
                                                                    for r in range (0,len(pos18)):
                                                                        for s in range (0,len(pos19)):
                                                          #save positions as amino acids                  
                                                                            oligo = pos1[a] + pos2[b] + pos3[c] + pos4[d] + pos5[e] + pos6[f] + pos7[g] + pos8[h] + pos9[i] + pos10[j] + pos11[k] + pos12[l] + pos13[m] + pos14[n] + pos15[o] + pos16[p] + pos17[q] + pos18[r] + pos19[s]
                                                          #                  print(oligo)
                                                                            OL = len(oligo)
                                                                            codonarray = []
                                                          # Set up array to get around "replace" errors                      
                                                                            for var in range(OL):

                                                                                  #Convert AA to Codons, using codon optimization values
                                                                                  if oligo[var] == 'F':
                                                                                      bias = random.randint(0, 10) / 10
                                                                                      if bias <= 0.59:
                                                                                          codonarray.append(subf[0])
                                                                                      elif bias <= 1:
                                                                                          codonarray.append(subf[1])

                                                                                  if oligo[var] == 'L':
                                                                                      bias = random.randint(0, 10) / 10
                                                                                      if bias <= 0.28:
                                                                                          codonarray.append(subl[0])
                                                                                      elif bias <= 0.57:
                                                                                          codonarray.append(subl[1])
                                                                                      elif bias <= .7:
                                                                                          codonarray.append(subl[2])
                                                                                      elif bias <= .76:
                                                                                          codonarray.append(subl[3])
                                                                                      elif bias <= .9:
                                                                                          codonarray.append(subl[4])
                                                                                      elif bias <= 1:
                                                                                          codonarray.append(subl[5])

                                                                                  if oligo[var] == 'Y':
                                                                                      bias = random.randint(0, 10) / 10
                                                                                      if bias <= 0.56:
                                                                                          codonarray.append(suby[0])
                                                                                      elif bias <= 1:
                                                                                          codonarray.append(suby[1])

                                                                                  if oligo[var] == 'H':
                                                                                      bias = random.randint(0, 10) / 10
                                                                                      if bias <= 0.64:
                                                                                          codonarray.append(subh[0])
                                                                                      elif bias <= 1:
                                                                                          codonarray.append(subh[1])

                                                                                  if oligo[var] == 'Q':
                                                                                      bias = random.randint(0, 10) / 10
                                                                                      if bias <= 0.69:
                                                                                          codonarray.append(subq[0])
                                                                                      elif bias <= 1:
                                                                                          codonarray.append(subq[1])

                                                                                  if oligo[var] == 'I':
                                                                                      biasi = random.randint(0, 10) / 10
                                                                                      if biasi <= 0.46:
                                                                                          codonarray.append(subi[0])
                                                                                      elif biasi <= 0.72:
                                                                                          codonarray.append(subi[1])
                                                                                      elif biasi <= 1:
                                                                                          codonarray.append(subi[2])

                                                                                  if oligo[var] == 'M':
                                                                                      bias = random.randint(0, 10) / 10
                                                                                      if bias <= 1:
                                                                                          codonarray.append(subm[0])

                                                                                  if oligo[var] == 'N':
                                                                                      bias = random.randint(0, 10) / 10
                                                                                      if bias <= 0.59:
                                                                                          codonarray.append(subn[0])
                                                                                      elif bias <= 1:
                                                                                          codonarray.append(subn[1])

                                                                                  if oligo[var] == 'K':
                                                                                      biask = random.randint(0, 10) / 10
                                                                                      if biask <= 0.58:
                                                                                          codonarray.append(subk[0])
                                                                                      elif biask <= 1:
                                                                                          codonarray.append(subk[1])

                                                                                  if oligo[var] == 'V':
                                                                                      bias = random.randint(0, 10) / 10
                                                                                      if bias <= .39:
                                                                                          codonarray.append(subv[0])
                                                                                      elif bias <= 0.6:
                                                                                          codonarray.append(subv[1])
                                                                                      elif bias <= .81:
                                                                                          codonarray.append(subv[2])
                                                                                      elif bias <= 1:
                                                                                          codonarray.append(subv[3])

                                                                                  if oligo[var] == 'D':
                                                                                      bias = random.randint(0, 10) / 10
                                                                                      if bias <= 0.65:
                                                                                          codonarray.append(subd[0])
                                                                                      elif bias <= 1:
                                                                                          codonarray.append(subd[1])

                                                                                  if oligo[var] == 'E':
                                                                                      bias = random.randint(0, 10) / 10
                                                                                      if bias <= 0.7:
                                                                                          codonarray.append(sube[0])
                                                                                      elif bias <= 1:
                                                                                          codonarray.append(sube[1])

                                                                                  if oligo[var] == 'S':
                                                                                      bias = random.randint(0, 10) / 10
                                                                                      if bias <= 0.26:
                                                                                          codonarray.append(subs[0])
                                                                                      elif bias <= 0.42:
                                                                                          codonarray.append(subs[1])
                                                                                      elif bias <= .63:
                                                                                          codonarray.append(subs[2])
                                                                                      elif bias <= .73:
                                                                                          codonarray.append(subs[3])
                                                                                      elif bias <= .86:
                                                                                          codonarray.append(subs[4])
                                                                                      elif bias <= 1:
                                                                                          codonarray.append(subs[5])

                                                                                  if oligo[var] == 'C':
                                                                                      bias = random.randint(0, 10) / 10
                                                                                      if bias <= .63:
                                                                                          codonarray.append(subc[0])
                                                                                      elif bias <= 1:
                                                                                          codonarray.append(subc[1])

                                                                                  if oligo[var] == 'W':
                                                                                      biasw = random.randint(0, 10) / 10
                                                                                      if biasw <= 1:
                                                                                          codonarray.append(subw[0])

                                                                                  if oligo[var] == 'P':
                                                                                      bias = random.randint(0, 10) / 10
                                                                                      if bias <= 0.31:
                                                                                          codonarray.append(subp[0])
                                                                                      elif bias <= 0.46:
                                                                                          codonarray.append(subp[1])
                                                                                      elif bias <= .88:
                                                                                          codonarray.append(subp[2])
                                                                                      elif bias <= 1:
                                                                                          codonarray.append(subp[3])

                                                                                  if oligo[var] == 'R':
                                                                                      biasr = random.randint(0, 10) / 10
                                                                                      if biasr <= 0.14:
                                                                                          codonarray.append(subr[0])
                                                                                      elif biasr <= 0.2:
                                                                                          codonarray.append(subr[1])
                                                                                      elif biasr <= .27:
                                                                                          codonarray.append(subr[2])
                                                                                      elif biasr <= .31:
                                                                                          codonarray.append(subr[3])
                                                                                      elif biasr <= .79:
                                                                                          codonarray.append(subr[4])
                                                                                      elif biasr <= 1:
                                                                                          codonarray.append(subr[5])

                                                                                  if oligo[var] == 'T':
                                                                                      bias = random.randint(0, 10) / 10
                                                                                      if bias <= 0.35:
                                                                                          codonarray.append(subt[0])
                                                                                      elif bias <= 0.57:
                                                                                          codonarray.append(subt[1])
                                                                                      elif bias <= .87:
                                                                                          codonarray.append(subt[2])
                                                                                      elif bias <= 1:
                                                                                          codonarray.append(subt[3])

                                                                                  if oligo[var] == 'A':
                                                                                      bias = random.randint(0, 10) / 10
                                                                                      if bias <= 0.38:
                                                                                          codonarray.append(suba[0])
                                                                                      elif bias <= 0.5:
                                                                                          codonarray.append(suba[1])
                                                                                      elif bias <= .79:
                                                                                          codonarray.append(suba[2])
                                                                                      elif bias <= 1:
                                                                                          codonarray.append(suba[3])

                                                                                  if oligo[var] == 'G':
                                                                                      bias = random.randint(0, 10) / 10
                                                                                      if bias <= 0.47:
                                                                                          codonarray.append(subg[0])
                                                                                      elif bias <= 0.66:
                                                                                          codonarray.append(subg[1])
                                                                                      elif bias <= .88:
                                                                                          codonarray.append(subg[2])
                                                                                      elif bias <= 1:
                                                                                          codonarray.append(subg[3])
                                                                                          
                                                                            count = count + 1
                                                                            printable=' '.join(codonarray)
                                                          #Store in the console
                                                                            print(printable)
                                                          #Send to Txt file                  
                                                                            appendfile=open('OligoCodons.txt','a')
                                                                            appendfile.write('\n')
                                                                            countstring=str(count)
                                                                            appendfile.write(countstring)
                                                                            appendfile.write('\t')
                                                                            appendfile.write(printable)        
                                                                                                                                                                                  
                                                                                

#Determine how many total Oligos
print(count)


#This is working as intended, just get into a file

