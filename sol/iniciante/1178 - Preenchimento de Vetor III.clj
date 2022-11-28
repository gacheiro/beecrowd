; 1178 - Preenchimento de Vetor III
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1178

(let [n (Double/parseDouble (read-line))]
  (loop [i 0
         x n]
    (when (< i 100)
      (println (format "N[%d] = %.4f" i x))
      (recur (inc i) (/ x 2)))))
