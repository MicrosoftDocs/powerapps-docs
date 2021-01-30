---
title: Share a canvas app with guest users | Microsoft Docs
description: Share your canvas app with guest users 
author: alaug
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 01/11/2021
ms.author: alaug
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Share a canvas app with guest users
 
Power Apps canvas apps can be shared with guest users of an Azure Active Directory tenant. This enables inviting external business partners, contractors, and third parties to run your company’s canvas apps.

## Prerequisites

- In Azure Active Directory (Azure AD), enable B2B external collaboration for the tenant. More information: [Enable B2B external collaboration and manage who can invite guests](/azure/active-directory/b2b/delegate-invitations)

    - Enable B2B external collaboration is on by default. However, the settings can be changed by a tenant admin.  For more information about Azure AD B2B, see [What is guest user access in Azure AD B2B?](/azure/active-directory/b2b/what-is-b2b)  

- Access to an account that can add guest users to an Azure AD tenant. Admins and users with the Guest Inviter role can add guests to a tenant.

- The guest user must have a license with Power Apps use rights that matches the capability of the app assigned through one of the following tenants:

    - The tenant hosting the app being shared.
    - The home tenant of the guest user.

## Steps to grant guest access

1. Select **New guest user** to add guest users in Azure AD. More information: [Quickstart: Add a new guest user in Azure AD](/azure/active-directory/b2b/b2b-quickstart-add-guest-users-portal).

    ![Add guest in Azure AD](media/share-app/guest_access_doc_1.png "Add guest in Azure AD")

2. If the guest user doesn't already have a license in their home tenant, assign a license to the guest user.

   - To assign guest users from admin.microsoft.com, see [Assign licenses to one user](/office365/admin/subscriptions-and-billing/assign-licenses-to-users).

   - To assign guest users from portal.azure.com, see [Assign or remove licenses](/azure/active-directory/fundamentals/license-users-groups).
 
   > [!IMPORTANT]
   > You may need to disable the Microsoft 365 admin center preview to assign a license to a guest. 

