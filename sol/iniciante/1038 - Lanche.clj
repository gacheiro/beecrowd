; 1038 - Lanche
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1038

(require '[clojure.string :as str])

(defn get-price [cod]
  (case cod
    1 4.0
    2 4.5
    3 5.0
    4 2.0
    5 1.5))

(let [[cod, qnt] (map #(Integer/parseInt %)
                 (str/split (read-line) #" "))
      total-price (* (get-price cod) qnt)]
  (println "Total: R$" (format "%.2f" total-price)))
