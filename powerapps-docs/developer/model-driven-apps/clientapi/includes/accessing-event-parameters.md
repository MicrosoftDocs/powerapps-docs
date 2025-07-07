## Accessing eventParameters

Within the Copilot Studio topic, the `eventParameters` from the API call can be accessed using the variable `Activity.Value`. Use [Parse value node](/microsoft-copilot-studio/authoring-variables?tabs=webApp#parse-value-node) to convert the JSON into a record with one or more fields. Selecting **From sample data** for **Data type** allows providing a JSON example to create the record.

### Example

In Microsoft Copilot Studio, where a topic is registered that accepts an ID (entity record ID) as an input parameter. Based on the input, it retrieves the related activities of that entity record and returns the results as an Copilot Studio event activity. The PCF context API enables the execution of these methods within the context of PCF controls. 

```javascript
const response = await context.copilot.executeEvent( 
    "Microsoft.PowerApps.Copilot.RelatedActivities", 
    { id:"aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb"}); 
```

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
