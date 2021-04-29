# 1608 - Bolos da Maria
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1608


def main():
    num_tests = int(input())

    for _ in range(num_tests):
        (cash,
         _,
         num_cake_types) = [int(x) for x in input().split()]

        ingredient_costs = [int(i) for i in input().split()]

        max_num_of_cakes = 0
        for _ in range(num_cake_types):
            cake_description = [int(b) for b in input().split()]
            cake_cost = 0
            
            for idx_ingredient, quantity in zip(cake_description[1::2],
                                                cake_description[2::2]):
                cake_cost += ingredient_costs[idx_ingredient] * quantity
            
            if cash//cake_cost > max_num_of_cakes:
                max_num_of_cakes = cash//cake_cost

        print(max_num_of_cakes)


if __name__ == "__main__":
    main()
