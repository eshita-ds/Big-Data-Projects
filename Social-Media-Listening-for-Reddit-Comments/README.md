# Social Media Listening for Reddit Comments

## Introduction

Social media has become a central part of daily life. Research by Pew Research Center shows nearly 70% of Americans use social media, with YouTube and Reddit experiencing notable growth as of 2021. Around 22% of Americans use Reddit, spending an average of 24 minutes daily on the platform. Reddit’s unique subreddits foster interest-based, text-focused discussions, making it a valuable channel for analyzing user behavior and sentiment. Its anonymity often results in honest discourse, providing rich data for understanding consumer opinions and preferences.

Social media listening involves tracking and analyzing conversations, mentions, and trends on social platforms. It enables brands to address feedback, improve products, and develop effective marketing strategies. In today’s digital era, incorporating social media listening is crucial for understanding customer views and actions. Insights gained can inform marketing plans, product development, and brand strategies.

Reddit, with its wealth of authentic user-generated content, serves as a key resource for social media listening. Its data is relatively easy to access, making it ideal for analysis. Two approaches to social media listening were explored: historical and real-time data. Historical data provides a retrospective view, helping identify trends and plan campaigns, while real-time data offers immediate insights, aiding ongoing campaigns, events, and promotions.

## Solution Overview
The historical data for analysis was sourced from the r/technology subreddit, a popular community with over 16 million members discussing technology trends. By April 2024, this dataset included over 1.4 million comments across 15,000 posts, starting from June 2023. PySpark was used to process the data at scale.

Exploratory data analysis was conducted on posts and comments, followed by the calculation of key metrics such as reach, impressions, sentiment, and share of voice. These metrics, visualized through a Streamlit web application, provide insights into customer perceptions and discussions on Reddit, helping brands and products understand unfiltered public sentiment. A detailed workflow diagram shown below outlines the process from raw data to application.

