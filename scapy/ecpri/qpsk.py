import numpy as np
import  matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
# matplotlib.use("TkAgg")

num_symbols = 1000

x_int = np.random.randint(0, 4, num_symbols)
print(x_int)
x_degrees = x_int*360/4.0 + 45
x_radians = x_degrees*np.pi/180.0
print(x_degrees)
print(x_radians)
x_symbols = np.cos(x_radians) + 1j*np.sin(x_radians)
print(x_symbols)
# r = x_symbols
n = (np.random.randn(num_symbols) + 1j*np.random.randn(num_symbols))/np.sqrt(2)
# print(n)
r = x_symbols + n * np.sqrt(0.01)


# plt.ion()
plt.plot(np.real(r), np.imag(r), '.')
# plt.plot(np.imag(r), '.')
plt.grid(True)
plt.show()