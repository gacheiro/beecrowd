# 1262 - Leitura Múltipla
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1262

def clock_cycles(trace, procs)
    # cada W consome 1 ciclo
    write_cycles = trace.count("W")

    # divide os R em blocos com split
    # conta quantos ciclos cada bloco de R demora
    # depois soma tudo
    read_blocks = trace.split("W")
    read_cycles = read_blocks
                    .map{ |block| (block.length.to_f / procs).ceil }
                    .inject(0, :+) # aqui eh o mesmo que .sum (que nao ta funcionando)

    write_cycles + read_cycles
end

def main

    loop do 
        trace = gets        
        if trace.nil?
            break
        end
        trace = trace.chomp
        procs = gets.to_i
        puts clock_cycles(trace, procs)
    end
end

main
