def record_alert_feedback(alert_id: str, user_id: str, feedback_type: str) -> dict:
    """
    Research Gap 6: Closed-Loop Warning.
    Records whether a user understood the alert or needs more info.
    feedback_type should be "UNDERSTOOD", "NEED_MORE_INFO", or "NOT_USEFUL"
    """
    # MVP Mock: In production, this writes to Supabase PostgreSQL table `feedback_events`
    
    status = "RECORDED"
    follow_up_action = "NONE"
    
    if feedback_type == "NEED_MORE_INFO":
        follow_up_action = "TRIGGER_AI_EXPLANATION"
        
    print(f"Feedback recorded for Alert {alert_id} by User {user_id}: {feedback_type}")
    
    return {
        "status": status,
        "alert_id": alert_id,
        "follow_up_action": follow_up_action
    }
