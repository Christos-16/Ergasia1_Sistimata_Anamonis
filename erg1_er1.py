#Οδηγίες για να τρέξει κάποιος τον κώδικα σε Visual Studio Code:

#Πρέπει να έχετε εγκαταστήσει στον υπολογιστή σας την Python, τις βιβλιοθήκες numpy και matplotlib για να εκτελέσετε αυτόν τον κώδικα στο Visual Studio Code.
#Μπορείτε να κατεβάσετε την Python από τον επίσημο ιστότοπο https://www.python.org/downloads.
#Μπορείτε να χρησιμοποιήσετε την εντολή pip στο τερματικό του υπολογιστή σας για να εγκαταστήσετε τα πακέτα numpy και matplotlib.
#Για παράδειγμα: pip install numpy matplotlib
#Εγκαταστήστε τα Numpy και Matplotlib αντιγράφοντας τον κώδικα.
#Αφού εγκατασταθούν η Python και τα απαιτούμενα πακέτα,
#μπορείτε να αντιγράψετε τον κώδικα στο Visual Studio Code και να τον εκτελέσετε χρησιμοποιώντας το πλήκτρο "Run" ή το πλήκτρο F5.


import numpy as np
import matplotlib.pyplot as plt

# Σε αυτό το μέρος του κώδικα μπορείτε να καθορίσετε ποιες θα είναι οι τιμές των mu και lambda
mu = 1
lambda_vals = np.arange(0, 1, 0.1)

# Εδώ γίνεται η αρχικοποίηση των κενών πινάκων για την αποθήκευση των αποτελεσμάτων
W_system_vals = []
W_queue_vals = []

# Βρόγχος επανάληψης για κάθε τιμή της lambda μεταβλητής
for lambda_val in lambda_vals:
    # Calculate alpha and rho
    alpha = lambda_val / mu
    rho = lambda_val / mu
    
    # Υπολογίστε την πιθανότητα να υπάρχουν n πελάτες στο σύστημα
    prob = np.zeros(30)
    prob[0] = 1 - alpha
    for i in range(1, 30):
        prob[i] = prob[0] * np.power(alpha, i)
    
    #  Υπολογισμός των μετρήσεων της ουράς M/M/1
    N_system = alpha / (1 - alpha)
    W_system = 1 / (mu * (1 - alpha))
    W_queue = W_system - (1 / mu)
    N_queue = lambda_val * W_queue
    
    # Προσάρτηση των αποτελεσμάτων στους πίνακες
    W_system_vals.append(W_system)
    W_queue_vals.append(W_queue)

# Σχεδιάστε τα αποτελέσματα
plt.plot(lambda_vals, W_system_vals, label='Καθυστέρηση του συστήματος')
plt.plot(lambda_vals, W_queue_vals, label='Καθυστέρηση στην ουρά αναμονής')
plt.xlabel('Lambda')
plt.ylabel('Καθυστέρηση')
plt.legend()
plt.show()


#Σε αυτό το πρόγραμμα αναπτύσσεται ένα γράφημα που δείχνει πόσο χρόνο πρέπει να περιμένουν οι πελάτες σε μια ουρά. 
#Χρησιμοποιούνται κάποια εργαλεία που ονομάζονται Numpy και Matplotlib για να βοηθήσουν στην κατασκευή του γραφήματος.
#Το πρόγραμμα ξεκινά λέγοντας στον υπολογιστή ποιες θα είναι οι τιμές των "mu" και "lambda". 
#Στη συνέχεια μέσα στο πρόγραμμα χρησιμοποιείται ένας βρόχος για να υπολογίσει την καθυστέρηση για διαφορετικές τιμές του "lambda" και αποθηκεύονται τα αποτελέσματα σε κάποιες κενές λίστες. 
#Τέλος, σχεδιάζονται τα αποτελέσματα στο γράφημα και τα εμφανίζονται στην οθόνη(δεξιά αν το τρέχουμε στο repl.it ή σε νέο παράθυρο εάν το τρέχουμε σε Visual Studio Code).