![image](https://github.com/user-attachments/assets/33a8a0fb-22c8-42d3-a9b5-ad2f52c75811)

### Data Flow
- **Data Collection:** Raw data from r/technology subreddit is collected and stored in a Google Cloud Storage (GCS) bucket via batch processing.
- **Data Processing:** Posts and comments are separated and processed using PySpark for large-scale data handling.
Processing includes filtering, text mining, cleaning, visualization, and machine learning.
- **Topic Modeling:** Latent Dirichlet Allocation (LDA), an unsupervised machine learning algorithm, analyzes post titles to identify key themes (details in later sections).
- **Data Storage:** Processed data is saved as CSV files (post titles and comments) in the GCS bucket for further use.
- **Dashboard Development:** A Streamlit dashboard provides an interactive interface to analyze social media trends and metrics via keyword-based searches.

## Data Pre-processing & Analysis
- **PySpark for Data Processing:**
  - Backbone for handling large Reddit datasets with data cleansing, transformation, and aggregation.
  - Utilized RDDs for distributed computing and DataFrames for efficient large-scale data processing.
  - Ideal for processing large volumes of Reddit comments.

- **Sentiment Analysis:**
  - TextBlob analyzed sentiment and subjectivity in comments to gauge public opinion and emotional tone.

- **Supporting Libraries:**
  - Pandas & NumPy: For smaller data subsets and numerical computations.
  - Seaborn & Matplotlib: For data visualization to identify trends and outliers.
  - re & nltk: For text cleaning and preparation, including regex for handling non-ASCII characters and URLs.
    
- **NLP Techniques:**
  - Tokenization: Breaking text into word fragments for analysis.
  - Stop Word Removal: Filtering out non-essential words.
  - Stemming & Lemmatization: Reducing words to their root or base form using custom PySpark UDFs and WordNetLemmatizer.
- **Sentiment Analysis Purpose:**
  - Identifies positive, negative, or neutral sentiment in text to support customer service, branding, and market research.

## Modeling (Unsupervised Machine Learning)
The historical dataset doesn’t contain any labeled data and hence we cannot use
any supervised learning techniques. However, we have attempted two unsupervised
machine-learning techniques - k-means clustering and topic modeling using Latent
Dirichlet Allocation (LDA) on the cleaned post title. To reduce noise and improve the
signal, we also focused on the largest tag i.e. Artificial Intelligence. We did not attempt
any machine learning approaches on comments text due to a lot of noise in the data.

### K-means clustering
- **Application on Reddit Data:**
  - Cleaned Reddit post titles (focused on AI-tagged data) were converted into a TFIDF matrix using the top 1000 features for clustering.
  - TFIDF scores measure the importance of terms, emphasizing relevant over frequent words.
- **Pre-Clustering Analysis:**
  - Hopkins Test was conducted to assess cluster tendency:
  - Overall data: Hopkins statistic = 0.0117 (low clustering tendency).
  - AI-tagged posts: Hopkins statistic = 0.02017 (slightly better but still low).
- **Clustering Attempts:**
  - The elbow curve method was used to determine the optimal number of clusters (k).
  - No clear clusters or optimal k values were identified from the elbow plots for either dataset.

**Conclusion**: Despite attempts with k-means clustering and pre-clustering analysis, the data showed a low clustering tendency, making it difficult to identify meaningful clusters.


### Latent Dirichlet Allocation (LDA)

- **Application on Reddit Data:**
  - Applied LDA with five topics on AI-tagged Reddit posts using the same TFIDF feature set as in k-means clustering.
  - Multiple iterations with combinations of topics and n-grams (unigrams, bigrams, trigrams) were tested to identify meaningful themes.
- **Key Topics Identified (AI-Tagged Posts):**
  - Topic 0: News on AI training data, authorship, and copyright.
  - Topic 1: Risks of AI, including deepfakes and misuse (e.g., references to LLMs and abuse).
  - Topic 2: AI tool news, prominently Google’s Gemini launch.
  - Topic 3: Mixed topics on AI announcements and tool updates.
  - Topic 4: New AI product launches and controversies (e.g., Humane AI pin, student use of AI tools).
- **Visualization of LDA Outputs:**
  - Word clouds and word distributions were created to intuitively interpret topics.
  - Topic probability distributions for documents were also studied.

**Conclusion:** LDA successfully identified distinct themes in AI-tagged Reddit posts, enabling summarization and visualization of topic relevance and trends.


## Real-Time Dashboard Implementation
We utilized our understanding of Kafka and API usage to handle real-time data
fetch from Reddit. Kafka is an open-source distributed event streaming platform used
for building real-time data pipelines and streaming applications. It is designed to handle
large volumes of data with high throughput and low latency. Kafka is scalable, faulttolerant,
and durable, making it an ideal choice for building reliable and robust data
streaming applications. We are using Kafka to fetch real-time data from reddit using
PRAW library. We have deployed Kafka on Amazon AWS EC2 instance.

![image](https://github.com/user-attachments/assets/46734577-6fc0-4ebd-9194-30edb5138ef2)

Created a Streamlit App to run our entire pipeline end to end by invoking the
producer and consumer on EC2 instance and fetching real time data from Reddit. Once
the data is retrieved, pre-processing and visualization is handled at real time as
well. All this happens on a click of a button on the app. The user passes a keyword in
the designated input box and clicks a button. As consumer and producer need to be
running parallely, we have used the threading library to create parallel threads
and then waiting until both finish. The app is published to Streamlit using a github
repo and it internally invokes Producer and Consumer by using a pre-configured
bootstrap server on EC2 compute instance on AWS.

![image](https://github.com/user-attachments/assets/ddb44d17-6e66-4536-b71f-c3ccc7460bd7)

## File Reference
#### Python Files
- Reddit social media listening - technology subreddit.ipynb: This files
contains the python code and unsupervised machine learning code.
- PySpark_Reddit_DataProcessing.ipynb: This file contains the pyspark code
for data processing and data transformation.
#### Streamlit Files-Historical
- streamlit_reddit_historical.py: This file contains the streamlit code for historical
app
- requirement.txt: File contains all the libraries that are required for streamlit app
#### Streamlit Files – Real Time Streamlit App
- DashStyles.css – Style sheets for Dashboard App
- RedditDashboard.py – Python file for Streamlit dashboard
- functions.py – Helper functions for the Streamlit App
- reddit-kafka.pem – Private Key for launching EC2 Instance
- reddit-logo-new.svg – Image file for Reddit Logo
- requirements.txt – Requirements file with Python libraries for Streamlit installation

## How to run the App ? 

Run the app using the following command
`streamlit run RedditDashboard.py`

**App URL:** `https://reddit-realtime-listening.streamlit.app/`


**Note**: Prior to running the app, we need to initialize the Kafka Broker using the following command on the EC2 instance.

`ssh -i "reddit-kafka.pem" ec2-user@ec2-18-234-36-200.compute-1.amazonaws.com`

## License

MIT License

Copyright (c) 2024 Eshita Gupta

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
