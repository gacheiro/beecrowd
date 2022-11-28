; 1064 - Positivos e Média
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1064

(defn positivos [seq]
  (for [x seq :when (> x 0)]
    x))

(defn count-positivos [seq]
  (count (positivos seq)))

(defn media [seq]
  (/ (apply + seq) (count seq)))

(let [seq (map #(Float/parseFloat %)
               [(read-line) (read-line)
                (read-line) (read-line)
                (read-line) (read-line)])]
  (println (count-positivos seq) "valores positivos")
  (println (format "%.1f" (media (positivos seq)))))
