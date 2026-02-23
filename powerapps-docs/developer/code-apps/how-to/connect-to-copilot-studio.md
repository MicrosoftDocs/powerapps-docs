---
title: "How to: Connect to Copilot Studio"
description: "Learn how to connect your code app Copilot Studio and invoke an agent."
ms.author: jordanchodak
author: jordanchodakWork
ms.date: 02/18/2026
ms.reviewer: jdaly
ms.topic: how-to
contributors:
 - JimDaly
---
# How to: Connect your code app to Microsoft Copilot Studio agents

Microsoft Copilot Studio agents bring AI-powered capabilities to your code apps. This article shows you how to add the Microsoft Copilot Studio connector to your code app and invoke agents to process user input and return intelligent responses.

## Prerequisites

- An initialized code app project
- A published Microsoft Copilot Studio agent in your environment
- Basic understanding of [how to connect code apps to data](connect-to-data.md)

## Ensure you have a Microsoft Copilot Studio connection

To connect your code app to a Copilot Studio agent, you need a Microsoft Copilot Studio connection in your environment. Check whether one already exists or create a new one.

### Check for existing connections

To see if you already have a Microsoft Copilot Studio connection using the [`pac connection list`](/power-platform/developer/cli/reference/connection#pac-connection-list) command :

```bash
pac connection list
```

Look for a connection with the API ID `/providers/Microsoft.PowerApps/apis/shared_microsoftcopilotstudio`, and copy the `connectionId` value.

### Create a new connection

If you don't have an existing connection, you must create one through the Power Apps maker portal UI. Follow the instructions in [how to connect code apps to data](connect-to-data.md) and ensure that you copy the `connectionId`.

## Add the Microsoft Copilot Studio connector

After creating a Microsoft Copilot Studio connection, use the PAC CLI [`pac code add-data-source`](/power-platform/developer/cli/reference/code#pac-code-add-data-source) command to add it to your code app:

```bash
pac code add-data-source -a "shared_microsoftcopilotstudio" -c <connectionId>
```

This command automatically:

- Updates your `power.config.json` file with the Copilot Studio data source
- Generates TypeScript model and service files in the `src/generated` folder

## Publish and get your agent name

Before you can invoke an agent from your code app, you need to publish it and get its name.

### Publish your agent

1. Open your agent in [Copilot Studio](https://copilotstudio.microsoft.com)
1. Select **Publish** to publish your agent

### Get your agent name

1. In Copilot Studio, go to **Channels**.
1. Select **Web app**.
1. View the connection string to find your agent name.

The URL format is:
```
https://{id}.environment.api.powerplatform.com/copilotstudio/dataverse-backed/authenticated/bots/{agentName}/conversations?api-version=2022-03-01-preview
```

**Example agent name:** `cr3e1_customerSupportAgent`

> [!TIP]
> Copy the agent name exactly as it appears in the URL. Agent names are case-sensitive and typically include a publisher prefix.

## Invoke a Copilot Studio agent

With the connector added, you can call a Copilot Studio agent from your code app. The following steps show you how to import the generated service, send a message to the agent, and handle its response.

### Use the `ExecuteCopilotAsyncV2` action

Use the `ExecuteCopilotAsyncV2` action to invoke agents from code apps. This action returns agent responses synchronously. It's the [Execute Agent and wait action](/connectors/microsoftcopilotstudio/#execute-agent-and-wait) action included with the [Microsoft Copilot Studio connector](/connectors/microsoftcopilotstudio).

**API path:** `/proactivecopilot/executeAsyncV2`

### Import the generated service

After adding the data source, import the generated TypeScript service:

```typescript
import { CopilotStudioService } from './generated/services/CopilotStudioService';
```

### Send a message to the agent

Use the `ExecuteCopilotAsyncV2` method to send a message and await the agent's response:

```typescript
const response = await CopilotStudioService.ExecuteCopilotAsyncV2({
  message: "What is the status of my order?",
  notificationUrl: "https://notificationurlplaceholder",
  agentName: "cr3e1_customerSupportAgent"
});
```

### Request parameters

The `ExecuteCopilotAsyncV2` method accepts the following parameters:

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| `message` | Yes | string | The prompt or data to send to the agent. Can be a JSON string for structured data. |
| `notificationUrl` | Yes | string | Placeholder URL (use `"https://notificationurlplaceholder"`). The API requires this URL but doesn't use it in synchronous mode. |
| `agentName` | Yes | string | The name of your published Copilot Studio agent. |

### Response structure

The response contains the following properties:

| Property | Type | Description |
|----------|------|-------------|
| `responses` | `string[]` | Array of response strings from the agent |
| `conversationId` | `string` | The conversation ID for tracking |
| `lastResponse` | `string` | The most recent response from the agent |
| `completed` | `boolean` | Whether the agent finished processing |

### Example: Get agent response

```typescript
const response = await CopilotStudioService.ExecuteCopilotAsyncV2({
  message: "Summarize the latest product trends",
  notificationUrl: "https://notificationurlplaceholder",
  agentName: "cr3e1_trendAnalyzer"
});

if (response.data.completed) {
  const agentResponse = response.data.lastResponse;
  console.log("Agent response:", agentResponse);
}
```

### Example: Parse JSON responses

Agents often return responses as JSON strings. Parse the responses to extract specific data:

```typescript
const response = await CopilotStudioService.ExecuteCopilotAsyncV2({
  message: JSON.stringify({ query: "monthly sales" }),
  notificationUrl: "https://notificationurlplaceholder",
  agentName: "cr3e1_dataAnalyzer"
});

if (response.data.responses && response.data.responses.length > 0) {
  // Parse the JSON response
  const parsedData = JSON.parse(response.data.responses[0]);
  const summary = parsedData.summary;
  const metrics = parsedData.metrics;

  console.log("Summary:", summary);
  console.log("Metrics:", metrics);
}
```

## Troubleshooting

If you encounter issues connecting to or invoking a Copilot Studio agent, the following solutions address the most common problems.

### Agent doesn't return a response

**Solution:** Make sure you're using the `ExecuteCopilotAsyncV2` operation (`/proactivecopilot/executeAsyncV2`). Other endpoints have known limitations:

- `ExecuteCopilot` (`/execute`) - Only returns `ConversationId`, not the response (fire-and-forget).
- `ExecuteCopilotAsync` (`/executeAsync`) - Might return 502 "Cannot read server response" errors.

### Property casing errors in response

**Solution:** Response property casing might vary between implementations. Check for all variations:

- `conversationId`
- `ConversationId`
- `conversationID`

Use optional chaining or check for multiple casing variations.

```typescript
const convId = response.data.conversationId ??
               response.data.ConversationId ??
               response.data.conversationID;
```

### Agent returns empty or unexpected responses

**Solution:** Verify that:

1. You published your agent in Copilot Studio.
1. The agent name is correct and matches the published agent.
1. The message format matches what your agent expects.
1. Your agent has topics configured to handle the input.


## See also

- [Connect your code app to data](connect-to-data.md)
- [Microsoft Copilot Studio documentation](/microsoft-copilot-studio/)
- [Power Platform connectors reference](/connectors/connector-reference/)
