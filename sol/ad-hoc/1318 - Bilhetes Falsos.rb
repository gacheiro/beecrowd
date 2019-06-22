# 1318 - Bilhetes Falsos
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1318

def bilhetes_falsos(bilhetes)
    conta_ids = Hash.new(0)
    bilhetes.each do |b|
        conta_ids[b] += 1
    end
    conta_ids.select{ |k, v| v > 1 }.length
end

def main
    loop do
        n, m = gets.split(" ").map(&:to_i)
        return if n.zero?

        bilhetes = gets.split(" ").map(&:to_i)
        puts bilhetes_falsos(bilhetes)
    end
end

main
