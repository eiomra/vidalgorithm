def calculate_similarity(video1, video2):
    category_similarity = 1 if video1['category'] == video2['category'] else 0
    tag_similarity = len(set(video1['tags']).intersection(set(video2['tags'])))
    return category_similarity + tag_similarity
