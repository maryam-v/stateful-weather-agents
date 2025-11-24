# Weather Agent Orchestration 🚀

A modular AI pipeline built with Google ADK that demonstrates **multi‑agent orchestration**, **stateful sessions**, and **tool delegation**.  
Agents handle greetings, farewells, current weather, and forecasts, while session state stores user preferences and conversation summaries.

---

## ✨ Features
- **Greeting Agent** → handles simple hellos.
- **Farewell Agent** → handles polite goodbyes.
- **Weather Agent** → retrieves current weather with unit conversion.
- **Forecast Agent** → provides 3‑day forecasts.
- **Session Manager** → stores user preferences, summaries, and tool outputs.
- **Runner** → orchestrates async agent calls with streaming support.
- **Config** → centralized secrets and defaults via `.env`.

---

## 📂 Project Structure

```

stateful-weather-agents/
├── weather_app/
│   ├── __init__.py
│   ├── agents.py
│   ├── tools.py
│   ├── session.py
│   ├── runner.py
│   ├── config.py
│   └── main.py
├── tests/
│   ├── test_agents.py
│   ├── test_tools.py
│   ├── test_session.py
│   └── conftest.py
└── .github/workflows/tests.yml

```
---


## ⚙️ Setup

1. **Clone the repo**
```bash
git clone https://github.com/yourusername/weather-app.git
cd weather-app
```

2. **Create a virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```
3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4.**Create .env file**

```env
OPENWEATHER_API_KEY=your_openweather_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

---

## ▶️ Usage

Run the demo:

```bash
python main.py
```
Example Output:

```
INFO: SessionManager initialized for app 'weather_app'
INFO: Session 'session_demo' created for user 'user_demo'
INFO: Agent response: The weather in London is Overcast clouds with a temperature of 7°C.
INFO: Agent response: The 3-day forecast for Tokyo is: Broken clouds, 11°C; Clear sky, 13°C; Clear sky, 12°C.
INFO: Agent response: Hello, World!

--- Final Session State ---
user_preference_temperature_unit: Fahrenheit
user_preference_location: Montreal
last_city_checked_stateful: London
last_weather_report: The weather in London is Overcast clouds with a temperature of 7°C.
last_forecast_city: Tokyo
last_forecast_report: 3-day forecast for Tokyo: Broken clouds, 11°C; Clear sky, 13°C; Clear sky, 12°C
```

---

## 🧪 Testing

Run all tests:

```bash
test tests/
```

With coverage:

```bash
pytest --cov=.
```

---

## 🏗️ Architecture

**Session State** stores preferences, summaries, and tool outputs.

**Root Agent** delegates to sub‑agents:

1. **Greeting Agent**

2. **Farewell Agent**

3. **Forecast Agent**

4. **Weather Agent**

---

## 📜 License

This project is licensed under the MIT License.
