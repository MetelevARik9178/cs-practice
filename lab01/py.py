sr = 0
for i in range(3):
    a = int(input())
    sr += a
sr /= 3
print(f'{sr:.1f}')

a, b = float(input()), float(input())
print(f'{a * b:.1f}')
print(f'{2 * a + 2 * b:.1f}')

a, b = float(input()), int(input())
print(f'{a*b:.2f}')

print(f'{float(input()) * 9 / 5 + 32:.1f}')

s = int(input())
print(s // 3600)
print(s % 3600 // 60)
print(s % 60)

a, b = str(input()), str(input())
print(f'Студент: {a}. Группа: {b}.')

a = int(input())
a4 = a % 10
a //= 10
a3 = a % 10
a //= 10
a2 = a % 10
a //= 10
a1 = a
print(a1)
print(a2)
print(a3)
print(a4)
print(a1 + a2 + a3 + a4)
print(f'{a4}{a3}{a2}{a1}')