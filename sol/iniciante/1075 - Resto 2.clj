; 1075 - Resto 2
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1075

(let [n (Integer/parseInt (read-line))]
  (doseq [i (range 10001) :when (= (mod i n) 2)]
    (println i)))
