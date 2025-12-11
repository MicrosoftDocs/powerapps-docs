---
title: "How to: Application Lifecycle Management (ALM) for code apps"
description: "Learn best practices for ALM with Power Apps code apps."
ms.author: jordanchodak
author: jordanchodakWork
ms.date: 12/11/2025
ms.reviewer: jdaly
ms.topic: how-to
contributors:
- JimDaly
---

# How to: Application Lifecycle Management (ALM) for code apps (preview)

Application Lifecycle Management (ALM) is the process of managing the lifecycle of an application from initial planning through development, deployment, and ongoing maintenance. ALM for code apps builds on the same principles used throughout the Power Platform, extending them to scenarios where custom code is part of the solution.

For code apps, ALM ensures:

- Consistency across environments: Move apps seamlessly from development to production.
- Governance and compliance: Enforce organizational standards and security policies.
- Predictable deployments: Reduce risk and improve reliability.

## Prerequisites

- A Power Platform environment with Dataverse
- [Power Platform CLI (PAC)](/power-platform/developer/cli/introduction?tabs=windows) installed. Check that you have the latest version.
- A non‑default solution for your work (and ideally, set it as the preferred solution)

## Save to your preferred solution by default

If your environment has a preferred solution configured, new apps now save to that solution by default when deployed with [pac code push](/power-platform/developer/cli/reference/code#pac-code-push). This enables healthy ALM from day one by avoiding default solutions. 

Learn more about why preferred solutions matter and how to set them up: [Set a preferred solution](/power-apps/maker/data-platform/preferred-solution)

## Add to a specific solution

To target a specific solution (rather than the preferred solution), use the [`-s` parameter](/power-platform/developer/cli/reference/code#pac-code-push) when pushing your app:

```shell
pac code push -s <solutionName>
```

## Add to a solution in Power Apps UI

If you've already deployed your code app to an environment with the [pac code push](/power-platform/developer/cli/reference/code#pac-code-push) command, add it to a solution in Power Apps:

1. Go to [Power Apps](https://make.powerapps.com).
2. Navigate to **Solutions**.
3. Select **Add existing** -> **App** -> **Code app** and select the app you want to add.

## Deploy using Pipelines

Once the app is in a solution, use Power Platform Pipelines to deploy across stages (Dev → Test → Prod) with preflight checks for dependencies, connection references, and more.

[Learn how to use pipelines in the Power Platform](/power-platform/alm/pipelines).

## Limitations

At this time, Code apps:

- Don't support use of [solution packager](/power-platform/alm/solution-packager-tool).
- Don't support [source code integration](/power-platform/alm/git-integration/overview).
