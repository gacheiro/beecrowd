; 1172 - Substituição em Vetor I
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1172

(defn print-v [xs]
  (dotimes [i 10]
    (println (format "X[%d] = %d" i (nth xs i)))))

(let [xs (for [_ (range 10)]
           (Integer/parseInt (read-line)))]
  (print-v (map #(if (> % 0) % 1) xs)))
