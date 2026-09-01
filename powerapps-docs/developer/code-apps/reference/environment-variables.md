---
title: Power Apps CLI environment variables
description: Reference the environment variables supported by the Power Apps CLI for authentication, automation, app configuration, data sources, and telemetry.
#customer intent: As a developer, I want to configure Power Apps CLI commands with environment variables so that I can automate code app workflows.
ms.topic: reference
ms.service: powerapps
ms.subservice: code-apps
ms.author: ergonza
ms.reviewer: jdaly
author: ergonza93
ms.date: 08/31/2026
---

# Power Apps CLI environment variables

Use environment variables to configure Power Apps CLI authentication and provide command options in scripts and CI/CD pipelines. Environment variables defined by the Power Apps CLI use the `PA_CLI_` prefix.

> [!NOTE]
> Environment variables are named values that the operating system makes available to applications. Power Apps CLI recognizes the variables described in this reference. To learn how environment variables work and how to manage them, see [about Environment Variables](/powershell/module/microsoft.powershell.core/about/about_environment_variables).
>
> This reference describes operating system environment variables that configure the Power Apps CLI. These variables are different from [Power Platform solution environment variables](../how-to/use-environment-variables.md), which store configuration values used by an app.

For a command option, the CLI resolves a value in this order:

1. Command-line option
1. Environment variable
1. Default value, if the option has one
1. Interactive prompt, when supported

An option supplied on the command line takes precedence over its corresponding environment variable.

> [!IMPORTANT]
> Environment variables can expose secrets to other processes, logs, or shell history. Store `PA_CLI_SP_CLIENT_SECRET` in your CI/CD platform's secret store, mask it from logs, and don't commit secrets to source control.

### Set environment variables

The following examples set `PA_CLI_ENVIRONMENT_ID` before running a Power Apps CLI command.

#### [PowerShell](#tab/powershell)

```powershell
$env:PA_CLI_ENVIRONMENT_ID = "<environment-id>"
pa app list
```

#### [Bash](#tab/bash)

```bash
export PA_CLI_ENVIRONMENT_ID="<environment-id>"
pa app list
```

---

The environment variable remains available to commands started from the same terminal session. Use your shell's standard command to remove it when it's no longer needed.


## Authentication

