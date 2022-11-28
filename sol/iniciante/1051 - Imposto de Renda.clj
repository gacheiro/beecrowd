; 1051 - Imposto de Renda
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1051

(defn imposto [x]
  (cond
    (<= x 2000) 0.0
    (<= x 3000) (* (- x 2000) 0.08)
    (<= x 4500) (+ (* (- x 3000) 0.18) (imposto 3000))
    :else (+ (* (- x 4500) 0.28) (imposto 4500))))

(let [x (Float/parseFloat (read-line))
      desconto (imposto x)]
  (if (> desconto 0)
    (do (println (format "R$ %.2f" desconto)))
    (do (println "Isento"))))
