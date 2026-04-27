---
title: "How to: Add a Dataverse action or function to your code app"
description: "Learn how to add Dataverse actions and functions to a Power Apps code app using the CLI"
ms.author: pakempar
author: pavankm
ms.date: 04/07/2026
ms.topic: how-to
ms.reviewer:
 - JimDaly
---

# How to: Add a Dataverse action or function to your code app

This guide shows you how to discover and add Dataverse operations (actions and functions)
to a Power Apps code app by using the `find-dataverse-api` and `add-dataverse-api` CLI commands.

> [!NOTE]
> This feature is available only in the latest npm CLI (preview), not in the classic Power Apps CLI (pac CLI).
> For more information, see [Quickstart with npm CLI](npm-quickstart.md).

## Prerequisites

- A Power Apps code app initialized with `npx power-apps init`
- `@microsoft/power-apps` version `1.1.1` or later in your `package.json`
- Authenticated CLI session (`npx power-apps` prompts if needed)
- Access to the Dataverse environment containing the operation you want to use

## Step 1: Discover available operations

Use `find-dataverse-api` to search for operations in your environment by name:

```bash
npx power-apps find-dataverse-api --search "WhoAmI"
```

The output lists matching operations with their kind (Action or Function), parameters, binding
entity (if any), and return type:

```
====================================================================================================
Dataverse Operations
====================================================================================================

  WhoAmI  (Function)
  Returns: mscrm.WhoAmIResponse

----------------------------------------------------------------------------------------------------
Total: 1 operation(s)
====================================================================================================
```

You can also search for actions. For example, to find the `AddToQueue` action:

```bash
npx power-apps find-dataverse-api --search "AddToQueue"
```

```
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

To get the raw JSON (useful for scripting and for coding agents), add `--json`:

```bash
npx power-apps find-dataverse-api --search "WhoAmI" --json
```

The search is a case-insensitive substring match on the operation name.

## Step 2: Add the operation to your app

After you find the operation name, run the following command:

```bash
npx power-apps add-dataverse-api --api-name WhoAmI
# or using the short alias:
npx power-apps add-dataverse-api -n WhoAmI
```

The command:

1. Fetches the operation definition from your environment's Dataverse `$metadata`.
1. Writes a schema file at `<schemaPath>/dataverse/WhoAmI.Schema.json`.
1. Saves schema files for any Dataverse entities referenced by the operation's parameters or return
   type (skips if they already exist).
1. Updates `power.config.json`:
   - Adds `databaseReferences["default.cds"]` if not already present.
   - For bound operations, adds the binding entity to `dataSources` if not already present.
1. Regenerates `dataSourcesInfo.ts` to include the new operation.
1. Generates a TypeScript model and service class under `<codeGenPath>/generated/`.

On success, you see:

```
Dataverse API 'WhoAmI' added successfully.
Hint: Run 'npx power-apps run' to test locally, or 'npx power-apps push' to deploy.
```

## Step 3: Use the generated service in your app code

The command generates a dedicated `<ApiName>Service` class for the operation. For example,
after adding `WhoAmI`, import `WhoAmIService` from the generated services directory:

```typescript
import { WhoAmIService } from './generated/services/WhoAmIService';
```

The service exposes a typed static method named after the operation. For example:

```typescript
const result = await WhoAmIService.WhoAmI();
// result.value contains: { BusinessUnitId: string, UserId: string, OrganizationId: string }
```

For a bound action such as `AddToQueue`, the first argument is always the GUID of the record
to operate on:

```typescript
import { AddToQueueService } from './generated/services/AddToQueueService';

const result = await AddToQueueService.AddToQueue(
  queueId,    // string (GUID of the destination queue)
  target,     // Record<string, unknown> (the activity to add)
  sourceQueue,         // Record<string, unknown> | undefined
  queueItemProperties  // Record<string, unknown> | undefined
);
// result.value contains: { QueueItemId: string }
```

Parameter and return types come from the Dataverse schema:

- GUID parameters are typed as `string`.
- Lookup parameters that reference a Dataverse entity are typed as `Record<string, unknown>`.
- Operations with no return value produce `Promise<IOperationResult<void>>`.
- Operations that return a scalar (for example, `boolean`, `number`) produce
  `Promise<IOperationResult<T>>` with the corresponding TypeScript type.
- Operations that return a complex type or entity produce `Promise<IOperationResult<Record<string, unknown>>>`.

## Rerun for the same operation

Running `add-dataverse-api` again with the same `--api-name` is safe and idempotent:

- The command overwrites the schema file with the latest definition from Dataverse.
- It regenerates `dataSourcesInfo.ts`.
- It removes duplicate entries in `power.config.json` - it doesn't add duplicates.
- It doesn't overwrite entity schema files that already exist.

Use this command to pick up changes to an operation's signature after an update in the
environment.

## Files created or modified

The `add-dataverse-api` command creates or updates the following files in your project:

| File                                                   | What changes                                                           |
| ------------------------------------------------------ | ---------------------------------------------------------------------- |
| `<schemaPath>/dataverse/<ApiName>.Schema.json`         | Created or overwritten - operation schema                                |
| `<schemaPath>/dataverse/<EntityName>.Schema.json`      | Created (skipped if already exists) - schemas for referenced entities    |
| `<schemaPath>/appschemas/dataSourcesInfo.ts`           | Regenerated to include the new operation                               |
| `power.config.json`                                    | Updated with `default.cds` reference and (if bound) the binding entity |
| `<codeGenPath>/generated/models/<EntityName>Model.ts`  | Generated TypeScript models for referenced entity data sources         |
| `<codeGenPath>/generated/services/<ApiName>Service.ts` | Generated service class (one file per operation)                       |

## Bound vs. unbound operations

**Bound operations** are scoped to a specific entity record. The generated method always takes an
`id: string` parameter as its first argument, which is the GUID of the record to operate on.

**Unbound operations** are environment-wide and do not require a record ID. Their methods take
only the declared parameters.

Both kinds are added with the same command—the CLI detects the operation type automatically.

## Troubleshooting

**"No operations found"**—the search is substring-based and case-insensitive, but only matches
the operation name. Try a shorter or different term. Use `--json` to confirm the raw response.

**Stale generated files**—if you renamed or removed an operation and the old generated files
remain, delete them manually and rerun `add-dataverse-api` to regenerate.

**`pac code add-data-source` skips the action or function**—the schema files
generated by `add-dataverse-api` use a `Microsoft.PowerApps/dataverseOperation` type that is not
recognized by the PAC CLI. If any operation schema files are present in the Dataverse schema
folder, `pac code add-data-source` skips them with:

```
Skipping unsupported Dataverse operation schema '...AddRecurrence.Schema.json':
```

This behavior means the PAC CLI doesn't support the `Microsoft.PowerApps/dataverseOperation`
schema type, so it skips these files instead of failing.
The PAC CLI still supports the other schema files that represent Dataverse entity data sources or
connectors, and you can add them by using `pac code add-data-source`.

## Related articles

[Use Web API actions](../../data-platform/webapi/use-web-api-actions.md)   
[Use Web API functions](../../data-platform/webapi/use-web-api-functions.md)
