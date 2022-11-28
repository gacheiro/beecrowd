; 1114 - Senha Fixa
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1114

(doseq [_ (range) :let [pwd (read-line)]]
  (if (= pwd "2002")
    (do (println "Acesso Permitido")
        (System/exit 0))
    (do (println "Senha Invalida"))))
