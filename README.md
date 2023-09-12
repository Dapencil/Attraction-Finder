# Attraction Finder

## Description

Attraction Finder is a web application that allows you to discover attractions from around the world. With just a few clicks, you can search for attractions based on location, description, and season. Whether you're planning a trip or simply curious about different places, Attraction Finder makes it easy to explore and learn about exciting destinations.

### Features

- **Place**: Search for attractions by location, such as cities, countries, or landmarks.
- **Description**: Find attractions with specific keywords in their descriptions, making it easy to discover places that match your interests.
- **Season**: Plan your trips more effectively by filtering attractions based on the best season to visit.

## Technology

Attraction Finder is built using the following technologies:

- [Flask](https://flask.palletsprojects.com/): A lightweight web framework for Python that powers the backend of the application.
- [LangChain](https://github.com/langchain/langchain): A language processing library that helps analyze and categorize attraction descriptions.
- [SerpApi](https://serpapi.com/): An API for accessing search engine results, which enables Attraction Finder to retrieve attraction data.

## Disclaimer

**Note**: This search method and the displayed images are for demonstration purposes only. Attraction Finder does not intend to infringe on any copyrights or intellectual property rights. The images and data are sourced from publicly available information and are used to showcase the application's functionality.

## Installation

To run Attraction Finder locally, follow these steps:

1. Install `virtualenv` if you haven't already:

   ```shell
   pip install virtualenv
   ```

2. Create a virtual environment named `venv`:

   ```shell
   virtualenv venv
   ```

3. Activate the virtual environment. Use the appropriate command based on your operating system:

   For Windows:

   ```shell
   .\venv\Scripts\activate
   ```

   For Linux or macOS:

   ```shell
   source ./venv/bin/activate
   ```

4. Install the project dependencies from `requirements.txt`:

   ```shell
   pip install -r requirements.txt
   ```

## Running the Server

Once you have completed the installation, you can run the Attraction Finder server:

```shell
python -m flask run
```

Visit `http://localhost:5000` in your web browser to access Attraction Finder.

Enjoy exploring attractions from around the world with Attraction Finder!
