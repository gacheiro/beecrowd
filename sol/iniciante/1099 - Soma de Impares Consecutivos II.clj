; 1099 - Soma de Impares Consecutivos II
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1099

(require '[clojure.string :as str])

(defn odd-seq [x, y]
  (for [i (range x y) :when (odd? i)]
    i))

(let [n (Integer/parseInt (read-line))]
  (dotimes [_ n]
    (let [xs (map #(Integer/parseInt %)
                  (str/split (read-line) #" "))
          min-x (apply min xs)
          max-x (apply max xs)]
      (println
        (apply + (odd-seq (inc min-x) max-x))))))
