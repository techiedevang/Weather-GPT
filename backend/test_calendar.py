from app.integration.google_calendar import fetch_todays_events

print("Authenticating with Google Calendar...")
events = fetch_todays_events()

print("\n--- Upcoming Events ---")
if not events:
    print("No events found for today.")
else:
    for e in events:
        print(f"- {e['title']} at {e['time']}")
print("-----------------------")
