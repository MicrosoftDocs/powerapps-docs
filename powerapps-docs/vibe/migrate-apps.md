---
title: Migrate apps created from Power Apps Vibe
description: Learn how to migrate an app you built in Power Apps Vibe, either with one-click migration to Apps in Copilot Studio or by downloading its source code and rebuilding it in Copilot Cowork or Apps in Copilot Studio.
author: szlo
ms.author: szlo
ms.reviewer: joshuapa
ms.date: 11/04/2026
ms.topic: how-to
contributor: joshuapartlow
---

# Migrate apps from Power Apps Vibe

Power Apps Vibe (https://vibe.powerapps.com) is retiring. You can keep editing your Vibe apps through November 30, 2026. Starting December 1, 2026, you won't be able to edit your apps in Power Apps Vibe, but you can still migrate them to Copilot Studio or Copilot Cowork, or download their source code.

> [!IMPORTANT]
> What changes after November 30, 2026
> - Through November 30, 2026: You can edit your apps in Power Apps Vibe, migrate them, and download their source code.
> - Starting December 1, 2026: You can no longer edit apps in Power Apps Vibe. For each app, you can:
>   - Migrate it, with one-click migration or manual migration, and keep building it in Apps in Copilot Studio or Copilot Cowork.
>   - Download its source code to keep a copy.
> - Anything that requires editing in Vibe, such as publishing draft tables, must be done by November 30, 2026.

## Choose how to migrate your app

There are two ways to migrate a Vibe app:

1. **[One-click migration](#option-1-one-click-migration)** (recommended): Select **Migrate app** in Power Apps Vibe to move your app from Vibe to Copilot Studio. You don't need to download source code or write a prompt.
1. **[Manual migration](#option-2-manual-migration)**: Download your app's source code, attach it to a migration prompt, and rebuild the app in **Apps in Copilot Studio** or **Copilot Cowork**.

Use this table to choose a migration path.

| Feature | One-click migration | Manual migration |
| --- | --- | --- |
| Where you start | Power Apps Vibe | Power Apps Vibe |
| Where your new app lives | Apps in Copilot Studio | Apps in Copilot Studio or Copilot Cowork, your choice |
| Download source code | Not needed | Required. You attach the .zip file to a prompt. |
| Write a migration prompt | Not needed | Required |
| Billing | Copilot Credits | Copilot Credits |

With either path, the new app is separate from your original app. Keep your original app until you confirm that the new app works as expected.

## Before you migrate

### Prerequisites

The prerequisites depend on where your new app lives. One-click migration moves your app from Vibe to Copilot Studio. With manual migration, you can choose between Copilot Studio or Copilot Cowork.

| Requirement | Apps in Copilot Studio (one-click or manual migration) | Copilot Cowork (manual migration only) |
| --- | --- | --- |
| Program participation | Your organization participates in the public preview of apps in Copilot Studio. | Your organization participates in the [Frontier program](https://www.microsoft.com/copilot/resources/frontier-program). |
| Access and licensing | Access to Copilot Studio, with app creation turned on. The **App (Preview)** tile is on by default, but your admin can turn it off. | A Microsoft 365 Copilot license, with Copilot Cowork turned on for your organization. |
| Billing | Copilot Credits. Usage-based billing applies to using, building, previewing, and testing apps. For more information, see [Overview of usage-based billing](/microsoft-copilot-studio/agents-experience/billing-credit-overview). | Copilot Credits. Building apps consumes Copilot Credits. For more information, see [Usage-based billing and cost management for Copilot Credits](/microsoft-365/copilot/usage-based-billing-overview-copilot-credits). |
| Environment | Permission to create apps in your personal developer environment (PDE), where apps are built by default. | Permission to create apps in your personal developer environment (PDE), where apps are built by default. |

If your organization doesn't allow you to create a personal developer environment, see [Troubleshooting](#troubleshooting). For more information about apps in Copilot Studio, see [Apps overview (preview)](/microsoft-copilot-studio/apps-experience/apps-overview).

> [!IMPORTANT]
> Apps in Copilot Studio is in public preview. Preview features aren't meant for production use and might have restricted functionality.

## Option 1: One-click migration

By using one-click migration, you can move an app that you built in Power Apps Vibe to Copilot Studio, directly from Vibe. After migration, you can chat with an agent in Copilot Studio to update, publish, and share your app. 

### How one-click migration works

One-click migration creates a new app in Copilot Studio from your Vibe app. Your original app stays in Power Apps Vibe, unchanged, until Vibe is officially retired.

1. **Check the prerequisites.** Ensure you can create apps in Copilot Studio and edit your app in Power Apps Vibe.
1. **Migrate your app.** Open your app for editing in Power Apps Vibe, and confirm the migration in the dialog that appears.
1. **Review your migrated app.** Open the new app in Copilot Studio, and compare it with your original app.
1. **Verify your data connections.** Confirm that the new app uses your existing data, not sample data.
1. **Publish and share your app.** Publish the new app, and share it with the people who use your original app.

| Part of your app | What happens during one-click migration |
| --- | --- |
| Screens, navigation, components, and logic | Migrated from your app's source code. |
| Data in Dataverse tables or SharePoint lists | Stays where it is. Your new app connects to the same data. |
| Data connections | Reconnected automatically during migration. |
| Environment | Created in your Personal Developer Environment. |
| Sharing and app links | Not carried over. Share your new app after you publish it. |
| Sharing restrictions | Your admin's sharing policies for your app's environment apply. |
| Your original Vibe app | Not changed. |

### Prerequisites for one-click migration

Before you migrate your app, ensure that:

- **You meet the [prerequisites](#prerequisites) for Apps in Copilot Studio.**
- **Personal developer environment (PDE) enabled.** One-click migration automatically routes your new app to your (PDE). Migration will fail if PDE is disabled by your admin. 
- **You can edit the app in Power Apps Vibe.** One-click migration is available only to people who can edit the app, which is usually the app's original author.
- **You have access to the Dataverse tables or SharePoint lists that your app uses.**

### Migrate your app with one click

1. Sign in to [Power Apps Vibe](https://vibe.powerapps.com).
1. Open your app, and then select **Edit**. A migration dialog appears.
1. In the migration dialog, review the details, and then select **Yes, migrate**.

   > [!TIP]
   > If you closed the migration dialog, select **Migrate app** in the command bar to start the migration process.

1. Wait while your app migrates. Don't close the browser tab until migration finishes. Migration takes several minutes.
1. When migration finishes, a message confirms that your app was migrated successfully. To open your app in Copilot Studio for editing, follow the steps in [Review your migrated app in Copilot Studio](#review-your-migrated-app-in-copilot-studio).

### Review your migrated app in Copilot Studio

When migration finishes, Power Apps Vibe shows a message that your app was migrated successfully. The message includes a prompt that loads your app in Copilot Studio so you can continue editing it. From now on, you edit your app in Copilot Studio, not in Power Apps Vibe.

1. In the migration message, copy the prompt exactly as it appears.
1. Select **Microsoft Copilot Studio** link in the dialog, which opens Copilot Studio in a new tab with a prompt input box. 

   You can also sign in to [Copilot Studio](https://copilotstudio.microsoft.com), ensure the **New experience** toggle is on, and then select the **App** tile.

1. Paste the prompt that you copied into the message box, and then select **Submit**. The prompt includes your app's name and the name and ID of its environment, such as:

   ```text
   Load app <app name> in environment <environment name> <environment ID>
   ```

1. Once your app is loaded in Copilot studio, test your app in the preview.
1. From the app's dropdown menu, review **Data** and **Connections** to confirm that the app uses your existing tables or lists.
1. Compare the new app with your original app in Power Apps Vibe. Check every screen, field, label, button, and rule.
1. If something is missing or different, describe the change in the message box. For example prompts, see [Refine your migrated app](#refine-your-migrated-app).
1. When your app is ready, [publish and share it](#publish-and-share-in-copilot-studio).

For next steps, including how to verify your data, publish and share your app, and edit it later, see [After you migrate](#after-you-migrate).

> [!IMPORTANT]
> **Known issue:** If your migrated app is in an environment other than your personal developer environment, you might not be able to open it from the app list in Copilot Studio. A fix is rolling out over the next week starting November 16th.
>
> Until the fix reaches your region, open your app from Copilot Studio Preview:
>
> 1. Go to [https://copilotstudio.preview.microsoft.com](https://copilotstudio.preview.microsoft.com), and sign in with your work account.
> 2. In the left navigation pane, select **Apps (Preview)**.
> 3. Select your app to open it.

## Option 2: Manual migration

To migrate an app manually, download its source code, and then ask the agent to rebuild the app from it by attaching the code file. With manual migration, you choose where to rebuild your app: Apps in Copilot Studio or Copilot Cowork.

Use manual migration if you want to rebuild your Vibe app in Copilot Cowork, if one-click migration isn't available to you yet, or if one-click migration doesn't work for your app.

### How manual migration works

Manual migration rebuilds your app instead of moving it. You attach your app's source code to a prompt, and the agent builds a new app that matches the original as closely as possible.

1. **Prepare your data.** Publish any draft tables, and collect the details the agent needs to connect to your data. For details, see [Prepare your data](#prepare-your-data).
1. **Download your app's source code** from Power Apps Vibe.
1. **Rebuild your app** in Apps in Copilot Studio or Copilot Cowork by attaching the source code to a migration prompt.
1. **Review, publish, and share** your new app.

| Part of your app | What happens during manual migration |
| --- | --- |
| Screens, navigation, components, and logic | Rebuilt from your source code. |
| Data in Dataverse tables or SharePoint lists | Stays where it is. Your new app connects to the same data. |
| Draft tables | Not migrated. Publish them before you migrate. |
| Data connections | Not carried over. The agent connects your new app to your data. |
| Sharing restrictions | Your admin's sharing policies for your app's environment apply. For example, your admin can turn off sharing by link, with guests, or with groups, and can limit how many people you share an app with. |

### Choose where to rebuild your app

In both experiences, you attach your source code to a prompt, and an agent rebuilds the app. Use this table to choose where to rebuild. For the full requirements, see [Prerequisites](#prerequisites).

| Consideration | Apps in Copilot Studio | Copilot Cowork |
| --- | --- | --- |
| Where you build | Copilot Studio | Microsoft Copilot |
| Availability | Public preview | Frontier program only |
| Licensing | Access to Copilot Studio | Microsoft 365 Copilot license |
| Billing | Copilot Credits | Copilot Credits |
| Share your app | With specific people or groups | With a link, to people in your organization who can use Microsoft Copilot |

### Prepare your data

Your data stays where it is during migration, but your new app needs to connect to it. Before you rebuild your app, publish any draft tables, and collect the details that identify your data.

#### Publish draft tables in Vibe

Draft tables exist in memory only and aren't published to a data source until you explicitly publish them. Unpublished draft tables aren't migrated with your app.

1. Sign in to [Power Apps Vibe](https://vibe.powerapps.com), and open your app for editing.
1. Select **Publish**.
1. In the **Publish** menu, under **Data environment**, choose the environment where you want to publish your tables. You publish your Dataverse tables in the same environment as your app.

#### Collect your data details

Collect these details for your migration prompt. If your prompt doesn't name your data, the agent might create sample data instead of connecting to your existing data.

**If your app uses Dataverse tables:**

- **Environment ID**: The ID of the environment that contains your tables, such as `aaaabbbb-0000-cccc-1111-dddd2222eeee`. To find it, use one of these methods:
  - In the Power Platform admin center, select **Manage** > **Environments**, select your environment, and then copy the **Environment ID** from the **Details** section.
  - In [Power Apps](https://make.powerapps.com), select **Settings** (gear icon) > **Session details**, and then copy the **Environment ID** value.
  - If you downloaded your app's source code, use the `environmentId` value in the `power.config.json` file.

  For more information, see [Find your environment and organization IDs and organization name](/power-platform/admin/determine-org-id-name).
- **Table logical names**: The logical name of each table that your app uses, such as `cr8a1_inspection`. In [Power Apps](https://make.powerapps.com), select **Tables**, open the table, and then select **Tools** > **Copy logical name**.

> [!NOTE]
> If your environment ID starts with `Default-`, your tables are in your organization's default environment. Rebuilt apps can't connect to Dataverse tables in the default environment yet.

**If your app uses SharePoint lists:**

- **Site URL**: The address of the SharePoint site that contains your lists, such as `https://contoso.sharepoint.com/sites/Operations`. If you have the URL of a list, use the part before `/Lists/`.
- **List names**: The name of each list that your app uses.

Ensure you have access to the tables or lists that your app uses.

### Download your app's source code

1. Sign in to [Power Apps Vibe](https://vibe.powerapps.com).
1. Open your app, and then select **Edit**.
1. On the command bar, select **Download source**.

Your app's source code downloads as a .zip file. You attach this file to your migration prompt, so don't extract it.

### Write your migration prompt

The agent uses attached files as reference material, not as instructions. Your prompt tells the agent what to build and how to use your source code. A good migration prompt:

- Says that you're migrating your own app.
- Describes what the app does, even though the source code is attached.
- Tells the agent exactly which data to connect to.
- Ends with instructions to rebuild the app from the exact source code.

Copy the following template, and replace the placeholders in angle brackets (`<>`). Keep the last three paragraphs as they are.

```text
I'm migrating my app, <app name>, from Power Apps Vibe. I built this app, and the attached .zip file contains its complete source code. Name the new app <app name>.

<App name> helps <who uses the app> <do what>. It has these screens: <screen names>. Users can <main tasks, such as creating, updating, and approving records>.

<Data instruction. Choose one from the "Data instructions" section.>

Rebuild this app by referencing the exact source code in the attached .zip file. Before you start, extract the .zip file and read every file, including pages, components, styles, and configuration files. Treat the source code as the specification, and make the new app match the original as exactly as possible:
- Keep the same screens, navigation, and layout.
- Keep all visible text, including headings, labels, buttons, and messages, word for word.
- Keep the same fields, columns, forms, and views.
- Keep the same business logic, calculations, validation rules, filters, and sorting.
- Keep the same create, edit, and delete actions for each table or list.
- Match the colors, fonts, icons, and spacing in the source code's styles as closely as possible.

Reuse the original code wherever it works in the new app, and change only what's needed for it to run there, such as data connections. Don't add, remove, rename, or redesign anything. If you can't reproduce something exactly, use the closest match and tell me what's different.

This is the full scope of the app. If you build it in stages, then after each stage, list the screens and features from the source code that aren't built yet, so we can continue until the app is complete.
```

#### Data instructions

Replace the data placeholder in the template with the instruction that matches your app.

**Dataverse tables**

```text
Connect the app to my existing Dataverse tables in environment <environment ID>: <table logical names>. Create the app in that same environment. Use only these tables for the app's data. Don't create new tables, and don't use sample data.
```

**SharePoint lists**

```text
Connect the app to my existing SharePoint lists on <site URL>: <list names>. Use only these lists for the app's data. Don't create new lists, and don't use sample data.
```

**No data source**

```text
This app doesn't connect to a data source. Keep the same data that's in the source code.
```

#### Example

This example shows the first three paragraphs of a migration prompt for an app that uses Dataverse tables. Add the last three paragraphs of the template after them, unchanged.

```text
I'm migrating my app, Field Inspection Tracker, from Power Apps Vibe. I built this app, and the attached .zip file contains its complete source code. Name the new app Field Inspection Tracker.

Field Inspection Tracker helps safety inspectors schedule site inspections, record findings, and assign follow-up tasks. It has these screens: Dashboard, Sites, Inspections, Inspection details, and Follow-ups. Users can create and edit inspections, mark each finding as pass or fail, and assign follow-ups with due dates.

Connect the app to my existing Dataverse tables in environment aaaabbbb-0000-cccc-1111-dddd2222eeee: cr8a1_site, cr8a1_inspection, cr8a1_followup. Create the app in that same environment. Use only these tables for the app's data. Don't create new tables, and don't use sample data.
```

> [!TIP]
>
> - Use phrases like "I'm migrating my app" and "I built this app." Avoid phrases like "similar to" or "inspired by," which ask the agent for a new design instead of a faithful rebuild.
> - Use table logical names, such as `cr8a1_inspection`, not display names.
> - Attach the .zip file to the same message as your prompt.

### Rebuild your app in Copilot Studio

Before you start, ensure you meet the [prerequisites](#prerequisites) for Apps in Copilot Studio, and have your app's .zip file (10 MB or smaller) and your migration prompt ready.

1. Sign in to [Copilot Studio](https://copilotstudio.microsoft.com).
1. On **Home**, ensure the **New experience** toggle is on.
1. Select the **App** tile. You can also select **Apps (Preview)** > **New app**.
1. Paste your migration prompt into the message box.
1. Select **+**, and then attach your app's .zip file.
1. Select **Submit**.
1. Answer any follow-up questions. If Copilot Studio asks you to approve access to your data, review the request, and then approve it.
1. When the agent finishes, test your app in the preview. If the agent built the app in stages, reply **Continue with the deferred items** until the app is complete.
1. From the app's dropdown menu, review **Data** and **Connections** to confirm that the app uses your existing tables or lists.
1. Compare the new app with your original app, and ask for any changes. For example prompts, see [Refine your migrated app](#refine-your-migrated-app).

When your app is ready, [publish and share it](#publish-and-share-in-copilot-studio).

### Rebuild your app in Copilot Cowork

Use the App skill in Copilot Cowork to rebuild your app in Microsoft Copilot.

Before you start, ensure you meet the [prerequisites](#prerequisites) for Copilot Cowork, and have your app's .zip file and your migration prompt ready.

1. Go to [Microsoft Copilot](https://copilot.cloud.microsoft), and select **Cowork** at the top of the page.
1. In the message box, enter `/app`, a space, and then paste your migration prompt.
1. Select **Add attachments** (**+**) > **Upload images and files**, and then select your app's .zip file. If the file is in OneDrive or SharePoint, select **Attach cloud files** instead. You can also drag the file into the message box.
1. Select **Send**.
1. If Cowork asks you to confirm an action or approve access to your data, review the request, and then approve it.
1. When the agent finishes, review your app. If the agent built the app in stages, reply **Continue with the deferred items** until the app is complete.
1. Compare the new app with your original app, and ask for any changes. For example prompts, see [Refine your migrated app](#refine-your-migrated-app).

When your app is ready, [publish and share it](#publish-and-share-in-copilot-cowork).

## After you migrate

The steps in this section apply to both migration paths, unless noted.

### Verify your data connections

Your data stays in your Dataverse tables or SharePoint lists. With one-click migration, your new app reconnects to your data automatically. With manual migration, the agent reconnects your new app to your data based on the data instruction in your prompt.

After migration, confirm that the app uses your data:

1. Check that the app shows your existing records, not sample data.
1. If your app adds or changes records, create, edit, and delete a test record to confirm that the app can update your data.
1. In Copilot Studio, review the app's **Data** and **Connections**.

If the app shows sample data, send a prompt like this one. If your app uses SharePoint lists, use your site URL and list names instead.

```text
This app is using sample data instead of my data. Connect it to my existing Dataverse tables in environment <environment ID>: <table logical names>. Don't create new tables, and don't use sample data.
```

### Refine your migrated app

The agent might not reproduce every detail on the first try. Use follow-up prompts to close the gaps.

| Task | One-click migration | Manual migration |
| --- | --- | --- |
| Find what's different | `List every screen, field, label, and rule in this app, so I can compare it with my original Vibe app.` | `Compare the new app with the source code in the attached .zip file. List every screen, field, label, and rule that's missing or different, and then fix them.` |
| Finish a staged build | Not applicable | `Continue with the deferred items.` |
| Fix one screen | `On the <screen name> screen, add the <field or control> that's missing. Keep everything else the same.` | `Make the <screen name> screen match <file path> in the attached source code exactly.` |
| Restore exact text | `Change the heading on the <screen name> screen to "<exact text>".` | `Use the exact headings, labels, and button text from the source code on every screen.` |
| Restore logic | `When a user submits the <form name> form, require the <field name> field, the same as the original app.` | `Use the same validation rules as the original app. Use <file path> in the source code as the reference.` |

If you used manual migration and the agent can't find your source code, attach the .zip file again.

### Publish and share your app

When you publish your app, you make it and your latest changes available to the users you share it with. Your admin's sharing policies for your app's environment apply. For example, your admin can turn off sharing by link, with guests, or with groups, and can limit how many people you share an app with.

#### Publish and share in Copilot Studio

1. Select **Publish**.
1. Select **Share**, and then share the app with people or groups in your organization.

#### Publish and share in Copilot Cowork

> [!TIP]
> If you plan to [move your app to a different environment](#move-your-app-to-a-different-environment), move it before you share it. After a move, you need to share your app again.

1. Select **Publish**.
1. Open the app for editing, and then select **Share** to generate a link.
1. Send the link to the people in your organization who use your original app. They need to be able to use Microsoft Copilot.

### Move your app to a different environment

This section applies to apps that you rebuilt in Copilot Cowork with manual migration.

By default, Copilot Cowork builds your app in your personal developer environment (PDE). If your organization wants the app in a different environment, such as a shared team or production environment, ask Cowork to move it there.

#### Prerequisites for moving your app

- **Get the environment ID** of the environment that you want to move your app to. For steps, see [Collect your data details](#collect-your-data-details).
- **Make sure you can create apps in that environment.**

> [!NOTE]
> Moving your app doesn't move your Dataverse tables. Your tables stay in their original environment.

#### Move your app

1. In Copilot Cowork, open your app. For steps, see [Edit your app in Copilot Cowork](#edit-your-app-in-copilot-cowork).
1. In the message box, enter this prompt, and replace `<environment ID>` with the ID of the environment that you want to use:

   ```text
   Move this app to this environment with the environment ID: <environment ID>
   ```

1. Select **Send**.
1. If Cowork asks you to confirm the move or approve access, review the request, and then approve it.
1. When the move finishes, open the app and confirm that it works as expected. For steps, see [Verify your data connections](#verify-your-data-connections).
1. Share your app with your users again. For steps, see [Publish and share in Copilot Cowork](#publish-and-share-in-copilot-cowork).

### Edit your app after migration

After your app is migrated, update it by chatting with the agent in the same place where you built the app.

#### Edit your app in Copilot Studio

Use these steps for apps that you migrated with one-click migration and for apps that you rebuilt in Copilot Studio.

1. Sign in to [Copilot Studio](https://copilotstudio.microsoft.com).
1. In the left navigation pane, select **Apps (Preview)**.
1. Select your app to open it.
1. Describe the changes that you want in the message box.
1. Test your changes in the preview.
1. Select **Publish** to make your changes available to your users.

#### Edit your app in Copilot Cowork

In Copilot Cowork, your app lives in a conversation, not in a separate app list.

1. Go to [Microsoft Copilot](https://copilot.cloud.microsoft), and select **Cowork** at the top of the page.
1. In the conversation list on the side, find the conversation that contains your app. It's usually named **Edit Application Settings**.
1. Open the conversation, and describe the changes that you want in the message box.
1. Review your changes in the preview.
1. Select **Publish** to make your changes available to your users.

> [!TIP]
> To find your app more easily later, rename the conversation to your app's name, and pin it to the top of the conversation list. Select **More options** (**...**) next to the conversation, and then select **Rename** or **Pin**.

## Known limitations

- Migration creates a new app. Your original app's link and sharing aren't migrated.
- With manual migration, your original app's data connections aren't migrated. The agent connects your new app to your data.
- Your new app might not look identical to the original. The agent uses tested color themes, so it picks the closest match to your colors. Custom web fonts are replaced with a supported font.
- With manual migration, draft tables aren't migrated. Publish them to Dataverse before you migrate.
- With manual migration, rebuilt apps can't connect to Dataverse tables in the default environment.
- In Copilot Studio, attachments must be 10 MB or smaller, with up to 10 files per message.

## Troubleshooting

| Issue | What to do |
| --- | --- |
| You don't see **Migrate app** in Power Apps Vibe. | One-click migration is rolling out worldwide starting November 4, 2026, so it might not be available to you yet. Check again later, or use [manual migration](#option-2-manual-migration). |
| The app shows sample data instead of your data. | Send the prompt in [Verify your data connections](#verify-your-data-connections) with your environment ID and table logical names, or your site URL and list names. |
| The agent can't find your table. | Check the environment ID and logical name. Make sure the table is published, isn't in the default environment, and that you have permission to use it. |
| The agent can't find your list. | Check the site URL and list names, and make sure you have access to the site. |
| Your app was connected to a SharePoint list that no longer exists. | If the list was deleted, ask the site owner to restore it from the SharePoint site's recycle bin, and then ask the agent to reconnect the app to it. If the list was renamed or moved, send the agent the new site URL and list name. If the list can't be restored, ask the agent to create a new list with the columns that the app needs, such as: `The <list name> list that this app used no longer exists. Create a new SharePoint list named <list name> on <site URL> with the columns that this app needs, and connect the app to it.` The new list starts empty, so data from the original list isn't restored. |
| The agent says your environment is being set up. | Setting up an environment for the first time takes about two minutes. Wait, and then ask the agent to continue. |
| The agent can't create your personal developer environment. | Your organization might not allow you to create a personal developer environment. Ask your admin to allow developer environment creation for you in the Power Platform admin center (**Developer environment assignments** in tenant settings), or to give you access to an existing environment where you can create apps. |
| The agent says there's no usable Dataverse connection in your environment. | In [Power Apps](https://make.powerapps.com), select your environment, go to **Connections** > **New connection**, and create a Microsoft Dataverse connection. Then ask the agent to continue. |
| Copilot Studio doesn't accept your .zip file. | Attach the .zip file instead of individual code files. If the file is larger than 10 MB, remove generated folders such as `node_modules` and `dist`, and then compress the remaining files again. |
| Parts of your app are missing. | Reply **Continue with the deferred items**, or use the prompts in [Refine your migrated app](#refine-your-migrated-app). |
| You don't see the **App** tile in Copilot Studio. | On **Home**, turn on the **New experience** toggle. If you still don't see the tile, your admin might have turned off app creation, or your organization might not participate in the public preview. |
| You can't find your migrated app in Copilot Studio. | In the left navigation pane, select **Apps (Preview)**. For details, see [Edit your app in Copilot Studio](#edit-your-app-in-copilot-studio). |
| You don't see the App skill in Cowork. | The App skill is available only to Frontier program members. Contact your admin. |
| You can't find your app in Cowork. | Look in the conversation list for a conversation named **Edit Application Settings**. For details, see [Edit your app in Copilot Cowork](#edit-your-app-in-copilot-cowork). |

## Related content

- [What is Microsoft Copilot Managed Runtime (preview)](/microsoft-365/managed-apps/index)
- [Apps overview (preview)](/microsoft-copilot-studio/apps-experience/apps-overview)
- [Get started with Copilot Cowork](/microsoft-365/copilot/cowork/get-started)
- [Usage-based billing and cost management for Copilot Credits](/microsoft-365/copilot/usage-based-billing-overview-copilot-credits)
- [Find your environment and organization IDs and organization name](/power-platform/admin/determine-org-id-name)

