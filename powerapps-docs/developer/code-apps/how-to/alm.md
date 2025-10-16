---
title: "How to: Application Lifecycle Management (ALM) for code apps"
description: "Learn best practices for ALM with Power Apps code apps."
ms.author: jordanchodak
author: jordanchodakWork
ms.date: 10/16/2025
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

## Steps

After deploying a code app to an environment with the [pac code push](/power-platform/developer/cli/reference/code#pac-code-push) command, you should add the app to a solution using the Power Apps UI. Use these steps

1. Go to [Power Apps](https://make.powerapps.com).
2. Navigate to **Solutions**.
3. Select **Add existing** -> **App** -> **Code app** and select the app you want to add.
4. Deploy your solution via pipelines. [Learn how to use pipelines in the Power Platform](/power-platform/alm/pipelines).

## Limitations

At this time, Code apps:

- Aren't saved to a solution by default.
- Don't support use of [solution packager](/power-platform/alm/solution-packager-tool).
- Don't support [source code integration](/power-platform/alm/git-integration/overview).
