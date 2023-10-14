from scipy import signal
import matplotlib.pyplot as plt


h = ([1,0.5],[1.,0.6,0.08])
tempoRespotaImpulso, amplitudeRespotaImpulso = signal.impulse(h);
plt.plot(tempoRespotaImpulso, amplitudeRespotaImpulso)
plt.show()


tempoRespostaDegrau, amplitudeRespostaDegrau = signal.step(h);
plt.plot(tempoRespostaDegrau, amplitudeRespostaDegrau)
plt.show()


