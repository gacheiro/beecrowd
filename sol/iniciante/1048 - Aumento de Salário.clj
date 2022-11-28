; 1048 - Aumento de Salário
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1048

(defn aumento-salario [x]
  (cond
    (<= x 400) [(* x 1.15) (* x 0.15) 15]
    (<= x 800) [(* x 1.12) (* x 0.12) 12]
    (<= x 1200) [(* x 1.1) (* x 0.1) 10]
    (<= x 2000) [(* x 1.07) (* x 0.07) 7]
    :else [(* x 1.04) (* x 0.04) 4]))

(let [x (Float/parseFloat (read-line))]
  (println (apply format
                  "Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: %d %%"
                  (aumento-salario x))))