| Environment variable | Description |
| --- | --- |
| `PA_CLI_ACCOUNT` | Specifies the account for [`pa auth login`](cli.md#pa-auth-login) or [`pa auth switch`](cli.md#pa-auth-switch). |
| `PA_CLI_SP_CLIENT_ID` | Specifies the Microsoft Entra application (client) ID for service principal authentication. |
| `PA_CLI_SP_CLIENT_SECRET` | Specifies the client secret for service principal authentication. |
| `PA_CLI_SP_TENANT_ID` | Specifies the Microsoft Entra directory (tenant) ID for service principal authentication. |
| `PA_CLI_USE_SP_AUTH` | Set the value to `true` (lowercase) to use service principal authentication. |

The three `PA_CLI_SP_`* credential variables are required when service principal authentication is selected. Although `CI=true` also selects service principal authentication for compatibility, use `PA_CLI_USE_SP_AUTH=true` to make the authentication mode explicit.

For setup instructions, see [Publish Power Apps code apps with a service principal](../how-to/use-service-principal.md).

## Global command options

These variables correspond to options that are available across [Power Apps CLI commands](cli.md).

| Environment variable | Corresponding option | Description |
| --- | --- | --- |
| `PA_CLI_CLOUD` | `--cloud` | Selects the target cloud. Valid values are:<br />- `public` (default)<br />- `usgov`<br />- `usgovhigh`<br />- `usgovdod`<br />- `china`<br />Values are case-insensitive. |
| `PA_CLI_ENVIRONMENT_ID` | `--environment-id` | Specifies the target Power Platform environment ID. |

## App initialization

These variables supply options to [`pa app init`](cli.md#pa-app-init).

| Environment variable | Corresponding option | Description |
| --- | --- | --- |
| `PA_CLI_APP_BUILD_PATH` | `--build-path` | Specifies the build output directory. The default is `./dist`. |
| `PA_CLI_APP_DESCRIPTION` | `--description` | Specifies the app description. |
| `PA_CLI_APP_DISPLAY_NAME` | `--display-name` | Specifies the app display name. |
| `PA_CLI_APP_FILE_ENTRY_POINT` | `--file-entry-point` | Specifies the HTML entry point in the build output. The default is `index.html`. |
| `PA_CLI_APP_TYPE` | `--app-type` | Specifies the app type. Valid values are:<br />- `CodeApp` (default)<br />- `MobileApp`<br />The value is saved in `power.config.json` and used as the app type when the app is published. |
| `PA_CLI_APP_URL` | `--app-url` | Specifies the local app URL during [`pa app init`](cli.md#pa-app-init). The value is saved as `localAppUrl` in `power.config.json` and becomes the default URL for future [`pa app run`](cli.md#pa-app-run) commands. The default is `http://localhost:3000`. |

## Run apps

These variables supply options to [`pa app run`](cli.md#pa-app-run).

| Environment variable | Corresponding option | Description |
| --- | --- | --- |
| `PA_CLI_LOCAL_APP_URL` | `--local-app-url` | Overrides the `localAppUrl` value from `power.config.json` for the current command without changing the saved configuration. If neither value is set, the default is `http://localhost:3000`. |
| `PA_CLI_PORT` | `--port` | Specifies the port for the Power Apps local host. The default is `8080`. |

## Share apps

These variables supply options to [`pa app share`](cli.md#pa-app-share).

| Environment variable | Corresponding option | Description |
| --- | --- | --- |
| `PA_CLI_SHARE_ACCESS` | `--access` | Specifies the access level. Valid values are:<br />- `play` (default)<br />- `edit`<br /> |
| `PA_CLI_SHARE_PRINCIPAL` | `--principal` | Specifies one or more comma-separated email addresses or Microsoft Entra object IDs. |

## Solutions, connectors, and data sources

| Environment variable | Corresponding option | Description |
| --- | --- | --- |
| `PA_CLI_CONNECTION_DISPLAY_NAME` | `--display-name` | Specifies the display name when creating a connection. |
| `PA_CLI_CONNECTION_ID` | `--connection-id` | Specifies a connector connection instance ID. |
| `PA_CLI_CONNECTION_REF` | `--connection-ref` | Specifies a connection reference logical name. |
| `PA_CLI_CONNECTION_SEARCH` | `--search` | Filters results from [`pa connection list`](cli.md#pa-connection-list). |
| `PA_CLI_CONNECTOR` | `--connector` | Specifies a connector ID, such as `shared_office365users`. |
| `PA_CLI_CONNECTOR_SEARCH` | `--search` | Filters results from [`pa connector list`](cli.md#pa-connector-list). |
| `PA_CLI_DATASET` | `--dataset` | Specifies a dataset, such as a SharePoint site or SQL database. |
| `PA_CLI_DATA_SOURCE_NAME` | `--name` | Specifies the data source to refresh or remove. |
| `PA_CLI_ORG_URL` | `--org-url` | Overrides the Dataverse organization URL used to retrieve metadata when adding a data source. |
| `PA_CLI_PROCEDURE` | `--procedure` | Specifies a SQL stored procedure. |
| `PA_CLI_SOLUTION_ID` | `--solution-id` | Specifies the solution for [`pa app push`](cli.md#pa-app-push), [`pa app add data-source`](cli.md#pa-app-add-data-source), or [`pa connection list-references`](cli.md#pa-connection-list-references). |
| `PA_CLI_SOLUTION_SEARCH` | `--search` | Filters results from [`pa solution list`](cli.md#pa-solution-list). |
| `PA_CLI_TABLE` | `--table` | Specifies a table or connector resource name. |

For the commands that accept each option, see the [Power Apps CLI command reference](cli.md).

## Dataverse APIs and Power Automate flows

| Environment variable | Corresponding option | Description |
| --- | --- | --- |
| `PA_CLI_DATAVERSE_API_NAME` | `--api-name` | Specifies the Dataverse action or function to add with [pa app add dataverse-api](cli.md#pa-app-add-dataverse-api). |
| `PA_CLI_DATAVERSE_API_SEARCH_TERM` | `--search` | Filters Dataverse actions and functions by name with [`pa app find-dataverse-api`](cli.md#pa-app-find-dataverse-api). |
| `PA_CLI_FLOW_DATA_SOURCE_NAME` | `--flow-name` | Specifies the flow data source to remove from the app with [`pa app remove flow`](cli.md#pa-app-remove-flow) |
| `PA_CLI_FLOW_ID` | `--flow-id` | Specifies the Power Automate flow to add with [`pa app add flow`](cli.md#pa-app-add-flow). |
| `PA_CLI_FLOW_SEARCH` | `--search` | Filters the available Power Automate flows by name with [`pa app list-flows`](cli.md#pa-app-list-flows) |
| `PA_CLI_REMOVE_FLOW_ID` | `--flow-id` | Specifies the Power Automate flow to remove with [`pa app remove flow`](cli.md#pa-app-remove-flow) |

## Telemetry and console output

| Environment variable | Corresponding option | Description |
| --- | --- | --- |
| `PA_CLI_CONSOLE_ONLY` | `--console-only` | Set the value to `true` (lowercase) with [`pa telemetry enable`](cli.md#pa-telemetry-enable) or [`pa telemetry disable`](cli.md#pa-telemetry-disable) to write telemetry only to the console and not send it remotely. |
| `PA_CLI_OUTPUT_TO_CONSOLE` | `--output-to-console` | Set the value to `true` (lowercase) with [`pa telemetry enable`](cli.md#pa-telemetry-enable) or [`pa telemetry disable`](cli.md#pa-telemetry-disable) to mirror remotely sent telemetry events to the console. |
| `PA_CLI_TELEMETRY` | None | Set one of these values to disable telemetry for the current process:<br />- `0`<br />- `false`<br />- `no`<br />- `off`<br />Values are case-insensitive, and surrounding spaces are ignored. |

For persistent telemetry settings, see [Manage telemetry settings for the Power Apps CLI](../how-to/telemetry.md).

## Standard environment variables

The CLI also observes this standard environment variable:

| Environment variable | Description |
| --- | --- |
| `NO_COLOR` | Set this variable to a nonempty value to disable ANSI color output. You can also use the `--no-color` option. |


## Related information

- [Power Apps CLI command reference](cli.md)
- [Publish Power Apps code apps with a service principal](../how-to/use-service-principal.md)
- [Manage telemetry settings for the Power Apps CLI](../how-to/telemetry.md)
