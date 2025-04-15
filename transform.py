# transform.py
def transform_metric_data(raw_data):
    # This can be used for scaling, cleaning, or formatting
    transformed = {
        "timestamp": raw_data["timestamp"],
        "video_id": raw_data["video_id"],
        "metric": raw_data["metric"],
        "value": int(raw_data["value"]) if raw_data["value"] is not None else 0
    }
    return transformed
