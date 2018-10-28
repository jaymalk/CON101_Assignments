#!/usr/bin/env python3
from matplotlib import pyplot as plt
def main():
    k = 10
    c = 0.5
    for i in range(10):
        time = [0]
        x = [1]
        v = [0]
        del_t = 1/(10*pow(2, i))
        div_t = (k*del_t**2 + c*del_t + 1)
        while time[-1] < 5:
            x_t = x[-1]
            v_t = v[-1]
            v.append((v_t-k*del_t*x_t)/div_t)
            v_t = v[-1]
            x.append(x_t + del_t*v_t)
            time.append(time[-1]+del_t)
        if i == 9:
            plt.plot(time, x, linestyle = 'dashed', color = 'k', linewidth = 0.75)
            break
        plt.plot(time, x)
    plt.grid(True, which='both')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()

if __name__ == '__main__':
    main()
