; 1176 - Fibonacci em Vetor
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1176

(defn fib-nth [n]
  (loop [a 0
         b 1
         i 0]
    (cond
      (< i n) (recur b (+ a b) (inc i))
      :else    a)))

(let [n (Integer/parseInt (read-line))]
  (dotimes [_ n]
    (let [i (Integer/parseInt (read-line))]
      (println (format "Fib(%d) = %d" i (fib-nth i))))))
