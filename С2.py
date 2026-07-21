import sys

# Увеличиваем лимит рекурсии на случай глубоких вызовов, хотя макс. глубина здесь 20
sys.setrecursionlimit(2000)


def solve():
    # Быстрый ввод/вывод для олимпиадных задач
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    t = int(input_data[0])
    out = []

    idx = 1
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        # Проверяем на возможность перестановки
        # Слой на позиции i (0-индексация) не может иметь над собой больше i слоёв
        possible = True
        for i in range(n):
            if a[i] > i:
                possible = False
                break

        if not possible:
            out.append("NO")
            continue

        moves = []
        current = [1] * n  # Изначально все слои (размеров 1..n) находятся на кухне (позиция 1)

        def reach(k, target):
            """
            k: текущий рассматриваемый слой (1-индексация)
            target: массив целевых стержней для слоев 1..n
            """
            if k == 0:
                return

            i = k - 1
            T = target[i]
            C = current[i]

            # Если текущая позиция k-го слоя уже совпадает с целевой, переходим к (k-1)
            if C == T:
                reach(k - 1, target)
                return

            S = C
            A = 6 - S - T  # Так как S и T — это 1, 2, или 3, то сумма всех стержней = 6

            I = target[:]
            needed_S = a[i]
            needed_A = i - needed_S

            # Распределяем слои от 0 до i-1 так, чтобы ровно needed_S оказались на S, а needed_A на A.
            # Для минимизации ходов стараемся не двигать слои, которые уже находятся на нужных позициях.
            for j in range(i):
                if current[j] == S and needed_S > 0:
                    I[j] = S
                    needed_S -= 1
                elif current[j] == A and needed_A > 0:
                    I[j] = A
                    needed_A -= 1
                else:
                    I[j] = 0

            for j in range(i):
                if I[j] == 0:
                    if needed_S > 0:
                        I[j] = S
                        needed_S -= 1
                    else:
                        I[j] = A
                        needed_A -= 1

            # 1. Приводим диски меньше k к промежуточному состоянию I
            reach(k - 1, I)

            # 2. Двигаем сам слой k
            moves.append(f"{k} {S} {T}")
            current[i] = T

            # 3. Достраиваем диски меньше k на их конечное место
            reach(k - 1, target)

        # Вызываем для всего торта, чтобы он оказался на празднике (позиция 3)
        reach(n, [3] * n)

        out.append("YES")
        out.append(str(len(moves)))
        out.extend(moves)

    # Печатаем все ответы за один раз для скорости
    sys.stdout.write('\n'.join(out) + '\n')

solve()