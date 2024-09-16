# Virtual Decision-Making Assistant

## Overview

This project is a chatbot built using LangChain and OpenAI's GPT-3 that acts as a professional advisor, guiding users through the process of choosing an item, such as a movie, city, book, or any other category. The bot helps users by understanding their preferences, providing recommendations, comparing different options, and addressing any doubts they might have. This assistant is designed to offer structured and predictable responses, ensuring a seamless and professional user experience.

## Features

- **Greeting**: The bot starts by warmly greeting the user and inquiring about the type of item they need help choosing (e.g., movie, city, book).
- **Understanding Preferences**: The bot asks users about their specific preferences or criteria, such as genre, climate, or author.
- **Providing Recommendations**: Based on the user's preferences, the bot recommends an option from the relevant category, using real-time data from external APIs (e.g., OMDb for movies).
- **Comparing Options**: If the user is undecided between two options, the bot provides a structured comparison, highlighting key aspects like ratings, features, or pros and cons.
- **Addressing Doubts**: The bot allows users to express doubts or ask questions, providing clear and concise answers to help them make an informed decision.
- **Closing**: The bot offers to assist further with more recommendations or helps finalize the user's choice.

## Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package installer)

### Required Packages

Before running the application, install the necessary Python packages:

```bash
pip install openai langchain requests
