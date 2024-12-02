# Music Recommendation using Face Emotion Recognition

#### This project integrates facial emotion recognition and music recommendation to create a personalized music experience. Using real-time facial emotion detection, it matches the user’s mood with curated playlists, ensuring the music resonates with their emotional state.


### Table of Contents
1. Introduction
2. Features
3. Technologies Used
4. Installation
5. Usage
6. Project Workflow
7. Dataset
8. Results
9. Future Scope


### Introduction
Music has a profound effect on human emotions, aiding in mood enhancement and self-awareness. This project leverages Convolutional Neural Networks (CNN) for facial emotion recognition and recommends music playlists tailored to the detected emotions. It aims to simplify playlist management and enhance user experience with minimal manual effort.


### Features
* Real-time Emotion Detection: Uses a webcam to capture user expressions.
* Emotion-based Music Recommendation: Suggests playlists based on emotions like Happy, Sad, Angry, Neutral, and Surprised.
* Optimized with CNN: Provides high accuracy in emotion detection.
* Curated Playlists: Each playlist is emotion-specific, designed to complement or uplift the user’s mood.


### Technologies Used
* Python: Primary programming language.
* OpenCV: For real-time face detection.
* TensorFlow/Keras: For building and training CNN models.
* Spotipy: For Spotify playlist integration.
* Pandas: For handling and saving data.
* Tkinter: GUI for a seamless user experience.


### Installation
### Prerequisites:
    * Python 3.8+
    * Spotify Developer Account
    * FER2013 Dataset
### Steps:
1. Clone this repository:
   ```bash
    git clone https://github.com/your-repo-url.git
    cd your-repo
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up Spotify API credentials:
   * Visit Spotify Developer Dashboard.
   * Create an app and note the Client ID and Client Secret.
   * Add them to your .env file:
     ```bash
     SPOTIFY_CLIENT_ID=your_client_id
     SPOTIFY_CLIENT_SECRET=your_client_secret
     ```
4. Ensure the FER2013 dataset is downloaded and placed in the data/ directory.


### Usage
1. Start the application:
   ```bash
   python app.py
   ```
2. Follow the on-screen instructions to:
   * Enable your webcam.
   * Detect your facial emotion.
   * Receive curated music recommendations.


### Project Workflow
1. Face Capture:
   * Capture the user’s face using OpenCV.
2. Emotion Detection:
   * CNN processes the facial image to classify emotions.
3. Playlist Recommendation:
   * Map detected emotion to a pre-defined playlist via Spotify API.


### Dataset
   * FER2013: A labeled dataset of 48x48 pixel grayscale images with various facial expressions.
   * Emotion categories: Happy, Sad, Angry, Neutral, and Surprised.


### Results
| Algorithm |	Validation Accuracy |	Testing Accuracy |
| --------- | -------------------- | ------------------ |
| SVM |	66.0% |	66.9% |
| ELM |	62.0% |	63.4% |
| CNN |	95.0% |	71.5% |

CNN outperformed other algorithms in both validation and testing phases.



### Future Scope
* Improve accuracy under poor lighting and low-resolution camera conditions.
* Extend emotion categories (e.g., Fear, Disgust).
* Implement music therapy for stress, anxiety, and depression management.
* Add multilingual support for global users.
