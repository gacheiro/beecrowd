# 1251 - Diga-me a Frequência
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1251

def count(caracteres)
    counter = Hash.new(0)
    caracteres.each do |c|
        counter[c] += 1
    end
    counter.to_a.sort do |c1_n1, c2_n2|
        c1, n1 = c1_n1 # caracter, frequencia
        c2, n2 = c2_n2
        if n1 == n2
            c2 <=> c1  # mesma frequencia, ordena pelo ascii maior
        else
            n1 <=> n2 
        end
    end
end

def main
    nova_linha = false
    loop do
        linha = gets
        return if linha.nil?
        if nova_linha 
            # para só imprimir uma nova linha ENTRE dois casos de teste
            puts()
        end

        caracteres = linha.chomp.split('').map(&:ord)
        return if caracteres.empty?
        count(caracteres).each do |c, n|
            puts("#{c} #{n}")
        end
        nova_linha = true
    end
end

main
