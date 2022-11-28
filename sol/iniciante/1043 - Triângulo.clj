; 1043 - Triângulo
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1043

(require '[clojure.string :as str])

(defn triangulo? [a b c]
  (and (< a (+ b c))
       (< b (+ a c))
       (< c (+ a b))))

(defn perimetro [a b c]
  (+ a b c))

(defn area-trapezio [a b c]
  (* (/ (+ a b) 2) c))

(let [[a b c] (map #(Float/parseFloat %)
                   (str/split (read-line) #" "))]
  (if (triangulo? a b c)
    (println "Perimetro =" (format "%.1f" (perimetro a b c)))
    (println "Area =" (format "%.1f" (area-trapezio a b c)))))
