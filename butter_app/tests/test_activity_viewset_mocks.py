correct_activity = [
    {
        "id": "X13200400Z",
        "activity_date": "2021-04-16T08:05:35.941465",
        "track_id": "T12h456",
        "status": "A",
        "billing_amount": 10.84,
    },
    {
        "id": "X13200450Z",
        "activity_date": "2021-04-16T08:05:35.941465",
        "track_id": "T12h456",
        "status": "A",
        "billing_amount": 10.84,
    },
]
wrong_date_activity = [
    {
        "id": "wrong_date",
        "activity_date": "2021-16T08:05:35.941465",
        "track_id": "T12h456",
        "status": "A",
        "billing_amount": 10.84,
    }
]
wrong_status_activity = [
    {
        "id": "wrong_status",
        "activity_date": "2021-4-16T08:05:35.941465",
        "track_id": "T12h456",
        "status": "X",
        "billing_amount": 10.84,
    }
]
negative_price_task_activity = [
    {
        "id": "negative_price",
        "activity_date": "2021-4-16T08:05:35.941465",
        "track_id": "T12h456",
        "status": "X",
        "billing_amount": 10.84,
    }
]
aggregate_activity = [
    {
        "id": "X13200000Z",
        "activity_date": "2021-04-16T08:05:35.941465",
        "track_id": "T1234567",
        "status": "A",
        "billing_amount": 10.54,
    },
    {
        "id": "X13200001Z",
        "activity_date": "2021-04-16T08:05:36.941465",
        "track_id": "T1234567",
        "status": "S",
        "billing_amount": 10.54,
    },
    {
        "id": "X13200002Z",
        "activity_date": "2021-04-16T08:05:37.941465",
        "track_id": "T1234567",
        "status": "R",
        "billing_amount": 0.54,
    },
]
aggregate_activity_result = {
    "track_id": "T1234567",
    "amount": 10.00,
    "last_status": "R",
}
