---
title: Sign in to Power Apps
description: Learn about signing in to Power Apps for the first time, choosing an environment, creating an app, playing or editing an app, and other common tasks.
author: alaug
ms.topic: how-to
ms.collection: get-started
ms.reviewer: 
ms.date: 1/24/2025
ms.subservice: canvas-maker
ms.author: alaug
search.audienceType: 
  - maker
contributors:
  - tapanm-msft
  - alaug
  - Mattp123
---
# Sign in to Power Apps 

To create, edit, or play an app, sign in to Power Apps at [https://make.powerapps.com](https://make.powerapps.com). To create canvas apps, you must have the [environment maker predefined security role](/power-platform/admin/database-security#predefined-security-roles). 

To learn more about the [Power Apps](https://make.powerapps.com) home page, go to [Get started with Power Apps](intro-maker-portal.md).

## Choose an environment

Whether you're creating an app, a flow, a data connection, or a table in Microsoft Dataverse, much of what you do in Power Apps is contained in a specific environment. Environments create boundaries between different types of work. For example, an organization might have separate environments for different departments. Many organizations use environments to separate apps that are still being developed from those that are ready for widespread use. You might have access to multiple environments or only one. If you have the appropriate permissions, you might even be able to create your own environments.

To verify which environment you're in, find the environment switcher near the right side of the header.

> [!div class="mx-imgBorder"] 
> ![Environment switcher.](media/intro-maker-portal/environment-switcher.png)

With the environment selector, environments are grouped into two categories:  **Build apps with Dataverse** and **Other environments**. Select **Filter** to filter the list of environments by your role, data platform (Dataverse or none), and environment type, such as production or sandbox.

:::image type="content" source="media/intro-maker-portal/environment-picker2.png" alt-text="Environment selector to filter and select an environment" lightbox="media/intro-maker-portal/environment-picker2.png":::

Environments where you have either system administrator and/or system customizer security role membership appear under **Build apps with Dataverse**. The **Other environments** list displays environments where you have only environment maker or editing privileges to at least one of the canvas apps in the environment.

> [!TIP]
> Hover over an environment in the list to view the details of the environment.

#### Filter environments by role

|Filter role  |Power Platform role or description  |
|---------|---------|
|Admin     | System administrator <br /> Environment admin        |
|Maker with data access     | System administrator <br />  System customizer        |
|Maker without full data access     | Environment maker (with or without Dataverse)     |
|Shared app contributor     | User without a maker-level security role assigned but with edit permission to at least one canvas app in the environment        |

> [!IMPORTANT]
>
> - To view the environment list in the environment switcher in Power Apps, you must have the Environment Maker, System Customizer, or System Administrator security role in the environment. For information about predefined security roles, go to [Predefined security roles](/power-platform/admin/database-security#predefined-security-roles) in the Microsoft Power Platform admin guide.
> - Make sure that you're in the right environment *before* you create an app, a flow, or a similar component. You can't easily move components from one environment to another.

> [!NOTE]
>
> - Every member in an organization can access [the default environment](/power-platform/admin/environments-overview#the-default-environment). Like any environment, users can see apps where they have sufficient privileges to access an app.
> - All users with the Environment Maker security role in an environment can see all model-driven apps in that environment, including the default environment. More information: [Model-driven app privileges to view and access apps](../model-driven-apps/app-visibility-privileges.md).
> - When you create an app in one environment, you won't be able to see it from another environment. In addition, people who want to run your app must have access to the environment in which you created it.

For more information, see [Environments overview](/power-platform/admin/environments-overview).

## Sign in using Azure B2B collaboration

> [!NOTE]
>
> - A **resource tenant** is the Microsoft Entra tenant where an app is expected to exist, and where the user is expected to create and edit the app. For Azure B2B makers, this tenant is different from the tenant their account resides. 
> - A **home tenant** is where the user's account resides and authenticates against.
> - To create and edit apps in a resource tenant, an admin must [follow these steps](/power-platform/admin/invite-users-azure-active-directory-b2b-collaboration#power-apps-support-for-b2b-guest-maker-preview) to give Azure B2B users the prerequisite privileges to build apps. 

When a user signs into [Power Apps](https://make.powerapps.com), they sign into their **home tenant**&mdash;the Microsoft Entra tenant where their credentials are provisioned. After signing in, a user can change the directory, they intend to build apps in using the **Switch directory** link as shown here:

:::image type="content" source="media/intro-maker-portal/intro_to_maker_portal_switch_directory_1.png" alt-text="Azure B2B Maker - switch directory option.":::

The switch directory link opens Power Apps settings that contain a **Directories** tab that lists all the Microsoft Entra tenants the user exists in as a member or an Azure B2B guest. Selecting **Switch** triggers [Power Apps](https://make.powerapps.com) to sign out of the current tenant and then sign into the selected tenant.

:::image type="content" source="media/intro-maker-portal/intro_to_maker_portal_switch_directory_2.png" alt-text="Azure B2B Maker - switch tenant.":::

### Frequently asked questions

#### As an Azure B2B maker, why am I unable to share apps?

The Power Apps sharing experience requires users to have permissions in the tenant included when the Azure Microsoft Entra ID [external collaboration settings has guest user access to "(most inclusive)"](/azure/active-directory/b2b/delegate-invitations). Azure B2B makers without sufficient privileges see the following error dialog in the sharing experience.

:::image type="content" source="media/intro-maker-portal/intro_to_maker_portal_Azure_B2B_share_error.png" alt-text="Invalid domain name in the request url.":::

#### Can I work in Power Apps in both my home tenant and a resource tenant?

- Yes, but in separate browser sessions. For example, Microsoft Edge might be open in its standard mode and a separate session might be started in a new **InPrivate** window.
- If multiple tabs in the same browser session are open, only resources in the most recently signed in tenant are accessible.

#### Can I sign in to Power Apps, in a resource tenant with GDAP?

No, [https://make.powerapps.com](https://make.powerapps.com) doesn't recognize [Granular delegated admin privileges (GDAP)](/partner-center/customers/gdap-introduction); however, the [Power Platform admin center does](/partner-center/customers/gdap-supported-workloads#dynamics-365-and-power-platform). 

## Sign in using Microsoft Account (preview)

Anyone can build Power Apps, even if you don't have a work or school account. Simply sign up for a Dynamics 365 Sales trial using a [Microsoft Account](https://account.microsoft.com/) and then use that account to sign into [Power Apps](https://make.powerapps.com). 

During the 30 day trial period, you can make and play with as many apps as you like. You can also build with apps with Dataverse or other premium connectors. However, if you plan to run these apps beyond the trial period or share them with others, then you need to create a (free) Microsoft Entra account. 

> [!IMPORTANT]
>
> - This is a preview feature.
> - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)] 

### Where can I get a license with Power Apps use rights for my Microsoft Account?

The Dynamics 365 Sales free trial includes Power Apps use rights, along with other Dynamics and Power Platform use rights. You can sign up here: [Dynamics 365 free trial](https://www.microsoft.com/dynamics-365/free-trial).

![image](https://user-images.githubusercontent.com/11514622/217617662-25109f3c-d85a-404b-a4b3-459c08de04a1.png)

> [!NOTE]
> Not all Power Apps free licenses support Microsoft Account sign-up. The list of free licenses that allow free sign-up is expected to grow over time.

### How do I create model-driven apps and use Dataverse?

Select or create an environment with Dataverse. You can create Developer environments with Dataverse for free.

1. Sign in to [Power Apps](https://make.powerapps.com).
2. Select the environment picker. 
3. In the **Need your own environment?** prompt, select **Try it now** to create an environment with Dataverse. 

### How do I access Power Platform admin center?

Power Platform admin center (https://admin.powerplatform.microsoft.com) doesn’t support Microsoft Account sign-in. However, your Microsoft Account is associated with a Microsoft Entra tenant and you can provision a Microsoft Entra based identity to use in the Power Platform admin center. 

1. Follow the steps under **How do I create a Microsoft Entra identity with the same administrative privileges as my Microsoft Account?**
2. Using the newly created Microsoft Entra identity, sign in to [https://admin.powerplatform.microsoft.com](https://admin.powerplatform.microsoft.com). 

### How do I create a Microsoft Entra identity with the same administrative privileges as my Microsoft Account?

1.	Sign in to [https://portal.azure.com](https://portal.azure.com). 
2.	Search for **Microsoft Entra ID**.
3.	[Add a new user](/azure/active-directory/fundamentals/add-users-azure-active-directory#add-a-new-user). 
4.	[Associate or add an Azure subscription to your Microsoft Entra tenant](/entra/fundamentals/how-subscriptions-associated-directory#assign-roles). For administrative purposes, you must assign the same admin role as your Microsoft Account has in Microsoft Entra ID, such as [Power Platform or Dynamics 365](/power-platform/guidance/adoption/pp-admin) admin.

### The free license assigned to my Microsoft Account expired, how can I access Power Apps?

If your Microsoft Account is associated with a Microsoft Entra tenant, you’ll be able to sign in to [Power Apps](https://make.powerapps.com) and edit your apps. However, without an active license you can't play the apps. 

Today, Microsoft accounts are bound to limited trial periods, you can't sign up for the same free license twice with the same account. Also, Microsoft accounts can't  [purchase Power Apps plans](https://powerapps.microsoft.com/pricing/).

You might proceed with building and running apps by creating a Microsoft Entra identity in the same Microsoft Entra tenant your Microsoft Account is associated and sign up for a [Power Apps Developer plan](https://powerapps.microsoft.com/developerplan/) with that identity. With your Microsoft Account, you need to [share your apps](share-app.md) with your Microsoft Entra identity to proceed with editing and playing them. 

To create a Microsoft Entra identity with administrative rights, follow the steps under “How do I create a Microsoft Entra identity with the same administrative privileges as my Microsoft Account?”.

### Can I use my Microsoft Account with the Power Platform PowerShell cmdlets?

No. In the meantime, you can follow the steps called out in questions above where you add a new Microsoft Entra identity to the Microsoft Entra tenant associated with your Microsoft Account to use the [Power Platform PowerShell cmdlets](/power-platform/admin/powerapps-powershell). 

### Can I share my apps with other users?

Yes, however, you need to add users to the Microsoft Entra tenant associated with your Microsoft Account, you'll need to assign a license to these users, and then share your app with these users. As an admin, you can assign free licenses to users but these will expire. 

1. To create a Microsoft Entra identity with administrative rights, follow the steps under **How do I create a Microsoft Entra identity with the same administrative privileges as my Microsoft Account?**.
2. For each user you’d like to share an app, add their identity to Microsoft Entra ID. 
   1. Sign in to [https://portal.azure.com)](https://portal.azure.com). 
   2. Search for **Microsoft Entra ID**.
   3. [Add a new user](/azure/active-directory/fundamentals/add-users-azure-active-directory#add-a-new-user) or [Add a guest user](/azure/active-directory/fundamentals/add-users-azure-active-directory#add-a-new-guest-user). You can add users that have either a Microsoft Account or Microsoft Entra identity. 
3. With your Microsoft Entra admin identity, either [purchase Power Apps plans](https://powerapps.microsoft.com/pricing/). As an admin, you’ll receive 25 Power Apps per user trials. All of these trials expire. 
4. With your Microsoft Entra admin identity, assign licenses to the users you added to your Microsoft Entra tenant. With your Microsoft Entra admin identity, [assign licenses to the users](/azure/active-directory/fundamentals/license-users-groups#assign-licenses-to-users-or-groups) you added to your Microsoft Entra tenant. 
5. Sign in to [Power Apps](https://make.powerapps.com) to proceed with [sharing your apps to users](share-app-guests.md). 

### Can I run my apps in Power Apps mobile?

Yes. You must launch an app from an app link. Without launching an app directly, Power Apps mobile doesn’t support Microsoft Account sign in out of the context of launching an app. 

You can get the app link for an app by going to, [Power Apps](https://make.powerapps.com) > **Apps** > (select an app) > **Details** > See the **Web link** property.

## Next steps

[Build an app](getting-started.md#build-an-app)

[What is Microsoft Dataverse?](../data-platform/data-platform-intro.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
