# 1632 - Variações
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1632

def letter_comb(letter)
    "aeios".include?(letter.downcase)? 3 : 2
end

def number_of_combinations(password)
    password.each_char
            .map{ |l| letter_comb(l) }
            .reduce(1, :*)  # multiplica o num de comb de cada letra
end

def main
    n = gets.to_i
    n.times do
        pwd = gets.chomp
        puts number_of_combinations(pwd)
    end
end

main
