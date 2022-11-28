; 1019 - Conversão de Tempo
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1019

(def timestamp (Integer/parseInt (read-line)))

(defn print-time [timestamp]
  (let [hours (int (/ timestamp 3600))
        minutes (int (/ (mod timestamp 3600) 60))
        seconds (mod timestamp 60)]
    (println (str hours ":" minutes ":" seconds))))

(print-time timestamp)
