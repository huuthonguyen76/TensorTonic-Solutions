import numpy as np

def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    # Write code here
    rater1 = np.asarray(rater1, dtype=float)
    rater2 = np.asarray(rater2, dtype=float)
    
    n = len(rater1)
    p0 = (rater1 == rater2).sum() / len(rater1)
    pe = 0.0

    labels = np.unique(np.append(rater1, rater2))
    if len(labels) == 1:
        return 1.0

    for i in np.unique(labels):
        pe += (rater1 == i).sum() / n * (rater2 == i).sum() / n
    
    return (p0 - pe) / (1 - pe + 0.0000001)