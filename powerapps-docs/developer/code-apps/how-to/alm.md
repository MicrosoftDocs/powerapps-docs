---
title: "How to: Application Lifecycle Management (ALM) for code apps"
description: "Learn best practices for ALM with Power Apps code apps."
ms.author: jordanchodak
author: jordanchodakWork
ms.date: 10/15/2025
ms.reviewer: 
ms.topic: how-to
contributors:

---

# How to: Application Lifecycle Management (ALM) for code apps (preview)

Application Lifecycle Management (ALM) is the process of managing the lifecycle of an application from initial planning through development, deployment, and ongoing maintenance. ALM for code apps builds on the same principles used throughout the Power Platform, extending them to scenarios where custom code is part of the solution.

For code apps, ALM ensures: 
- Consistency across environments: Move apps seamlessly from development to production. 
- Governance and compliance: Enforce organizational standards and security policies. 
- Predictable deployments: Reduce risk and improve reliability. 

## Steps

After deploying a code app to an environment with the `pac code push` command, you should add the app to a solution via the Power Apps UI. Here are the steps to do so:

1. Go to **make.powerapps.com**.
2. Navigate to **Solutions**.
3. Select **Add existing** -> **App** -> **Code app** and select the app you want to add.
4. Deploy your solution via pipelines. For how to use pipelines in the Power Platform, go [here](/power-platform/alm/pipelines).

## Limitations

- Code apps are not yet saved to a solution by default.
- Code apps do not yet support use of [solution packager](/power-platform/alm/solution-packager-tool).
- Code apps do not yet support source code integration.
