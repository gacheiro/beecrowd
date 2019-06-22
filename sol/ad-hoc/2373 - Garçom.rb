# 2373 - Garçom
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2373

def main
    copos_quebrados = 0

    n = gets.to_i    
    n.times do
        l, c = gets.split(" ").map(&:to_i)
        if l > c
            copos_quebrados += c
        end
    end
    puts copos_quebrados
end

main
