---
title: Maker matching using an integrated virtual agent in Power Apps (preview)
description: Learn how to use a chat bot integrated in Microsoft Power Apps to find maker resources in your organization.
ms.date: 04/07/2023
author: mduelae
ms.author: mkaur
ms.reviewer: mkaur
ms.topic: how-to
ms.subservice: common
ms.custom: bap-template
search.audienceType: 
  - maker, admin
---

# Maker matching using an integrated virtual agent in Power Apps (preview)

[This article is prerelease documentation and is subject to change.]

Maker matching allows you to use an integrated chat bot in Power Apps to find internal maker resources and connect with experienced makers in your organization. The integrated virtual agent is available in all three Power Apps personas:

**Makers** can use the chat bot to get help from internal and public documentation and other experienced makers in the organization, known as advisors.

**Advisors** respond to requests for help that makers submit through the chat bot.

**Admins** tell the chat bot where to find internal documentation and which advisors can help new makers.

> [!IMPORTANT]
> - This is a preview feature. Preview features aren't meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - This feature will be deprecated on April 30, 2024.

## Find maker resources

1. Sign in to [Power Apps](https://make.powerapps.com) and select **Ask a Virtual Agent** at the bottom of the navigation pane.

1. Interact with the bot to find helpful resources based on the key terms and phrases you enter.

    :::image type="content" source="media/skills-match/skills-match-2.png" alt-text="Screenshot of a maker conversation with a chat bot in Power Apps.":::
Chat bot interactions are broken into three stages:

- Stage 1: Microsoft documentation

- Stage 2: Internal resources

- Stage 3: Advisor engagement

### Stage 1: Microsoft documentation

In the first stage of engagement, the virtual agent helps you find Microsoft documentation that relates to your responses.

In the following example, the user wants help with connecting data, specifically to help troubleshoot a data export error.

:::image type="content" source="media/skills-match/skills-match-3.png" alt-text="Screenshot of the start of a bot conversation about exporting data.":::

 In response to the user's answers to its prompts, the bot directs the user to an article about exporting data from Microsoft Dataverse.

:::image type="content" source="media/skills-match/skills-match-4.png" alt-text="Screenshot of a bot answering a user question with a Microsoft product documentation article.":::

### Stage 2: Internal resources

If you select **No** when the chat bot asks whether the Microsoft documentation solved your problem, then the second stage begins. In this stage, the bot suggests organizational resources that an [admin has previously identified](#add-internal-resources), like internal documentation, a Yammer community, and Microsoft Teams groups.

:::image type="content" source="media/skills-match/skills-match-6.png" alt-text="Screenshot of a bot suggesting internal maker resources in a conversation with a user.":::

### Stage 3: Advisor engagement

Stage 3 begins if you select **Next** to find an advisor in your organization. The chat bot presents a list of experienced makers in your organization who have offered to help new makers.

:::image type="content" source="media/skills-match/skills-match-7.png" alt-text="Screenshot of a bot suggesting advisors in a conversation with a user.":::

Select **View more advisors** to get more suggestions. Select **Send message** to compose an email or a Teams chat with the advisor, depending on the advisor's preferred contact method.

## Sign up to be an advisor

Power Apps invites successful makers to become advisors based on their usage of the product. Admins can also nominate advisors. Nominated makers can opt in to the advisor program at any time.

### Respond to an invitation

If an admin has nominated you as an advisor, a notification in the app asks whether you'd like to opt in to help other makers. The notification is also displayed if Power Apps detects that you have enough experience with making apps to help others.

:::image type="content" source="media/skills-match/skills-match-8.png" alt-text="Screenshot of the invitation to become a Power Apps advisor.":::

### Sign up in your Power Apps profile

If you respond to the invitation with **Maybe later**, you can opt in to become an advisor when you're ready.

1. Select **Settings** in the upper-right corner of the screen, and then select **Power Apps settings**.

1. Select **Advisor program** in the navigation pane.

    The **Advisor program** tab is only available if your admin has nominated you in the Power Platform admin center.

1. Under **Set availability**, select the toggle to tell Power Apps that people can contact you with questions. If you need a break from answering questions, turn off your availability.

1. Select the communication method you prefer, email or Microsoft Teams chat.

:::image type="content" source="media/skills-match/skills-match-9.png" alt-text="Screenshot of the advisor settings in the Power Apps user profile.":::

## Set up maker matching

If you're an admin, you can set up internal resources and add and remove advisors in the Power Platform admin center.

### Add internal resources

1. Sign in to the [Power Platform admin center](https://admin.powerplatform.com).

1. In the navigation pane, select **Power Apps assets**.

1. Enter the links to your organization's internal **Documentation**, **Teams Group**, and **Yammer Community**.

    :::image type="content" source="media/skills-match/skills-match-10.png" alt-text="Screenshot of adding internal Documentation, Teams Group, and Yammer Community links in the Power Platform admin center.":::

1. Select **Save**.

### Add and remove advisors

As a Power Platform administrator, you can add and remove advisors. Adding an advisor nominates the maker for the advisor program. The maker must opt in to join.

By default, makers who are identified by the system and have opted in to the advisor program are added to the advisor list automatically. If advisors are identified by the system but removed by an administrator, only an administrator can add them back.

1. Sign in to the [Power Platform admin center](https://admin.powerplatform.com).

1. In the navigation pane, select **Power Apps assets**.

1. Select the **Advisors** tab.

    :::image type="content" source="media/skills-match/skills-match-11.png" alt-text="Screenshot of the Advisors tab in the Power Platform admin center.":::

1. Add or remove an advisor:

    - To add an advisor, select **Add an advisor** and enter the requested information.

    - To remove an advisor, selecting the menu (**&hellip;**), and then select **Remove**.

## Turn off maker matching for your tenant

Power Platform admins can turn off maker matching for a tenant using the Windows PowerShell **Set-TenantSettings** cmdlet.

To display the current setting, run the following command at the PowerShell prompt:

   ```powershell
   $settings=Get-TenantSettings 
   $settings.PowerPlatform.PowerApps.disableMakerMatch
   ```

To turn off maker matching, run the following command:

   ```powershell
   $settings.powerPlatform.powerApps.disableMakerMatch = $True
   Set-TenantSettings -RequestBody $settings
   ```

## Known issues

The virtual agent panel may be blank when you [restart the virtual agent](virtual-agent.md#restart-or-close-a-session). To fix the issue, refresh your browser page.
