---
title: "Manage CLI telemetry settings"
description: "Learn how to configure and manage telemetry settings for Power Platform CLI code commands."
ms.author: pakempar
author: pakempar
ms.date: 12/09/2025
ms.topic: how-to
---
# Manage telemetry settings for the Power Platform CLI code commands

The Power Platform CLI (PAC CLI) `code` commands collect limited telemetry to help improve reliability, performance, and usability. This section explains what is collected, how it flows, and how you can control it.

> [!NOTE]
> This section refers to the telemetry settings for the Power Platform CLI `code` commands, and not the telemetry collected when your code app is played. Learn more about the Power Platform CLI here: [Microsoft Power Platform CLI](/power-platform/developer/cli/introduction?tabs=windows)

## Why enable telemetry

When telemetry is enabled, the Power Platform CLI sends the following information:

- Activity events – High‑level actions such as running commands or completing scenarios (for example, model and service files generation, environment selection).
- Error events – Failures and exceptions (command failures, unexpected errors), including error names and messages.
- Scenario timing – Start/stop of key flows, with elapsed time for performance analysis.
- Environment context – Non‑PII metadata about the environment and region (e.g., region, geo, cluster), used to route telemetry correctly.
- Tenant identifier (when available) – If the CLI has successfully authenticated, the current tenant ID is attached for diagnostics and aggregation.

> [!NOTE]
> Telemetry failures never block CLI operations.

## Toggling telemetry 

The PAC `telemetry` verb allows you to manage telemetry settings. These changes are persisted across runs.

See [pac telemetry reference](/power-platform/developer/cli/reference/telemetry) for information on how to use the verb.

## `code` command‑specific telemetry

Starting with version 1.51.1 of the Power Platform CLI, you can manage telemetry for the `code` command alone, without affecting other PAC CLI commands.

The user‑configurable settings are stored in a JSON file under the CLI config directory (see [Locating the CLI Config Directory and Settings File](#locating-the-cli-config-directory-and-settings-file)). The settings file is located at `C:\Users\<username>\.powerapps-cli\userSettings.json`.

The effective settings object is:

- `enabled: boolean` – Whether remote telemetry is enabled.
- `consoleOnly: boolean` – Whether to only log telemetry to the console and never send it remotely.
- `outputToConsole: boolean` – Whether to additionally mirror telemetry events to the console.

> [!NOTE]
> If you have disabled telemetry globally for the PAC CLI, the `code` command will not send telemetry, even if you enable it for the `code` command.

These options combine as follows:

1. Telemetry fully disabled
	 - `enabled = false`
	 - `consoleOnly = false`
	 - `outputToConsole = false` (or `true` if you still want to see events)
	 - Result:
		 - No telemetry is sent to the backend.

2. Telemetry enabled, remote only (default)
	 - `enabled = true`
	 - `consoleOnly = false`
	 - `outputToConsole = false`
	 - Result:
		 - No telemetry is printed to the console.

3. Telemetry enabled, remote + console
	 - `enabled = true`
	 - `consoleOnly = false`
	 - `outputToConsole = true`
	 - Result:
		 - Events are sent remotely.
		 - The same events are also printed locally.

4. Console‑only telemetry (no remote send)
	 - `consoleOnly = true` (this setting takes precedence)
	 - `enabled` is effectively ignored for remote sending.
	 - `outputToConsole` is not required; console logging is implied.
	 - Result:
		 - Only console logging is used.
		 - No telemetry is sent externally, everything stays in your terminal.

> [!NOTE]
> If no settings file exists, the code commands use defaults equivalent to:
>
> - `enabled = true`
> - `consoleOnly = false`
> - `outputToConsole = false`

## Piping telemetry to a file

When telemetry is configured to output to the console (using `consoleOnly: true` or `outputToConsole: true`), you can redirect the output to a file. This is particularly useful for capturing logs for debugging or support requests.

### Windows Command Prompt

Use the `>` operator to redirect stdout and `2>&1` to include stderr if needed.

```cmd
pac code add-data-source .... > telemetry.log 2>&1
```

### PowerShell (Windows, macOS, Linux)

Use the `Out-File` cmdlet or redirection operators.

```powershell
pac code add-data-source .... | Out-File -FilePath telemetry.log -Encoding utf8
```
