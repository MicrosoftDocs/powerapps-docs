---
title: "How to: Sign in and manage accounts with the Power Apps CLI - Power Apps"
ms.topic: how-to
ms.service: powerapps
ms.subservice: code-apps
description: Learn how to sign in, check your status, switch between accounts, and sign out when you build Power Apps code apps with the npm-based Power Apps CLI.
#customer intent: As a developer, I want to know how to sign in, check my status, switch between accounts, and sign out when I build Power Apps code apps with the npm-based Power Apps CLI.
ms.author: jordanchodak
author: jordanchodakWork
ms.date: 06/19/2026
ms.reviewer: jdaly
---

# How to: Sign in and manage accounts with the Power Apps CLI

The npm-based Power Apps CLI includes commands to sign in, check which account is active, switch between accounts, and sign out. Use these commands to control which account the CLI uses when you initialize a code app, add data sources, and publish to Power Platform.

> [!NOTE]
> When you run `npx power-apps init`, the CLI signs you in automatically if you're not already signed in. Use the commands in this article when you want to sign in ahead of time, work with more than one account, or resolve authentication issues.

## Sign in

Use the `login` command to sign in interactively through your system browser.

```bash
npx power-apps login
```

The command always opens the browser, even if you're already signed in. This behavior lets you add another account. After you sign in, that account becomes the active account.

To prefill the username field in the browser, pass the `--account` flag with an email address:

```bash
npx power-apps login --account user@contoso.com
```

> [!NOTE]
> The `--account` value only pre-fills the email on the sign-in page. It doesn't check the email against accounts you're already signed in to.

## Check which account is active

Use the `auth-status` command to see which accounts you're signed in to and which one is active.

```bash
npx power-apps auth-status
```

What you see depends on how many accounts you're signed in to:

- **No accounts** – You aren't signed in yet.
- **One account** – The CLI shows `Signed in as <email>`.
- **Two or more accounts** – The CLI lists your accounts and marks the active one with an asterisk (`*`). If no account is active, it prompts you to run `auth-switch`.

## Switch the active account

If you're signed in to more than one account, use the `auth-switch` command to change which account is active. This command switches accounts without signing you in or out.

```bash
npx power-apps auth-switch
```

When you run the command without any flags, the CLI shows a picker where you can choose an account. To choose an account directly, pass the `--account` flag with the email address or account ID:

```bash
npx power-apps auth-switch --account user@contoso.com
```

What happens depends on how many accounts you're signed in to:

- **No accounts** – The CLI prompts you to run `login` first.
- **One account** – The CLI keeps that account active.
- **Two or more accounts** – The CLI shows the picker so you can choose. To skip the picker, pass `--account` with the email address or account ID.

## Sign out

Use the `logout` command to sign out and remove your saved sign-in information from your computer.

```bash
npx power-apps logout
```

If you're not signed in, the command still completes without an error.

> [!NOTE]
> The `logout` command signs you out of *all* accounts. It can't sign you out of just one account. To change which account is active, use `auth-switch` instead.

