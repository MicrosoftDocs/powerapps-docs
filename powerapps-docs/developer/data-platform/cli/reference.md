---
title: Dataverse CLI Reference (preview)
description: Discover the commands you can use with the Dataverse CLI
ms.date: 07/31/2026
ms.reviewer: jdaly
ms.topic: reference
author: kewear
ms.author: kewear
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - arorashivam96
---
# Dataverse CLI reference (preview)

> [!NOTE]
> - This is a preview feature.
> - [!INCLUDE [cc-preview-features-definition](../../../includes/cc-preview-features-definition.md)]


This article describes the commands available in the [Dataverse CLI](index.md). Every command supports a `--help` option that lists its usage, options, and examples. Commands that return data support a `--json` option for raw JSON output that's useful in scripts.

The following global options can be used with any command:

|Option|Description|
|---|---|
|`--log-level <level>`|Set the logging level: `Trace`, `Debug`, `Information`, `Warning`, `Error`, or `Critical`. Default: `Warning`.|
|`--log-file`|Log to a file in the temporary directory instead of the console.|
|`--context <value>`|Operation context appended to the User-Agent. You can also set the `DATAVERSE_OPERATION_CONTEXT` environment variable.|

| Command | Description |
|---|---|
|[`api describe`](#api-describe-command)|Describe an API|
|[`api invoke`](#api-invoke-command)|Invoke an API by name|
|[`api list`](#api-list-command)|List discoverable APIs|
|[`api request`](#api-request-command)|Send an authenticated HTTP request|
|[`auth create`](#auth-create-command)|Create a new authentication profile|
|[`auth list`](#auth-list-command)|List all authentication profiles|
|[`auth remove`](#auth-remove-command)|Remove an authentication profile|
|[`auth select`](#auth-select-command)|Select the active authentication profile|
|[`auth who`](#auth-who-command)|Show the current authentication profile|
|[`data associate`](#data-associate-command)|Link two records via a relationship|
|[`data count`](#data-count-command)|Count records in a table|
|[`data create`](#data-create-command)|Create a new record|
|[`data delete`](#data-delete-command)|Delete a record|
|[`data describe`](#data-describe-command)|Describe an entity's schema|
|[`data disassociate`](#data-disassociate-command)|Remove a relationship between two records|
|[`data get`](#data-get-command)|Retrieve a single record by ID or alternate key|
|[`data query`](#data-query-command)|Execute an OData, FetchXML, or SQL query|
|[`data update`](#data-update-command)|Update an existing record|
|[`data upload`](#data-upload-command)|Upload a file to a file column on an existing record|
|[`data upsert`](#data-upsert-command)|Create or update a record by alternate key|
|[`erp batch cancel`](#erp-batch-cancel-command)|Cancel a Finance and Operations batch job|
|[`erp batch list`](#erp-batch-list-command)|List Finance and Operations batch jobs|
|[`install`](#install-command)|Install a specific version, or update to the latest version|
|[`mcp`](#mcp-command)|Start the MCP server for Dataverse or ERP|
|[`mcp allow`](#mcp-allow-command)|Allow an app as an MCP client|
|[`org list`](#org-list-command)|List all accessible environments|
|[`org who`](#org-who-command)|Show current organization and user info|
|[`skill delete`](#skill-delete-command)|Delete a skill from Dataverse|
|[`skill download`](#skill-download-command)|Download a skill from Dataverse|
|[`skill list`](#skill-list-command)|List active skills in the environment|
|[`skill upload`](#skill-upload-command)|Upload a skill to Dataverse|

> [!NOTE]
> Many commands support a `--target <dataverse\|erp>` option that routes the operation to Dataverse (the default) or to the linked Finance and Operations (ERP) environment. Commands that connect to an environment support an `--environment <url>` (`-env`) option to override the current profile's environment URL.

## `api describe` command

Show the metadata for a single API. For Dataverse custom APIs, the output includes request parameter and response property descriptions when the metadata provides them.

Dataverse names are unprefixed by default. You can use ERP-qualified names in the form `erp:ServiceGroup/Service/Operation`.

### `api describe` parameters

| Parameter | Description |
|---|---|
|`--target`|Resolve an unqualified name against `dataverse` or `erp`.|
|`--service-group`|ERP only. Narrow the operation lookup to one service group.|
|`--service`|ERP only. Narrow the operation lookup to one service.|
|`--environment`|Override the Dataverse environment URL.|
|`--json`|Output raw JSON.|

### `api describe` examples

```powershell
dataverse api describe sample_CustomAPIExample
dataverse api describe msdyn_DoesKBExist
dataverse api describe GetUserSessionInfo --target erp --service-group UserSessionService --service AifUserSessionService
```

## `api invoke` command

Invoke a discovered API by name. Use `name=value` syntax for parameters. If a value contains spaces, quote the whole token. Some Dataverse APIs accept a string parameter whose contents are themselves JSON. In that case, pass the JSON text as the value by using your shell's normal quoting and escaping rules.

By default, JSON responses are rendered in a friendly text format that keeps the output property names. Use `--json` to preserve the raw JSON payload.

### `api invoke` parameters

| Parameter | Description |
|---|---|
|`--target`|Resolve an unqualified name against `dataverse` or `erp`.|
|`--service-group`|ERP only. Narrow the operation lookup to one service group.|
|`--service`|ERP only. Narrow the operation lookup to one service.|
|`--param`|Add a named parameter in `name=value` form. Repeatable.|
|`--bind`|The binding path for entity-bound Dataverse APIs.|
|`--method`, `-X`|Override the inferred HTTP method.|
|`--body`|Use a raw JSON body instead of named parameters.|
|`--body-file`|Read a raw JSON body from a file.|
|`--header`, `-H`|Add an HTTP header in `key:value` form.|
|`--include`, `-i`|Include the response status and headers.|
|`--environment`|Override the Dataverse environment URL.|
|`--json`|Output raw JSON instead of friendly text.|

### `api invoke` examples

Invoke a Dataverse function. This example shows the use of the Dynamics 365 Contact Center [CCaaS_GetPresence](/dynamics365/contact-center/extend/api/ccaas_getpresence) function.

```powershell
dataverse api invoke CCaaS_GetPresence ApiVersion=1.0
```

Invoke the Dataverse [AISummarize action](/power-apps/developer/data-platform/webapi/reference/aisummarize) with spaces in a parameter value:

```powershell
dataverse api invoke AISummarize "Text=The customer reported intermittent login failures..."
```

Invoke an ERP custom service:

```powershell
dataverse api invoke GetUserSessionInfo --target erp --service-group UserSessionService --service AifUserSessionService
```

## `api list` command

List discoverable APIs, such as Dataverse custom APIs and ERP invocable service endpoints. Results show the API identity, friendly name, kind, and description when available. You can pass an optional query term to filter the results.

### `api list` parameters

| Parameter | Description |
|---|---|
|`--target`|The target system to search: `dataverse` (default) or `erp`.|
|`--service-group`|ERP only. Filter to a single service group.|
|`--service`|ERP only. Filter to a single service.|
|`--limit`|The maximum number of APIs to return. Default: `50`.|
|`--page`|The 1-based page number when paging through results. Default: `1`.|
|`--environment`|Override the Dataverse environment URL.|
|`--json`|Output raw JSON.|

### `api list` examples

```powershell
dataverse api list
dataverse api list invoice --target dataverse
dataverse api list --target erp GetUserSessionInfo
dataverse api list --target erp --service-group UserSessionService --service AifUserSessionService
```

## `api request` command

Send a raw authenticated HTTP request to Dataverse or ERP. Use this command when you need full control over the path, method, headers, and body.

### `api request` parameters

| Parameter | Description |
|---|---|
|`--target`|The target system: `dataverse` or `erp`. Required.|
|`--path`|The request path. Required.|
|`--method`, `-X`|The HTTP method. Default: `GET`, or `POST` when a body is supplied.|
|`--body`|An inline JSON request body.|
|`--body-file`|A file that contains a JSON object request body.|
|`--header`, `-H`|Add an HTTP header in `key:value` form.|
|`--include`, `-i`|Include the response status and headers.|
|`--environment`|Override the Dataverse environment URL.|

### `api request` examples

```powershell
dataverse api request --target dataverse --path /api/data/v9.2/sample_CustomAPIExample --body "{\"Input\":\"value\"}"
dataverse api request --target erp --path /api/services/UserSessionService/AifUserSessionService/GetUserSessionInfo --body "{}"
```

## `auth create` command

Create a new authentication profile.

### `auth create` parameters

Use these parameters to specify the behavior of the `auth create` command.

| Parameter | Description |
|---|---|
|`--environment`, `-env`|The URL for the Dataverse environment you want to authenticate with.|
|`--name`, `-n`|An optional name for the profile. Use the name to select the profile later.|
|`--cloud`, `-ci`|The target cloud: `Public`, `UsGov`, `UsGovHigh`, `UsGovDod`, or `China`.|
|`--deviceCode`, `-dc`|Use the device code authentication flow, for environments without a browser.|
|`--username`, `-un`|The username for username and password authentication.|
|`--password`, `-p`|The password for username and password authentication.|
|`--applicationId`, `-id`|The application (client) ID for service principal (SPN) authentication.|
|`--clientSecret`, `-cs`|The client secret for service principal authentication.|
|`--certificateDiskPath`, `-cdp`|The path to a *.pfx* certificate file for certificate-based authentication.|
|`--certificatePassword`, `-cp`|The password for the certificate.|
|`--tenant`, `-t`|The tenant ID. Required for service principal authentication.|
|`--managedIdentity`, `-mi`|Use an Azure managed identity.|
|`--githubFederated`, `-ghf`|Use GitHub Actions federated authentication.|
|`--azureDevOpsFederated`, `-adof`|Use Azure DevOps federated authentication.|
|`--clientid`, `-cid`|A custom Microsoft Entra app client ID to use instead of the default Dataverse CLI app.|
|`--no-default-environment`|Don't set the environment as the default.|
|`--accept-cleartext-caching`|Allow a plaintext token cache on Linux.|


### `auth create` examples

The following examples demonstrate how to use the `auth create` command.

#### Interactive authentication

This command opens a browser or system dialog for additional information.

```powershell
dataverse auth create --environment https://myorg.crm.dynamics.com
```

#### Named profile

Create a profile with a specific name.

```powershell
dataverse auth create --environment https://myorg.crm.dynamics.com --name prod
```

#### Device code flow 

Use the device code flow for environments without a browser.

```powershell
dataverse auth create --environment https://myorg.crm.dynamics.com --deviceCode
```

#### Service principal with client secret

Use a service principal when you need unattended authentication, such as in a CI/CD pipeline or another automated script where interactive sign-in isn't possible. Provide the application ID, client secret, and tenant ID of an app registration that has access to the environment.

```powershell
dataverse auth create --applicationId <appId> --clientSecret <secret> --tenant <tenantId>
```

#### Custom Entra app client ID

Use your own app registration instead of the default.

```powershell
dataverse auth create --environment https://myorg.crm.dynamics.com --clientid <your-app-guid>
```


## `auth list` command

List all authentication profiles. Add `--json` for raw JSON output.

### `auth list` examples

```powershell
dataverse auth list
dataverse auth list --json
```

## `auth remove` command

Remove one or all authentication profiles.

### `auth remove` parameters

| Parameter | Description |
|---|---|
|`--index`, `-i`|Remove the profile with the specified 1-based index, as shown in `auth list`.|
|`--name`, `-n`|Remove the profile with the specified name.|
|`--all`|Remove all profiles.|

### `auth remove` examples

```powershell
dataverse auth remove --index 1
dataverse auth remove --name prod
dataverse auth remove --all
```

## `auth select` command

Select the active authentication profile. Run the command without options to list all profiles.

### `auth select` parameters

| Parameter | Description |
|---|---|
|`--index`, `-i`|Select the profile by its 1-based index, as shown in `auth list`.|
|`--name`, `-n`|Select the profile by name.|

### `auth select` examples

Open an interactive picker. Use the arrow keys, or type to filter:

```powershell
dataverse auth select
```

Select a profile by index or by name:

```powershell
dataverse auth select --index 1
dataverse auth select --name prod
```

## `auth who` command

Show the current, active authentication profile. Add `--json` for raw JSON output.

### `auth who` examples

```powershell
dataverse auth who
dataverse auth who --json
```

## `data associate` command

Associate two records through a navigation property (relationship). This command is supported for Dataverse only.

### `data associate` parameters

| Parameter | Description |
|---|---|
|`--table`, `-t`|The entity set name of the primary record. Required.|
|`--id`, `-i`|The GUID of the primary record. Required.|
|`--relationship`, `-rel`|The navigation property name. Required.|
|`--related`|The entity set name of the related table. Required.|
|`--related-id`|The GUID of the related record. Required.|
|`--environment`, `-env`|Override the environment URL.|
|`--json`|Output raw JSON.|

### `data associate` examples

```powershell
dataverse data associate --table accounts --id <guid> --relationship contact_customer_accounts --related contacts --related-id <related-guid>
```

## `data count` command

Count the records in a table, optionally filtered.

### `data count` parameters

| Parameter | Description |
|---|---|
|`--table`, `-t`|The entity set name. Required unless you use `--fetchxml`.|
|`--filter`, `-f`|An OData `$filter` expression.|
|`--fetchxml`|A FetchXML aggregate query for complex counts.|
|`--target`|Route to `dataverse` (default) or the linked `erp` environment.|
|`--cross-company`|ERP only. Count across all companies. Default: the user's default company.|
|`--environment`, `-env`|Override the environment URL.|
|`--json`|Output raw JSON.|

### `data count` examples

```powershell
dataverse data count --table accounts
dataverse data count --target erp --table Currencies --filter "CurrencyCode eq 'AED'"
```

## `data create` command

Create a new record in a Dataverse table. Set lookup columns by using `@odata.bind` syntax.

### `data create` parameters

| Parameter | Description |
|---|---|
|`--table`, `-t`|The entity set name. Required.|
|`--data`, `-d`|A JSON object with the field values.|
|`--data-file`|The path to a JSON file with the record data.|
|`--return`, `-r`|Return the full created record.|
|`--target`|Route to `dataverse` (default) or the linked `erp` environment.|
|`--environment`, `-env`|Override the environment URL.|
|`--json`|Output raw JSON.|

### `data create` examples

```powershell
dataverse data create --table accounts --data '{"name":"Contoso"}'
dataverse data create --table contacts --data '{"firstname":"Alice","parentcustomerid_account@odata.bind":"accounts(<guid>)"}'
```

> [!TIP]
> Use `--data-file` for complex JSON. Use `--return --json` to get the full created record.

## `data delete` command

Delete a single record by its primary key or by an alternate key.

### `data delete` parameters

| Parameter | Description |
|---|---|
|`--table`, `-t`|The entity set name. Required.|
|`--id`, `-i`|The record GUID.|
|`--key`, `-k`|An alternate key.|
|`--no-confirm`|Skip the confirmation prompt.|
|`--target`|Route to `dataverse` (default) or the linked `erp` environment.|
|`--environment`, `-env`|Override the environment URL.|
|`--json`|Output raw JSON.|

### `data delete` examples

```powershell
dataverse data delete --table accounts --id 00000000-0000-0000-0000-000000000001 --no-confirm
```

## `data describe` command

Describe an OData entity's schema. For Dataverse, the command calls `EntityDefinitions(LogicalName='<table>')` with `$expand` driven by `--include`, plus a second call to `customapis` when `--include actions` is set. Built-in Dataverse actions such as `Assign` and `SetState` aren't enumerated. For ERP, a single call to `/Metadata/PublicEntities` returns properties, bound actions, and navigations together.

### `data describe` parameters

| Parameter | Description |
|---|---|
|`--target`|The target: `dataverse` (default) or `erp`.|
|`--table`, `-t`|Required. For Dataverse, the logical name, such as `account`. For ERP, the entity set name, such as `BatchJobs`.|
|`--include`|A comma-separated list of sections to include: `entity`, `properties`, `relations`, `actions`, or `all`. Aliases: `attributes`=`properties`, `relationships`=`relations`. Default for ERP: `all`. Default for Dataverse: `entity,properties`.|
|`--json`|Output raw JSON.|

### `data describe` examples

```powershell
dataverse data describe --table account
dataverse data describe --target dataverse --table account --include all
dataverse data describe --target erp --table BatchJobs
```

## `data disassociate` command

Remove a relationship between two records. This command is supported for Dataverse only.

### `data disassociate` parameters

| Parameter | Description |
|---|---|
|`--table`, `-t`|The entity set name of the primary record. Required.|
|`--id`, `-i`|The GUID of the primary record. Required.|
|`--relationship`, `-rel`|The navigation property name. Required.|
|`--related-id`|The GUID of the related record, for a many-to-many relationship. Omit this parameter to clear a lookup.|
|`--environment`, `-env`|Override the environment URL.|
|`--json`|Output raw JSON.|

### `data disassociate` examples

```powershell
dataverse data disassociate --table accounts --id <guid> --relationship contact_customer_accounts --related-id <related-guid>
```

## `data get` command

Retrieve a single record by its ID (primary key) or by an alternate key.

### `data get` parameters

| Parameter | Description |
|---|---|
|`--table`, `-t`|The entity set name. Required.|
|`--id`, `-i`|The record GUID (primary key).|
|`--key`, `-k`|An alternate key, for example `"col='val'"`.|
|`--select`, `-s`|A comma-separated list of columns (`$select`).|
|`--expand`, `-x`|An OData `$expand` expression for related records.|
|`--target`|Route to `dataverse` (default) or the linked `erp` environment.|
|`--environment`, `-env`|Override the environment URL.|
|`--json`|Output raw JSON.|

### `data get` examples

```powershell
dataverse data get --table accounts --id 00000000-0000-0000-0000-000000000001
dataverse data get --target erp --table Currencies --key "CurrencyCode='AED'" --select "CurrencyCode,Name"
```

## `data query` command

Execute an OData, FetchXML, or SQL query against a Dataverse table.

### `data query` parameters

| Parameter | Description |
|---|---|
|`--table`, `-t`|The entity set name to query. Required for OData queries.|
|`--select`, `-s`|A comma-separated list of columns (`$select`).|
|`--filter`, `-f`|An OData `$filter` expression.|
|`--orderby`, `-o`|An OData `$orderby` expression.|
|`--top`|The maximum number of records to return (1-5000).|
|`--expand`, `-x`|An OData `$expand` expression for related records.|
|`--fetchxml`|An inline FetchXML query.|
|`--fetchxml-file`|The path to a file that contains a FetchXML query.|
|`--sql`|A SQL `SELECT` query (preview).|
|`--sql-file`|The path to a file that contains a SQL query.|
|`--all`, `-a`|Follow pagination to retrieve all records.|
|`--max-records`|The maximum number of records to retrieve when using `--all`. Default: `100000`.|
|`--target`|Route to `dataverse` (default) or the linked `erp` environment.|
|`--cross-company`|ERP only. Query across all companies. Default: the user's default company.|
|`--environment`, `-env`|Override the environment URL.|
|`--json`|Output raw JSON.|

### `data query` examples

```powershell
dataverse data query --table accounts --select "name,revenue" --filter "revenue gt 1000000"
dataverse data query --fetchxml "<fetch><entity name='account'><attribute name='name'/></entity></fetch>"
dataverse data query --sql "SELECT name, revenue FROM account WHERE revenue > 1000000"
dataverse data query --target erp --table Currencies --select "CurrencyCode,Name" --top 10
```

### Learn more

- [Use OData to query data](../webapi/query/overview.md)
- [Query Data Using FetchXML in Dataverse](../fetchxml/overview.md)
- [Use SQL to query data by using the Dataverse Web API](../webapi/query/sql.md)

## `data update` command

Update one or more fields on an existing record, identified by its ID or by an alternate key. Set lookup columns by using `@odata.bind` syntax.

### `data update` parameters

| Parameter | Description |
|---|---|
|`--table`, `-t`|The entity set name. Required.|
|`--id`, `-i`|The record GUID.|
|`--key`, `-k`|An alternate key.|
|`--data`, `-d`|A JSON object with the fields to update.|
|`--data-file`|The path to a JSON file with the update data.|
|`--return`, `-r`|Return the full updated record.|
|`--target`|Route to `dataverse` (default) or the linked `erp` environment.|
|`--environment`, `-env`|Override the environment URL.|
|`--json`|Output raw JSON.|

### `data update` examples

```powershell
dataverse data update --table accounts --id 00000000-0000-0000-0000-000000000001 --data '{"name":"Contoso (updated)"}'
```

## `data upload` command

Upload a local file into a Dataverse file column on an existing record. The command automatically selects a single-request or chunked upload based on the file size, unless you specify `--mode`. In auto mode, files under 128 MB are uploaded in a single request, and larger files use a chunked upload. When you omit `--mime-type`, the command infers the MIME type from the file extension. Unknown extensions default to `application/octet-stream`.

### `data upload` parameters

| Parameter | Description |
|---|---|
|`--table`, `-t`|The table schema or logical name, such as `account`. Required. The command resolves the entity set from metadata.|
|`--id`, `-i`|The record GUID. Required.|
|`--column`, `-c`|The file column attribute name. Required.|
|`--file`, `-f`|The path to the local file. Required.|
|`--mode`, `-m`|The upload strategy: `auto` (default), `small`, or `chunk`.|
|`--mime-type`|An explicit MIME type. Default: inferred from the file extension.|
|`--overwrite`|Overwrite an existing file. By default, the command fails if the column isn't empty.|
|`--environment`, `-env`|Override the environment URL.|
|`--json`|Output raw JSON.|

### `data upload` examples

```powershell
dataverse data upload --table account --id <guid> --column new_document --file report.pdf
dataverse data upload -t account -i <guid> -c new_document -f photo.jpg --overwrite
dataverse data upload -t account -i <guid> -c new_document -f big.bin --mode chunk
```

## `data upsert` command

Create a record if it doesn't exist, or update it if it does. The record is identified by an alternate key. [Learn to use an alternate key to reference a record](../use-alternate-key-reference-record.md)

### `data upsert` parameters

| Parameter | Description |
|---|---|
|`--table`, `-t`|The entity set name. Required.|
|`--key`, `-k`|An alternate key. Required.|
|`--data`, `-d`|A JSON object with the field values.|
|`--data-file`|The path to a JSON file.|
|`--update-only`|Fail if the record doesn't exist (`If-Match: *`).|
|`--create-only`|Fail if the record already exists (`If-None-Match: *`).|
|`--return`, `-r`|Return the full record after the operation.|
|`--target`|Route to `dataverse` (default) or the linked `erp` environment.|
|`--environment`, `-env`|Override the environment URL.|
|`--json`|Output raw JSON.|

### `data upsert` examples

```powershell
dataverse data upsert --table accounts --key "accountnumber='ACC-100'" --data '{"name":"Contoso"}'
```


## `erp batch cancel` command

Cancel a Finance and Operations batch job by its `RecId`. Use [`erp batch list`](#erp-batch-list-command) to find the `RecId`.

### `erp batch cancel` examples

```powershell
dataverse erp batch cancel <recid>
```

## `erp batch list` command

List batch jobs on the Finance and Operations instance that's linked to your Dataverse environment. The command requires an authentication profile connected to a Dataverse environment that has a linked Finance and Operations instance. The Finance and Operations URL is derived automatically from the current Dataverse connection.

### `erp batch list` parameters

| Parameter | Description |
|---|---|
|`--company`|Filter by legal entity (`dataAreaId`), such as `USMF`.|
|`--status`|Filter by status: `Waiting`, `Executing`, `Finished`, `Error`, or `Cancelled`.|
|`--top`|The maximum number of results to return. Default: `20`.|
|`--caption`|Filter by caption (case-insensitive substring match).|
|`--json`|Output raw JSON.|

### `erp batch list` examples

```powershell
dataverse erp batch list
dataverse erp batch list --status Waiting
dataverse erp batch list --status Executing --top 20
```

## `install` command

Install a specific version of the Dataverse CLI, or update to the latest version. The command detects whether you installed the CLI globally or are using `npx` and installs accordingly.

### `install` examples

Install the latest version:

```powershell
dataverse install latest
```

Install a specific version:

```powershell
dataverse install 1.0.0
```

## `mcp` command

Starts a Model Context Protocol (MCP) server that connects to your environment, so that AI assistants such as Claude Desktop can interact with your data. The target is auto-detected from the URL: a Dataverse URL starts the Dataverse MCP server, and a Finance and Operations URL, such as `https://myorg.operations.dynamics.com`, starts the ERP MCP server.

### `mcp` syntax

```powershell
dataverse mcp <orgUrl> [options]
```

The `<orgUrl>` argument is your organization URL, for example `https://myorg.crm.dynamics.com`.

### `mcp` parameters

| Parameter | Description |
|---|---|
|`--validate`|Validate the MCP endpoints and authentication setup without starting the server.|
|`--log-level`|Set the logging level: `Trace`, `Debug`, `Information`, `Warning`, `Error`, or `Critical`. Default: `Warning`.|
|`--log-file`|Log to a file in the temporary directory.|
|`--preview`|Use the preview MCP endpoint (`api/mcp_preview` instead of `api/mcp`). Not supported for ERP.|

### `mcp` examples

Validate the setup (a recommended first step):

```powershell
dataverse mcp https://myorg.crm.dynamics.com --validate
```

Start the server by using the stdio transport:

```powershell
dataverse mcp https://myorg.crm.dynamics.com
```

Use the preview endpoint, or enable debug file logging:

```powershell
dataverse mcp https://myorg.crm.dynamics.com --preview
dataverse mcp https://myorg.crm.dynamics.com --log-level Debug --log-file
```

## `mcp allow` command

Ensure that a Microsoft Entra application is in the Dataverse MCP allowed clients list for the current profile's environment. This command is an alternative to the manual admin step described in the [prerequisites](index.md#prerequisites). The authenticated user must have Dataverse admin permissions on the target environment.

### `mcp allow` syntax

```powershell
dataverse mcp allow <appId> [options]
```

The `<appId>` argument is the application (client) ID to allow, as a GUID.

### `mcp allow` parameters

| Parameter | Description |
|---|---|
|`--erp`|Allow the application on the linked Finance and Operations instance instead of Dataverse.|

### `mcp allow` examples

```powershell
dataverse mcp allow 0c412cc3-0dd6-449b-987f-05b053db9457
dataverse mcp allow 0c412cc3-0dd6-449b-987f-05b053db9457 --erp
```

> [!NOTE]
> Finance and Operations caches the allowlist in the AOS, so a newly allowed app ID can take up to about five minutes to take effect.

## `org list` command

List all environments that you can access.

### `org list` parameters

| Parameter | Description |
|---|---|
|`--filter`|Filter the list of environments by a search term.|
|`--json`|Output raw JSON.|

### `org list` examples

```powershell
dataverse org list
dataverse org list --filter contoso
dataverse org list --json
```

## `org who` command

Show information about the current organization and user, using the active authentication profile. The `env` command is an alias for `org`.

### `org who` parameters

| Parameter | Description |
|---|---|
|`--environment`, `-env`|Override the environment URL.|
|`--json`|Output raw JSON.|

### `org who` examples

```powershell
dataverse org who
dataverse org who --environment https://myorg.crm.dynamics.com
dataverse org who --json
```

## `skill` commands

Manage Dataverse skills&mdash;reusable instruction sets (a `SKILL.md` file and its resource files) that AI agents use&mdash;that are stored in the connected environment. The top-level `skill` commands provide create, read, update, and delete operations against the environment. Locally, skills are stored under `.claude/skills/<name>/`.

> [!NOTE]
> Skill authoring and evaluation commands, such as `make`, `update`, `get`, and `eval`, are separate from these commands. For more information, run `dataverse workspace skill --help`.

### `skill delete` command

Delete a skill and all its resources from the active Dataverse environment. Use [`skill list`](#skill-list-command) to find skill unique names.

```powershell
dataverse skill delete new_lead-qualification
```

### `skill download` command

Download one or more skills from the active Dataverse environment to disk. The command downloads the `SKILL.md` file and all resource files, preserving the directory structure. Use [`skill list`](#skill-list-command) to find skill unique names.

|Parameter|Description|
|---|---|
|`--all`|Download all active skills from the environment. Can't be combined with a skill unique name.|
|`--output`, `-o`|The base directory for output. Default: `.claude/skills/`. With `--all`, each skill is written to `<path>/<name>/`.|
|`--json`|Output the skill content as JSON without writing files. Optionally specify a file path to write to.|

```powershell
dataverse skill download new_lead-qualification
dataverse skill download --all --output ./skills
```

### `skill list` command

List all active skills in the connected Dataverse environment.

|Parameter|Description|
|---|---|
|`--resources`, `-r`|Also list the resource files for each skill.|
|`--json`|Output as JSON. Optionally specify a file path to write to.|

```powershell
dataverse skill list
dataverse skill list --resources
```

### `skill upload` command

Upload one or more skills from disk to the active Dataverse environment. The command supports directories, *.zip* files, *.skill* files, and *.md* files.

You can pass a skill `<name>`, which resolves to `.claude/skills/<name>/`, or an explicit `<path>` to a directory or file.

|Parameter|Description|
|---|---|
|`--all`|Upload all skills under `.claude/skills/`. Can't be combined with a skill name or path.|
|`--json`|Output the result as JSON. Optionally specify a file path to write to.|

```powershell
dataverse skill upload lead-qualification
dataverse skill upload ./my-skill.zip
dataverse skill upload --all
```

### See also

[Work with data using the Dataverse CLI](index.md)

