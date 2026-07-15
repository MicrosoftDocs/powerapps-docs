---
title: Customize Microsoft 365 Copilot in Power Apps
description: Learn how to customize Microsoft 365 Copilot with declarative agents, custom engine agents, and Copilot Studio agents in Power Apps.
author: Mattp123
ms.service: powerapps
ms.subservice: mda-maker
ms.author: hemantg
ms.reviewer: matp
ms.date: 06/12/2026
ms.update-cycle: 180-days
ms.topic: how-to
applies_to: 
  - "powerapps"
search.audienceType: 
  - maker
contributors:
  - makolomi
  - Jacob-Wilkinson
  - devkeydet
  - mduelae
  - shwetamurkute
ms.collection: bap-ai-copilot
ai-usage: ai-assisted
---
# Customize Microsoft 365 Copilot with an agent

[!INCLUDE [customize-microsoft-365-copilot](~/../shared/customize-microsoft-365-copilot.md)] 

One way to create a declarative agent for a model-driven app is to turn on Microsoft 365 Copilot directly in your app. For more information, see [Enable your app for Microsoft 365 Copilot](/power-apps/maker/model-driven-apps/enable-your-app-copilot).

You can create your own app-specific agent mode in Power Apps by combining a default agent with the `Xrm.Copilot.*` APIs. The default agent defines the tailored Microsoft 365 Copilot experience that opens for users, and the APIs create the bidirectional connection between your app and Microsoft 365 Copilot.

## Set a default agent

If you build a custom agent as a companion to your model-driven app, you can set it as the default agent so it loads automatically when the app and the Microsoft 365 Copilot side pane open. This makes your agent the starting point for the experience and is the first part of building your own agent mode.

When you set a default agent:

- Your agent is selected without any action from the user.
- Users go straight to the tailored experience you designed for the app.
- App-specific workflows and guidance are ready as soon as Microsoft 365 Copilot opens.

A default agent is especially useful for scenario-focused agents that extend the core experience of the app and act as the front door to the app-specific Microsoft 365 Copilot experience you want users to have.

:::image type="content" source="media/microsoft-365-chat-model-driven-apps/default-agent.png" alt-text="Screenshot that shows how to set a default agent for Microsoft 365 Copilot in your model-driven app." lightbox="media/microsoft-365-chat-model-driven-apps/default-agent.png":::

## Xrm.Copilot APIs

The `Xrm.Copilot.*` client APIs let developers integrate Microsoft 365 Copilot directly into model-driven app experiences. With these APIs, your app can interact directly with the Microsoft 365 Copilot side pane and respond to Microsoft 365 Copilot-driven actions, so you can create richer, end-to-end agentic scenarios.

Used together with a default agent, these APIs complete the agent mode pattern: your agent is the starting point, your app can send prompts and context into Microsoft 365 Copilot, and Microsoft 365 Copilot can invoke actions back inside your app.

For the full API surface, see [Xrm.Copilot (Client API reference) in model-driven apps](../../developer/model-driven-apps/clientapi/reference/xrm-copilot.md).

These APIs let you:

- **Send prompts to Microsoft 365 Copilot**. Use `sendPromptToM365Copilot` to start a Microsoft 365 Copilot interaction from your app.
- **Open and control the Microsoft 365 Copilot side pane**. Use `openM365CopilotPanel` to make sure the Microsoft 365 Copilot pane is visible when needed.
- **Pass app context to Microsoft 365 Copilot**. Use `updateContext` (preview) to send extra grounding signals from your app.
- **Work with agents**. Use `getCurrentAgent` to check which agent is active.
- **Handle Microsoft 365 Copilot actions in your app**. Use `addActionHandler` to register custom handlers that process actions sent from Microsoft 365 Copilot responses.

Together, these APIs create a true bidirectional experience between the app UI and the agent, so agents can drive UI updates, trigger workflows, or run custom business logic.

### Handle Microsoft 365 Copilot actions with addActionHandler

Use the [`addActionHandler`](../../developer/model-driven-apps/clientapi/reference/xrm-copilot.md) API when your app needs to handle structured actions that Microsoft 365 Copilot emits.

When you build the action payload:

- Set `type` to **PowerApps** to target the Power Apps host.
- Set `action` (for example, `MyNamespace.MyMessage`) to the actionId you register in `addActionHandler`.
- Use `actionData` for the payload that your code processes and passes to the Power Apps host.

The following sections show two supported scenarios.

#### Adaptive Cards

Microsoft 365 Copilot responses can include Adaptive Cards with `Action.Submit` buttons that send action messages to the Power Apps host.

Example:

```json
{
  "type": "AdaptiveCard",
  "$schema": "https://adaptivecards.io/schemas/adaptive-card.json",
  "version": "1.5",
  "body": [
    {
      "type": "TextBlock",
      "text": "Click Go and I will send data to the host to process.",
      "wrap": true,
      "id": "txtSendMessage"
    },
    {
      "type": "ActionSet",
      "actions": [
        {
          "type": "Action.Submit",
          "title": "Go",
          "id": "btnGo",
          "data": {
            "type": "PowerApps",
            "action": "MyNamespace.MyMessage",
            "actionData": {
              "foo": "bar"
            }
          }
        }
      ]
    }
  ]
}
```

#### MCP apps

Microsoft 365 Copilot responses can include HTML that sends action messages to the Power Apps host.

Example:

```html
<Button
  appearance="outline"
  icon={<ArrowLeft24Regular />}
  onClick={() => {
    try {
      const message = {
        eventName: 'powerapps.copilot.chat.action',
        action: 'MyNamespace.MyMessage',
        actionData: {
          foo: 'bar'
        },
      };
      window.parent.parent.postMessage(message, '*');
    } catch (error) {
      // eslint-disable-next-line no-console
      console.error('Error posting HOST_ACTION message to parent window:', error);
    }
  }}
>
  Test
</Button>
```

## Limitations

- Agents you author can't yet use in-app user context to tailor their responses.
- When setting a default agent, the starter prompts from the agent do not render.

## Related information

- [Add Microsoft 365 Copilot for app users in model-driven apps](add-microsoft-365-copilot.md)
- [Use Microsoft 365 Copilot in model-driven apps](../../user/use-microsoft-365-copilot-model-driven-apps.md)
- [Add Microsoft 365 Copilot for app users in canvas apps (preview)](../../maker/canvas-apps/microsoft-365-copilot-canvas-app.md)
- [Use Microsoft 365 Copilot in canvas apps (preview)](../../user/use-microsoft-365-copilot-canvas-apps.md)
- [Customize Microsoft 365 Copilot with an agent in canvas apps](../canvas-apps/customize-microsoft-365-copilot-chat.md)
