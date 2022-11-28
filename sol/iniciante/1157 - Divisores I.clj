; 1157 - Divisores I
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1157

(let [n (Integer/parseInt (read-line))]
  (doseq [i (range 1 (inc n))]
    (when (= (mod n i) 0)
      (println i))))
