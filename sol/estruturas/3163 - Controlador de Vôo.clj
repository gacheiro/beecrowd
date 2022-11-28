; 3163 - Controlador de Vôo
; https://www.urionlinejudge.com.br/judge/pt/problems/view/3163

(require '[clojure.string :as str])

(defn get-flights []
  (loop [p (read-line) west [] north [] south [] east []]
    (let [in (read-line)]
      (if (str/starts-with? in "A")
        (do
          (case p
            "-1" (recur p (conj west in) north south east)
            "-2" (recur p west north (conj south in) east)
            "-3" (recur p west (conj north in) south east)
            "-4" (recur p west north south (conj east in))))
        (do
          (if (= in "0")
            [west north south east]
            (recur in west north south east)))))))

(let [flights (get-flights)
      max-length (apply max (map count flights))]
  (apply println (for [i (range max-length)]
                   (str/join " " (remove nil? (map #(get % i) flights))))))
