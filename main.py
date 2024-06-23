import sys
from components.data_parser import parse_data
from components.recommendation import get_recommendations

def main():
    users, videos = parse_data('data/data.json') 

#Checks if the wrong arguments are passed. It should be 2 arguments

    if len(sys.argv) != 3:
        print("Usage: python main.py <user_id> <number_of_recommendations>")
        return
    
    user_id = int(sys.argv[1])
    n = int(sys.argv[2])

    recommendations = get_recommendations(user_id, n, users, videos)
    print(f"Top {n} Video Recommendations: {recommendations}") #Prints recommended Video ID

if __name__ == "__main__":
    main()
