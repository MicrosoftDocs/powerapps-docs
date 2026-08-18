---
title: Add Power Automate flows to a code app
description: Learn how to discover, add, call, update, and remove Power Automate flows in a Power Apps code app by using the Power Apps CLI.
#customer intent: As a developer, I want to call Power Automate flows from my Power Apps code app.
ms.topic: how-to
ms.service: powerapps
ms.subservice: code-apps
ms.author: jordanchodak
ms.reviewer: jdaly
author: jordanchodakWork
ms.date: 08/13/2026
---

# Add Power Automate flows to a code app

This article shows you how to discover, add, call, update, and remove Power Automate cloud flows in a Power Apps code app by using the Power Apps CLI.

> [!IMPORTANT]
> Code apps support only solution-aware instant flows that use the Power Apps trigger. Scheduled flows, automated flows, and instant flows that use other triggers aren't supported.

## Prerequisites

- A Power Apps code app initialized with [`pa app init`](../reference/cli.md#pa-app-init)
- A solution-aware instant cloud flow that uses the Power Apps trigger
- `@microsoft/power-apps` version 1.1.1 or later

If the flow isn't in a solution, see [Add an existing cloud flow to a solution](/power-automate/create-flow-solution).

## Step 1: List available flows

Use the [`pa app list-flows`](../reference/cli.md#pa-app-list-flows) command to list the solution-aware flows in the current environment:

```bash
pa app list-flows
```

This command returns the available flows:

```console
Name                    Status   Modified On   Flow ID
──────────────────────────────────────────────────────────────────────────────
Approval Workflow       Started  2026-01-15    a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1
Send Notification       Started  2026-02-01    b1b1b1b1-cccc-dddd-eeee-f2f2f2f2f2f2

Total flows: 2
```

To filter the results by name, use the `--search` parameter:

```bash
pa app list-flows --search approval
```

Copy the **Flow ID** for the flow you want to add.

> [!NOTE]
> The command lists only solution-aware flows. If a flow isn't listed, add it to a solution first.

## Step 2: Add the flow

Use the [`pa app add flow`](../reference/cli.md#pa-app-add-flow) command to add the flow to the code app:

```bash
pa app add flow --flow-id <flow-id>
```

For example:

```bash
pa app add flow --flow-id a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1
```

Running the command again with the same flow ID updates the generated files with the latest flow definition.

### What the command does

The command:

- Downloads the flow's OpenAPI definition.
- Generates strongly typed TypeScript models and services.
- Adds the flow and its connection references to `power.config.json`.

> [!IMPORTANT]
> The person who runs [`pa app add flow`](../reference/cli.md#pa-app-add-flow) must have access to the flow and its underlying connections. The command fails if the person doesn't have access to a required connection.

### Generated files

The CLI creates files similar to the following example:

```text
src/
  services/
    ApprovalWorkflowService.ts
  models/
    ApprovalWorkflowModel.ts
schemas/
  logicflows/
    ApprovalWorkflow.Schema.json
```

The CLI also adds the flow configuration to `power.config.json`.

## Step 3: Call the flow

The generated service class provides a static `Run` method. The method signature is based on the input parameters in the flow's OpenAPI definition.

### Flow with input parameters

```typescript
import { ApprovalWorkflowService } from './services/ApprovalWorkflowService';

const result = await ApprovalWorkflowService.Run({
  requester: 'Alex',
  amount: 1500,
});

if (result.success) {
  console.log('Flow triggered. Response:', result.data);
} else {
  console.error('Flow failed:', result.error);
}
```

### Flow without input parameters

```typescript
import { SendNotificationService } from './services/SendNotificationService';

const result = await SendNotificationService.Run();

if (result.success) {
  console.log('Flow triggered.');
}
```

The result contains the following properties:

| Property | Type | Description |
| --- | --- | --- |
| `success` | `boolean` | Indicates whether the flow was triggered successfully. |
| `data` | Varies | Contains the typed response from the flow, if available. |
| `error` | `Error` | Contains error information when `success` is `false`. |

Open the generated service file to review the exact input and output types for the flow.

## Update a flow

If the flow definition changes, run [`pa app add flow`](../reference/cli.md#pa-app-add-flow) again with the same flow ID:

```bash
pa app add flow --flow-id a1b2c3d4-e5f6-7890-abcd-ef1234567890
```

The command updates the generated files and preserves the existing flow entry in `power.config.json`.

## Remove a flow

Use [`pa app remove flow`](../reference/cli.md#pa-app-remove-flow) to remove a flow by its data source name:

```bash
pa app remove flow --flow-name ApprovalWorkflow
```

Or remove it by its flow ID:

```bash
pa app remove flow --flow-id a1b2c3d4-e5f6-7890-abcd-ef1234567890
```

The command removes the flow from `power.config.json` and regenerates the models and services.

## Run and publish the app

Run the app locally:

```bash
npm run dev
```

Build the app, and then use [`pa app push`](../reference/cli.md#pa-app-push) to publish it:

```bash
npm run build
pa app push
```

## Limitations and considerations

| Limitation | Details |
| --- | --- |
| Power Apps trigger required | Only instant flows that use the Power Apps trigger are supported. |
| Solution-aware flows required | The flow must belong to a solution before you can add it. |
| Maker access required | The person adding the flow must have access to the flow and its underlying connections. |
| Dataverse permissions required | End users need sufficient Dataverse permissions to invoke the flow. Assign the App Opener security role or an equivalent role. |
| Manual update required | Run [`pa app add flow`](../reference/cli.md#pa-app-add-flow) again after the flow definition changes. |

## Related information

- [Quickstart: Create a code app using the Power Apps CLI](create-an-app-from-scratch.md)
- [Power Apps CLI command reference](../reference/cli.md)
- [Create a cloud flow in a solution](/power-automate/create-flow-solution)
- [Configure user security in an environment](/power-platform/admin/database-security)
