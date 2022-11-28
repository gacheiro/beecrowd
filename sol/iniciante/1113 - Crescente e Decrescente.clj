; 1113 - Crescente e Decrescente
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1113

(require '[clojure.string :as str])

(doseq [_ (range)]
  (let [[x y] (map #(Integer/parseInt %)
                   (str/split (read-line) #" "))]
  (when (= x y)
    (System/exit 0))
  (println (if (< x y) "Crescente" "Decrescente"))))
