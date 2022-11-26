
Beam cu 10 si mhd + no_inv merge pe:
-toate easy
-4 normal
- nu merge pe 5 si 6

Beam cu 10 si mhd pe:
-toate easy
-4,5,6 test1 si test3

A star cu mhd + no_inv merge pe:
-4 easy toate, 5 easy 1,3,5 nu merge pe 2,4     6 easy toate
(nici nu trebuie pe alea hard)

A star cu mhd pe:
-4 easy 2,4 nu 1 si 3,5, 5 easy toate 6 easy toate
(nici nu trebuie pe alea hard)

GLDS cu mhd + no_perm:
-4 easy merge: 3,4,5 nu mereg: 1,2 - iese din memorie
-5 easy merge:  python crashes
-6 easy merge : 1,3,4,5 pe 2 python crashes
-4 normal : MEM pe toate
-5 normal :MEM pe toate
-6 normal : MEM pe toate

GLDS cu mhd:
- nu merge pe nimic
- MEM pe toate


BLDS cu both:
-5 easy tle pe toate in afara de a doua
-4 easy toate
-6 easy toate
-4 normal

BLDS cu mhd:
-5 easy toate
-4 easy toate
-6 easy toate
-4 normal toate
-5 normal toate
-6 normal toate
## Manhattan meu e bun

## euristica cealalta nu e buna

## ar trebui sa treaca glds pe toate easy cu manhattan

### GLDS VS BEAM:
    [14:44, 26.11.2022] Andu: Nu, dar in medie e posibil daca alege un drum spre solutie sa fie unul lung
[14:44, 26.11.2022] Andu: Fata de cel mai scurt
[14:44, 26.11.2022] Andu: Asa beam-ul incearca mai multe path-uri in acelasi timp
[14:45, 26.11.2022] Andu: Dar da, la beam problema e ca nu se uita in fata mai mult
[14:45, 26.11.2022] Andu: Si de la blds-ul da cel mai bine
