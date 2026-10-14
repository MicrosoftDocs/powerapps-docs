---
title: Migrate apps created from Power Apps Vibe
description: Learn how to manually migrate your Vibe apps to other authoring surfaces
ms.topic: how-to
ms.service: powerapps
ms.author: szlo
ms.reviewer: mkaur
author: szlo
ms.date: 10/13/2026
ms.custom: vibe
---

# Migrate apps from Power Apps Vibe

Power Apps Vibe ([https://vibe.powerapps.com](https://vibe.powerapps.com/)) is retiring. You can access your Vibe apps until November 30, 2026. If you built apps in Power Apps Vibe, you can manually migrate them to Copilot Cowork or Copilot Studio, where you can continue to create and update apps using natural language.

An automated migration option is planned for mid-October. Until it's available, you can migrate your apps manually: download each app's source code, and then ask the agent to rebuild the app from it by attaching the code file.

## How migration works

Migration rebuilds your app instead of moving it. You attach your app's source code to a prompt, and the agent builds a new app that matches the original as closely as possible.

1. **Prepare your data.** Publish any draft tables, and collect the details the agent needs to connect to your data.
1. **Download your app's source code** from Power Apps Vibe.
1. **Rebuild your app** in Copilot Cowork or Apps in Copilot Studio by attaching the source code to a migration prompt.
1. **Review, publish, and share** your new app.

The new app is separate from your original app. Keep your original app until you confirm that the new app works as expected.

| Part of your app | What happens during migration |
| --- | --- |
| Screens, navigation, components, and logic | Rebuilt from your source code. |
| Data in Dataverse tables or SharePoint lists | Stays where it is. Your new app connects to the same data. |
| Draft tables | Not migrated. |
| Data connections | Not carried over. The agent connects your new app to your data. |
| Sharing restrictions | Your admin's sharing policies for your app's environment apply. For example, your admin can turn off sharing by link, with guests, or with groups, and can limit how many people you share an app with. |
| Application lifecycle management (ALM) | Not supported yet. You can't move your app to another environment, such as a test or production environment. |


## Choose where to rebuild your app

In both experiences, you attach your source code to a prompt, and an agent rebuilds the app. Use this table to choose where to rebuild.

| Consideration | Copilot Cowork | Apps in Copilot Studio |
| --- | --- | --- |
| Where you build | Microsoft 365 Copilot | Copilot Studio |
| Availability | Frontier program only | Public preview |
| Licensing | Microsoft 365 Copilot license | Access to Copilot Studio |
| Billing | Copilot Credits | Copilot Credits |
| Share your app | With a link, to people in your organization who can use Microsoft 365 Copilot | With specific people or groups |

## Prepare your data

Your data stays where it is during migration, but your new app needs to connect to it. Before you rebuild your app, publish any draft tables, and collect the details that tell the agent which data to use.

### Publish draft tables in Vibe

Draft tables exist in memory only and aren't published to a data source until you explicitly publish them. Unpublished draft tables aren't migrated with your app.

1. Sign in to [https://vibe.powerapps.com](https://vibe.powerapps.com/), and open your app to edit.
1. Select **Publish**.
1. In the Publish menu, choose the environment that you'd like to publish your tables in under **Data environment**.

You publish your Dataverse tables in the same environment as your app.

### Collect your data details

If your prompt doesn't name your data, the agent might create sample data instead of connecting to your existing data. Collect these details for your prompt.

**If your app uses Dataverse tables:**

- **Environment ID**: The ID of the environment that contains your tables, such as `aaaabbbb-0000-cccc-1111-dddd2222eeee`. Find this information in at [https://make.powerapps.com](https://make.powerapps.com) under the **Table** tab. In the [Power Platform admin center](https://admin.powerplatform.microsoft.com), select **Manage** > **Environments**, select your environment, and then copy the **Environment ID** from the **Details** section. You can also use the `environmentId` value in the `power.config.json` file in your downloaded source code. For more information, see [Find your environment and organization IDs and organization name](/power-platform/admin/determine-org-id-name).
- **Table logical names**: The logical name of each table that your app uses, such as `cr8a1_inspection`. In [Power Apps](https://make.powerapps.com), select **Tables**, open the table, and then select **Tools** > **Copy logical name**.

> [!NOTE]
> If your environment ID starts with `Default-`, your tables are in your organization's default environment. Rebuilt apps can't connect to Dataverse tables in the default environment yet. [TODO: Confirm with engineering, and add guidance for makers whose tables are in the default environment.]

**If your app uses SharePoint lists:**

- **Site URL**: The address of the SharePoint site that contains your lists, such as `https://contoso.sharepoint.com/sites/Operations`. If you have the URL of a list, use the part before `/Lists/`.
- **List names**: The name of each list that your app uses.

Ensure you have access to the tables or lists that your app uses.

## Download your app's source code

1. Sign in to [https://vibe.powerapps.com](https://vibe.powerapps.com/).
1. Open your app, and then select **Edit**.
1. On the command bar, select **Download source**.

Your app's source code downloads as a .zip file. Attach this file to your migration prompt, so don't extract it.

## Write your migration prompt

The agent uses attached files as reference material, not as instructions. Your prompt tells the agent what to build and how to use your source code. A good migration prompt:

- Says that you're migrating your own app.
- Describes what the app does, even though the source code is attached.
- Tells the agent exactly which data to connect to.
- Ends with instructions to rebuild the app from the exact source code.

Copy the following template, and replace the placeholders in angle brackets (`<>`). Keep the last three paragraphs as they are.

```text
I'm migrating my app, <app name>, from Power Apps vibe. I built this app, and the attached .zip file contains its complete source code. Name the new app <app name>.

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

### Data instructions

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

### Example

This example shows the first three paragraphs of a migration prompt for an app that uses Dataverse tables. Add the last three paragraphs of the template after them, unchanged.

```text
I'm migrating my app, Field Inspection Tracker, from Power Apps vibe. I built this app, and the attached .zip file contains its complete source code. Name the new app Field Inspection Tracker.

Field Inspection Tracker helps safety inspectors schedule site inspections, record findings, and assign follow-up tasks. It has these screens: Dashboard, Sites, Inspections, Inspection details, and Follow-ups. Users can create and edit inspections, mark each finding as pass or fail, and assign follow-ups with due dates.

Connect the app to my existing Dataverse tables in environment aaaabbbb-0000-cccc-1111-dddd2222eeee: cr8a1_site, cr8a1_inspection, cr8a1_followup. Create the app in that same environment. Use only these tables for the app's data. Don't create new tables, and don't use sample data.
```

> [!TIP]
> - Avoid phrases like "similar to" or "inspired by," which ask the agent for a new design instead of a faithful rebuild.
> - Use table logical names, such as `cr8a1_inspection`, not display names.
> - Attach the .zip file to the same message as your prompt.

## Migrate your app to Copilot Cowork

Use the App skill in Copilot Cowork to rebuild your app in Microsoft 365 Copilot.

### Prerequisites

- A Microsoft 365 Copilot license, with Copilot Cowork turned on for your organization.
- Membership in the [Frontier program](https://www.microsoft.com/copilot/resources/frontier-program). The App skill in Cowork is available only to Frontier program members.
- Copilot Credits. Cowork uses usage-based billing, and building apps consumes Copilot Credits. For more information, see [Usage-based billing and cost management for Copilot Credits](/microsoft-365/copilot/usage-based-billing-overview-copilot-credits).
- Your app's .zip file and your migration prompt.

### Rebuild your app in Cowork

1. Go to [Microsoft 365 Copilot](https://copilot.cloud.microsoft), and select **Cowork** at the top of the page.
1. In the message box, enter `/app`, a space, and then paste your migration prompt.
1. Select **Add attachments** (**+**) > **Upload images and files**, and then select your app's .zip file. If the file is in OneDrive or SharePoint, select **Attach cloud files** instead. You can also drag the file into the message box.
1. Select **Send**.
1. If Cowork asks you to confirm an action or approve access to your data, review the request, and then approve it.
1. When the agent finishes, review your app. If the agent built the app in stages, reply **Continue with the deferred items** until the app is complete.
1. Compare the new app with your original app, and ask for any changes. For example prompts, see [Refine your rebuilt app](#refine-your-rebuilt-app).

### Publish and share your app in Cowork

Your app saves automatically as you work. Publishing makes your app, and your latest changes, available to the users you share it with.

1. Select **Publish**.
1. Open the app for editing, and then select **Share** to generate a link.
1. Send the link to the people in your organization who use the app. They need to be able to use Microsoft 365 Copilot.

> [!IMPORTANT]
> Anyone with the link can open and use the app, including all its data, so share responsibly and only with users who should have access.

## Migrate your app to Copilot Studio

Use Apps in Copilot Studio to rebuild your app in Microsoft Copilot Studio.

> [!IMPORTANT]
> Apps in Copilot Studio is in public preview. Preview features aren't meant for production use and might have restricted functionality.

### Prerequisites

- Access to Copilot Studio, with app creation turned on. The **App (Preview)** tile is on by default, but your admin can turn it off.
- Copilot Credits. App creation is powered by the GitHub Copilot harness. Usage-based billing applies to using, building, previewing, and testing apps. These actions might consume Copilot Credits.
- Your app's .zip file, 10 MB or smaller, and your migration prompt.

### Rebuild your app in Copilot Studio

1. Sign in to [Copilot Studio](https://copilotstudio.microsoft.com).
1. On **Home**, select the **App** tile. You can also select **Apps (Preview)** > **New app**.
1. Paste your migration prompt into the message box.
1. Select **+**, and then attach your app's .zip file.
1. Select **Submit**.
1. Answer any follow-up questions.
1. When the agent finishes, test your app in the preview. If the agent built the app in stages, reply **Continue with the deferred items** until the app is complete.
1. From the app's dropdown menu, review **Data** and **Connections** to confirm that the app uses your existing tables or lists.
1. Compare the new app with your original app, and ask for any changes. For example prompts, see [Refine your rebuilt app](#refine-your-rebuilt-app).

### Publish and share your app in Copilot Studio

1. Select **Publish**.
1. Select **Share**, and then share the app with people or groups in your organization.

> [!NOTE]
> Sharing an app and sharing its underlying data are separate actions. Apps access connected data on behalf of the signed-in user, so the people you share the app with also need permission to use its tables or lists. The first time they open the app, they might need to create or consent to a connection.

## Verify your data connections

Your new app doesn't inherit your original app's data connections. Your data stays in your Dataverse tables or SharePoint lists, and the agent connects your new app to it based on the data instruction in your prompt.

After the agent builds your app, confirm that the app uses your data:

1. Check that the app shows your existing records, not sample data.
1. If your app adds or changes records, create, edit, and delete a test record to confirm that the app can update your data.
1. In Copilot Studio, review the app's **Data** and **Connections**.

If the app shows sample data, send a prompt like this one. If your app uses SharePoint lists, use your site URL and list names instead.

```text
This app is using sample data instead of my data. Connect it to my existing Dataverse tables in environment <environment ID>: <table logical names>. Don't create new tables, and don't use sample data.
```

## Refine your rebuilt app

The agent might not reproduce every detail on the first try. Use follow-up prompts to close the gaps.

| To do this | Try a prompt like this |
|---|---|
| Find what's different | `Compare the new app with the source code in the attached .zip file. List every screen, field, label, and rule that's missing or different, and then fix them.` |
| Finish a staged build | `Continue with the deferred items.` |
| Fix one screen | `Make the <screen name> screen match <file path> in the attached source code exactly.` |
| Restore exact text | `Use the exact headings, labels, and button text from the source code on every screen.` |
| Restore logic | `Use the same validation rules as the original app. Use <file path> in the source code as the reference.` |

If the agent can't find your source code, attach the .zip file again.

## Known limitations

1. Migration creates a new app. Your original app's link, sharing, and data connections aren't migrated.
1. Your new app might not look identical to the original. The agent uses tested color themes, so it picks the closest match to your colors. Custom web fonts are replaced with a supported font.
1. Apps with several screens are built in stages, one screen at a time.
1. If an app with the same name already exists, a number might be added to your new app's name, such as "(2)".
1. Draft tables aren't migrated. Publish them to Dataverse before you migrate.
1. Rebuilt apps can't connect to Dataverse tables in the default environment yet.
1. In Copilot Studio, attachments must be 10 MB or smaller, with up to 10 files per message.

## Troubleshooting

| Issue | What to do |
|---|---|
| The app shows sample data instead of your data. | Send the prompt in [Verify your data connections](#verify-your-data-connections) with your environment ID and table logical names. |
| The agent can't find your table. | Check the environment ID and logical name in your prompt. Make sure the table is published, isn't in the default environment, and that you have permission to use it. |
| The agent says your environment is being set up. | Setting up an environment for the first time takes about two minutes. Wait, and then ask the agent to continue. |
| The agent says there's no usable Dataverse connection in your environment. | In [Power Apps](https://make.powerapps.com), select your environment, go to **Connections** > **New connection**, and create a **Microsoft Dataverse** connection. Then ask the agent to continue. [TODO: Confirm this workaround.] |
| Copilot Studio doesn't accept your .zip file. | Attach the .zip file instead of individual code files. If the file is larger than 10 MB, remove generated folders such as `node_modules` and `dist`, and then compress the remaining files again. |
| Parts of your app are missing. | Reply **Continue with the deferred items**, or use the prompts in [Refine your rebuilt app](#refine-your-rebuilt-app). |
| You don't see the App skill in Cowork. | The App skill is available only to Frontier program members. Contact your admin. |
| You don't see the **App** tile in Copilot Studio. | On **Home**, turn on the **New experience** toggle. If you still don't see the tile, your admin might have turned off app creation. |

## Related content

- [Quickstart: Create an app with natural language in Microsoft Copilot Studio (preview)](/microsoft-copilot-studio/apps-experience/get-started)
- [Manage data in your app (preview)](/microsoft-copilot-studio/apps-experience/data-and-connections)
- [Get started with Copilot Cowork](/microsoft-365/copilot/cowork/get-started)
- [Use Copilot Cowork](/microsoft-365/copilot/cowork/use-cowork#build-apps-with-the-app-skill-frontier)
- [Usage-based billing and cost management for Copilot Credits](/microsoft-365/copilot/usage-based-billing-overview-copilot-credits)
- [Find your environment and organization IDs and organization name](/power-platform/admin/determine-org-id-name)
- [Create apps, data, and plans with Power Apps vibe](create-app-data-plan.md)
- [Use SharePoint lists as a data source in Power Apps vibe (preview)](add-data-source-sharepoint-lists.md)
