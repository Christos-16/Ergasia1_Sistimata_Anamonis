#Αυτός ο κώδικας υπολογίζει την καθυστέρηση σε ένα σύστημα που ονομάζεται ουρά M/M/s. Το σύστημα έχει s διακομιστές που μπορούν να επεξεργαστούν εργασίες με ρυθμό mu. Οι εργασίες φτάνουν στο σύστημα με ρυθμό lambda.


import math #Η βιβλιοθήκη math που περιέχει ορισμένες μαθηματικές συναρτήσεις
import numpy as np #Η βιβλιοθήκη numpy παρέχει υποστήριξη για τη δημιουργία πινάκων
import matplotlib.pyplot as plt #Η βιβλιοθήκη matplotlib.pyplot χρησιμοποιείται για τη δημιουργία γραφικών παραστάσεων με 3 παραμέτρους, στη συνέχεια υπολογίζει πρώτα το rho, το οποίο αν είναι μεγαλύτερο ή ίσο απο το 1, σημαίνει ότι το σύστημα δεν είναι σταθερό και δεν μπορεί να διαχειριστεί την εισερχόμενη κίνηση

def mm_s_queue(s, lambd, mu):
    rho = lambd / (s * mu)
    if rho >= 1:
        raise ValueError("Το σύστημα δεν είναι σταθερό!") 
      #Στον κώδικα από τη γραμμή 8 ορίζεται η mm_s_queue συνάρτηση 
    p0 = sum([(s * rho) ** n / math.factorial(n) for n in range(s)])
    p0 += (s * rho) ** s / math.factorial(s) / (1 - rho)
    p0 = 1 / p0
  #Απο την γραμμή 13 εως και εδώ, υπολογίζεται το p0 το οποίο είναι η πιθανότητα το σύστημα να είναι άδειο. Στην πρώτη γραμμή υπολογίζεται το άθροισμα των πιθανοτήτων στις περιπτώσεις μεταξύ 0 και s-1 και στην δεύτερη γραμμή η πιθανότητα το σύστημα να είναι σε σταθερή κατάσταση και στην τελευταία γραμμή (κάνω μια προσπάθεια ο θεός να την πεί αν είναι σωστή η λογική μου) γίνεται ο υπολογισμός της τιμής του p0
    Lq = ((s * rho) ** (s + 1) / math.factorial(s) / (1 - rho)) * p0
    L = Lq + lambd / mu
  #Αυτό το τμήμα κώδικα υπολογίζει τον μέσο αριθμό εργασιών στην ουρά (Lq) και τον μέσο αριθμό εργασιών στο σύστημα (L) (κύριε εδώ έπεσε αναζήτηση στο internet δεν μπόρεσα να βρω άκρη)
    if lambd == 0:
        Wq = 0
    else:
        Wq = Lq / lambd
    W = Wq + 1 / mu
    return W, Wq, L, Lq

# Parameters
s = 3
mu = 0.5
lambd_values = np.linspace(0, 0.9, num=10)

#Αυτές οι γραμμές ορίζουν τις τιμές των s (αριθμός διακομιστών) και mu (ρυθμός εξυπηρέτησης) και δημιουργούν έναν πίνακα με 10 ρυθμούς αφίξεων (lambd)

# Υπολογισμός καθυστερήσεων για διαφορετικούς ρυθμούς άφιξης
delays_system = []
delays_queue = []
for lambd in lambd_values:
    W, Wq, L, Lq = mm_s_queue(s, lambd, mu)
    delays_system.append(W)
    delays_queue.append(Wq)

# Plot the results
plt.plot(lambd_values, delays_system, label="Σύστημα")
plt.plot(lambd_values, delays_queue, label="Ουρά αναμονής")
plt.xlabel("Ρυθμός άφιξης (λ)")
plt.ylabel("Καθυστέρηση")
plt.title("Ουρά M/M/3 με μ=0,5")
plt.legend()
plt.show()
