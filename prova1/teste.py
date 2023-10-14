import control as ctl
import numpy
import matplotlib.pyplot as plt

P_s = ctl.tf([1.,2.,2.,1.], [1.,1.7,0.8,0.1]);
print(P_s);

ps_ma = ctl.pole(P_s);
zs_ma = ctl.zero(P_s);

print('polos=', ps_ma);
print('zeros=', zs_ma);

if ps_ma < 1:
	print("Sistema estável")
else:
	print("Sistema instável")

pz = ctl.pzmap(P_s, 1, 0, 'Diagrama de polos e zeros')
plt.plot(pz)