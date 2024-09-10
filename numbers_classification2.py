import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Настройка рисунка и осей
fig, ax = plt.subplots(figsize=(15, 15))
ax.set_xlim(0, 20)
ax.set_ylim(0, 20)
ax.set_aspect('equal')

# Убираем оси
ax.axis('off')

# Определение кругов и текста
circles = {
    "Complex Numbers": (10, 10, 6),
    "Real Numbers": (10, 10, 4.5),
    "Rational Numbers": (10, 10, 3.5),
    "Irrational Numbers": (10, 10, 2.5),
    "Integer Numbers": (10, 10, 2),
    "Natural Numbers": (10, 10, 1.5),
    "Prime Numbers": (10, 10, 1.2),
    "Transcendental Numbers": (15, 10, 1.2),
    "Algebraic Numbers": (5, 10, 1.2),
    "Quaternions": (15, 15, 1.2),
    "Octonions": (5, 15, 1.2),
    "Sedenions": (15, 5, 1.2),
    "Trinions": (5, 5, 1.2),
}

# Нарисовать круги
for label, (x, y, r) in circles.items():
    circle = patches.Circle((x, y), r, edgecolor='black', facecolor='none', linewidth=2)
    ax.add_patch(circle)
    ax.text(x, y, label, ha='center', va='center', fontsize=10, fontweight='bold')

# Установить связи между кругами
connections = [
    ("Complex Numbers", "Real Numbers"),
    ("Real Numbers", "Rational Numbers"),
    ("Real Numbers", "Irrational Numbers"),
    ("Rational Numbers", "Integer Numbers"),
    ("Integer Numbers", "Natural Numbers"),
    ("Rational Numbers", "Prime Numbers"),
    ("Complex Numbers", "Transcendental Numbers"),
    ("Real Numbers", "Algebraic Numbers"),
    ("Algebraic Numbers", "Transcendental Numbers"),
    ("Complex Numbers", "Quaternions"),
    ("Quaternions", "Octonions"),
    ("Octonions", "Sedenions"),
    ("Sedenions", "Trinions")
]

# Нарисовать связи
for start, end in connections:
    start_x, start_y, _ = circles[start]
    end_x, end_y, _ = circles[end]
    ax.plot([start_x, end_x], [start_y, end_y], color='black', linestyle='--')

# Показать график
plt.title('Diagram of Number Types and Their Relationships')
plt.show()
