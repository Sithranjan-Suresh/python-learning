import csv

def calculate_rating_stats(data, industry=None):
    ratings = []
    for row in data:
        if row[3] !='NULL' and (not industry or row[1] == industry):
            ratings.append(float(row[3]))
        maxrating = max(ratings)
        minrating = min(ratings)
        avgrating = sum(ratings) / len(ratings)
    return maxrating, minrating, avgrating
    

with open("pandas\movies.csv") as f:
    data = list(csv.reader(f))
    header = data[0]
    movies = data[1:]

    maxrating, minrating, avgrating = calculate_rating_stats(movies)
    print("Max Rating:", maxrating)
    print("Min Rating:", minrating)
    print("Avg Rating:", avgrating)
