# 1261 - Pontos de Feno
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1261


def salary_calulator(hay_points):

    def get_salary(desc):
        return sum(hay_points.get(word, 0) for word in desc.split())
    
    return get_salary


def main():
    m, n = map(int, input().split())
    hay_points = {}

    for _ in range(m):
        word, value = input().split()
        hay_points[word] = int(value)

    get_salary = salary_calulator(hay_points)

    for _ in range(n):
        desc = []
        while True:
            line = input()
            if line == '.':
                break
            desc.append(line)
        print(get_salary(' '.join(desc)))
    

if __name__ == '__main__':
    main()
