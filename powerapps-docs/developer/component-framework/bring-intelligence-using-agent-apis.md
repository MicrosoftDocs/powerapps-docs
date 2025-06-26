---
title: "Bring intelligence into your components using Agent APIs (preview)"
description: "Learn about how you can integrate Copilot Studio topics into your custom components using Agent APIs"
author: adrianorth
ms.author: aorth
ms.date: 06/26/2025
ms.reviewer: jdaly
ms.topic: conceptual
ms.subservice: pcf
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---

# Bring intelligence into your component using Agent Xrm APIs (preview)

[!INCLUDE [preview-note-pp](~/../shared-content/shared/preview-includes/preview-note-pp.md)]

Agent APIs are a set of interfaces introduced in Microsoft Power Apps that allow components to interact with topics created in Microsoft Copilot Studio. These APIs are available in two forms:

- `Context.Copilot` methods used for PCF controls. This is the subject of this article.
- [Xrm.Copilot namespace used for client scripts in model-driven apps.](../model-driven-apps/clientapi/bring-intelligence-using-agent-apis.md)

These APIs are designed to enhance integration with Microsoft Copilot Studio (MCS), enabling more intelligent and responsive app experiences.

|API|Description|
|---------|---------|
|[copilot.executeEvent](reference/copilot/executeevent.md)|[!INCLUDE [executeevent-description](reference/copilot/includes/executeevent-description.md)]|
|[copilot.executePrompt](reference/copilot/executeprompt.md)|[!INCLUDE [executeprompt-description](reference/copilot/includes/executeprompt-description.md)]|

## Accessibility

When creating a code component, ensure the following best practices in [code component accessibility checks](code-components-best-practices.md#check-accessibility) are followed to have an accessible experience.


### Related articles

[FAQ for Agent APIs and Agent Response component](../../maker/common/faq-agent-api-component.md)<br />
[Copilot](reference/copilot.md)  
[executeEvent](reference/copilot/executeevent.md)  
[executePrompt](reference/copilot/executeprompt.md)  
[Power Apps component framework overview](overview.md)  
[Create your first code component](implementing-controls-using-typescript.md)  
[Learn Power Apps component framework](/training/paths/use-power-apps-component-framework)  
[Xrm.Copilot (Client API reference)](../model-driven-apps/clientapi/reference/xrm-copilot.md)  
[Add agent response with the form designer (preview)](../../maker/model-driven-apps/form-designer-add-configure-agent-response.md)
