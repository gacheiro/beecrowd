; 1035 - Teste de Seleção 1
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1035

(require '[clojure.string :as str])

(def problem-input (read-line))

(def grades (map #(Integer/parseInt %)
                 (str/split problem-input #" ")))

(defn valid? ([a b c d]
  (and (> b c)
       (> d a)
       (> (+ c d) (+ a b))
       (> b 0)
       (> d 0)
       (even? a))))

(if (apply valid? grades)
  (do (println "Valores aceitos")
      true)
  (do (println "Valores nao aceitos")
      false))
