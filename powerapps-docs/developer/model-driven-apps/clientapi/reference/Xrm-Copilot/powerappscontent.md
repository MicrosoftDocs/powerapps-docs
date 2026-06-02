---
title: PowerAppsContent Interface (Client API reference)
description: The interface that describes the context data passed to the Xrm.Copilot.updateContext method.
author: devkeydet
ms.author: marcsc
ms.date: 06/02/2026
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
  - JimDaly
---

# PowerAppsContent Interface (Client API reference)

[!INCLUDE [powerappscontent-description](includes/powerappscontent-description.md)]

## Properties

| Name| Type| Description|
|---|---|---|
| `schemaVersion`| `string`| Version of the content schema.|
| `appType`| `ModelApp` \| `CanvasApp` \| `CodeApp`| Type of the Power Apps application.|
| `appId`| `string`| Unique identifier of the app.|
| `orgId`| `string`| Unique identifier of the organization.|
| `geo`| `string`| Geographic region of the environment.|
| `entity`| `string`| Logical name of the primary table for the current page.|
| `filterXML`| `string`| FetchXML string scoping the data context.|
| `filterId`| `string`| Unique identifier of a saved view or filter.|
| `extendedContext`| `Array<Record<string, unknown>>`| Additional arbitrary key-value context pairs.|
| `telemetryContext`| `{ clientSessionId?: string; clientRequestId?: string }`| Telemetry correlation identifiers.|
| `selectedRecords`| `{ selectedContents: ISelectedRecordContents[] }`| Records currently selected by the user.|
| `messageAnnotationAppContext`| `string`| App context annotation for message rendering.|

### Related articles

[updateContext method](updatecontext.md)   
[Xrm.Copilot (Client API reference)](../xrm-copilot.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
