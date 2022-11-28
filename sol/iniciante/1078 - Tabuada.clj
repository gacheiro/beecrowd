; 1078 - Tabuada
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1078

(let [n (Integer/parseInt (read-line))]
  (doseq [i (range 1 11)]
    (println (format "%d x %d = %d" i n (* i n)))))
