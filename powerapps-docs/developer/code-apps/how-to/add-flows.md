---
title: Add Power Automate flows to a code app (preview)
description: Learn how to discover, add, invoke, and remove Power Automate cloud flows from a Power Apps code app by using the npm CLI.
#customer intent: As a Power Apps code apps developer, I want to add Power Automate cloud flows to my code app.
author: eschavez
ms.author: eschavez
ms.reviewer: jdaly
ms.date: 04/20/2026
ms.topic: how-to
---
# Add Power Automate flows to a code app (preview)

This article shows you how to discover, add, invoke, and remove Power Automate cloud flows from a Power Apps code app by using the npm CLI.

> [!IMPORTANT]
> Only **Manual** flows that use the **PowerApps trigger** are supported. You can't add flows with other trigger types to a code app. These unsupported trigger types include scheduled, automated, or instant flows with non-PowerApps triggers.

## Prerequisites

- An initialized Power Apps code app. See [Quickstart: Create a code app by using the npm CLI](./npm-quickstart.md).
- A Power Automate flow that's **solution-aware** and is an instant flow with the **PowerApps** trigger type. If your flow isn't in a solution yet, see [Add an existing flow to a solution](/power-automate/create-flow-solution).
- The [`@microsoft/power-apps`](https://www.npmjs.com/package/@microsoft/power-apps) npm package version **1.1.1** or later.

> [!NOTE]
> Flow commands are only available in the npm-based CLI (`npx power-apps`). They're **not** available in the Power Platform CLI (`pac code`) commands.

## Step 1: List available flows

Run the following command to list all solution-aware flows in your current environment:

```bash
npx power-apps list-flows
```

The command outputs a table of available flows:

```
Name                    Status   Modified On   Flow ID
──────────────────────────────────────────────────────────────────────────────
Approval Workflow       Started  2026-01-15    a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1
Send Notification       Started  2026-02-01    b1b1b1b1-cccc-dddd-eeee-f2f2f2f2f2f2

Total flows: 2
```

> [!NOTE]
> Only solution-aware flows are listed. If you are missing a flow, see: [Create a cloud flow in a solution](/power-automate/create-flow-solution)

To filter results by name, use the `--search` option:

```bash
npx power-apps list-flows --search approval
```

Copy the **Flow ID** value for the flow you want to add.

## Step 2: Add a flow to your code app

Run the following command, replacing `<flow-id>` with the value from the previous step:

```bash
npx power-apps add-flow --flow-id <flow-id>
```

**Example:**

```bash
npx power-apps add-flow --flow-id a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1
```

When the command succeeds, the CLI confirms the flow was added:

```
Flow added successfully.
```

> [!TIP]
> Re-running `add-flow` with the same flow ID is idempotent. Use it to pick up changes to the flow's definition (new parameters, updated connections, and so on) without manually cleaning up old files.

### What `add-flow` does

The command downloads the flow's OpenAPI definition, generates strongly-typed TypeScript files in your project, and updates `power.config.json` with the flow's connection references.

> [!IMPORTANT]
> The person running `add-flow` must have access to **read the flow** and to the flow's **underlying connections** (for example, an Office 365 Outlook connection). If access to a required connection is missing, the command fails with an authorization error.

### Generated files

After running `add-flow`, the CLI creates the following files in your project (file names are derived from the flow's display name):

```
src/
  services/
    ApprovalWorkflowService.ts   ← generated service class with typed methods
  models/
    ApprovalWorkflowModel.ts     ← generated TypeScript types for inputs/outputs
schemas/
  logicflows/
    ApprovalWorkflow.Schema.json ← flow's OpenAPI schema (do not edit manually)
```

The following entry is also added to `power.config.json`:

```json
"<uuid>": {
  "id": "/providers/microsoft.powerapps/apis/shared_logicflows",
  "displayName": "Logic flows",
  "dataSources": ["ApprovalWorkflow"],
  "workflowDetails": {
    "workflowEntityId": "<dataverse-entity-guid>",
    "workflowDisplayName": "Approval Workflow",
    "workflowName": "<flow-id>",
    "dependencies": {
      "shared_office365": "<dependency-uuid>"
    }
  }
}
```

## Step 3: Call the flow from your app

The generated service class exposes a `Run` static method. The exact signature depends on whether the flow's trigger defines input parameters.

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

### Flow with no input parameters

```typescript
import { SendNotificationService } from './services/SendNotificationService';

const result = await SendNotificationService.Run();

if (result.success) {
  console.log('Flow triggered.');
}
```

The `result` object has the following shape:

| Property  | Type               | Description                                        |
| --------- | ------------------ | -------------------------------------------------- |
| `success` | `boolean`          | `true` if the flow was triggered successfully.     |
| `data`    | (varies)           | Typed response payload from the flow, if any.      |
| `error`   | `Error` (optional) | Error details when `success` is `false`.           |

> [!NOTE]
> The exact input and output types are determined by the flow's OpenAPI definition. Open the generated service file to see the specific types for your flow. Parameters marked `x-ms-visibility: internal` with a default value are automatically inlined by the code generator and aren't exposed in the method signature.

## Updating a flow

If the flow's definition changes - for example, its author adds a new parameter or updates connection references - re-run `add-flow` with the same flow ID to pick up the latest definition and regenerate the service files:

```bash
npx power-apps add-flow --flow-id a1b2c3d4-e5f6-7890-abcd-ef1234567890
```

The command matches the flow by its `workflowEntityId` and reuses the existing UUID in `power.config.json`, so no manual cleanup is required.

## Removing a flow

To remove a flow from your code app, use `remove-flow`. You can identify the flow either by its data source name (as it appears in `power.config.json`) or by its original flow ID:

**By data source name:**

```bash
npx power-apps remove-flow --flow-name ApprovalWorkflow
```

**By flow ID:**

```bash
npx power-apps remove-flow --flow-id a1b2c3d4-e5f6-7890-abcd-ef1234567890
```

The command:

- Removes the flow from `power.config.json`.
- Regenerates all model services.

## Deploying your app

After adding flows and verifying the app locally with `npm run dev`, build and deploy as usual:

```bash
npm run build
npx power-apps push
```

## Limitations and considerations

Keep the following limitations and considerations in mind when you add flows to a code app.

| Limitation | Details |
| --- | --- |
| **Manual flows with PowerApps trigger only** | Only **Manual** flows that use the **PowerApps** trigger are supported. Flows with other trigger types (scheduled, automated, or instant flows with non-PowerApps triggers) aren't supported and don't function correctly in a code app. |
| **Solution-aware flows only** | The `list-flows` command shows only flows that belong to a solution. To add a non-solution flow, [add it to a solution first](/power-automate/create-flow-solution). |
| **Maker access required** | The maker running `add-flow` must have access to the flow **and** to the flow's underlying connections. If access to a required connection is missing, the command fails. |
| **Dataverse permissions required at runtime** | End users must have sufficient Dataverse permissions to invoke flows. Assign the **App Opener** security role (or equivalent). See [Configure user security in an environment](/power-platform/admin/database-security). |
| **Manual refresh required for flow changes** | If the flow's definition changes, re-run `add-flow` with the same flow ID. The app doesn't automatically detect flow changes. |
| **npm CLI only** | These commands aren't available in `pac code`. |

## Related articles

- [Quickstart: Create a code app by using the npm CLI](./npm-quickstart.md)
- [Add a data source to a code app](../overview.md)
- [Add an existing flow to a solution](/power-automate/create-flow-solution)
- [Configure user security in an environment](/power-platform/admin/database-security)