3. Share the canvas app. 

    1. Sign in to [Power Apps](https://make.powerapps.com).

    1. Select **Apps** from the left pane.

    1. Select a canvas app.

    1. Select **Share** from the command bar.

    1. Enter an email address for a guest user from an Azure AD tenant. More information: [What is guest user access in Azure AD B2B?](/azure/active-directory/b2b/what-is-b2b)

        ![Share with guest](media/share-app/guest_access_doc_2.png "Share with guest")

After you share an app for guest access, guests can discover and access apps shared with them from the email sent to them as part of sharing. You can also share the app URL directly with the guest instead. To find the URL, go to [Power Apps](https://make.powerapps.com), select **Apps** from left pane, select an app, and then select the **Details** tab. The app URL is displayed under **Web link**.

![Guests receive app share email](media/share-app/guest_access_doc_4.png "Guests receive app share email")

## Considerations and limitations for guest access

- Guests may only be assigned the **User** role, and not the **Co-owner** role, for apps shared with them.
- Power Apps guest access leverages Azure B2B.
- Power Apps recognizes guests outlined by states 1 – 4 in the [Azure B2B documentation](https://docs.microsoft.com/azure/active-directory/b2b/user-properties) the guest uses a web browser.
- Power Apps recognizes guests outlined by states 1, 3, and 4 in the [Azure B2B documentation](https://docs.microsoft.com/azure/active-directory/b2b/user-properties) when the guest uses [Power Apps Mobile](https://powerapps.microsoft.com/downloads). More information: [Open Power Apps Mobile, and sign in](../../mobile/run-powerapps-on-mobile.md#open-power-apps-and-sign-in)
- Power Apps can't recognize guests that authenticate using [Azure AD direct federation](https://docs.microsoft.com/azure/active-directory/b2b/direct-federation) or [Email one-time passcode authentication](https://docs.microsoft.com/azure/active-directory/external-identities/one-time-passcode).
- Power Apps [Per App Plans](https://docs.microsoft.com/power-platform/admin/powerapps-flow-licensing-faq#how-is-microsoft-power-apps-and-power-automate-licensed) are scoped to apps in a specific environment, so they can't be recognized across tenants. 
- Power Apps [included with Office](https://docs.microsoft.com/power-platform/admin/pricing-billing-skus#power-appspower-automate-for-microsoft-365) and Power Apps [Per User Plans](https://docs.microsoft.com/power-platform/admin/powerapps-flow-licensing-faq#how-is-microsoft-power-apps-and-power-automate-licensed) in:
    - Azure public cloud: Are recognized across tenants in guest scenarios as they're are not bound to a specific environment.
    - Azure national/sovereign clouds: Are not recognized across tenants in guest scenarios.
    <br> More information: [National clouds](https://docs.microsoft.com/azure/active-directory/develop/authentication-national-cloud), [Azure geographies](https://azure.microsoft.com/global-infrastructure/geographies/#geographies)

## Frequently Asked Questions

### What’s the difference between canvas app guest access and Power Apps portals?

Canvas apps enable building an app, tailored to digitizing business processes, without writing code in a traditional programming language such as C#. Guest access for canvas apps enables teams of individuals made up of different organizations participating in a common business process to access the same app resources that may be integrated with a wide variety of Microsoft and third-party sources. More information: [Overview of canvas-app connectors for Power Apps](/powerapps/maker/canvas-apps/connections-list).

[Power Apps portals](/powerapps/maker/portals/overview) provide the ability to build low-code, responsive websites that allow external users to interact with the data stored in Dataverse. It allows organizations to create websites that can be shared with users external to their organization either anonymously or through the login provider of their choice, such as LinkedIn, Microsoft Account, or other commercial login providers. 

The following table outlines a few core capability differences between Power Apps portals and canvas apps.  

| Portals or canvas apps| Interface | Authentication | Accessible data sources |
|------|--------|----------|-------------------|
| Power Apps portals | Browser only experience | Allows anonymous and authenticated access | Dataverse |
| Canvas apps | Browser and mobile apps | Requires authentication via Azure AD | Any ~150 out-of-box connectors and any custom connector  |
|

### Can guests access customized forms in SharePoint?

Yes. Any user that can access a SharePoint list with a customized form can create and edit items in the list, using the form. As long as the custom form only uses standard connectors, the guest isn't required to have any Power Apps license.

### Why is a guest accessing a customized form in SharePoint prompted for a trial?

If the custom form uses a premium connector, a guest must have a Power Apps license to access the custom form. If the custom form only uses standard connectors, your tenant must allow Power Platform internal consent plans to be assigned to users. For more details about Power Platform internal consent plans, read [block trial license commands](https://docs.microsoft.com/power-platform/admin/powerapps-powershell#block-trial-licenses-commands).  

### Can guests access apps embedded in SharePoint?

Yes. Though, access to canvas standalone apps require a license with Power Apps user rights that matches the capability of the app; including embedded apps. When embedding a canvas app in SharePoint using the Microsoft Power Apps embed control, enter the app id. To do this, enter the app ID in the **App web link or ID** box.

![Embed canvas app in SharePoint for guests](media/share-app/guest_access_doc_5.PNG "Embed canvas app in SharePoint for guests")

When embedding a canvas app in SharePoint via the iFrame HTML tag, reference the app using the full web URL. To find the URL, sign in to [Power Apps](https://make.powerapps.com), select an app, select the **Details** tab, and the URL is displayed under **Web link**.

![Canvas app details](media/share-app/guest_access_doc_6.PNG "Canvas app details")

### How come guests can launch the app shared with them but connections fail to be created?

As with non-guests, the underlying data source(s) accessed by the app must also be made accessible to the guest.

### What license must be assigned to my guest so they can run an app shared with them?

The same license that’s required for non-guests to run an app. For instance, if the app uses premium connectors, then a Power Apps Per App Plan or a Power Apps Per User Plan must be assigned to the guest.  

|    Plan                             | SharePoint customized form | Standalone canvas app using non-premium connectors | Standalone canvas app using premium connectors | Model driven app |
|---------------------------------|----------------------------|----------------------------------------------------|------------------------------------------------|------------------|
| SharePoint user (no PA license) | x                          |                                                    |                                                |                  |
| Power Apps Included w/ Office    | x                          | x                                                  |                                                |                  |
| Power Apps Per App Plan          | x                          | x                                                  | x                                              | x                |
| Power Apps Per User Plan         | x                          | x                                                  | x                                              | x                |

More details around pricing and capabilities of various plans can be found in [Microsoft Power Apps and Power Automate Licensing Guide](https://go.microsoft.com/fwlink/?linkid=2085130).

### In Power Apps Mobile, how does a guest see apps for their home tenant?

Any user that has accessed a canvas app, on their mobile device, that’s published in an Azure AD tenant that isn’t their home tenant must sign out of Power Apps and sign back in to Power Apps Mobile.  

### In Power Apps Mobile, how does a guest see apps in the guest tenant?

As the guest user, open the email received when an app in the guest tenant was shared, and select the **Open the app** button. This applies to both Azure Active Directory and Microsoft Account users.   

### Must a guest accept the Azure AD guest invitation before sharing an app with the guest?

No. If a guest launches an app shared with them before accepting a guest invitation, the guest will be prompted to accept the invitation as part of the sign-in experience while launching the app.  

### What Azure AD tenant are connections for a guest user created in?

Connections for an app are always made in the context of the Azure AD tenant the app is associated. For example, if an app is created in the Contoso tenant, the connections made for Contoso internal and guest users are in the context of the Contoso tenant.

### Can guests use Microsoft Graph via Microsoft Security Graph connector or a custom connector using Microsoft Graph APIs?

No, Azure AD guests can't query Microsoft Graph to retrieve information for a tenant in which they’re a guest.

### What Intune policies apply to guests using my Power Apps?

Intune only applies policies of a user’s home tenant. For instance, if Lesa@Contoso.com shares an app with Wanda@Fabrikam.com, Intune continues to apply Fabrikam.com policies on Wanda’s device regardless of the apps Wanda runs.

### What connectors support guest access?

All connectors that don't use Azure AD authentication of any type supports guest access. The following table enumerates all connectors that use Azure AD authentication and which connectors currently support guest access. More information: [List of all Power Apps connectors](https://docs.microsoft.com/connectors/connector-reference/connector-reference-powerapps-connectors)

| **Connector**                                     | **Supports guest access**                                              |
|---------------------------------------------------|------------------------------------------------------------------------|
| 10to8 Appointment Scheduling                      | No                                                                     |
| Adobe Creative Cloud                              | No                                                                     |
| Adobe Sign                                        | No                                                                     |
| Asana                                             | No                                                                     |
| AtBot Admin                                       | No                                                                     |
| AtBot Logic                                       | No                                                                     |
| Azure AD                                          | Yes                                                                    |
| Azure Automation                                  | Yes                                                                    |
| Azure Container Instance                          | Yes                                                                    |
| Azure Data Factory                                | Yes                                                                    |
| Azure Data Lake                                   | Yes                                                                    |
| Azure DevOps                                      | No                                                                     |
| Azure Event Grid                                  | No                                                                     |
| Azure IoT Central                                 | Yes                                                                    |
| Azure Key Vault                                   | No                                                                     |
| Azure Kusto                                       | Yes                                                                    |
| Azure Log Analytics                               | Yes                                                                    |
| Azure Resource Manager                            | Yes                                                                    |
| Basecamp 2                                        | No                                                                     |
| Bitbucket                                         | No                                                                     |
| Bitly                                             | No                                                                     |
| bttn                                              | No                                                                     |
| Buffer                                            | No                                                                     |
| Business Central                                  | No                                                                     |
| CandidateZip                                      | No                                                                     |
| Capsule CRM                                       | No                                                                     |
| Cloud PKI Management                              | No                                                                     |
| Cognito Forms                                     | No                                                                     |
| Commmon Data Service                               | Yes*                                                                     |
| Common Data Service (Legacy)                      | No                                                                     |
| D&B Optimizer                                     | No                                                                     |
| Derdack SIGNL4                                    | No                                                                     |
| Disqus                                            | No                                                                     |
| Document Merge                                    | No                                                                     |
| Dynamics 365                                      | No                                                                     |
| Dynamics 365 AI for Sales                         | Yes                                                                    |
| Dynamics 365 for Fin & Ops                        | No                                                                     |
| Enadoc                                            | No                                                                     |
| Eventbrite                                        | No                                                                     |
| Excel Online (Business)                           | No                                                                     |
| Excel Online (OneDrive)                           | No                                                                     |
| Expiration Reminder                               | No                                                                     |
| FreshBooks                                        | No                                                                     |
| GoToMeeting                                       | No                                                                     |
| GoToTraining                                      | No                                                                     |
| GoToWebinar                                       | No                                                                     |
| Harvest                                           | No                                                                     |
| HTTP with Azure AD                                | No                                                                     |
| Infusionsoft                                      | No                                                                     |
| Inoreader                                         | No                                                                     |
| Intercom                                          | No                                                                     |
| JotForm                                           | No                                                                     |
| kintone                                           | No                                                                     |
| LinkedIn                                          | No                                                                     |
| Marketing Content Hub                             | No                                                                     |
| Medium                                            | No                                                                     |
| Metatask                                          | No                                                                     |
| Microsoft Forms                                   | No                                                                     |
| Microsoft Forms Pro                               | No                                                                     |
| Microsoft Graph Security                          | No                                                                     |
| Microsoft Kaizala                                 | No                                                                     |
| Microsoft School Data Sync                        | No                                                                     |
| Microsoft StaffHub                                | No                                                                     |
| Microsoft Teams                                   | Yes                                                                    |
| Microsoft To-Do (Business)                        | No                                                                     |
| Muhimbi PDF                                       | No                                                                     |
| NetDocuments                                      | No                                                                     |
| Office 365 Groups                                 | Yes                                                                    |
| Office 365 Outlook                                | No                                                                     |
| Office 365 Users                                  | Yes                                                                    |
| Office 365 Video                                  | No                                                                     |
| OneDrive                                          | No                                                                     |
| OneDrive for Business                             | No                                                                     |
| OneNote (Business)                                | No                                                                     |
| Outlook Tasks                                     | Yes                                                                    |
| Outlook.com                                       | No                                                                     |
| Paylocity                                         | No                                                                     |
| Planner                                           | No                                                                     |
| Plumsail Forms                                    | No                                                                     |
| Power Apps for Admins | No |
| Power Apps for Makers | No |
| Power Automate Management | No |
| Power BI                                          | Yes                                                                    |
| Power Platform for Admins                                          | No                                                                    |
| Project Online                                    | No                                                                     |
| ProjectWise Design Integration                    | No                                                                     |
| Projectwise Share                                 | No                                                                     |
| SharePoint                                        | Yes                                                                    |
| SignNow                                           | No                                                                     |
| Skype for Business Online                         | No                                                                     |
| Soft1                                             | No                                                                     |
| Stormboard                                        | No                                                                     |
| Survey123                                         | No                                                                     |
| SurveyMonkey                                      | No                                                                     |
| Toodledo                                          | No                                                                     |
| Typeform                                          | No                                                                     |
| Vimeo                                             | No                                                                     |
| Webex Teams                                       | No                                                                     |
| Windows Defender Advanced Threat Protection (ATP) | No                                                                     |
| Word Online (Business)                            | No                                                                     |

\* When using the Common Data Service connector, ensure the guest user is licensed from the same tenant where you have Dataverse located.

### See also

- [Edit an app](edit-app.md)
- [Restore an app to a previous version](restore-an-app.md)
- [Export and import an app](export-import-app.md)
- [Delete an app](delete-app.md)
