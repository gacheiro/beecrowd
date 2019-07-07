# 1063 - Trilhos Novamente... Traçando Movimentos
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1063

def possible?(vagoes, ordem)
    # Essa função modifica o array ordem :(
    op = []
    pilha = []
    vagoes.each do |v|
        pilha << v
        op << 'I'
        while !pilha.empty? && pilha.last == ordem.first
            pilha.pop   # remove o último
            ordem.shift # remove o primeiro
            op << 'R'
        end
    end
    return pilha.empty?, op.join
end

def main
    loop do
        n = gets.to_i
        return if n.zero?
        vagoes = gets.chomp.split(' ')
        ordem = gets.chomp.split(' ')
        possible, operations = possible?(vagoes, ordem)
        if possible
            puts("#{operations}")
        else
            puts("#{operations} Impossible")
        end
    end
end

main
