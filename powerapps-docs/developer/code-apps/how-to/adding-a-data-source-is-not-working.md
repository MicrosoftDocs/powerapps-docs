---
title: Adding a data source is not working
description: Provides troubleshooting steps to an issue in which pac code add-data-source is not working.
ms.author:  jordanchodak
author: jordanchodakWork
ms.date: 10/14/2025
ms.reviewer: 
---

# Adding a data source to your code app is not working

This article provides troubleshooting steps for when the `pac code add-data-source` commmand fails.

## Symptoms

When you use the PAC CLI (Power Apps Command Line Interface) to add a data source, it sometimes fails. These failures usually aren’t caused by a bug in the CLI itself. Instead, they happen because something on your computer or network is blocking the connection or messing up authentication.

## Cause

There are two potential causes of this issue:

### Cause 1: Network security

Firewalls, proxies, or other network security components may be blocking the network calls made by the `pac.exe` process.

### Cause 2: Authentication issues

The authentication context used by the CLI may not have sufficient permissions, or it may be affected by conditional access policies.

## Troubleshooting steps

To diagnose the root cause, please follow these steps:

### Step 1

This helps confirm that your user account has the correct permissions and that the data source is reachable from your machine.

1. Open a web browser on the same machine where you are using the PAC CLI.

2. Navigate directly to the data source you are trying to add (e.g., the SharePoint site or the Dataverse environment URL).

3. Log in with the **same credentials** you used to authenticate with the PAC CLI (`pac auth create`).

4. If you cannot access the resource, there is likely a permissions issue with your user account.

5. If you can access it, move to Step 2. 

### Step 2

This is the most effective way to see the raw network communication between the PAC CLI and the data source endpoint.

1. Download and install **Fiddler Classic** (a tool to monitor network traffic). 

2. Start Fiddler and ensure it is capturing traffic (go to `File > Capture Traffic`).

3.  In a command prompt, run the `pac code add-data-source` command that is failing.

4. In the Fiddler session list, look for requests made to your data source endpoint (e.g., `yourorg.crm.dynamics.com` or `yourtenant.sharepoint.com`), and analyze the response.

    - A `200` status code indicates success.
    
    - A `401` (Unauthorized) or `403` (Forbidden) status code points to an authentication or permission issue.
    
    - Other error codes or a complete lack of response can indicate that a firewall or proxy is blocking the request.
