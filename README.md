# Dixit-Inspired AI: Creative Prompt Generator

An AI-powered tool designed to generate imaginative prompts for abstract illustrations, inspired by the storytelling game *Dixit*. This project combines **computer vision (CV)** and **natural language processing (NLP)** techniques to create prompts that match the whimsical and abstract nature of the game.

## 🌟 Features
- Extracts visual features from card images using **CLIP** (Contrastive Language–Image Pretraining).
- Generates creative, storytelling prompts with **GPT-2**, fine-tuned for the abstract art cards from the Dixit game
- Incorporates **Reinforcement Learning with Human Feedback (RLHF)** to refine prompts based on user input 
- Interactive web app using **Streamlit**

## 🛠️ Tools and Technologies
### Machine Learning
- **PyTorch**: Backbone framework for implementing CLIP and GPT-2 models.
- **Hugging Face Transformers**: For working with pre-trained models like CLIP and GPT-2.
- **Stable-Baselines3**: For integrating reinforcement learning to enhance prompt generation.

### Computer Vision
- **CLIP**: To extract embeddings that align visual features with textual descriptions.
- **OpenCV**: For preprocessing images, including resizing, normalization, and augmentation.

### Natural Language Processing
- **GPT-2**: To generate abstract and creative prompts.
- **SpaCy**: For optional text preprocessing.

### Deployment
- **Streamlit**: To build an interactive app for users to upload images and receive prompts.
- **Flask/FastAPI**: For serving the model as an API.
- **Docker**: For containerizing the workflow to ensure reproducibility and scalability.

### Data Handling
- **Pandas**: For managing datasets of images and corresponding prompts.
- **JSON**/**CSV**: For storing image-prompt annotations.

### Visualization
- **Matplotlib/Seaborn**: To visualize embeddings and analyze model performance.
- **Plotly**: For interactive visualizations (optional).

## 📚 Workflow
1. **Image Preprocessing**: Resize and normalize card images using OpenCV.
2. **Feature Extraction**: Use CLIP to generate image embeddings representing abstract visual features.
3. **Prompt Generation**: Pass embeddings into GPT-2 to create creative, storytelling prompts.
4. **Feedback Loop**: Collect human ratings for generated prompts and use RLHF to refine the model.
5. **Deployment**: Package the workflow into a web app or API using Streamlit or Flask.

## 🌈 Future Enhancements

- Expand functionality to generate short stories for the prompts to emulate the Dixit game.

## 🚀 Getting Started
### Requirements
Install dependencies using `pip`:

```bash
pip install torch transformers opencv-python pandas streamlit flask


