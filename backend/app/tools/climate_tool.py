from typing import Dict, Any

def get_climate_trends(location: str, time_period: str) -> Dict[str, Any]:
    return {
        "location": location if location else "Unknown",
        "time_period": time_period if time_period else "past 10 years",
        "trend_summary": "Average temperature has increased by 0.8°C. Rainfall patterns have become more erratic with shorter, more intense precipitation events.",
        "data_points": {
            "avg_temp_change_celsius": "+0.8",
            "extreme_weather_events_increase": "15%"
        },
        "source": "Historical Climate Dataset"
    }
