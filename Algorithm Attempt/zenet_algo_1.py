
x = 1
h = 2

n = z = f = r = l = 0

all_ders = []
combi_of_ders = []

L10 = { x^2000, n, z, f, r, l, h^10 }

l10 = [ x^2000, n, z, f, r, l, h^10 ]

for val in range(len(l10)):
    incor_der = []
    distance_pata = 0

    if l10[val] == 0:
        incor_der.append(l10[val])
    elif l10[val] != 0:
        distance_pata = l10[0] * l10[-1]


def taking_corr_pata():
    print("Avoiding current ders /{incor_der} ")
    print(f"{incor_der}")
    figure_cor_der = [der for der in incor_der]
    if figure_cor_der in all_ders:
        all_ders.remove(figure_cor_der)
        corr_pot_pata = all_ders[:]
        if len(corr_pot_pata) > 1:
            print("Pending Result for corr / {der}...")
            single_out_corr_der(corr_pot_pata)
        elif len(corr_pot_pata) == 1:
            corr_der_identified()



def corr_der_identified():
    print("Keep going into the pata...")
    print("Avoidance of incor / {der} ")
    print("Track len / corr }: {der}")
    print("Once len reached -> open next re/;{tricton} #key#")

pot = ["l", "R", "El"]
combos_der = []

def single_out_corr_der(paths):
    check_valid = False
    all_combinations_der = combi_of_ders[:]
    if paths in all_combinations_der:
        check_valid = True
    conquer_length = len(all_combinations_der)
    conquer_output = []
    conquer_splits = []
    conquer_splits2 = []
    conquer_final_der = None

    if check_valid:
        for com in range(paths):
            if all_combinations_der[combos_der[paths[com]]]:
                conquer_splits.append(all_combinations_der[combos_der[paths[com]]])
            elif all_combinations_der[combos_der[paths[-com]]]:
                conquer_splits2.append(all_combinations_der[combos_der[paths[-com]]])


p = ["a","b","c","d","e","f"]

k  = ("a","b","c","d","e","f")


print(L10)
print()
print()
print(k)

