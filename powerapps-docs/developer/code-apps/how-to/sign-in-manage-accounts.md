---
layout: Conceptual
title: "How to Sign in and manage accounts with the Power Apps CLI - Power Apps | Microsoft Learn"
ms.topic: how-to
description: Learn how to sign in, check your status, switch between accounts, and sign out when you build Power Apps code apps with the Power Apps CLI.
ms.author: jordanchodak
author: jordanchodakWork
ms.date: 08/03/2026
ms.reviewer: jdaly
---

# How to sign in and manage accounts with the Power Apps CLI

The Power Apps CLI includes commands to:

- [Sign in](#sign-in)
- [Check which account is active](#check-which-account-is-active)
- [Switch between accounts](#switch-the-active-account)
- [Sign out](#sign-out)

Use these commands to control which account the CLI uses when you:

- Initialize a code app
- Add data sources
- Publish to Power Platform

> [!NOTE]
> When you run [`pa app init`](../reference/cli.md#pa-app-init), the CLI signs you in automatically if you're not already signed in. Use the commands in this article when you want to sign in ahead of time, work with more than one account, or resolve authentication issues.

For a complete list of commands, see [Power Apps CLI command reference](../reference/cli.md).

## Sign in

Use the [`pa auth login`](../reference/cli.md#pa-auth-login) command to sign in interactively through your system browser.

```bash
pa auth login
```

The command always opens the browser, even if you're already signed in. This behavior lets you add another account. After you sign in, that account becomes the active account.

To prefill the username field in the browser, pass the `--account` option with an email address:

```bash
pa auth login --account user@contoso.com
```

> [!NOTE]
> The `--account` value only pre-fills the email on the sign-in page. It doesn't check the email against accounts you're already signed in to.

## Check which account is active

Use the [`pa auth status`](../reference/cli.md#pa-auth-status) command to see which accounts you're signed in to and which one is active.

```bash
pa auth status
```

What you see depends on how many accounts you're signed in to:

- **No accounts** - You aren't signed in yet.
- **One account** - The CLI shows `Signed in as <email>`.
- **Two or more accounts** - The CLI lists your accounts and marks the active one with an asterisk (`*`). If no account is active, it prompts you to run [`pa auth switch`](../reference/cli.md#pa-auth-switch).

## Switch the active account

If you're signed in to more than one account, use the [`pa auth switch`](../reference/cli.md#pa-auth-switch) command to change which account is active. This command switches accounts without signing you in or out.

```bash
pa auth switch
```

When you run the command without any options, the CLI shows a picker where you can choose an account. To choose an account directly, pass the `--account` option with the email address or account ID:

```bash
pa auth switch --account user@contoso.com
```

What happens depends on how many accounts you're signed in to:

- **No accounts** - The CLI prompts you to run [`pa auth login`](../reference/cli.md#pa-auth-login) first.
- **One account** - The CLI keeps that account active.
- **Two or more accounts** - The CLI shows the picker so you can choose. To skip the picker, pass `--account` with the email address or account ID.

## Sign out

Use the [`pa auth logout`](../reference/cli.md#pa-auth-logout) command to sign out and remove your saved sign-in information from your computer.

```bash
pa auth logout
```

If you're not signed in, the command still completes without an error.

> [!NOTE]
> The [`pa auth logout`](../reference/cli.md#pa-auth-logout) command signs you out of *all* accounts. It can't sign you out of just one account. To change which account is active, use [`pa auth switch`](../reference/cli.md#pa-auth-switch) instead.

## Related information

- [Power Apps CLI command reference](../reference/cli.md)
- [Quickstart: Create a code app by using the Power Apps CLI](npm-quickstart.md)
