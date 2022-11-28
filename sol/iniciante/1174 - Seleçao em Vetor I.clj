; 1174 - Seleçao em Vetor I
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1174

(dotimes [i 100]
  (let [n (Float/parseFloat (read-line))]
    (when (<= n 10)
      (println (format "A[%d] = %.1f" i n)))))
