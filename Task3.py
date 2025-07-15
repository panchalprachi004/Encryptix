books = [
    {"id": 1, "title": "Harry Potter and the Philosopher's Stone", "genres": ["Fantasy", "Adventure"]},
    {"id": 2, "title": "The Hobbit", "genres": ["Fantasy", "Adventure"]},
    {"id": 3, "title": "Pride and Prejudice", "genres": ["Romance", "Classic"]},
    {"id": 4, "title": "1984", "genres": ["Dystopian", "Science Fiction", "Political"]},
    {"id": 5, "title": "To Kill a Mockingbird", "genres": ["Classic", "Drama"]},
    {"id": 6, "title": "The Great Gatsby", "genres": ["Classic", "Romance"]},
    {"id": 7, "title": "The Fault in Our Stars", "genres": ["Romance", "Drama"]},
    {"id": 8, "title": "Dune", "genres": ["Science Fiction", "Adventure"]},
    {"id": 9, "title": "The Alchemist", "genres": ["Philosophy", "Adventure", "Drama"]},
]

# Function to calculate genre similarity (common genres)
def calculate_similarity(user_genres, book_genres):
    return len(set(user_genres) & set(book_genres))

# Function to get recommended books
def recommend_books(user_genres):
    recommendations = []

    for book in books:
        similarity = calculate_similarity(user_genres, book["genres"])
        if similarity > 0:
            recommendations.append((book["title"], similarity))

    # Sort by highest similarity score
    recommendations.sort(key=lambda x: x[1], reverse=True)

    return [book[0] for book in recommendations]

# ---- Main Program ----
print("📚 Welcome to the Book Recommendation System!")

# Get user's favorite genres
user_input = input("Enter your favorite genres (comma separated, e.g., Fantasy,Drama): ")
user_genres = [genre.strip().capitalize() for genre in user_input.split(",")]

# Get recommendations
results = recommend_books(user_genres)

# Display results
print("\n📖 Recommended Books for You:")
if results:
    for title in results:
        print("✅", title)
else:
    print("❌ Sorry, no matching books found. Try different genres.")
