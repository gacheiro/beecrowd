; 1173 - Preenchimento de Vetor I
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1173

(let [n (Integer/parseInt (read-line))]
  (loop [i 0
         x n]
    (when (< i 10)
      (println (format "N[%d] = %d" i x))
      (recur (inc i) (* x 2)))))
