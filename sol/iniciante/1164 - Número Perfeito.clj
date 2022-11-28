; 1164 - Número Perfeito
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1164

(import java.util.Scanner)

(defn divs [x]
  (for [i (range 1 x) :when (= (mod x i) 0)]
    i))

(let [s (Scanner. System/in)
      n (.nextInt s)]
  (dotimes [_ n]
    (let [x (.nextInt s)]
      (cond
        (= x (apply + (divs x))) (println x "eh perfeito")
        :else                    (println x "nao eh perfeito")))))
