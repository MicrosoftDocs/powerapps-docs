---
title: "Use single-tenant server-to-server authentication (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to access Microsoft Dataverse data in a single tenant from an application or service without explicit user authentication." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 04/06/2023
ms.reviewer: "pehecke"
ms.topic: how-to
author: "paulliew" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "pehecke" # MSFT alias of Microsoft employees only
search.audienceType:
  - developer
---

# Use single-tenant server-to-server authentication

The single-tenant server-to-server (S2S) scenario typically applies for enterprise organizations that have multiple Microsoft Dataverse environments using Active Directory Federation Services (AD FS) for authentication. However, it can also be applied by environments when the application won't be distributed to other environments.

An enterprise can create a web application or service to connect to any Dataverse environments associated with a single Microsoft Entra ID tenant.

## Differences from multi-tenant scenario

Creating a web application or service for single-tenant server-to-server authentication is similar to authentication for a multi-tenant organization but there are some important differences.

- Because all the organizations are in the same tenant, there is no need for a tenant administrator to grant consent for each organization. The application is simply registered once for the tenant.

- You have the opportunity to use certificates rather than keys if you prefer.

In the [See also](#bkmk_seealso) section at the end of this article, there are links to information on upgrading a single-tenant application to multi-tenancy.

<a name="bkmk_Requirements"></a>

## Requirements

To create and test a single-tenant application that uses server-to-server authentication you will need:

- An Microsoft Entra ID tenant to use when registering the provided sample application.
- A Dataverse subscription that is associated with the Microsoft Entra ID tenant.
- Administrator privileges in the Microsoft Entra ID tenant and Dataverse environment.

<a name="bkmk_registration"></a>

## Azure application registration

To create an application registration in Microsoft Entra ID, follow these steps.

1. Navigate to https://admin.microsoft.com and sign in.
1. Select **Admin centers** > **Microsoft Entra ID**.
1. From the left navigation panel, select **Applications** > **App registrations**.
1. Select **+ New registration**.
1. In the **Register an application** form provide a name for your app, select **Accounts in this organizational directory only**, and then select **Register**. A redirect URI is not needed for this walkthrough and the provided sample code.

    :::image type="content" source="media/S2S-app-registration-started.PNG" alt-text="Register an application form.":::

1. In the navigation panel, select **API permissions**.
1. On the **API permissions** page select **Grant admin consent for "org-name"**, if it is not already selected, and when prompted choose **Yes**. Note that Delegated permissions are not required for this server-to-server scenario.

    :::image type="content" source="media/S2S-api-permission-completed.PNG" alt-text="Granting API permissions.":::

1. Select **Overview** in the navigation panel then record the **Display name**, **Application (client) ID**, and **Directory (tenant) ID** values of the app registration.
1. In the navigation panel, select **Certificates & secrets**.
1. Below **Client secrets**, choose **+ New client secret** to create a secret.
1. In the form, enter a description and select **Add**. Record the secret string. You will not be able to view the secret again once you leave the current screen.

The Application ID, Directory ID, and client secret will be needed for web service authentication.

<a name="bkmk_appuser"></a>

## Application user creation

You can create an unlicensed "application user" in your environment. This application user will be given access to your environment's data on behalf of the end user who is using your application.

For instructions on creating an application user see [Create an application user](/power-platform/admin/manage-application-users#create-an-application-user).

For instructions on managing security roles for an application user see [Manage roles for an application user](/power-platform/admin/manage-application-users#manage-roles-for-an-application-user)

> [!NOTE]
> In an environment, only one application user for each Microsoft Entra ID registered application is supported. You will not be able to change the primary email address or username once the application user is created.<p/>
> When developing a real-world application using S2S, you should use a custom security role which can be stored in a solution and distributed along with your application.

## Enable or disable application users

When application users are created, they are automatically activated. In the event that an application user’s status is deactivated and you need to activate it, you do so using the Power Platform Admin Center. You can also use the Power Platform Admin Center to deactivate an application user that is no longer used.

More information: [Activate or deactivate an application user](/power-platform/admin/manage-application-users#activate-or-deactivate-an-application-user)

> [!CAUTION]
> Disabling an application user will break all the integration scenarios that use the application user.

<a name="bkmk_coding"></a>

## Application coding and execution

Follow these steps to download, build, and execute the sample application. The sample calls the Web API to return a list of the top 3 accounts (by name) in the organization.

1. Download the Visual Studio 2017 SingleTenantS2S [sample](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/CSharp/SingleTenantS2S).
2. Update the App.config file with your app registration and server key values.
3. Build and run the application.

### Expected results

An OData response listing the names of the top 3 accounts in your organization.

### Example console output

Shown below is example console output obtained from an organization that only had two accounts named "Test Account 1", and "Test Account 2".

```json
{
  "@odata.context": "https://crmue2.api.crm.dynamics.com/api/data/v9.1/$metadata#accounts(name)",
  "@Microsoft.Dynamics.CRM.totalrecordcount": -1,
  "@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded": false,

  "value": [
    {
      "@odata.etag": "W/\"4648334\"",
      "name": "Test Account 1",
      "accountid": "28630624-cac9-e811-a964-000d3a3ac063"
    },
    {
      "@odata.etag": "W/\"4648337\"",
      "name": "Test Account 2",
      "accountid": "543fd72a-cac9-e811-a964-000d3a3ac063"
    }
  ]
}
```

<a name="bkmk_seealso"></a>

### See also

[Use Multi-Tenant server-to-server authentication](use-multi-tenant-server-server-authentication.md)  
[Build web applications using server-to-server (S2S) authentication](build-web-applications-server-server-s2s-authentication.md)  
[How to: Sign in an Microsoft Entra ID user using the multi-tenant application pattern](/azure/active-directory/develop/howto-convert-app-to-be-multi-tenant)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
