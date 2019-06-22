# 1471 - Mergulho
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1471

require 'set'

def main
    loop do
        entrada = gets
        return if entrada.nil?
        n, r = entrada.split(" ").map(&:to_i)

        mergulhadores = Set.new(1..n)
        sobreviventes = gets.split(" ").map(&:to_i).to_set        
        mortos = mergulhadores - sobreviventes

        if mortos.empty?
            puts "*"
        else
            puts "#{mortos.to_a.sort.join(" ")} " # <- um espaço no final
        end
    end
end

main
