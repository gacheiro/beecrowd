; 1179 - Preenchimento de Vetor IV
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1179

(defn print-v [vec-name vec]
  (dotimes [i (count vec)]
    (println (format "%s[%d] = %d" vec-name i (get vec i)))))

(loop [i 0
       par []
       impar []]
  (if (< i 15)
    (cond
      (= (count par) 5)
        (do (print-v "par" par)
            (recur i [] impar))
      (= (count impar) 5)
        (do (print-v "impar" impar)
            (recur i par []))
      :else 
        (do (let [n (Integer/parseInt (read-line))]
              (cond
                (even? n) (recur (inc i) (conj par n) impar)
                :else (recur (inc i) par (conj impar n))))))
    (do
      (print-v "impar" impar)
      (print-v "par" par))))
