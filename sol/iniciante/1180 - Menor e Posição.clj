; 1180 - Menor e Posição
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1180

(import java.util.Scanner)

(let [s (Scanner. System/in)
      n (.nextInt s)]
  (loop [i 0
         pos 0
         min-x 9999]
    (if (< i n)
      (let [x (.nextInt s)]
        (cond
          (< x min-x) (recur (inc i) i x)
          :else       (recur (inc i) pos min-x)))
      (println (format "Menor valor: %d\nPosicao: %d" min-x pos)))))
