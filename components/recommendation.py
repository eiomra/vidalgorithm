from components.similarity_calculator import calculate_similarity

def get_recommendations(user_id, n, users, videos):
    # Converts videos list to a dictionary for easy access
    video_dict = {video['video_id']: video for video in videos}
    
    # Gets the watch history of the user
    user_watch_history = []
    for user in users:
        if user['user_id'] == user_id:
            user_watch_history = user['watch_history']
            break
    
    # Calculates similarity scores for each unwatched video
    unwatched_videos = [video for video in videos if video['video_id'] not in user_watch_history]
    similarity_scores = []

    for watched_video_id in user_watch_history:
        watched_video = video_dict[watched_video_id]
        for unwatched_video in unwatched_videos:
            # Checks if unwatched video is not already recommended or in watch history
            if unwatched_video['video_id'] not in user_watch_history:
                similarity = calculate_similarity(watched_video, unwatched_video)
                similarity_scores.append((unwatched_video['video_id'], similarity))

    # Sorts videos based on similarity scores
    similarity_scores.sort(key=lambda x: x[1], reverse=True)

    # Gets top N unique recommended video IDs
    recommended_video_ids = []
    seen_video_ids = set()

    for video_id, _ in similarity_scores:
        if video_id not in seen_video_ids and len(recommended_video_ids) < n:
            recommended_video_ids.append(video_id)
            seen_video_ids.add(video_id)
    
    return recommended_video_ids[:n]
