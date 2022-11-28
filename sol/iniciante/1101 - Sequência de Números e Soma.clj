; 1101 - Sequência de Números e Soma
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1101

(require '[clojure.string :as str])

(doseq [_ (range)]
  (let [[x y] (map #(Integer/parseInt %)
                   (str/split (read-line) #" "))]
    (when (or (<= x 0) (<= y 0))
      (System/exit 0))
    (let [start (min x y)
          end (max x y)
          seq (range start (inc end))]
      (println (format "%s Sum=%d" (str/join " " seq) (apply + seq))))))
