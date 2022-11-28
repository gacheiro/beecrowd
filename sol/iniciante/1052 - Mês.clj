; 1052 - Mês
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1052

(defn get-month-name [m]
  (case m
    1 "January"
    2 "February"
    3 "March"
    4 "April"
    5 "May"
    6 "June"
    7 "July"
    8 "August"
    9 "September"
    10 "October"
    11 "November"
    12 "December"))

(let [month (Integer/parseInt (read-line))]
  (println (get-month-name month)))
