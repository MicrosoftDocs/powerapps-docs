---
title: "Troubleshoot adding a data source (preview)"
description: "Learn how to troubleshoot issues when errors occur while adding a datasource using the PAC CLI pac code add-data-source command."
ms.author: jordanchodak
author: jordanchodakWork
ms.date: 10/14/2025
ms.reviewer: jdaly
ms.topic: article
contributors:
 - JimDaly
---
# Troubleshoot adding a data source (preview)

This article provides troubleshooting steps for when the PAC CLI (Power Apps Command Line Interface)  [pac code add-data-source](/power-platform/developer/cli/reference/code#pac-code-add-data-source) command fails.

## Symptoms

When you use the PAC CLI to add a data source, it might fail. These failures aren't usually caused by a problem in the PAC CLI. Failures usually happen because something on your computer or network is blocking the connection or messing up authentication.

## Cause

There are two potential causes of this issue:

### Cause 1: Network security

Firewalls, proxies, or other network security components might be blocking the network calls made by the `pac.exe` process.

### Cause 2: Authentication issues

The authentication context used by the CLI might not have sufficient permissions, or it might be affected by conditional access policies.

## Troubleshooting steps

To diagnose the root cause, follow these steps:

### Step 1: Verify browser connectivity

This step helps confirm that your user account has the correct permissions and that the data source is reachable from your computer.

1. Open a web browser on the same computer where you're using the PAC CLI.
1. Navigate directly to the data source you're trying to add. For example, the SharePoint site or the Dataverse environment URL.
1. Sign in with the **same credentials** you used to authenticate with the PAC CLI [pac auth create](/power-platform/developer/cli/reference/auth#pac-auth-create) command
1. If you can't access the resource, a permissions issue with your user account is the likely root cause.
1. If you can access it, move to Step 2.

### Step 2: Analyze network traffic

This is the most effective way to see the raw network communication data between the PAC CLI and the data source endpoint.

1. Download and install [Fiddler Classic](https://www.telerik.com/fiddler/fiddler-classic). Fiddler is tool to monitor network traffic.
1. Start Fiddler and ensure it's capturing traffic. Go to **File** > **Capture Traffic**.
1. In a command prompt, run the failing `pac code add-data-source` command.
1. In the Fiddler session list, look for requests made to your data source endpoint. For example: `yourorg.crm.dynamics.com` or `yourtenant.sharepoint.com`.
1. Analyze the response information:

    - A `200` status code indicates success.
    - A `401` (Unauthorized) or `403` (Forbidden) status code points to an authentication or permission issue.
    - Other error codes or a complete lack of response can indicate that a firewall or proxy is blocking the request.
