import numpy as np
import matplotlib.pyplot as plt

f = 2  
fs = 20 * f  
t = np.arange(0, 2 + 1/fs, 1/fs) 
a = 2  

msg = a * np.sin(2 * np.pi * f * t)
x1 = msg + a

quant = np.round(x1).astype(int)


def dec2bin(decimal_array):
    return [format(x, '08b') for x in decimal_array]

def bin2dec(binary_strings):
    return np.array([int(b, 2) for b in binary_strings])

encoded = dec2bin(quant)
decoded = bin2dec(encoded)

recovered = decoded - a

plt.figure(figsize=(10, 10))

plt.subplot(3, 1, 1)
plt.plot(t, msg)
plt.xlabel('TIME')
plt.ylabel('AMPLITUDE')
plt.title('Message Signal')
plt.ylim(-3, 3)

plt.subplot(3, 1, 2)
plt.plot(t, recovered)
plt.xlabel('TIME')
plt.ylabel('AMPLITUDE')
plt.title('Recovered Signal')
plt.ylim(-3, 3)

plt.subplot(3, 1, 3)
plt.plot(t, msg, 'b', label='Original')
plt.plot(t, recovered, 'r', label='Recovered')
plt.xlabel('TIME')
plt.ylabel('AMPLITUDE')
plt.title('Recovered VS Original Signal')
plt.ylim(-3, 3)
plt.legend()

plt.tight_layout()
plt.show()

print("Discrete Sampled Values of Message Signal:")
print(x1[:10])  
print("\nQuantized Sampled Values:")
print(quant[:10]) 
print("\nPCM coded Values:")
print(encoded[:10]) 
