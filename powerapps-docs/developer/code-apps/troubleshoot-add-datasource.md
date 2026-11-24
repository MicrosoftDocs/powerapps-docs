---
title: Troubleshoot Adding a Data Source
description: Troubleshoot adding a data source with the pa app add data-source command by identifying configuration, authentication, and network errors. Follow these steps.
ms.author: jordanchodak
author: jordanchodakWork
ms.date: 11/24/2026
ms.reviewer: jdaly
ms.topic: troubleshooting
ai-usage: ai-assisted
contributors:
 - JimDaly
---

# Troubleshoot adding a data source

Troubleshoot adding a data source when the Power Apps CLI [`pa app add data-source`](reference/cli.md#pa-app-add-data-source) command fails. Follow these steps to identify configuration, authentication, or network issues and add the data source successfully.


## Symptoms

Failures can happen because of configuration, authentication, network connectivity, or your organization's connector policy.

| Symptom | Example message |
| --- | --- |
| Fetch failed | `Fetch Failed` (no additional stack) |
| Timeout or network errors | `ETIMEDOUT`, `ENOTFOUND`, or `ECONNRESET` |
| Environment mismatch | Data source not found or unexpected schema |
| Connector or actions blocked by policy | Exit code `2` when the connector or all actions are blocked |
| Expected generated method is missing | Notice that actions were skipped because of your organization's connector policy |

## Prerequisites

1. Verify that you have the latest Power Apps CLI installed. Update it if you're not sure.
1. Use [`pa auth login`](reference/cli.md#pa-auth-login) to sign in and [`pa auth status`](reference/cli.md#pa-auth-status) to verify the active account:

   ```bash
   pa auth login
   pa auth status
   ```

1. Verify that your network allows outbound HTTPS calls to Power Platform endpoints.

## Steps to troubleshoot data source errors

To diagnose the root cause, follow these steps.

### Check connector policy messages

If the CLI reports that your organization's policy blocks the connector or all its actions, contact your Power Platform administrator. Retrying authentication or changing network settings doesn't resolve a policy block. The command stops before creating a connection or data source files.

If the command succeeds but reports skipped actions, the generated service doesn't include those actions. Use an allowed action or ask your administrator to review the policy.

If the CLI warns that it can't check policy because the tenant couldn't be identified or the policy service is unavailable, the command continues without that check. Don't treat this warning as confirmation that the connector is allowed. Invalid policy responses and canceled authentication fail the command. See [`pa app add data-source` remarks](reference/cli.md#pa-app-add-data-source-remarks).

### Step 1: Validate configuration

Open the `power.config.json` file and confirm:

- `environmentId` matches the environment you want to target.
- `region` is set to `prod`, unless you want to target another region. Add it if it's missing.

### Step 2: Cross-check environment context

Use [`pa auth status`](reference/cli.md#pa-auth-status) to confirm that the correct account is active:

```bash
pa auth status
```

Compare the `environmentId` in `power.config.json` with the environment ID shown in the Power Apps environment URL.

Example `power.config.json` snippet:

```json
{
  "environmentId": "aaaabbbb-0000-cccc-1111-dddd2222eeee",
  "region": "prod"
}
```

### Step 3: Rerun the add data source command

Run [`pa app add data-source`](reference/cli.md#pa-app-add-data-source) again. For example:

```bash
pa app add data-source --connector dataverse --table account
```

Check the output for HTTP status codes or error messages.

### Step 4: Validate network and security settings

If the command still fails:

- Confirm that no corporate proxy or firewall blocks CLI processes or other nonbrowser traffic.
- Approve the required Power Platform endpoints. See [Power Platform connectivity requirements](/power-platform/admin/online-requirements).

#### Verify browser connectivity

This step helps confirm that your user account has the correct permissions and that the data source is reachable from your computer.

1. Open a web browser on the same computer where you're using the Power Apps CLI.
1. Go directly to the data source you're trying to add, such as the SharePoint site or Dataverse environment URL.
1. Sign in with the same account shown by [`pa auth status`](reference/cli.md#pa-auth-status).
1. If you can't access the resource, a permissions issue with your user account is the likely root cause.
1. If you can access it, continue to [Analyze network traffic](#analyze-network-traffic).

#### Analyze network traffic

Use a network-monitoring tool to inspect communication between the Power Apps CLI and the data source endpoint.

1. Download and install [Fiddler Classic](https://www.telerik.com/fiddler/fiddler-classic).
1. Start Fiddler and ensure that it's capturing traffic. Go to **File** > **Capture Traffic**.
1. In a command prompt, run the failing [`pa app add data-source`](reference/cli.md#pa-app-add-data-source) command.
1. In the Fiddler session list, look for requests made to your data source endpoint, such as `yourorg.crm.dynamics.com` or `yourtenant.sharepoint.com`.
1. Analyze the response:

   - A `200` status code indicates success.
   - A `401` (Unauthorized) or `403` (Forbidden) status code points to an authentication or permission issue.
   - Other error codes or a complete lack of response can indicate that a firewall or proxy is blocking the request.

### Step 5: Clear or reset the auth context

If the wrong account is active, use [`pa auth switch`](reference/cli.md#pa-auth-switch):

```bash
pa auth switch
```

If the account isn't listed, use [`pa auth login`](reference/cli.md#pa-auth-login):

```bash
pa auth login
```

To clear all saved authentication information and sign in again, use [`pa auth logout`](reference/cli.md#pa-auth-logout), and then use [`pa auth login`](reference/cli.md#pa-auth-login):

```bash
pa auth logout
pa auth login
```

### Escalation data for technical support

Before you contact technical support to file an issue, provide:

- CLI version from [`pa --version`](reference/cli.md#power-apps-cli-global-options)
- Operating system and shell, such as Windows Command Prompt, PowerShell, or WSL
- The full command used
- Sanitized debug output
- `power.config.json` after you redact sensitive values
