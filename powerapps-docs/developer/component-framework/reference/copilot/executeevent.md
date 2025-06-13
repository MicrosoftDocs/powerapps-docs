---
title: executeEvent (Power Apps component framework API reference) (preview)
description: Executes a Microsoft Copilot Studio topic based on the registered Event Name. 
author: adrianorth
ms.author: aorth
ms.date: 05/05/2025
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# executeEvent (preview)

[!INCLUDE [preview-note-pp](~/../shared-content/shared/preview-includes/preview-note-pp.md)]

[!INCLUDE[./includes/executeevent-description.md](./includes/executeevent-description.md)]

## Available for

Model-driven apps

## Syntax

`context.copilot.executeEvent(eventName, eventParameters).then(successCallback, errorCallback);`

## Parameters

| Parameter Name| Type| Required | Description|
| --- | --- | --- | --- |
| `eventName` | string | Yes | Event Name registered in the MCS topic  |
| `eventParameters` | Unknown  | Yes | Parameters needed for the event execution. These depend on what the topic does.|
| `successCallback` | Function | Yes | A function to call when the operation succeeds.|
| `errorCallback`   | Function | Yes | A function to call when the operation fails.|

## Return Value

Type: `Promise<`[MCSResponse](mcsresponse.md)`>`

See [Promise](https://developer.mozilla.org/docs/Web/JavaScript/reference/Global_Objects/Promise) and [MCSResponse](mcsresponse.md)

## Example

In Microsoft Copilot Studio, where a topic is registered that accepts an ID (entity record ID) as an input parameter. Based on the input, it retrieves the related activities of that entity record and returns the results as an MCS event activity. The PCF context API enables the execution of these methods within the context of PCF controls. 

```typescript
const response = await context.copilot.executeEvent( 
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


### Related articles

[Copilot](../copilot.md)  
[executePrompt](executeprompt.md)  
[Power Apps component framework API reference](../../reference/index.md)  
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
