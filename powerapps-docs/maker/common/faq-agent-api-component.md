---
title: FAQ for Agent APIs and Agent Response component in model-driven apps
description: This FAQ provides information about the AI technology used in model-driven apps, along with key considerations and details about how AI is used, how it was tested and evaluated, and any specific limitations.
ms.date: 06/18/2025
ms.custom: 
  - responsible-ai-faqs
ms.topic: article
author: adrianorth
ms.author: aorth
ms.reviewer: jdaly
---

# FAQ for Agent APIs and Agent Response component

These frequently asked questions (FAQ) describe the AI impact of Agent APIs feature in model-driven apps.

## What is Agent APIs and Agent Response component?

Microsoft Power Apps has introduced APIs and code components designed to interface with the topics created within Microsoft Copilot Studio (MCS) from model-driven apps. These APIs are available as XRM and PCF. The code component is available in the Form Designer to be added to forms.

## What are capabilities of the Agent APIs and Agent Response component?

The new APIs can either call a specific topic in MCS or send a prompt that MCS orchestrates. The response from both APIs is a JSON structure the caller can use within their model driven app. The APIs are available for use in the Xrm events of model driven apps and also use within custom PCF control.

The Agent Response component provides a simplified component to call the Agent API with a topic for MCS. The component renders the results of the MCS response in the form.

## What is the intended use of the Agent APIs and Agent Response component?

The APIs are intended to allow customization of model driven apps to include application calls to MCS and allow the results to be integrated into the app. It provides a simplified process to call MCS.

## How was Agent APIs and Agent Response component evaluated? What metrics are used to measure performance?

In our evaluations, we look at how accurately the response is from MCS. MCS responses are evaluated for satisfying Microsoft's responsible AI principles.

## What are the limitations of Agent APIs and Agent Response component? How can users minimize the impact of the Agent APIs limitations when using the system?

The APIs and component are optional for makers to use and makers need to consider how best to use the APIs and component within their customizations.

## What operational factors and settings allow for effective and responsible use of the feature?

Makers are required to ensure that the MCS topics are returning accurate and appropriate responses. Makers using the API are responsible to handle the response as part of their customization.

In addition, makers are strongly encouraged to indicate to users where AI has been used in the user experience. This is like how Microsoft shows "AI-generated content may be incorrect".

## See also

- [Bring intelligence into your component using Agent Xrm APIs (preview)](../../developer/component-framework/bring-intelligence-using-agent-apis.md)
- [Bring intelligence into your app using Agent Xrm APIs (preview)](../../developer/model-driven-apps/clientapi/bring-intelligence-using-agent-apis.md)
- [Use Agent Response component in the model-driven app forms (preview)](../model-driven-apps/form-designer-add-configure-agent-response.md)

[!INCLUDE [footer-banner](../../includes/footer-banner.md)]
