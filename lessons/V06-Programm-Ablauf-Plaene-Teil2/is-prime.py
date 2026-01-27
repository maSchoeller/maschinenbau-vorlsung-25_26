# BEGIN IstPrimzahl
#     EINGABE(n)
#     IF n < 2 THEN
#         AUSGABE("Keine Primzahl")
#     ELSE
#         ist_prim ← WAHR
#         i ← 2
#         WHILE i * i ≤ n DO
#             IF n MOD i = 0 THEN
#                 ist_prim ← FALSCH
#             ENDIF
#             i ← i + 1
#         ENDWHILE
#         IF ist_prim THEN
#             AUSGABE("Primzahl")
#         ELSE
#             AUSGABE("Keine Primzahl")
#         ENDIF
#     ENDIF
# END IstPrimzahl

# prime_candidate = int(input("Gib eine Zahl ein: "))

for prime_candidate in range(10000000000,100000000000):
    if prime_candidate < 2:
        print("keine Primzahl!")
    else:
        ist_prim = True
        aktueller_teiler = 2
        while aktueller_teiler * aktueller_teiler <= prime_candidate:
            if prime_candidate % aktueller_teiler == 0:
                ist_prim = False
                break
            aktueller_teiler += 1
        if ist_prim:
            print(f"{prime_candidate} ist eine Primzahl!!")
        # else:
            # print(f"{prime_candidate} ist keine Primzahl.")