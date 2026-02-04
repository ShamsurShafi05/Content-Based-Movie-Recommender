# 🎬 Content-Based Movie Recommender System

A movie recommendation system built with Streamlit that suggests similar movies based on content features using sentence transformers and cosine similarity.

🔗 **Live Demo:** [https://content-based-movie-recommender-he48pa7appjjbt5ljht3yt7.streamlit.app/](https://content-based-movie-recommender-he48pa7appjjbt5ljht3yt7.streamlit.app/)

---

## Key Highlights

- **Comparative Analysis**: Evaluated 3 vectorization techniques (Count Vectorizer, TF-IDF, Sentence Transformers)
- **Data-Driven Decision**: Selected Sentence Transformers based on performance metrics
- **Visualizations**: Included detailed comparison charts in analysis notebook
- **Optimized Performance**: Smart caching for instant recommendations

---

## 📋 Overview

This application recommends movies similar to your favorite ones by analyzing movie metadata including:
- Overview / Plot
- Genre
- Keywords
- Cast
- Crew

The system uses **Sentence Transformers** to create semantic embeddings of movie features and calculates **cosine similarity** to find the most similar movies.

---

## Features

- Content-based filtering using state-of-the-art sentence embeddings
- Comprehensive vectorization comparison (Count, TF-IDF, Sentence Transformers)
- Performance analysis with visualizations in Jupyter notebook
- Fast similarity computation with cached results
- Clean and intuitive user interface
- Data-driven model selection based on empirical results
- Deployed on Streamlit Cloud for easy access

---

## Technologies Used

- **Python 3.x**
- **Streamlit** - Web application framework
- **Sentence Transformers** - For creating semantic embeddings
- **Scikit-learn** - For cosine similarity computation
- **Pandas** - Data manipulation
- **NumPy** - Numerical operations
- **Pickle** - Model serialization

---

## 📊 Dataset

This project uses the **TMDB 5000 Movie Dataset** which contains:
- 5,000 movies
- Movie metadata (genres, keywords, cast, crew, overview)
- Release dates and popularity metrics

---

## How It Works

1. **Data Preprocessing**: Movie features (overview, genres, keywords, cast, crew) are combined into a single text representation
2. **Embedding Generation**: Sentence Transformer models convert text into dense vector embeddings
3. **Similarity Calculation**: Cosine similarity is computed between all movie embeddings
4. **Recommendation**: When a user selects a movie, the system returns the most similar movies based on cosine similarity scores

---

## Methodology & Analysis

This project includes a comprehensive comparison of **three different vectorization techniques**:

1. **Count Vectorizer** - Basic bag-of-words approach
2. **TF-IDF Vectorizer** - Term frequency-inverse document frequency weighting
3. **Sentence Transformers** - State-of-the-art semantic embeddings (chosen for final implementation)

### Why Sentence Transformers?

After comparing all three approaches (detailed analysis in `analysis_notebook.ipynb`), Sentence Transformers were selected because they:
- ✅ Capture semantic meaning, not just word frequency
- ✅ Understand context and relationships between words
- ✅ Produce more relevant and accurate recommendations
- ✅ Handle synonyms and related concepts better

**See the complete comparison with visualizations in the notebook!**

---

## Local Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/movie-recommender.git
   cd movie-recommender
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open in browser**
   ```
   The app will open automatically at http://localhost:8501
   ```

---

## Project Structure

```
movie-recommender/
│
├── app.py                      # Main Streamlit application
├── analysis_notebook.ipynb     # 🔬 ANALYSIS: Vectorization comparison & visualizations
├── movies.pkl                  # Processed movie data with embeddings
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore file
│
└── .streamlit/                 # Streamlit configuration (optional)
    └── config.toml
```

** Important:** Check `analysis_notebook.ipynb` for the complete analysis comparing Count Vectorizer, TF-IDF, and Sentence Transformers with performance metrics and visualizations!

---

## Usage

1. Visit the live demo: [https://content-based-movie-recommender-he48pa7appjjbt5ljht3yt7.streamlit.app/]
2. Select a movie from the dropdown menu
3. Choose the number of recommendations you want (1-10)
4. Click "Get Recommendations"
5. Explore similar movies!

---

## Configuration

### Streamlit Cloud Deployment

The app is configured to:
- Load movie embeddings from `movies.pkl`
- Generate similarity matrix on first run (cached for performance)
- Use `@st.cache_resource` for efficient memory usage

### Customization

You can modify the recommendation algorithm by:
- Changing the sentence transformer model in `analysis_notebook.ipynb`
- Adjusting the features used for similarity
- Modifying the number of recommendations returned

---

## Performance

- **Initial Load**: ~5-10 seconds (generates similarity matrix)
- **Subsequent Loads**: Instant (uses cached similarity matrix)
- **Recommendation Speed**: < 1 second per query

---

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## Known Issues

- Large similarity matrix generation may timeout on Streamlit Cloud free tier (solved with caching)
- Limited to TMDB 5000 dataset (can be expanded with more data)

---

## Future Enhancements

- [ ] Include user ratings in recommendations
- [ ] Add hybrid filtering (content + collaborative)
- [ ] Implement advanced filtering (by genre, year, rating)
- [ ] Add movie details and trailers
- [ ] Export recommendations to CSV
- [ ] Multi-language support

---

## Acknowledgments

- **TMDB** for providing the movie dataset
- **Sentence Transformers** library for state-of-the-art embeddings
- **Streamlit** for web framework
- The open-source community for inspiration

---

## Screenshots

### Home Page
![Home Page](screenshots/home.png)

### Recommendations
![Recommendations](screenshots/recommendations.png)

---

## Star History

If you found this project helpful, please consider giving it a star! ⭐

---

**Built with ❤️ using Streamlit and Sentence Transformers**
