# 1103 - Alarme Despertador
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1103

def main
    loop do
        h1, m1, h2, m2 = gets.split(" ").map(&:to_i)
        return if h1.zero? && m1.zero? && h2.zero? && m2.zero?

        dormiu_as, acordou_as = h1*60 + m1, h2*60 + m2 # em minutos
        if acordou_as >= dormiu_as
            puts acordou_as - dormiu_as
        else
            # passou da meia noite
            puts (24*60 - dormiu_as) + acordou_as
        end
    end
end

main
