#### Response

```json
[
    {
        "type": "event",
        "timestamp": "2025-02-05T16:05:53.4074714+00:00",
        "replyToId": "bbbbbbbb-1111-2222-3333-cccccccccccc",
        "attachments": [],
        "value": {
            "@odata.context": "https://*.dynamics.com/api/data/v9.2/$metadata#activitypointers(subject,prioritycode)",
            "value": [
                {
                    "@odata.etag": "W/\"6825587\"",
                    "@odata.type": "#Microsoft.Dynamics.CRM.phonecall",
                    "activityid": "cccccccc-2222-3333-4444-dddddddddddd",
                    "activitytypecode": "phonecall",
                    "prioritycode": 2,
                    "subject": "Discuss new opportunity (sample)"
                },
                {
                    "@odata.etag": "W/\"6826236\"",
                    "@odata.type": "#Microsoft.Dynamics.CRM.phonecall",
                    "activityid": "dddddddd-3333-4444-5555-eeeeeeeeeeee",
                    "activitytypecode": "phonecall",
                    "prioritycode": 2,
                    "subject": "Likes our new products (sample)"
                }
            ]
        },
        "name": "MS.CopilotApiDemo.RelatedActivities"
    }
]
```