; 1065 - Pares entre Cinco Números
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1065

(defn conta-pares [seq]
  (count (for [x seq :when (even? x)]
    x)))

(let [seq (map #(Integer/parseInt %)
               [(read-line) (read-line) (read-line) (read-line) (read-line)])]
  (println (conta-pares seq) "valores pares"))
