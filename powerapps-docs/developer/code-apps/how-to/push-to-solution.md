---
title: Push a code app into a solution from the CLI (preview)
description: Use the power-apps push command to add your code app to a Dataverse solution for healthy application lifecycle management (ALM).
ms.date: 07/20/2026
ms.topic: how-to
ms.collection: bap-ai-copilot
author: jordanchodak
ms.author: jordanchodak
ms.reviewer: jdaly
---

# Push a code app into a solution (preview)

Starting with [Power Apps client library for code apps](https://www.npmjs.com/package/@microsoft/power-apps) version **1.2.7**, the npm-based CLI can automatically place your app inside a Dataverse solution when you run `power-apps push`.

Putting an app in a solution is what makes it portable across environments (dev to test to prod) through standard application lifecycle management (ALM): export the solution from one environment and import it into another, and your app comes along with it. For more information, see [How to: Application Lifecycle Management (ALM) for code apps](alm.md).

With this behavior you can:

- Let the CLI pick the right solution automatically on the first push, so you get sensible ALM behavior with zero configuration.
- Target a specific solution by its ID, on any push.
- Deploy safely to environments without Dataverse. The app still pushes, just without a solution.

The behavior is identical whether you run interactively or in an automated pipeline, so what you test locally is exactly what runs in continuous integration and continuous delivery (CI/CD).

## Prerequisites

- An initialized Power Apps code app. See [Quickstart: Create a code app from scratch by using the new npm CLI (preview)](npm-quickstart.md).
- To add the app to a solution, a Power Platform environment with Dataverse. In environments without Dataverse, the app deploys without a solution.

## Usage

Run the command from the root of your code app project.

Push your app and let the CLI choose the best solution for you on the first push:

```bash
power-apps push
```

Push your app into a specific solution:

```bash
power-apps push --solution-id <id>
```

The CLI prints which solution it used (or explains why it didn't use one) before the upload begins.

### Options

| Option | Alias | Required | Description |
|---|---|---|---|
| `--solution-id` | `-s` | No | The ID (GUID) of the solution to add the app to. You can also set it with the `SOLUTION_ID` environment variable. If omitted, the CLI selects a solution automatically. |

### To find a solution ID

1. In [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc)
1. Open **Solutions** and select your solution
1. Copy the ID from the URL: 

   `https://make.powerapps.com/environments/<environment ID>/solutions/<copy this solution ID>/overview`

## How automatic solution selection works

When you omit `--solution-id`, the CLI's behavior depends on whether this is the first push of the app or a subsequent one.

### First push

When the app doesn't exist in the environment yet, the CLI resolves a target solution in this order:

1. **Preferred solution**: If the environment has Dataverse enabled, the CLI uses your preferred solution. If you don't explicitly set a preferred solution, Dataverse defaults to the [Common Data Service Default Solution](../../../maker/data-platform/solutions-overview.md#default-solutions). 

   The CLI confirms: `Adding the app to your preferred solution.`

   > [!TIP]
   > For predictable ALM, set a preferred solution on your environment. Then every first push lands your apps in the solution you expect, without needing the `--solution-id` flag. [Learn how to set your preferred solution](../../../maker/data-platform/preferred-solution.md)

1. **Default solution**: If no preferred solution is available, the CLI falls back to the all-components Default solution.

   The CLI confirms: `No preferred solution found; adding the app to the Default solution.`

1. **No solution**: If Dataverse isn't enabled, or no solution can be resolved, the app is pushed without a solution. The deployment still succeeds.

   When Dataverse isn't enabled, the CLI confirms: `Dataverse is not enabled in this environment; pushing the app without a solution.`
   
   When no solution is found, the CLI confirms: `No preferred or Default solution was found; pushing the app without a solution.`

### Subsequent pushes

When the app already exists, the following rules apply:

- **Without `--solution-id`**: the CLI leaves the app's existing solution membership untouched. Your updates deploy without changing which solutions the app belongs to.
- **With `--solution-id`**: the CLI adds the app to that solution. This action works on every push, so you can add an existing app to an additional solution at any time - not just on the first deploy.

## Target a specific solution explicitly

Passing `--solution-id` always takes precedence over automatic selection:

```bash
power-apps push --solution-id <id>
```

The CLI confirms: `Adding the app to solution 'id'.`

The CLI validates the solution ID value before uploading anything, so mistakes fail fast with a clear message and never leave a half-deployed app:

| Problem | Error message |
|---|---|
| Not a GUID | `Invalid --solution-id value: expected a GUID, got '<value>'.` |
| Solution doesn't exist in the environment | `Solution '<id>' was not found in environment '<env>'.` |
| Environment has no Dataverse | `Cannot add the app to a solution because Dataverse is not enabled in environment '<env>'. Re-run 'power-apps push' without --solution-id.` |

## Use solution targeting in CI/CD

Because the behavior is identical interactively and in automation, you can drive solution targeting from a build pipeline with the `SOLUTION_ID` environment variable:

```bash
SOLUTION_ID=<id> power-apps push
```

This approach is deterministic, non-interactive, and identical to the local experience.

## Limitations

- You must target a solution by its ID (GUID). Solution names aren't accepted. Use the maker portal or the CLI's solution listing commands to look up the ID for a friendly name.
- At this time, code apps don't support source code integration.
