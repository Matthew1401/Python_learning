# -*- coding: utf-8 -*-
#Obliczanie zapotrzebowania kalorycznego dla
#a) kobiety
#b) siebie samego
#https://www.flynerd.pl/2017/01/python-1-zabawy-w-konsoli.html


print ("a) dla 25-letniej kobiety o wzroście 1.7m i wadze 63kg, która uprawia sport kilka razy w tygodniu.")
wk=170
mk=63
wS=(10*mk+6.25*wk-5*25-161)*1.6
print("Współczynnik S dla kobiety wynosi:", wS)
print()

print("b) siebie samej / samego.")
mm=80
wm=181
wSm=(10*mm+6.25*wm-5*19+5)*1.6
print("Współczynnik S dla mnie wynosi:", wSm)