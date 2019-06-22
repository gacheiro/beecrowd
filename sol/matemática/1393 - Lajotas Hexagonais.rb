# 1393 - Lajotas Hexagonais (Programação Dinâmica)
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1393

def quantos_caminhos(n)
    caminhos = Array.new(n, 0)

    # caso base
    # so há uma forma de chegar nas lajotas 0 e 1
    caminhos[0], caminhos[1] = 1, 1
    
    (2..n).each do |i|
        # pra chegar na lajota i é a soma das quantidades
        # de vezes das duas lajotas anteriores
        # por ex. caminhos[2] = caminhos[1] + caminhos[0] (que é 2) 
        caminhos[i] = caminhos[i-1] + caminhos[i-2]
    end
    caminhos[n]
end

def main
    loop do
        n = gets.to_i
        return if n.zero?
        puts quantos_caminhos(n)
    end
end

main
