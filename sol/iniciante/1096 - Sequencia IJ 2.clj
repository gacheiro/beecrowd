; 1096 - Sequencia IJ 2
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1096

(let [I (flatten (map #(take 3 (repeat %)) (range 1 10 2)))
      J (cycle [7 6 5])]
  (loop [i I
         j J]
    (when-not (empty? i)
      (println (format "I=%d J=%d" (first i) (first j)))
      (recur (rest i) (rest j)))))
