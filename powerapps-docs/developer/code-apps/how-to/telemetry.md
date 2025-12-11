---
title: "How to: Manage telemetry settings for the Power Platform CLI code commands"
description: "Learn how to configure and manage telemetry settings for Power Platform CLI code commands."
ms.author: pakempar
author: pavankm
ms.date: 12/11/2025
ms.topic: how-to
---
# How to: Manage telemetry settings for the Power Platform CLI code commands

The Power Platform CLI (PAC CLI) [`code` commands](/power-platform/developer/cli/reference/code) collect limited telemetry to help Microsoft improve reliability, performance, and usability. This section explains what is collected, how it flows, and how you can control it.

> [!NOTE]
> This section refers to the telemetry settings for the Power Platform CLI [`code` commands](/power-platform/developer/cli/reference/code), and not the telemetry collected when your code app is played. Learn more about the Power Platform CLI here: [Microsoft Power Platform CLI](/power-platform/developer/cli/introduction)

## Why enable telemetry?

When telemetry is enabled, the Power Platform CLI sends the following information:

- **Activity events** – High‑level actions such as running commands or completing scenarios (for example, model and service files generation, environment selection).
- **Error events** – Failures and exceptions (command failures, unexpected errors), including error names and messages.
- **Scenario timing** – Start/stop of key flows, with elapsed time for performance analysis.
- **Environment context** – Non‑PII metadata about the environment and region (e.g., region, geo, cluster), used to route telemetry correctly.
- **Tenant identifier** (when available) – If the CLI has successfully authenticated, the current tenant ID is attached for diagnostics and aggregation.

> [!NOTE]
> Telemetry failures never block CLI operations.

## Toggling telemetry

The [PAC `telemetry` commands](/power-platform/developer/cli/reference/telemetry) allows you to manage telemetry settings for all PAC CLI operations. These changes are persisted across runs.

## `code` command‑specific telemetry

Starting with version 1.51.1 of the Power Platform CLI, you can manage telemetry for the [`code` commands](/power-platform/developer/cli/reference/code), without affecting other PAC CLI commands.

The user‑configurable settings are stored in a `userSettings.json` JSON file under the CLI config directory named `.powerapps-cli`.

The `userSettings.json` file content has three properties:

```json
{
  "enabled": true,
  "consoleOnly": false,
  "outputToConsole": false
}
```

### [Windows](#tab/windows)

The `.powerapps-cli` folder is located in the location designated by the `USERPROFILE` environment variable.

You can create this file manually or use the following PowerShell script:

```powershell
$settingsPath = Join-Path $env:USERPROFILE ".powerapps-cli\userSettings.json"
$settingsDir = Split-Path $settingsPath
if (-not (Test-Path $settingsDir)) { New-Item -ItemType Directory -Path $settingsDir -Force }
$settings = @{
    enabled = $true
    consoleOnly = $false
    outputToConsole = $false
}
$settings | ConvertTo-Json | Set-Content $settingsPath
```

### [Linux or Mac](#tab/linuxormac)

The `.powerapps-cli` folder is located in the location designated by the `HOME` environment variable.

You can create this file manually or use the following script:

```bash
mkdir -p "$HOME/.powerapps-cli" && cat > "$HOME/.powerapps-cli/userSettings.json" <<'EOF'
{
  "enabled": true,
  "consoleOnly": false,
  "outputToConsole": false
}
EOF
```

---

The purpose of these boolean properties are described in the following table:

|Property|Description|
|---|---|
|`enabled`|Whether remote telemetry is enabled.|
|`consoleOnly`|Whether to only log telemetry to the console and never send it remotely.|
|`outputToConsole`|Whether to additionally mirror telemetry events to the console.|

> [!NOTE]
> If you have disabled telemetry globally for the PAC CLI using the [PAC `telemetry` commands](/power-platform/developer/cli/reference/telemetry), the `code` command will not send telemetry, even if you enable it for the `code` command.

The following sections describe valid combinations of values and their outcomes:

### Telemetry enabled, remote only (default)

If no `userSettings.json` file exists, this is the behavior.
No telemetry is printed to the console.

```json
{
  "enabled": true,
  "consoleOnly": false,
  "outputToConsole": false
}
```

### Telemetry fully disabled

```json
{
  "enabled": false,
  "consoleOnly": false,
  "outputToConsole": false
}
```

Set `outputToConsole` to `true` if you still want to see events.

### Telemetry enabled, remote + console

Events are sent remotely. The same events are also printed locally.

```json
{
  "enabled": true,
  "consoleOnly": false,
  "outputToConsole": true
}
```

### Console‑only telemetry (no remote send)

When `consoleOnly` is true, only console logging is used. No telemetry is sent externally, everything stays in your terminal.

```json
{
  "enabled": false,
  "consoleOnly": true,
  "outputToConsole": false
}
```

- `enabled` is effectively ignored for remote sending.
- `outputToConsole` is not required; console logging is implied.


## Piping telemetry to a file

When telemetry is configured to output to the console (using `consoleOnly: true` or `outputToConsole: true`), you can redirect the output to a file. This is particularly useful for capturing logs for debugging or support requests.

### Windows Command Prompt

Use the `>` operator to redirect `stdout` and `2>&1` to include `stderr` if needed.

```cmd
pac code add-data-source .... > telemetry.log 2>&1
```

### PowerShell (Windows, macOS, Linux)

Use the `Out-File` cmdlet or redirection operators.

```powershell
pac code add-data-source .... | Out-File -FilePath telemetry.log -Encoding utf8
```
