---
title: Power Apps CLI Command Reference
description: Explore the Power Apps CLI command reference to create, develop, connect, and publish Power Apps code apps. Review commands and parameters.
#customer intent: As a developer, I want a complete reference for the Power Apps CLI commands available for Power Apps code apps.
ms.topic: reference
ms.author: jordanchodak
ms.reviewer: jdaly
author: jordanchodakWork
ms.date: 08/31/2026
---

# Power Apps CLI command reference

Use this Power Apps CLI command reference to quickly find commands for creating, developing, connecting, and publishing Power Apps code apps. The CLI uses grouped commands in the following format:

```console
pa <command-group> <command>
```

These are the command groups:

| Command group | Description |
| --- | --- |
| `pa app` | Create, run, connect, and publish code apps. |
| `pa auth` | Sign in and manage accounts. |
| `pa connector` | Find connectors available in a Power Platform environment. |
| `pa connection` | Create and manage connections and discover their resources. |
| `pa solution` | Find solutions available in a Power Platform environment. |
| `pa telemetry`| Manage CLI telemetry settings.|

## Global options

Use `--help` at any level to display help in the terminal:

```console
pa --help
pa app --help
pa app init --help
```

Use `--version` to display the installed Power Apps CLI version:

```console
pa --version
```

## Power Apps CLI commands

These commands are available:

