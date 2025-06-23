---
title: "Bring intelligence into your app using Agent Xrm APIs (preview)"
description: "Learn about how you can integrate Copilot Studio topics into your model-driven apps using Agent Xrm APIs."
author: adrianorth
ms.author: aorth
ms.date: 06/18/2025
ms.reviewer: jdaly
ms.topic: conceptual
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---

# Bring intelligence into your app using Agent Xrm APIs (preview)

[!INCLUDE [preview-note-pp](~/../shared-content/shared/preview-includes/preview-note-pp.md)]

Agent APIs are a set of interfaces introduced in Microsoft Power Apps that allow model-driven apps to interact with topics created in Microsoft Copilot Studio. These APIs are available in two forms:

- `Xrm.Copilot` namespace used for client scripts in model-driven apps. This article describes these APIs.
- [PCF (for use in custom controls)](../../component-framework/bring-intelligence-using-agent-apis.md).

These APIs are designed to enhance integration with Microsoft Copilot Studio (MCS), enabling more intelligent and responsive app experiences.

|API|Description|
|---------|---------|
|[Xrm.Copilot.executeEvent](reference/Xrm-Copilot/executeevent.md)|[!INCLUDE [executeevent-description](reference/Xrm-Copilot/includes/executeevent-description.md)]|
|[Xrm.Copilot.executePrompt](reference/Xrm-Copilot/executeprompt.md)|[!INCLUDE [executeprompt-description](reference/Xrm-Copilot/includes/executeprompt-description.md)]|


### Related articles

[FAQ for Agent APIs and Agent Response component](../../../maker/common/faq-agent-api-component.md)  
[Xrm.Copilot (Client API reference)](reference/xrm-copilot.md)  
[Xrm.Copilot.executeEvent (Client API reference)](reference/Xrm-Copilot/executeevent.md)  
[Xrm.Copilot.executePrompt (Client API reference)](reference/Xrm-Copilot/executeprompt.md)  
[Copilot (Power Apps component framework API reference)](../../component-framework/reference/copilot.md)
