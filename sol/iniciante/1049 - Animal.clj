; 1049 - Animal
; https://www.urionlinejudge.com.br/judge/pt/problems/view/1049

(defn get-animal [tipo dieta]
  (case [tipo dieta]
    ["ave" "carnivoro"] "aguia"
    ["ave" "onivoro"] "pomba"
    ["mamifero" "onivoro"] "homem"
    ["mamifero" "herbivoro"] "vaca"
    ["inseto" "hematofago"] "pulga"
    ["inseto" "herbivoro"] "lagarta"
    ["anelideo" "hematofago"] "sanguessuga"
    ["anelideo" "onivoro"] "minhoca"))

(let [_ (read-line)
      tipo (read-line)
      dieta (read-line)]
  (println (get-animal tipo dieta)))
