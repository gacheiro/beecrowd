# 2180 - Viagem à Marte na Velocidade de Primo
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2180

require 'prime'

def gera_10_primos(n)
    primos = []
    n.step do |p|
        if Prime.prime?(p)
            primos << p
        end
        return primos if primos.size == 10
    end
end

def main
    peso = gets.to_i
    velocidade = gera_10_primos(peso).reduce(&:+)
    horas = 60000000/velocidade
    dias = horas/24

    puts "#{velocidade} km/h\n#{horas} h / #{dias} d"
end

main
