---
title: "Troubleshoot adding a data source (preview)"
description: "Power Apps code apps architecture during development and runtime"
ms.author: jordanchodak
author: jordanchodakWork
ms.date: 10/14/2025
ms.reviewer: jdaly
ms.topic: article
contributors:
 - JimDaly
---
# Troubleshoot adding a data source (preview)

This article provides troubleshooting steps for when the PAC CLI (Power Apps Command Line Interface)  [pac code add-data-source](/power-platform/developer/cli/reference/code#pac-code-add-data-source) commmand fails.

## Symptoms

When you use the PAC CLI to add a data source, it sometimes fails. These failures usually aren't caused by a bug in the CLI itself. Instead, they happen because something on your computer or network is blocking the connection or messing up authentication.

## Cause

There are two potential causes of this issue:

### Cause 1: Network security

Firewalls, proxies, or other network security components may be blocking the network calls made by the `pac.exe` process.

### Cause 2: Authentication issues

The authentication context used by the CLI may not have sufficient permissions, or it may be affected by conditional access policies.

## Troubleshooting steps

To diagnose the root cause, follow these steps:

### Step 1

This step helps confirm that your user account has the correct permissions and that the data source is reachable from your machine.

1. Open a web browser on the same machine where you are using the PAC CLI.
1. Navigate directly to the data source you are trying to add. For example the SharePoint site or the Dataverse environment URL.
1. Log in with the **same credentials** you used to authenticate with the PAC CLI [pac auth create](/power-platform/developer/cli/reference/auth#pac-auth-create) command
1. If you cannot access the resource, a permissions issue with your user account is the likely root cause.
1. If you can access it, move to Step 2.

### Step 2

This is the most effective way to see the raw network communication data between the PAC CLI and the data source endpoint.

1. Download and install [Fiddler Classic](https://www.telerik.com/fiddler/fiddler-classic) (a tool to monitor network traffic).
1. Start Fiddler and ensure it is capturing traffic. Go to **File** > **Capture Traffic**.
1. In a command prompt, run the `pac code add-data-source` command that is failing.
1. In the Fiddler session list, look for requests made to your data source endpoint. For example `yourorg.crm.dynamics.com` or `yourtenant.sharepoint.com`.
1. Analyze the response information:

    - A `200` status code indicates success.
    - A `401` (Unauthorized) or `403` (Forbidden) status code points to an authentication or permission issue.
    - Other error codes or a complete lack of response can indicate that a firewall or proxy is blocking the request.
