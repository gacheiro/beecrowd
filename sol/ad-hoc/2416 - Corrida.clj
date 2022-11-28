; 2416 - Corrida
; https://www.urionlinejudge.com.br/judge/pt/problems/view/2416

(import java.util.Scanner)

(let [s (Scanner. System/in)
      c (.nextInt s)
      n (.nextInt s)]
  (println (mod c n)))
