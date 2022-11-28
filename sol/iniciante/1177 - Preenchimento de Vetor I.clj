; 1177 - Preenchimento de Vetor I
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1177

(let [n (Integer/parseInt (read-line))]
  (loop [i 0
         xs (take 1000 (cycle (range n)))]
    (when (< i 1000)
      (println (format "N[%d] = %d" i (first xs)))
      (recur (inc i) (rest xs)))))
