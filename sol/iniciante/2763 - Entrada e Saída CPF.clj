; 2763 - Entrada e Saída CPF
; https://www.beecrowd.com.br/judge/pt/problems/view/2763

(use '[clojure.string :only (join split)])

(println (join "\n"
           (split (read-line) #"[.-]")))
