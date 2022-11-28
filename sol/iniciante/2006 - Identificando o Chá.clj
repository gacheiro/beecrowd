; 2006 - Identificando o Chá
; https://www.urionlinejudge.com.br/judge/pt/problems/view/2006

(import java.util.Scanner)

(let [s (Scanner. System/in)
      tea (.nextInt s)]
  (loop [i 0
         wins 0]
    (if (< i 5)
      (cond
        (= (.nextInt s) tea) (recur (inc i) (inc wins))
        :else (recur (inc i) wins))
      (println wins))))
