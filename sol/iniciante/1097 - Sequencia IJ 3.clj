; 1097 - Sequencia IJ 3
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1097

(let [I (flatten (map #(take 3 (repeat %)) (range 1 10 2)))
      J (flatten (map #(range % (- % 3) -1) (range 7 16 2)))]
  (loop [i I
         j J]
    (when-not (empty? i)
      (println (format "I=%d J=%d" (first i) (first j)))
      (recur (rest i) (rest j)))))
