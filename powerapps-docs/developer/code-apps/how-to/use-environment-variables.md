---
title: "How to: Use environment variables in code app data sources"
description: "Learn how to reference Power Platform environment variables when adding data sources to a code app"
ms.author: pakempar
author: pavankm
ms.date: 03/31/2026
ms.topic: how-to
ms.reviewer: jdaly
---
# How to: Use environment variables in code app data sources

Use environment variables in your data source configuration so your code app can move between environments without hardcoding dataset or table values.

## Why use environment variables?

When you reference environment variables in `pac code add-data-source`, your app configuration stores the variable reference. The app then resolves actual values from the target environment.

This approach helps with application lifecycle management (ALM) across Dev, Test, and Prod.

## Prerequisites

- A code app initialized by using [pac code init](/power-platform/developer/cli/reference/code#pac-code-init)
- A connection already created in Power Apps
- Environment variables created in your solution

For guidance on creating environment variables, see [Use environment variables in Power Platform solutions](../../../maker/data-platform/environmentvariables.md).

## Add a data source by using environment variable references

Use the environment variable schema names prefixed with `@envvar:` for tabular arguments such as dataset and table.

```powershell
pac code add-data-source --apiid shared_sharepointonline --connectionId <your_connection_id> --dataset "@envvar:crd1b_SharepointSiteVar" --table "@envvar:crd1b_sharepointList"
```

In this example:

- `crd1b_SharepointSiteVar` is the environment variable schema name for the SharePoint site (dataset)
- `crd1b_sharepointList` is the environment variable schema name for the SharePoint list (table)

## Verify the result

After running the command, open `power.config.json` in your code app.

You should see the `@envvar:` references persisted in the data source configuration. This behavior means that when you move the app to another environment, it uses the values configured for those environment variables in that environment.
