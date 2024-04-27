# Reporto

## Overview

In many regions, the manual analysis of lab reports is slow, error-prone, and often hindered by the scarcity of healthcare providers. This project addresses these challenges by introducing an AI-powered application designed to automate and enhance the analysis and interpretation of lab reports, reducing wait times and the anxiety associated with them.

## Problem Statement

Analyzing lab reports manually can be time-consuming and is prone to human error, leading to delays that are exacerbated by the limited availability of healthcare providers in some areas. This waiting period can significantly impact patients awaiting important health information.

## Project Description

Our solution, developed during a hackathon, utilizes a combination of multiple AI agents to improve the efficiency and accuracy of lab report analysis. The system comprises the following components:

- **OCR Model**: Extracts text from scanned lab reports with high accuracy.
- **Summarization Agent**: Condenses critical information to capture the essence of the report efficiently.
- **Security Agent**: Ensures privacy by anonymizing the data, removing any personally identifiable information to protect patient confidentiality.
- **Recommendation and Analysis Agent**: Provides personalized advice and detailed analysis based on the anonymized results, adhering to medical best practices and guidelines.

The integration of these agents creates a comprehensive system that delivers secure and immediate health insights, which is particularly beneficial in underserved areas.

## Features

- **Text Extraction**: Utilizes state-of-the-art OCR technology to convert images of lab reports into editable text formats.
- **Data Summarization**: Employs advanced natural language processing techniques to summarize lengthy reports into concise, actionable insights.
- **Privacy Protection**: Implements robust algorithms to ensure that all processed data complies with privacy laws and standards.
- **Customized Recommendations**: Analyzes data to provide health recommendations that align with up-to-date medical guidelines.

## Setup Instructions

Follow these steps to set up and run the project on your local machine:

### Prerequisites
- Git: Ensure Git is installed on your machine. If not, download and install it from [git-scm.com](https://git-scm.com/).

### Step 1: Clone the Repository
1. Open your command line interface (CLI).
2. Navigate to the directory where you want to clone the repository.
3. Run the following command to clone the repository:
   ```bash
   git clone git@github.com:Motaseam-Yousef/reporto.git
   ```
4. Change into the cloned directory:
   ```bash
   cd reporto
   ```

### Step 2: Set Up Your Environment
1. (Optional) Create a virtual environment to manage dependencies:
   ```bash
   python -m venv venv
   ```
   Activate the virtual environment:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On MacOS/Linux:
     ```bash
     source venv/bin/activate
     ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### step 3: Add you credintials
1. Make .env file and put your API keys in it
GEMINI_API_KEY 
ELEVENLABS_API_KEY -> TTS

### Step 4: Run the Application
1. Execute the main script or start the application server (adjust this step based on your project specifics):
   ```bash
   python main.py
   ```

## Good Luck 
