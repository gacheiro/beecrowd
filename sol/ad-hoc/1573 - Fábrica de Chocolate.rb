# 1573 - Fábrica de Chocolate
# https://www.urionlinejudge.com.br/judge/pt/problems/view/

def main
    loop do
        a, b, c = gets.split(" ").map(&:to_i)
        return if a.zero?

        volume = a * b * c
        lado_cubo = (volume ** (1/3.0)).to_i # raiz cúbica
        puts lado_cubo
    end
end

main
