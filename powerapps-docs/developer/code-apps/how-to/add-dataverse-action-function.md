---
title: Add a Dataverse action or function to a code app
description: Learn how to discover and add Dataverse actions and functions to a Power Apps code app by using the Power Apps CLI.
#customer intent: As a developer, I want to call Dataverse actions and functions from my Power Apps code app.
ms.topic: how-to
ms.author: jordanchodak
ms.reviewer: jdaly
author: jordanchodakWork
ms.date: 08/13/2026
contributors:
 - pavankm
---

# Add a Dataverse action or function to your code app

This article shows you how to discover and add Dataverse actions and functions to a Power Apps code app by using the Power Apps CLI.

## Prerequisites

- A Power Apps code app initialized with [`pa app init`](../reference/cli.md#pa-app-init)
- `@microsoft/power-apps` version 1.1.1 or later in your `package.json`
- Access to the Dataverse environment that contains the operation you want to use

The CLI prompts you to sign in if you aren't already authenticated.

## Step 1: Find available operations

Use [`pa app find-dataverse-api`](../reference/cli.md#pa-app-find-dataverse-api) to search for operations by name in the environment configured for your code app:

```bash
pa app find-dataverse-api --search "WhoAmI"
```

The output lists matching operations and includes the operation type, parameters, binding table, and return type.

```console
====================================================================================================
Dataverse Operations
====================================================================================================

  WhoAmI  (Function)
  Returns: mscrm.WhoAmIResponse

----------------------------------------------------------------------------------------------------
Total: 1 operation(s)
====================================================================================================
```

This function and the return type are documented here:

- [WhoAmI function](xref:Microsoft.Dynamics.CRM.WhoAmI)
- [WhoAmIResponse complex type](xref:Microsoft.Dynamics.CRM.WhoAmIResponse)

You can also search for actions. For example:

```bash
pa app find-dataverse-api --search "AddToQueue"
```

```console
====================================================================================================
Dataverse Operations
====================================================================================================

  AddToQueue  (Action)
  Bound to: mscrm.queue
  Parameters:
    - Target: mscrm.crmbaseentity
    - SourceQueue?: mscrm.queue
    - QueueItemProperties?: mscrm.queueitem
  Returns: mscrm.AddToQueueResponse

----------------------------------------------------------------------------------------------------
Total: 1 operation(s)
====================================================================================================
```

This action, parameter types, and the types returned are documented here:

- [AddToQueue action](xref:Microsoft.Dynamics.CRM.AddToQueue)
- [crmbaseentity entity type](xref:Microsoft.Dynamics.CRM.crmbaseentity)
- [queue entity type](xref:Microsoft.Dynamics.CRM.queue)
- [queueitem entity type](xref:Microsoft.Dynamics.CRM.queueitem)
- [AddToQueueResponse complex type](xref:Microsoft.Dynamics.CRM.AddToQueueResponse)

The search uses a case-insensitive substring match on the operation name. To return JSON for scripting or coding-agent scenarios, include `--json`:

```bash
pa app find-dataverse-api --search "WhoAmI" --json
```

## Step 2: Add the operation

After you find the operation name, add it to the app:

```bash
pa app add dataverse-api --api-name WhoAmI
```

The command:

1. Gets the operation definition from the [Dataverse `$metadata` endpoint](../../data-platform/webapi/web-api-service-documents.md#csdl-metadata-document).
1. Writes the operation schema to `<schemaPath>/dataverse/<ApiName>.Schema.json`.
1. Saves schemas for Dataverse tables referenced by the operation.
1. Updates `power.config.json`.
1. Regenerates `dataSourcesInfo.ts`.
1. Generates TypeScript models and a service class under `<codeGenPath>/generated/`.

When you add the operation, the CLI returns a confirmation:

```console
Dataverse API 'WhoAmI' added successfully.
```

## Step 3: Use the generated service

The command generates an `<ApiName>Service` class for the operation. After adding `WhoAmI`, import its service:

```typescript
import { WhoAmIService } from './generated/services/WhoAmIService';
```

Call the generated method:

```typescript
const result = await WhoAmIService.WhoAmI();
// result.value contains BusinessUnitId, UserId, and OrganizationId.
```

For a [bound action](../../data-platform/webapi/use-web-api-actions.md#bound-actions) such as `AddToQueue`, the first argument is the ID of the record the action operates on:

```typescript
import { AddToQueueService } from './generated/services/AddToQueueService';

const result = await AddToQueueService.AddToQueue(
  queueId,
  target,
  sourceQueue,
  queueItemProperties
);
```

Parameter and return types are based on the Dataverse schema:

- GUID parameters use the `string` type.
- Lookup parameters that reference a Dataverse table use `Record<string, unknown>`.
- Operations without a return value use `Promise<IOperationResult<void>>`.
- Operations that return a scalar value use `Promise<IOperationResult<T>>`.
- Operations that return a complex type or table use `Promise<IOperationResult<Record<string, unknown>>>`.

## Update an operation

Run [`pa app add dataverse-api`](../reference/cli.md#pa-app-add-dataverse-api) again with the same operation name to get the latest definition:

```bash
pa app add dataverse-api --api-name WhoAmI
```

The command overwrites the operation schema, regenerates `dataSourcesInfo.ts`, removes duplicate configuration entries, and preserves existing referenced table schema files.

## Files created or updated

| File | Change |
| --- | --- |
| `<schemaPath>/dataverse/<ApiName>.Schema.json` | Creates or overwrites the operation schema. |
| `<schemaPath>/dataverse/<TableName>.Schema.json` | Creates schemas for referenced tables if they don't already exist. |
| `<schemaPath>/appschemas/dataSourcesInfo.ts` | Regenerates the data source information. |
| `power.config.json` | Adds the Dataverse reference and, for a bound operation, the binding table. |
| `<codeGenPath>/generated/models/<TableName>Model.ts` | Generates models for referenced tables. |
| `<codeGenPath>/generated/services/<ApiName>Service.ts` | Generates the service class for the operation. |

## Troubleshooting

**No operations found**

The search only matches the operation name. Try a shorter or different search term. Include `--json` to inspect the response.

**Generated files are out of date**

Run [`pa app add dataverse-api`](../reference/cli.md#pa-app-add-dataverse-api) again with the same operation name. If you renamed or removed the operation and obsolete generated files remain, delete those files before regenerating the operation.

## Related information

- [Quickstart: Create a code app using the Power Apps CLI](create-an-app-from-scratch.md)
- [Power Apps CLI command reference](../reference/cli.md)
- [Connect your code app to Dataverse](connect-to-dataverse.md)
