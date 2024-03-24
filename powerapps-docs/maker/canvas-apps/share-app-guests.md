---
title: Share a canvas app with guest users (contains video)
description: Learn about how to share canvas app with guest users.
author: alaug
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 01/27/2023
ms.subservice: canvas-maker
ms.author: alaug
search.audienceType: 
  - maker
contributors:
  - mduelae
  - alaug
---
# Share a canvas app with guest users

Canvas apps can be shared with guest users of a Microsoft Entra tenant. This enables inviting external business partners, contractors, and third parties to run your company's canvas apps.

Watch this video to learn how to share an app with guests:
> [!VIDEO https://www.microsoft.com/videoplayer/embed/RWLTiv]

## Prerequisites

- In Microsoft Entra ID, enable B2B external collaboration for the tenant. More information: [Enable B2B external collaboration and manage who can invite guests](/azure/active-directory/b2b/delegate-invitations)

  > [!NOTE]
  > B2B external collaboration is enabled by default; however, you need to verify that the settings weren't changed by a tenant admin. For more information about Microsoft Entra B2B, go to [What is guest user access in Microsoft Entra B2B?](/azure/active-directory/b2b/what-is-b2b).

- Access to an account that can add guest users to an Microsoft Entra tenant. Admins and users with the Guest Inviter role can add guests to a tenant.

- To access an app that doesn't connect to Dataverse, the guest user must have a license with Power Apps use rights that matches the capability of the app assigned through one of the following tenants:

  - The tenant hosting the app being shared
  - The home tenant of the guest user

- To access an app that connects to Dataverse, the guest user must have a license with Power Apps use rights that matches the capability of the app. And it must be assigned in the tenant hosting the app. The exception to this prerequisite is when an app is hosted in a [Microsoft Dataverse for Teams environment](/power-platform/admin/about-teams-environment).
  
> [!NOTE]
> Ensure that you perform the steps listed below on the **resource tenant**, and not on the **home tenant**.
> - A **resource tenant** is where the app is expected to exist, and where the user is expected to create the app using Power Apps as a guest.
> - A **home tenant** is where the user's account resides and authenticates against.

## Steps to grant guest access

1. In Microsoft Entra ID, select **New guest user**. More information: [Quickstart: Add a new guest user in Microsoft Entra ID](/azure/active-directory/b2b/b2b-quickstart-add-guest-users-portal)

    ![Add a guest in Microsoft Entra ID.](media/share-app/guest_access_doc_1.png "Add a guest in Microsoft Entra ID")

2. If the guest user doesn't already have a license in their home tenant, assign a license to the guest user.

   - To assign guest users from admin.microsoft.com, go to [Assign licenses to one user](/office365/admin/subscriptions-and-billing/assign-licenses-to-users).

   - To assign guest users from portal.azure.com, go to [Assign or remove licenses](/azure/active-directory/fundamentals/license-users-groups).
 
   > [!IMPORTANT]
   > You might need to disable the Microsoft 365 admin center preview to assign a license to a guest.

3. Share the canvas app by doing the following:

    1. Sign in to [Power Apps](https://make.powerapps.com).

    1. On the left pane, select **Apps**.

    1. Select a canvas app.

    1. On the command bar, select **Share**.

    1. Enter an email address for a guest user from an Microsoft Entra tenant. More information: [What is guest user access in Microsoft Entra B2B?](/azure/active-directory/b2b/what-is-b2b)

       ![Share with guest.](media/share-app/guest_access_doc_2.png "Share with guest")

After you share an app for guest access, guests can discover and access apps shared with them from the email sent to them as part of sharing. You can also share the app URL directly with the guest instead. To find the URL, go to [Power Apps](https://make.powerapps.com), select **Apps** on left pane, select the app, and then select the **Details** tab. The app URL is displayed under **Web link**.

![Guests receive app share email.](media/share-app/guest_access_doc_4.png "Guests receive app share email")

## Considerations and limitations for guest access

- Users accessing web experiences in different Microsoft Entra tenants must acces Power Apps in a standalone browser session (different browser or InPrivate browser session) otherwise Power Apps may not pick up the correct Azure B2B user identity for the app being accessed. 
- Power Apps guest access uses Azure B2B.
- Power Apps Mobile doesn't support authentication using [Microsoft Entra direct federation](/azure/active-directory/b2b/direct-federation). More information: [Sign in using Power Apps Mobile](../../mobile/run-powerapps-on-mobile.md#sign-in)
- Power Apps [per app plans](/power-platform/admin/powerapps-flow-licensing-faq#how-is-microsoft-power-apps-and-power-automate-licensed) are scoped to apps in a specific environment, so they can't be recognized across tenants.
- Power Apps [included with Office](/power-platform/admin/pricing-billing-skus#power-appspower-automate-for-microsoft-365) and Power Apps [per user plans](/power-platform/admin/powerapps-flow-licensing-faq#how-is-microsoft-power-apps-and-power-automate-licensed) have the following characteristics:
  - In the Azure public cloud, they're recognized across tenants in guest scenarios because they aren't bound to a specific environment.
  - In Azure national or sovereign clouds, they're recognized across tenants in guest scenarios. More information: [National clouds](/azure/active-directory/develop/authentication-national-cloud), [Azure geographies](https://azure.microsoft.com/global-infrastructure/geographies/#geographies)
  - Licenses are not recognized across tenants in difference Azure clouds.
  - Not all connectors create connections in the resource tenant by default. 

## Frequently asked questions

### What's the difference between canvas app guest access and Power Pages?

With canvas apps, you can build an app that's tailored to digitizing business processes, without writing code in a traditional programming language such as C#. Guest access for canvas apps enables teams of individuals made up of different organizations participating in a common business process to access the same app resources that might be integrated with a wide variety of Microsoft and third-party sources. More information: [Overview of canvas-app connectors for Power Apps](./connections-list.md)

[Power Pages](/power-pages/introduction) provide you the ability to build low-code, responsive websites that allow external users to interact with the data stored in Dataverse. With Power Pages, organizations can create websites that can be shared with users external to their organization either anonymously or through the sign-in provider of their choice, such as LinkedIn, Microsoft account, or other commercial sign-in provider.

The following table outlines a few core capability differences between Power Pages and canvas apps. 

| Guest access in | Interface | Authentication | Accessible data sources |
|------|--------|----------|-------------------|
| Power Pages | Browser-only experience | Allows anonymous and authenticated access | Dataverse |
| Canvas apps | Browser and mobile apps | Requires authentication via Microsoft Entra ID | Any of approximately 150 out-of-the-box connectors and any custom connector  |

### Can guests access customized forms in SharePoint?

See [What license must be assigned to my guest so they can run an app shared with them?](#what-license-must-be-assigned-to-my-guest-so-they-can-run-an-app-shared-with-them)

### Why is a guest who accesses a customized form in SharePoint prompted for a trial?

If the custom form uses a premium connector, a guest must have a Power Apps license to access the custom form. If the custom form only uses standard connectors, your tenant must allow Microsoft Power Platform internal consent plans to be assigned to users. For more details about Power Platform internal consent plans, read [block trial license commands](/power-platform/admin/powerapps-powershell#block-trial-licenses-commands).  

### Can guests access apps embedded in SharePoint?

Yes. However, access to canvas standalone apps requires that the user have a license with Power Apps user rights that matches the capability of the app; this includes embedded apps. When embedding a canvas app in SharePoint by using the Power Apps embed control, enter the app ID. To do this, enter the app ID in the **App web link or ID** box.

![Embed a canvas app in SharePoint for guests.](media/share-app/guest_access_doc_5.PNG "Embed a canvas app in SharePoint for guests")

When embedding a canvas app in SharePoint via the iFrame HTML tag, reference the app by using the full web URL. To find the URL, sign in to [Power Apps](https://make.powerapps.com), select an app, and then select the **Details** tab. The URL is displayed under **Web link**.

![Canvas app details.](media/share-app/guest_access_doc_6.PNG "Canvas app details")

### How is it that guests can open the app shared with them, but no data connections are created?

As is the case with non-guests, the underlying data sources accessed by the app must also be made accessible to the guest.

### What license must be assigned to my guest so they can run an app shared with them?

The following table explains whether the guests can run (use) customized Microsoft Lists or SharePoint library forms, canvas apps, and model-driven apps using the referenced license.

|    Plan                             | Customized Microsoft Lists or SharePoint library form (using non-premium connectors) | Customized Microsoft Lists or SharePoint library (using premium connectors) | Canvas app (using non-premium connectors) | Canvas app (using premium connectors) | Model-driven app |
|---------------------------------|----------------------------------------------------|------------------------------------------------|------------------| - | - |
| No license | &check;                                               | &cross;                 | &cross; | &cross; | &cross; |
| SharePoint user (without Power Apps license) | &check;                                               | &cross;                 | &cross; | &cross; | &cross; |
| Power Apps included with Office    | &check;                                                  | &cross;                                               | &check;                 | &cross; | &cross; | 
| Power Apps per app plan          | &check;                                                  | &check;                                               | &check;                | &check; | &check; |
| Power Apps per user plan         | &check;                                                  | &check;                                              | &check;                | &check; | &check; |

For more information about pricing and the capabilities of various plans, go to [Microsoft Power Apps and Power Automate Licensing Guide](https://go.microsoft.com/fwlink/?linkid=2085130).

### In Power Apps Mobile, how does a guest see apps for their home tenant?

Any user who has used their mobile device to access a canvas app that was published in an Microsoft Entra tenant that isn't their home tenant, can [switch to a different directory](../../mobile/tenant-switcher.md).

### In Power Apps Mobile, how does a guest see apps in the guest tenant?

The guest user opens the email they received when an app in the guest tenant was shared, and selects **Open the app**. This applies to both Microsoft Entra and Microsoft account users. You can  also create a deep link. For more information, see [Use deep links with Power Apps mobile](/power-apps/mobile/run-powerapps-on-mobile).

### Must a guest accept the Microsoft Entra guest invitation before an app can be shared with them?

No. If a guest opens an app that was shared with them before they accepted a guest invitation, the guest will be prompted to accept the invitation as part of the sign-in experience while opening the app.  

### In which Microsoft Entra tenant are connections created for a guest user?

Connections for an app are always made in the context of the Microsoft Entra tenant the app is associated with. For example, if an app is created in the Contoso tenant, the connections made for Contoso internal and guest users are made in the context of the Contoso tenant.

### Can guests use Microsoft Graph with Power Apps?

By default, Azure B2B users have limited permission to access information from Microsoft Graph. A user’s permission as recognized in Microsoft Graph determine what is returned to these users when using connectors such as Microsoft Security Graph, Office 365 Users, Office 365 Groups, and custom connectors using Microsoft Graph APIs. Learn more about Microsoft Graph permissions in [Default user permissions](/entra/fundamentals/users-default-permissions?context=graph%2Fcontext#restrict-guest-users-default-permissions) and [Working with users in Microsoft Graph](/graph/api/resources/users?#user-and-group-search-limitations-for-guest-users-in-organizations).  

### Which Intune policies apply to guests who are using my apps?

Intune only applies the policies of a user's home tenant. For instance, if Lesa@Contoso.com shares an app with Wanda@Fabrikam.com, Intune continues to apply Fabrikam.com policies on Wanda's device, regardless of the apps Wanda runs.

### Which connectors create connections in the resource tenant by default?

Users relying on Azure B2B to access an app only has implications on connectors that use Microsoft Entra ID for authentication. Some Microsoft Entra ID based connectors default to creating a connection in the resource tenant, while others default to creating a connection in the home tenant. Connectors that don't use any type of Microsoft Entra ID authentication work the same for guests and members in a tenant. The following table enumerates all connectors that do use Microsoft Entra ID authentication and default creates connections in the resource tenant. More information: [List of all Power Apps connectors](/connectors/connector-reference/connector-reference-powerapps-connectors)

| **Connector**                                     | **Creates connection in resource tenant by default**                                             |
|---------------------------------------------------|------------------------------------------------------------------------|
| Microsoft Entra                                          | Yes                                                                    |
| Azure Automation                                  | Yes                                                                    |
| Azure Container Instance                          | Yes                                                                    |
| Azure Data Factory                                | Yes                                                                    |
| Azure Data Lake                                   | Yes                                                                    |
| Azure IoT Central                                 | Yes                                                                    |
| Azure Kusto                                       | Yes                                                                    |
| Azure Log Analytics                               | Yes                                                                    |
| Azure Resource Manager                            | Yes                                                                    |
| Microsoft Dataverse                               | Yes*                                                                     |
| Dynamics 365 AI for Sales                         | Yes                                                                    |
| Microsoft Teams                                   | Yes                                                                    |
| Office 365 Groups                                 | Yes                                                                    |
| Office 365 Users                                  | Yes                                                                    |
| Outlook Tasks                                     | Yes                                                                    |
| Power BI                                          | Yes                                                                    |
| SharePoint                                        | Yes                                                                    |

\* When using the Microsoft Dataverse as the data source, ensure that the guest user is licensed from the same tenant where you have Dataverse data located.


### See also

[Edit an app](edit-app.md)  
[Restore an app to a previous version](restore-an-app.md)  
[Export and import an app](export-import-app.md)  
[Delete an app](delete-app.md)  


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
