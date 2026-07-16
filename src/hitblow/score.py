MULTIPLIERS={
    "Easy":1,
    "Normal":2,
    "Hard":3,
}

def calculate_score(difficulty,tries):
    return(11-tries)*100*MULTIPLIERS[difficulty]