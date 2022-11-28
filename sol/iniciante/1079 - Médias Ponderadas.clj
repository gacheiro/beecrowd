; 1079 - Médias Ponderadas
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1079

(require '[clojure.string :as str])

(let [n (Integer/parseInt (read-line))]
  (dotimes [_ n]
    (let [[a b c] (map #(Float/parseFloat %)
                       (str/split (read-line) #" "))
          media (/ (+ (* a 2) (* b 3) (* c 5)) 10)]
      (println (format "%.1f" media)))))
