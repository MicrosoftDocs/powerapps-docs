---
title: PowerAppsContent Interface (Client API reference) (preview)
description: The interface that describes the context data passed to the Xrm.Copilot.updateContext method.
author: devkeydet
ms.author: marcsc
ms.date: 04/23/2026
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
  - JimDaly
---

# PowerAppsContent Interface (Client API reference) (preview)

[!INCLUDE [preview-note-pp](~/../shared-content/shared/preview-includes/preview-note-pp.md)]

An interface that describes the context data passed to the [updateContext](updatecontext.md) method. All properties are optional.

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
