# Weather Dashboard 🌤️

This is a simple weather dashboard web application built using Flask and OpenWeatherMap API. The app allows users to enter a city name and view the current weather details, including temperature, humidity, wind speed, and weather conditions.

## Features
- Fetch real-time weather data for any city
- User-friendly interface with responsive design
- Error handling for invalid city names
- Sky blue-themed background for a fresh, clean look

## Tech Stack
- Python (Flask)
- HTML, CSS (Bootstrap)
- OpenWeatherMap API

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/weather-dashboard.git
   cd weather-dashboard
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Mac/Linux
   venv\Scripts\activate    # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory and add your OpenWeatherMap API key:
   ```plaintext
   API_KEY=your_openweathermap_api_key
   ```

## Usage
1. Run the application:
   ```bash
   python app.py
   ```

2. Open your browser and go to:
   ```plaintext
   http://127.0.0.1:5000/
   ```

3. Enter a city name and click "Get Weather" to see the results.

## Project Structure
```
├── static/
│   └── styles.css
├── templates/
│   └── index.html
├── app.py
├── requirements.txt
└── README.md
```

## API Reference
- [OpenWeatherMap API](https://openweathermap.org/api)

## Contributing
Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

## License
This project is licensed under the MIT License.