| Command | Description |
| --- | --- |
| [`pa app add data-source`](#pa-app-add-data-source) | Add a connector or tabular data source to the code app. |
| [`pa app add dataverse-api`](#pa-app-add-dataverse-api) | Add a Dataverse action or function to the code app. |
| [`pa app add flow`](#pa-app-add-flow) | Add a Power Automate flow to the code app. |
| [`pa app find-dataverse-api`](#pa-app-find-dataverse-api) | Find Dataverse actions and functions in the current environment. |
| [`pa app init`](#pa-app-init) | Initialize a code app in the current directory. |
| [`pa app list`](#pa-app-list) | List code apps in the current environment. |
| [`pa app list-environment-variables`](#pa-app-list-environment-variables) | List environment variables available to the code app. |
| [`pa app list-flows`](#pa-app-list-flows) | List solution-aware Power Automate flows in the current environment. |
| [`pa app push`](#pa-app-push) | Publish a new version of the code app to Power Apps. |
| [`pa app refresh data-source`](#pa-app-refresh-data-source) | Refresh the generated files for a data source. |
| [`pa app remove data-source`](#pa-app-remove-data-source) | Remove a data source from the code app. |
| [`pa app remove flow`](#pa-app-remove-flow) | Remove a Power Automate flow from the code app. |
| [`pa app run`](#pa-app-run) | Start the Power Apps local host for the code app. |
| [`pa app share`](#pa-app-share) | Share the code app with users or service principals. |
| [`pa auth login`](#pa-auth-login) | Sign in through the system browser. |
| [`pa auth logout`](#pa-auth-logout) | Sign out and remove saved authentication information. |
| [`pa auth status`](#pa-auth-status) | Display signed-in accounts and identify the active account. |
| [`pa auth switch`](#pa-auth-switch) | Change the active account. |
| [`pa connection create`](#pa-connection-create) | Create a connection for a connector. |
| [`pa connection list`](#pa-connection-list) | List connections in the current environment. |
| [`pa connection list-datasets`](#pa-connection-list-datasets) | List datasets available through a connection. |
| [`pa connection list-procedures`](#pa-connection-list-procedures) | List SQL stored procedures available in a dataset. |
| [`pa connection list-references`](#pa-connection-list-references) | List connection references in a solution. |
| [`pa connection list-tables`](#pa-connection-list-tables) | List tables available in a dataset. |
| [`pa connector list`](#pa-connector-list) | List connectors available in the current Power Platform environment. |
| [`pa solution list`](#pa-solution-list) | List solutions in the current environment. |
| [`pa telemetry disable`](#pa-telemetry-disable) | Disable telemetry collection. |
| [`pa telemetry enable`](#pa-telemetry-enable) | Enable telemetry collection. |
| [`pa telemetry status`](#pa-telemetry-status) | Display the current telemetry settings. |

## `pa app add data-source`

Adds a connector or tabular data source to the code app.

```console
pa app add data-source --connector <connector-id> [options]
```

### `pa app add data-source` parameters

| Parameter | Description |
| --- | --- |
| `--connector` | The connector identifier, such as `shared_office365users`. |
| `--connection-id` | The connection ID to use for the data source. |
| `--connection-ref` | The logical name of a connection reference. |
| `--solution-id` | The solution that contains the connection reference. |
| `--dataset` | The dataset for a tabular data source. |
| `--table` | The table to add. |
| `--org-url` | The Dataverse organization URL to use when retrieving table metadata. |
| `--procedure` | The SQL stored procedure to add. |

These parameters have corresponding [Solutions, connectors, and data sources](environment-variables.md#solutions-connectors-and-data-sources) environmental variables.

## `pa app add dataverse-api`

Adds a Dataverse action or function to the code app.

```console
pa app add dataverse-api --api-name <operation-name>
```

### `pa app add dataverse-api` parameters

| Parameter | Description |
| --- | --- |
| `--api-name` | The name of the Dataverse action or function to add. |

[`PA_CLI_DATAVERSE_API_NAME`](environment-variables.md#dataverse-apis-and-power-automate-flows) is the corresponding environmental variable for the `--api-name` parameter.

Learn more:

- [Learn how to update a Dataverse operation](../how-to/add-dataverse-action-function.md#update-an-operation)
- [Troubleshoot Dataverse operations](../how-to/add-dataverse-action-function.md#troubleshooting)

## `pa app add flow`

Adds a Power Automate flow to the code app.

```console
pa app add flow --flow-id <flow-id>
```

### `pa app add flow` parameters

| Parameter | Description |
| --- | --- |
| `--flow-id` | The ID of the Power Automate flow to add. |

[`PA_CLI_FLOW_ID`](environment-variables.md#dataverse-apis-and-power-automate-flows) is the corresponding environmental variable for the `--flow-id` parameter.

The command:

- Downloads the flow's OpenAPI definition.
- Generates strongly typed TypeScript models and services.
- Adds the flow and its connection references to `power.config.json`.

If a flow definition changes, run this command again to regenerate code for the latest version.

> [!IMPORTANT]
> The person who runs `pa app add flow` must have access to the flow and its underlying connections. The command fails if the person doesn't have access to a required connection.


Learn more about scenarios where you use this command:

- [Learn what happens when you add a Power Automate flow](../how-to/add-flows.md#what-the-command-does)
- [Learn how to update a Power Automate flow](../how-to/add-flows.md#update-a-flow)
- [Review limitations and considerations for Power Automate flows](../how-to/add-flows.md#limitations-and-considerations)

## `pa app find-dataverse-api`

Finds Dataverse actions and functions in the current environment.

```console
pa app find-dataverse-api --search <operation-name> [--json]
```

### `pa app find-dataverse-api` parameters

| Parameter | Description |
| --- | --- |
| `--search` | The operation name to search for. |
| `--json` | Return the results as JSON. |

These parameters have corresponding [Dataverse APIs and Power Automate flows](environment-variables.md#dataverse-apis-and-power-automate-flows) environmental variables.

[Learn how to find available Dataverse operations](../how-to/add-dataverse-action-function.md#step-1-find-available-operations)

## `pa app init`

Initializes a code app in the current directory.

```console
pa app init [--display-name <name>] [--environment-id <environment-id>]
```

### `pa app init` parameters

| Parameter | Description |
| --- | --- |
| `--display-name` | The display name of the code app. |
| `--environment-id` | The Power Platform environment for the code app. |
| `--description` | The description of the code app. |
| `--build-path` | The directory that contains the compiled app assets. |
| `--file-entry-point` | The HTML entry point in the build output. |
| `--app-type` | The app type. Valid values are `CodeApp` and `MobileApp`. |
| `--app-url` | The URL of the locally running code app. |
| `--cloud` | The Power Platform cloud instance. |

These parameters have corresponding [App initialization](environment-variables.md#app-initialization) environmental variables.

Learn more about scenarios where you can use this command: 

- [Review prerequisites for adding a Dataverse action or function](../how-to/add-dataverse-action-function.md#prerequisites)
- [Review prerequisites for adding Power Automate flows](../how-to/add-flows.md#prerequisites)
- [Learn how to initialize a code app](../how-to/create-an-app-from-scratch.md#step-2-install-dependencies-and-initialize-the-code-app)
- [Learn how sign-in works when you initialize a code app](../how-to/sign-in-manage-accounts.md#how-to-sign-in-and-manage-accounts-with-the-power-apps-cli)

## `pa app list`

Lists code apps in the current environment.

```console
pa app list
```

## `pa app list-environment-variables`

Lists environment variables available to the code app.

```console
pa app list-environment-variables
```

## `pa app list-flows`

Lists solution-aware Power Automate flows in the current environment.

```console
pa app list-flows [--search <term>]
```

Example:

```bash
pa app list-flows
```

```console
Name                    Status   Modified On   Flow ID
──────────────────────────────────────────────────────────────────────────────
Approval Workflow       Started  2026-01-15    a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1
Send Notification       Started  2026-02-01    b1b1b1b1-cccc-dddd-eeee-f2f2f2f2f2f2

Total flows: 2
```

### `pa app list-flows` parameters

| Parameter | Description |
| --- | --- |
| `--search` | Filter flows by name. |

[`PA_CLI_FLOW_SEARCH` ](environment-variables.md#dataverse-apis-and-power-automate-flows) is the corresponding environmental variable for the `--search` parameter.

## `pa app push`

Publishes a new version of the code app to Power Apps.

```console
pa app push [--solution-id <solution-id>]
```

### `pa app push` parameters

| Parameter | Description |
| --- | --- |
| `--solution-id` | The ID of the solution to add the code app to. |
| `--non-interactive`| Publishes the app non-interactively. [Learn to publish apps with a service principal](../how-to/use-service-principal.md). |

[`PA_CLI_SOLUTION_ID`](environment-variables.md#solutions-connectors-and-data-sources) is the environmental variable to use with the `--solution-id` parameter.

[Learn how to create a code app by using the Power Apps CLI](../how-to/create-an-app-from-scratch.md).

## `pa app refresh data-source`

Refreshes the generated files for a data source.

```console
pa app refresh data-source --name <data-source-name>
```

### `pa app refresh data-source` parameters

| Parameter | Description |
| --- | --- |
| `--name` | The name of the data source to refresh. |

## `pa app remove data-source`

Removes a data source from the code app.

```console
pa app remove data-source --connector <connector-id> --name <data-source-name> [--force]
```

### `pa app remove data-source` parameters

| Parameter | Description |
| --- | --- |
| `--connector` | The connector identifier for the data source. |
| `--name` | The name of the data source to remove. |
| `--force` | Remove the data source without prompting for confirmation. |

## `pa app remove flow`

Removes a Power Automate flow from the code app.

```console
pa app remove flow [--flow-name <name> | --flow-id <flow-id>] [--force]
```

### `pa app remove flow` parameters

| Parameter | Description |
| --- | --- |
| `--flow-name` | The name of the Power Automate flow to remove. |
| `--flow-id` | The ID of the Power Automate flow to remove. |
| `--force` | Remove the flow without prompting for confirmation. |

[`PA_CLI_FLOW_DATA_SOURCE_NAME` and `PA_CLI_REMOVE_FLOW_ID`](environment-variables.md#dataverse-apis-and-power-automate-flows) are corresponding environmental variables to use whith these parameters.

[Learn how to remove a flow](../how-to/add-flows.md#remove-a-flow)

## `pa app run`

Starts the Power Apps local host for the code app.

```console
pa app run [--port <port>] [--local-app-url <url>]
```

### `pa app run` parameters

| Parameter | Description |
| --- | --- |
| `--port` | The port for the local host. |
| `--local-app-url` | The URL of the locally running code app. |

These parameters have corresponding [Run apps](environment-variables.md#run-apps) environmental variables.

## `pa app share`

Shares the code app with users or service principals.

```console
pa app share --principal <principal> [--access play|edit]
```

### `pa app share` parameters

| Parameter | Description |
| --- | --- |
| `--principal` | Comma-separated email addresses or Microsoft Entra object IDs for the users or service principals to share with. |
| `--access` | The access level to grant: `play` (default) or `edit`. |

These parameters have corresponding [Share apps](environment-variables.md#share-apps) environmental variables.


### `pa app share` remarks

The code app must already be published and have an app ID from a successful [`pa app push`](#pa-app-push) command. Grant `edit` access when a service principal needs to run [`pa app push`](#pa-app-push).

When sharing with a service principal, use the Enterprise Application object ID, not the App Registration object ID.

## `pa auth login`

Signs in through the system browser.

```console
pa auth login
```

To prepopulate the account on the sign-in page, use:

```console
pa auth login --account user@contoso.com
```

### `pa auth login` parameters

| Parameter | Description |
| --- | --- |
| `--account` | The account to prepopulate on the sign-in page. |

[`PA_CLI_ACCOUNT`](environment-variables.md#authentication) is the corresponding environmental variable for the `--account` parameter.

- [Learn how to sign in](../how-to/sign-in-manage-accounts.md#sign-in)
- [Learn how to switch the active account](../how-to/sign-in-manage-accounts.md#switch-the-active-account)

## `pa auth logout`

Signs out and removes saved authentication information.

```console
pa auth logout
```

> [!NOTE]
> This command signs you out of *all* accounts. It can't sign you out of just one account. To change which account is active, use [`pa auth switch`](#pa-auth-switch) instead.

[Learn how to sign out](../how-to/sign-in-manage-accounts.md#sign-out)

## `pa auth status`

Displays signed-in accounts and identifies the active account.

To display authentication status as JSON, use:

```console
pa auth status --json
```

### `pa auth status` parameters

| Parameter | Description |
| --- | --- |
| `--json` | Return the authentication status as JSON. |

[Learn how to check which account is active](../how-to/sign-in-manage-accounts.md#check-which-account-is-active)

## `pa auth switch`

Changes the active account.

```console
pa auth switch --account user@contoso.com
```

### `pa auth switch` parameters

| Parameter | Description |
| --- | --- |
| `--account` | The account to make active. |

[`PA_CLI_ACCOUNT`](environment-variables.md#authentication) is the corresponding environmental variable for the `--account` parameter.

Learn more about when you can use this command:

- [Learn how to check which account is active](../how-to/sign-in-manage-accounts.md#check-which-account-is-active)
- [Learn how to switch the active account](../how-to/sign-in-manage-accounts.md#switch-the-active-account)
- [Learn how to sign out](../how-to/sign-in-manage-accounts.md#sign-out)

## `pa connection create`

Creates a connection for a connector.

```console
pa connection create --connector <connector-id> [--display-name <name>] [--json]
```

### `pa connection create` parameters

| Parameter | Alias | Required | Description |
| --- | --- | --- | --- |
| `--connector` | - | Yes | The connector identifier, such as `shared_office365` or `shared_teams`. |
| `--display-name` | `-n` | No | The display name for the connection. If you don't provide a name, the CLI uses a default name. |
| `--json` | - | No | Returns the result as JSON. |

### `pa connection create` examples

Create an Office 365 Outlook connection:

```bash
pa connection create --connector shared_office365
```

Create a Microsoft Teams connection with a custom display name:

```bash
pa connection create --connector shared_teams --display-name "My Teams"
```

Create a connection and return the result as JSON:

```bash
pa connection create --connector shared_office365 --json
```

### `pa connection create` output

When the command succeeds, it returns the connection ID. Use the connection ID when you add the connector as a data source to the code app.

[Learn how to create a connection from the Power Apps CLI](../how-to/create-connection.md)

## `pa connection list`

Lists connections in the current environment.

```console
pa connection list [--search <term>] [--json]
```

### `pa connection list` parameters

| Parameter | Description |
| --- | --- |
| `--search` | Filter connections by name. |
| `--json` | Return the results as JSON. |

These parameters have corresponding [Solutions, connectors, and data sources](environment-variables.md#solutions-connectors-and-data-sources) environmental variables.

## `pa connection list-datasets`

Lists datasets available through a connection.

```console
pa connection list-datasets --connector <connector-id> [--connection-id <connection-id>]
```

### `pa connection list-datasets` parameters

| Parameter | Description |
| --- | --- |
| `--connector` | The connector identifier. |
| `--connection-id` | The connection ID to use when listing datasets. |

## `pa connection list-procedures`

Lists SQL stored procedures available in a dataset.

```console
pa connection list-procedures --connection-id <connection-id> --dataset <dataset>
```

### `pa connection list-procedures` parameters

| Parameter | Description |
| --- | --- |
| `--connection-id` | The connection ID to use when listing stored procedures. |
| `--dataset` | The dataset that contains the stored procedures. |

## `pa connection list-references`

Lists connection references in a solution.

```console
pa connection list-references --solution-id <solution-id>
```

### `pa connection list-references` parameters

| Parameter | Description |
| --- | --- |
| `--solution-id` | The ID of the solution that contains the connection references. |

[`PA_CLI_SOLUTION_ID`](environment-variables.md#solutions-connectors-and-data-sources) is the corresponding environmental variable to use with the `--solution-id`  parameter.

## `pa connection list-tables`

Lists tables available in a dataset.

```console
pa connection list-tables --connector <connector-id> [--connection-id <connection-id>] [--dataset <dataset>]
```

### `pa connection list-tables` parameters

| Parameter | Description |
| --- | --- |
| `--connector` | The connector identifier. |
| `--connection-id` | The connection ID to use when listing tables. |
| `--dataset` | The dataset that contains the tables. |

## `pa connector list`

Lists connectors available in the current Power Platform environment.

```console
pa connector list [--search <term>] [--json]
```

### `pa connector list` parameters

| Parameter | Description |
| --- | --- |
| `--search` | Filter connectors by name or display name. |
| `--json` | Return the complete connector list as JSON. |

[`PA_CLI_CONNECTOR_SEARCH`](environment-variables.md#solutions-connectors-and-data-sources) is the corresponding environmental variable to use with the `--search` parameter.


### `pa connector list` output

In an interactive terminal, results appear in pages of 20 rows. Press <kbd>Enter</kbd> to show the next page. Press <kbd>Esc</kbd> or <kbd>Q</kbd> to exit. When you redirect the output or include `--json`, the command returns the complete list.

By default, the command returns a table with the following columns:

| Column | Description |
| --- | --- |
| Display Name | The connector's display name, such as *Office 365 Outlook*. |
| Connector | The connector identifier, such as `shared_office365`. Use this value with the `--connector` option of [`pa connection create`](#pa-connection-create). |

When you use the `--json` parameter, the JSON output includes the following fields:

| Field | Description |
| --- | --- |
| `id` | The connector ID. |
| `name` | The connector identifier, such as `shared_office365`. |
| `displayName` | The connector display name. |
| `description` | The connector description. |
| `isTabular` | Indicates whether the connector supports tabular data operations. |


### `pa connector list` examples

List all available connectors:

```bash
pa connector list
```

Search for connectors:

```bash
pa connector list --search teams
```

Return the connector list as JSON:

```bash
pa connector list --json
```

[Learn how to list available connectors](../how-to/create-connection.md#step-1-list-available-connectors)

## `pa solution list`

Lists solutions in the current environment, including their friendly name, unique name, and solution ID.

```console
pa solution list [--search <term>] [--json]
```

### `pa solution list` parameters

| Parameter | Description |
| --- | --- |
| `--search` | Filter solutions by friendly name or unique name. The filter is a case-insensitive substring match. |
| `--json` | Return the complete solution list as JSON. |

[`PA_CLI_SOLUTION_SEARCH`](environment-variables.md#solutions-connectors-and-data-sources) is the corresponding environmental variable for the `--search` parameter.

In an interactive terminal, results appear in pages of 20 rows. Press <kbd>Enter</kbd> to show the next page. Press <kbd>Esc</kbd> or <kbd>Q</kbd> to exit. When you redirect the output or include `--json`, the command returns the complete list.

## `pa telemetry disable`

Disables telemetry collection.

```console
pa telemetry disable
```

## `pa telemetry enable`

Enables telemetry collection.

```console
pa telemetry enable
```

## `pa telemetry status`

Displays the current telemetry settings.

```console
pa telemetry status
```

## Related information

- [Power Apps CLI environment variables](environment-variables.md)
- [Quickstart: Create a code app using the Power Apps CLI](../how-to/create-an-app-from-scratch.md)
- [Sign in and manage accounts with the Power Apps CLI](../how-to/sign-in-manage-accounts.md)
- [Add data sources to your code app](../how-to/connect-to-data.md)
