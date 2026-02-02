---
title: "Troubleshoot adding a data source"
description: "Learn how to troubleshoot issues when errors occur while adding a datasource using the PAC CLI pac code add-data-source command."
ms.author: jordanchodak
author: jordanchodakWork
ms.date: 11/12/2025
ms.reviewer: jdaly
ms.topic: article
contributors:
 - JimDaly
---
# Troubleshoot adding a data source

This article provides troubleshooting steps for when the PAC CLI (Power Apps Command Line Interface)  [pac code add-data-source](/power-platform/developer/cli/reference/code#pac-code-add-data-source) command fails.


## Symptoms

Failures usually happen because something on your computer or network is blocking the connection or disrupting authentication.

| Symptom                  | Example Message                           |
| ------------------------ | ----------------------------------------- |
| Fetch Failed             | `Fetch Failed` (no additional stack)      |
| Timeout / network errors | `ETIMEDOUT`, `ENOTFOUND`, `ECONNRESET`    |
| Environment mismatch     | Data source not found / unexpected schema |

## Prerequisites

1. Verify you have the [latest Power Platform CLI installed](/power-platform/developer/cli/introduction#install-microsoft-power-platform-cli). Update it if you aren't sure.
1. Verify you are authenticated to the correct environment. Use [`pac auth create`](/power-platform/developer/cli/reference/auth#pac-auth-create) and [`pac auth list`](/power-platform/developer/cli/reference/auth#pac-auth-list) commands.
1. Verify your network allows outbound HTTPS calls to Power Platform endpoints.

## Troubleshooting steps

To diagnose the root cause, follow these steps:

### Step 1: Validate configuration

Open `power.config.json` file and confirm:

- `environmentId` matches the environment you intend to target.
- `region` is set to `prod`,  unless you are intentionally targeting another region. Add it if missing.

### Step 2: Cross-check environment context

Run the [`pac env who`](/power-platform/developer/cli/reference/env#pac-env-who) command.


Compare the `Environment ID` in the output with the `environmentId` value in `power.config.json`.

Example output (annotated):

```powershell
Connected as user@domain.com
Organization Information
  Org ID:                     00aa00aa-bb11-cc22-dd33-44ee44ee44ee
  Unique Name:                unq2889ab2be728ef118406000d3a33f
  Friendly Name:              User Name
  Org URL:                    https://myorg.crm.dynamics.com/
  User Email:                 user@domain.com
  User ID:                    aaaaaaaa-bbbb-cccc-1111-222222222222
  Environment ID:             aaaabbbb-0000-cccc-1111-dddd2222eeee  <-- Ensure this matches
```

Corresponding `power.config.json` example snippet:

```json
{
  "environmentId": "aaaabbbb-0000-cccc-1111-dddd2222eeee",
  "region": "prod"
}
```

### Step 3: Re-run command

Run the [`pac code add-data-source`](/power-platform/developer/cli/reference/code#pac-code-add-data-source) command again. For example:

```cmd
pac code add-data-source -a dataverse -t account
```

Look for HTTP status codes or error messages in the output.

### Step 4: Network & security validation

If still failing:

- Confirm no corporate proxy/firewall blocks CLI processes (non-browser traffic).
- Approve required Power Platform endpoints. [Review Power Platform connectivity requirements](/power-platform/admin/online-requirements)

#### Verify browser connectivity

This step helps confirm that your user account has the correct permissions and that the data source is reachable from your computer.

1. Open a web browser on the same computer where you're using the PAC CLI.
1. Navigate directly to the data source you're trying to add. For example, the SharePoint site or the Dataverse environment URL.
1. Sign in with the **same credentials** you used to authenticate with the PAC CLI [pac auth create](/power-platform/developer/cli/reference/auth#pac-auth-create) command
1. If you can't access the resource, a permissions issue with your user account is the likely root cause.
1. If you can access it, move to [Analyze network traffic](#analyze-network-traffic).

#### Analyze network traffic

This is the most effective way to see the raw network communication data between the PAC CLI and the data source endpoint.

1. Download and install [Fiddler Classic](https://www.telerik.com/fiddler/fiddler-classic). Fiddler is tool to monitor network traffic.
1. Start Fiddler and ensure it's capturing traffic. Go to **File** > **Capture Traffic**.
1. In a command prompt, run the failing `pac code add-data-source` command.
1. In the Fiddler session list, look for requests made to your data source endpoint. For example: `yourorg.crm.dynamics.com` or `yourtenant.sharepoint.com`.
1. Analyze the response information:

    - A `200` status code indicates success.
    - A `401` (Unauthorized) or `403` (Forbidden) status code points to an authentication or permission issue.
    - Other error codes or a complete lack of response can indicate that a firewall or proxy is blocking the request.

### Step 5: Clear/Reset auth context

If a mismatch is detected, you should clear or reset the auth context using the following PAC CLI commands.

```cmd
pac auth list
pac auth select --index <n>
pac env who
```

If incorrect, re-authenticate:

```cmd
pac auth create --environment <yourEnvironmentId>
```

### Escalation data

Before you contact technical support to file an issue, collect the following data.

Provide:

- CLI version. Use the `pac --version` command
- OS and shell (Windows cmd / PowerShell / WSL)
- The full command used
- Sanitized debug output excerpt
- `power.config.json` after you redact secrets