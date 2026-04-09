def main():
    scores = {}

    print("Enter player and score as 'name score' (or type 'stop' to finish):")

    while True:
        entry = input()
        
        if entry == "stop":
            break
        
        name, score = entry.split()
        score = int(score)
        
        scores[name] = scores.get(name, 0) + score

    if scores:
        top = max(scores, key=scores.get)
        print(f"Top scorer: {top} with {scores[top]} points.")