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

| Symptom                  | Example Message                           |
| ------------------------ | ----------------------------------------- |
| Fetch Failed             | `Fetch Failed` (no additional stack)      |
| Timeout / network errors | `ETIMEDOUT`, `ENOTFOUND`, `ECONNRESET`    |
| Environment mismatch     | Data source not found / unexpected schema |

## Prerquisites checklist
1. Latest Power Platform CLI installed (update if unsure).
2. Authenticated to the correct environment (`pac auth create` / `pac auth list`).
3. Network allows outbound HTTPS to Power Platform endpoints.

## Troubleshooting steps

To diagnose the root cause, follow these steps:

### Step 1: Validate Configuration
Open `power.config.json` and confirm:
- `environmentId` matches the environment you intend to target.
- `region` is set to `prod` (unless you intentionally target another region). Add it if missing.

### Step 2: Cross‑Check Environment Context
Run:
```cmd
pac env who
```
Compare the `Environment ID` in the output with the `environmentId` value in `power.config.json`.

Example output (annotated):
```
Connected as user@domain.com
Organization Information
  Org ID:                     2889ab2b-e728-ef11-8406-000d3a33f333
  Unique Name:                unq2889ab2be728ef118406000d3a33f
  Friendly Name:              User Name
  Org URL:                    https://myorgguid.crm.dynamics.com/
  User Email:                 user@domain.com
  User ID:                    dabaf5e1-a427-ef11-840a-6045bd07ba63
  Environment ID:             5c1dc2ed-bf65-e52c-ab22-ea1fc9c10106  <-- Ensure this matches
```

Corresponding `power.config.json` snippet:
```json
{
  "environmentId": "5c1dc2ed-bf65-e52c-ab22-ea1fc9c10106",
  "region": "prod"
}
```

### Step 3: Re‑run Command
```cmd
pac code add-data-source -a dataverse -t account
```
Look for HTTP status codes or error messages in the output.

### Step 4: Network & Security Validation
If still failing:
- Confirm no corporate proxy/firewall blocks CLI processes (non-browser traffic).
- Whitelist required Power Platform endpoints. Reference [Power Platform connectivity requirements](/power-platform/admin/online-requirements)

**Verify browser connectivity**

This step helps confirm that your user account has the correct permissions and that the data source is reachable from your computer.

1. Open a web browser on the same computer where you're using the PAC CLI.
1. Navigate directly to the data source you're trying to add. For example, the SharePoint site or the Dataverse environment URL.
1. Sign in with the **same credentials** you used to authenticate with the PAC CLI [pac auth create](/power-platform/developer/cli/reference/auth#pac-auth-create) command
1. If you can't access the resource, a permissions issue with your user account is the likely root cause.
1. If you can access it, move to Step 2.

**Analyze network traffic**

This is the most effective way to see the raw network communication data between the PAC CLI and the data source endpoint.

1. Download and install [Fiddler Classic](https://www.telerik.com/fiddler/fiddler-classic). Fiddler is tool to monitor network traffic.
1. Start Fiddler and ensure it's capturing traffic. Go to **File** > **Capture Traffic**.
1. In a command prompt, run the failing `pac code add-data-source` command.
1. In the Fiddler session list, look for requests made to your data source endpoint. For example: `yourorg.crm.dynamics.com` or `yourtenant.sharepoint.com`.
1. Analyze the response information:

    - A `200` status code indicates success.
    - A `401` (Unauthorized) or `403` (Forbidden) status code points to an authentication or permission issue.
    - Other error codes or a complete lack of response can indicate that a firewall or proxy is blocking the request.

### Step 5: Clear/Reset Auth Context (If Mismatch Detected)
```cmd
pac auth list
pac auth select --index <n>
pac env who
```
If incorrect, re-authenticate:
```cmd
pac auth create --environment <yourEnvironmentId>
```

### Escalation Data (Collect Before Filing Issue)
Provide:
- CLI version (`pac --version`)
- OS and shell (Windows cmd / PowerShell / WSL)
- Full command used
- Sanitized debug output excerpt
- `power.config.json` (redact secrets)

  
 
