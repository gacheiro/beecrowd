; 1132 - Múltiplos de 13
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1132

(defn sum-13 [x y]
  (loop [i x
         sum 0]
    (if (<= i y)
      (cond
        (= (mod i 13) 0) (recur (inc i) sum)
        :else            (recur (inc i) (+ i sum)))
      sum)))

(let [x (Integer/parseInt (read-line))
      y (Integer/parseInt (read-line))]
  (println (sum-13 (min x y) (max x y))))
