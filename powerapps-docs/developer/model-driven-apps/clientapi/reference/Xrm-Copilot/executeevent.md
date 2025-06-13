---
title: "executeEvent (Client API reference) in model-driven apps (preview)"
description: Includes description and supported parameters for the executeEvent method.
author: adrianorth
ms.author: aorth
ms.date: 06/16/2025
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType:
  - developer
contributors:
  - JimDaly
---

# executeEvent (Client API reference)  (preview)

[!INCLUDE [preview-note-pp](~/../shared-content/shared/preview-includes/preview-note-pp.md)]

[!INCLUDE[./includes/executeevent-description.md](./includes/executeevent-description.md)]

## Syntax

`Xrm.Copilot.executeEvent(eventName, eventParameters).then(successCallback, errorCallback); `

## Parameters

| Parameter Name| Type| Required | Description|
| --- | --- | --- | --- |
| `eventName` | string | Yes | Event Name registered in the MCS topic  |
| `eventParameters` | Unknown  | Yes | Parameters needed for the event execution. These depend on what the topic does.|
| `successCallback` | Function | Yes | A function to call when the operation succeeds.|
| `errorCallback`   | Function | Yes | A function to call when the operation fails.|

## Return Value

An array of [MCSResponse](mcsresponse.md)

## Example

In Microsoft Copilot Studio, a custom topic has been registered that accepts id (entity record id) as input parameter. Based on the input, it fetches the related activities of that entity record and returns the results as an MCS event activity.

```javascript
const response = await Xrm.Copilot.executeEvent(
   "Microsoft.PowerApps.Copilot.RelatedActivities", 
   { id:"aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb"});
```

### Response

```json
[
    {
        "type": "event",
        "timestamp": "2025-02-05T16:05:53.4074714+00:00",
        "replyToId": "bbbbbbbb-1111-2222-3333-cccccccccccc",
        "attachments": [],
        "value": {
            "@odata.context": "https://[ORG URI]/api/data/v9.2/$metadata#activitypointers(subject,prioritycode)",
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
                },
                {
                    "@odata.etag": "W/\"6818374\"",
                    "@odata.type": "#Microsoft.Dynamics.CRM.phonecall",
                    "activityid": "eeeeeeee-4444-5555-6666-ffffffffffff",
                    "activitytypecode": "task",
                    "prioritycode": 1,
                    "subject": "Pain admitted by sponsor (sample)"
                },
                {
                    "@odata.etag": "W/\"6818471\"",
                    "@odata.type": "#Microsoft.Dynamics.CRM.phonecall",
                    "activityid": "ffffffff-5555-6666-7777-aaaaaaaaaaaa",
                    "activitytypecode": "task",
                    "prioritycode": 1,
                    "subject": "Pre-proposal review conducted (sample)"
                }
            ]
        },
        "name": "MS.CopilotApiDemo.RelatedActivities"
    }
]
```



### Related articles

[Xrm.Copilot (Client API reference)](../xrm-copilot.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
