import numpy as np
import matplotlib.pyplot as plt

# =========================
# Problema (EDO separable):
# dy/dt = -k*y,  y(0)=y0
# Ejemplo real: enfriamiento simple / decaimiento
# =========================

k = 2.0     # constante (elige 1, 2, etc.)
y0 = 1.0    # condición inicial
h = 0.2     # paso (pedido)
t0 = 0.0
t_end = 1.0

def exacta(t):
    # Solución analítica por separación de variables:
    # y(t) = y0 * e^(-k t)
    return y0 * np.exp(-k * t)

def euler():
    # Euler: y_{n+1} = y_n + h*f(t_n, y_n), f=-k*y
    t_vals = [t0]
    y_vals = [y0]

    n_steps = int(round((t_end - t0) / h))
    t = t0
    y = y0

    for _ in range(n_steps):
        y = y + h * (-k * y)
        t = t + h
        t_vals.append(t)
        y_vals.append(y)

    return np.array(t_vals), np.array(y_vals)

# Calcular
t_eu, y_eu = euler()
y_ex = exacta(t_eu)
error = np.abs(y_eu - y_ex)

# Tabla para evidencia
print("t\tEuler\t\tExacta\t\tError")
for t, ye, yx, er in zip(t_eu, y_eu, y_ex, error):
    print(f"{t:.1f}\t{ye:.6f}\t{yx:.6f}\t{er:.6f}")

# Gráfica
plt.figure(figsize=(8,5))
plt.plot(t_eu, y_eu, marker="o", label="Euler (h=0.2)")
plt.plot(t_eu, y_ex, linestyle="--", label="Exacta (analítica)")
plt.title("Comparación: solución analítica vs Euler")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("comparacion.png")
print("\n✅ Se guardó la gráfica: comparacion.png")
