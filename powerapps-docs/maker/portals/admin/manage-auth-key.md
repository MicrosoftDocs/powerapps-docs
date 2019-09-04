---
title: "Connect a portal to a Dynamics 365 online organization | MicrosoftDocs"
description: "Learn how to connect a portal to a Dynamics 365 online organization and how to renew the authentication key."
author: sbmjais
manager: shujoshi
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 08/30/2019
ms.author: shjais
ms.reviewer:
---

# Connect to a Dynamics 365 online organization using a portal

[!include[cc-beta-prerelease-disclaimer](../../../includes/cc-beta-prerelease-disclaimer.md)]

A portal connects to a Dynamics 365 online organization using an Azure Active Directory application. The application is created in the same tenant where the portal is provisioned. The application is registered with the Dynamics 365 organization during the portal provisioning process.

![Connecting a portal with Dynamics 365 organization](../media/connect-with-dynamics.png "Connecting a portal with Dynamics 365 organization")

Each portal has a separate Azure Active Directory application associated with it, whether it is connected to the same Dynamics 365 organization or not. The default Azure Active Directory authentication provider created for a portal uses the same Azure Active Directory application to authenticate the portal. Authorization is enforced by web roles assigned to the user accessing the portal.

You can see the associated portal application in Azure Active Directory. The name of this application will be Microsoft CRM Portals, and the portal ID is in the **App ID URI** field in the Azure Active Directory application. The person who provisions the portal owns this application. You should not delete or modify this application, or you might break the portal functionality. You must be the application owner to manage a portal from the Portal Admin Center.

## Authentication key

For a Portal to connect to Dynamics 365 using an Azure Active Directory application, it requires an authentication key connected to the Azure Active Directory application. This key is generated when you provision a portal and the public part of this key is automatically uploaded to the Azure Active Directory application.

> [!IMPORTANT]
> The authentication key will expire in two years. It must be renewed every two years to ensure that your portal will continue to connect to the Dynamics 365 organization. If you do not update the key, the portal will stop working.  

### Authentication key details

The details of an authentication key is displayed on Portal Admin Center and portal.

**Portal Admin Center**

1. Open [PowerApps Portals admin center](admin-overview.md).

2. Select **Manage portal authentication key**. The authentication key is displayed along with its expiration date and thumbprint.

   > [!div class=mx-imgBorder]
   > ![Authentication key details in Portal Admin Center](../media/manage-auth-key.png "Authentication key details in Portal Admin Center")

**Portal**

1. Sign in to the portal as administrator.

2. Navigate to the URL <portal_path>/_services/about. The authentication key expiration date is displayed. 

   > [!div class=mx-imgBorder]
   > ![Portal service page](../media/portal-services-page.png "Portal service page")

> [!NOTE]
> To view authentication key information, you must sign in to the portal in the same browser session and you must have all website access permission.

### Authentication key expiration notification

Before the authentication key expires, you will be notified by emails, Portal Admin Center, and portal.

**Email**

Email will be sent to people who have signed up for email notification for the organization connected to their portal. More information about signing up for email notification: [Manage email notifications to admins](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/admin/manage-email-notifications)

Email notifications are sent at the following intervals: 
- 90 days 
- 60 days 
- 30 days 
- 15 days 
- 7 days 
- 6 days 
- 5 days 
- 4 days 
- 3 days 
- 2 days 
- 1 day 
- 12 hours 
- 6 hours 
- 3 hours

You will also be notified after the key expires every day until 1 week after key expiration.

> [!NOTE]
> - Intervals are calculated in UTC from the key expiration date.
> - Email is not guaranteed to be exactly at the intervals as listed above. Email notification can be delayed or missed. Be sure to check for the key expiration date online as well.

**Portal Admin Center**

A message about key expiration is displayed at the top of the page.

> [!div class=mx-imgBorder]
> ![Authentication key notification in Portal Admin Center](../media/portal-admin-center-auth-notif.png "Authentication key notification in Portal Admin Center")

**Portal**

When you navigate to the URL <portal_path>/_services/about, a notification about key expiration is displayed at the bottom of the page.

> [!NOTE]
> You must sign in to your portal in the same browser session, and you must be assigned all website access permission.

> [!div class=mx-imgBorder]
> ![Authentication key notification on portal](../media/portal-service-page-auth-notif.png "Authentication key notification on portal")

## Renew portal authentication key

You must renew the key every two years to ensure that your portal can connect to Dynamics 365 organization.

> [!NOTE]
> To renew the key, you must have permissions to manage your portal.

1. Open [PowerApps Portals admin center](admin-overview.md).

2. Select **Manage portal authentication key**. The authentication key is displayed along with its expiration date and thumbprint.

    > [!div class=mx-imgBorder]
    > ![Manage portal authentication key](../media/manage-portal-auth-key.png "Manage portal authentication key")

3. Select **Update key**.

4. Select **Update** in the message. The update process starts, and a message is displayed.

> [!NOTE]
> - While this process runs in the background, the portal will restart once.
> - When you update a key, it is updated for two years.
> - This process will take five to seven minutes.

### Troubleshooting

If the key update fails, an error message is displayed along with the following action:

- **Retry Authentication Key Update**. This action allows you to restart the portal authentication key update process. If the update fails multiple times, contact Microsoft support.

    > [!div class=mx-imgBorder]
    > ![Retry portal authentication key update](../media/retry-auth-key-update.png "Retry portal authentication key update")