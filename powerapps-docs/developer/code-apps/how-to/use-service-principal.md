---
title: Publish Power Apps Code Apps with a Service Principal
description: Learn how to share a Power Apps code app with a service principal and publish updates noninteractively in CI/CD pipelines. Follow these steps to get started.
#customer intent: As a developer, I want to use a service principal to publish code app updates from an automated process.
ms.topic: how-to
ms.service: powerapps
ms.subservice: code-apps
ms.author: jordanchodak
ms.reviewer: jdaly
author: jordanchodakWork
ms.date: 08/26/2026
---

# Publish Power Apps code apps with a service principal

Use a Microsoft Entra service principal to authenticate the Power Apps CLI without opening a browser or using a cached user account. This authentication method is useful for continuous integration and continuous delivery (CI/CD) pipelines and other automated processes that publish updates to an existing code app.

To publish an update, the service principal needs access to the target Power Platform environment and **edit** access to the code app. Environment-level permissions alone don't grant permission to update an existing app. App sharing and service principal authentication are separate features, but sharing the app is a prerequisite for publishing updates as the service principal.

> [!IMPORTANT]
> An app maker must share the app with the service principal before the service principal publishes its first update. Sharing is a one-time prerequisite, not part of the recurring publish process. A service principal can't grant itself access.

## Prerequisites

- A Power Apps code app that you already published
- An app maker account that has permission to share the app
- A Microsoft Entra service principal that has access to the target Power Platform environment

- These service principal values:
  - Application (client) ID
  - Client secret
  - Directory (tenant) ID
  - Enterprise Application object ID

## Understand the service principal identifiers

Microsoft Entra ID provides several identifiers for an app registration and its service principal. Use the correct identifier for each operation.

| Identifier | Where to find it | How it's used |
| --- | --- | --- |
| Application (client) ID | **App registrations** | Set the `PA_CLI_SP_CLIENT_ID` environment variable. |
| Directory (tenant) ID | **App registrations** | Set the `PA_CLI_SP_TENANT_ID` environment variable. |
| Enterprise Application object ID | **Enterprise applications** | Pass to [`pa app share --principal`](../reference/cli.md#pa-app-share). |

## Prerequisite: Share the app with the service principal

If the app already has **edit** access for the service principal, skip this section. Otherwise, complete these steps once from the app maker's computer. Don't include the sharing command in the CI/CD pipeline.

> [!IMPORTANT]
> Don't use the **Object ID** shown in **App registrations** in the Microsoft Entra admin center, where you find the application (client) ID, directory (tenant) ID, and client secret. Use the **Object ID** shown in **Enterprise applications** instead.
>
> Alternatively, if you know the application (client) ID, retrieve the Enterprise Application object ID by using the Azure CLI [`az ad sp show` command](/cli/azure/ad/sp#az-ad-sp-show):
>
> ```azurecli
> az ad sp show --id <application-client-id> --query id --output tsv
> ```

### Sign in as the app maker and share the code app

Don't enable service principal authentication when sharing the app.

Sign in interactively with the app maker account using the [`pa auth login` command](../reference/cli.md#pa-auth-login):

```console
pa auth login --account <maker-email>
```

Confirm that the app maker account is active using the [`pa auth status` command](../reference/cli.md#pa-auth-status):

```console
pa auth status
```

From the app folder, grant the service principal **edit** access using the [`pa app share` command](../reference/cli.md#pa-app-share):

```console
pa app share --principal <enterprise-application-object-id> --access edit
```

The `edit` access level grants the service principal permission to update the app by using the [`pa app push` command](../reference/cli.md#pa-app-push).

To grant permission to play the app without updating it, use `--access play`:

```console
pa app share --principal <enterprise-application-object-id> --access play
```

## Publish updates as the service principal

After the app has **edit** access for the service principal, use the service principal to publish updates from a CI/CD pipeline or a local computer. Repeat this procedure for each update. You don't need to share the app again unless the service principal's access is removed.

### Configure service principal authentication

Set the service principal authentication environment variables in the CI/CD job or terminal session that you use to publish the update. These variables cause the CLI to authenticate as the service principal instead of using a cached interactive account.


#### [PowerShell](#tab/ps)

```powershell
$env:PA_CLI_USE_SP_AUTH = "true"
$env:PA_CLI_SP_CLIENT_ID = "<application-client-id>"
$env:PA_CLI_SP_CLIENT_SECRET = "<client-secret>"
$env:PA_CLI_SP_TENANT_ID = "<tenant-id>"
```

#### [Bash](#tab/bash)

```bash
export PA_CLI_USE_SP_AUTH=true
export PA_CLI_SP_CLIENT_ID="<application-client-id>"
export PA_CLI_SP_CLIENT_SECRET="<client-secret>"
export PA_CLI_SP_TENANT_ID="<tenant-id>"
```

---

After you set the variables, run the build and publish commands from that terminal session or CI/CD job.

### Build and publish the update

Build the app by using the command configured for your project. For example:

```bash
npm run build
```

Publish the compiled app in noninteractive mode using the [`pa app push` command](../reference/cli.md#pa-app-push)

```console
pa app push --non-interactive
```

The CLI uses the service principal credentials from the environment variables and doesn't open a browser or use a cached interactive account.

When the command finishes, an exit code of `0` indicates that the update was published. A nonzero exit code indicates that the command failed.

## Related information

- [Power Apps CLI command reference](../reference/cli.md)
- [Application lifecycle management (ALM) for code apps](alm.md)
- [Sign in and manage accounts with the Power Apps CLI](sign-in-manage-accounts.md)

