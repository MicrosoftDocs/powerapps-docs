---
title: "How to: Application Lifecycle Management (ALM) for code apps"
description: "Learn how to use application lifecycle management (ALM) for Power Apps code apps to target solutions and deploy reliably across environments."
ms.author: jordanchodak
author: jordanchodakWork
ms.date: 08/14/2026
ms.reviewer: jdaly
ms.topic: how-to
contributors:
- JimDaly
---

# How to: Application Lifecycle Management (ALM) for code apps

Application Lifecycle Management (ALM) is the process of managing the lifecycle of an application from initial planning through development, deployment, and ongoing maintenance. ALM for code apps builds on the same principles used throughout the Power Platform, extending them to scenarios where custom code is part of the solution.

For code apps, ALM ensures:

- **Consistency across environments**: Move apps seamlessly from development to production.
- **Governance and compliance**: Enforce organizational standards and security policies.
- **Predictable deployments**: Reduce risk and improve reliability.

## Prerequisites

- An initialized Power Apps code app. See [Quickstart: Create a code app using the Power Apps CLI](create-an-app-from-scratch.md).
- [Power Apps CLI](../reference/cli.md) installed. Check that you have the latest version.
- To add the app to a solution, a Power Platform environment with Dataverse. In environments without Dataverse, the app publishes without a solution.

## Publish to a solution

The Power Apps CLI can automatically place your app inside a Dataverse solution when you run [`pa app push`](../reference/cli.md#pa-app-push).

Putting an app in a solution makes it portable across environments through standard ALM. When you export the solution from one environment and import it into another, the app moves with it.

You can:

- Let the CLI select a solution automatically on the first publish.
- Target a specific solution by its ID on any publish.
- Publish to an environment without Dataverse. The app publishes without a solution.

The behavior is identical whether you run the command interactively or in a CI/CD pipeline.

### Publish with automatic solution selection

Run the command from the root of your code app project:

```bash
pa app push
```

The CLI reports which solution it uses or explains why it publishes the app without one.

### Publish to a specific solution

Use the `--solution-id` option to target a specific solution:

```shell
pa app push --solution-id <solution-id>
```

| Option | Alias | Required | Description |
| --- | --- | --- | --- |
| `--solution-id` | `-s` | No | The ID (GUID) of the solution to add the app to. You can also set it with the `SOLUTION_ID` environment variable. If you omit this option, the CLI selects a solution automatically. |

To find a solution ID:

1. Go to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. Open **Solutions** and select your solution.
1. Copy the solution ID from the URL:

   `https://make.powerapps.com/environments/<environment-id>/solutions/<solution-id>/overview`

## How automatic solution selection works

When you omit `--solution-id`, the CLI behavior depends on whether this is the first publish of the app or a subsequent publish.

### First publish

When the app doesn't exist in the environment, the CLI resolves a target solution in this order:

1. **Preferred solution**: If the environment has Dataverse enabled, the CLI uses the preferred solution. If you don't explicitly set one, Dataverse uses the [Common Data Service Default Solution](../../../maker/data-platform/solutions-overview.md#default-solutions).

   > [!TIP]
   > For predictable ALM, [set a preferred solution](../../../maker/data-platform/preferred-solution.md) for the environment. Every first publish then adds code apps to the expected solution without requiring `--solution-id`.

1. **Default solution**: If no preferred solution is available, the CLI uses the all-components Default solution.

1. **No solution**: If Dataverse isn't enabled or no solution can be resolved, the app publishes without a solution.

### Subsequent publishes

When the app already exists:

- **Without `--solution-id`**: The CLI doesn't change the app's existing solution membership.
- **With `--solution-id`**: The CLI adds the app to that solution. You can add an existing app to another solution on any publish.

## Target a specific solution explicitly

Passing `--solution-id` takes precedence over automatic selection:

```bash
pa app push --solution-id <solution-id>
```

The CLI validates the solution ID before uploading:

| Problem | Result |
| --- | --- |
| The value isn't a GUID | The command stops and reports that the solution ID isn't valid. |
| The solution doesn't exist in the environment | The command stops and reports that it can't find the solution. |
| The environment doesn't have Dataverse | The command stops and directs you to publish again without `--solution-id`. |

## Add to a solution in Power Apps

If you already published your code app to an environment with [`pa app push`](../reference/cli.md#pa-app-push), add it to a solution in Power Apps:

1. Go to [Power Apps](https://make.powerapps.com).
1. Navigate to **Solutions**.
1. Select the solution.
1. Select **Add existing** > **App** > **Code app** and select the app you want to add.

## Use solution targeting in CI/CD

To target a solution from a build pipeline, set the `SOLUTION_ID` environment variable:

```bash
SOLUTION_ID=<solution-id> pa app push
```

This behavior is deterministic, noninteractive, and identical to local publishing.

## Deploy using pipelines

After you add the app to a solution, use Power Platform Pipelines to deploy across stages (Dev → Test → Prod) with preflight checks for dependencies, connection references, and more.

[Learn how to use pipelines in the Power Platform](/power-platform/alm/pipelines).

## Use connection references in your code app

For information about connection references, see [Use connection references to add a data source](connect-to-data.md#use-connection-references-to-add-a-data-source).

## Limitations

At this time, code apps:

- Require a solution ID (GUID) when you explicitly target a solution. Solution names aren't accepted.
- Don't support [source code integration](/power-platform/alm/git-integration/overview).
