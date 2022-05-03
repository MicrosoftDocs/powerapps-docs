---
title: "Set up a Postman environment (Microsoft Dataverse for Apps)| MicrosoftDocs"
description: "Learn how to set up and configure a Postman environment that connects with Microsoft Dataverse environments."
ms.date: 04/03/2022
author: divka78
ms.author: dikamath
manager: sunilg
ms.reviewer: jdaly
ms.topic: article
search.audienceType: 
  - developer
search.app: 
  - D365CE
contributors:
 - JimDaly
 - phecke
---

# Set up a Postman environment

 Managing authentication challenges many people. This article describes how to configure a Postman environment to work for your Dataverse environments without you having to register your own Azure Active Directory (Azure AD) application. It also shows how to use a Postman environment to save a set of variables that you use to connect. These variable values can be accessed within Postman by using this syntax: `{{variablename}}`. For more information with Postman variables, see [Postman Documentation > Variables](https://www.getpostman.com/docs/v6/postman/environments_and_globals/variables).

## Prerequisites

* Have a Power Apps Dataverse environment that you can connect to. 
* Download and install the [Postman desktop application](https://www.getpostman.com/apps).

<a name="bkmk_connectcds"></a> 

## Connect with your Dataverse environmentf
> [!IMPORTANT]
> 
> To save you time and get you started right away, we have provided a Client ID for an application that is registerd for all Dataverse environment, so you don't have to register your own Azure Active Directory (Azure AD) application to connect with Dataverse API.

The following steps show you how to set up a Postman environment to connect with Dataverse API. To register your own Azure AD application, see the steps described in [Walkthrough: Register a Dataverse app with Azure Active Directory](../walkthrough-register-app-azure-active-directory.md).

1. Launch the Postman desktop application. 
1. To create a new environment, select **Environments** on the left and click +.  
   :::image type="content" source="media/setup-postman-create-new-environment.png" alt-text=" media/setup-postman-create-new-environment.png ":::
1. Enter a name for your environment, for example, <b>MyNewEnvironment</b>. 
1. Sign into Power Apps to get your organizational base url. 
1. Select your Power Apps environment and then click the <b>Settings</b> button in the top-right corner. Then click <b>Developer resources</b>.
:::image type="content" source="media/setup-postman-powerapps-environment.png" alt-text="media/setup-postman-powerapps-environment.png":::
1. On the Developer resources page, retrieve the base url of the Web API endpoint.
:::image type="content" source="media/setup-postman-developerresource.png" alt-text="media/setup-postman-developerresource.png":::
1. Add the following key-value pairs into the editing space.
   | VARIABLE | INITIAL VALUE | ACTION |
   |----|---|---|
   |`url`| use the base url of your Web API endpoint | use the base url of your Web API endpoint|
   |`clientid`|`51f81489-12ee-4a9e-aaae-a2591f45987d`| Copy the value|
   |`version`|`9.2`| Copy the value | 
   |`webapiurl`|`{{url}}/api/data/v{{version}}/`| Copy the value |
   |`callback`|`https://localhost`| Copy the value |
   |`authurl`|`https://login.microsoftonline.com/common/oauth2/authorize?resource={{url}}`| Copy the value |

1. Your settings should appear something like below:
:::image type="content" source="media/setup-postman-create-new-environment-with-values.png" alt-text="media/setup-postman-create-new-environment-with-values.png":::        
1. Click **Save** to save your newly created environment named <b>MyNewEnvironment</b>.

### Generate an access token to use with your environment

To connect using **OAuth 2.0**, you must have an access token. Use the following steps to get a new access token:

1. Make sure the newly created environment <b>MyNewEnvironment</b> is selected. 
:::image type="content" source="media/setup-postman-preuathorization.png" alt-text="media/setup-postman-preauthorization.png":::
1. Click <b>+</b> right next to MyNewEnvironment. The following pane appears:
:::image type="content" source="media/setup-postman-untitledrequest.PNG" alt-text="media/setup-postman-untitledrequest":::
1. Select the **Authorization** tab. Then set the **Type** to **OAuth 2.0**, and set **Add authorization data to** to **Request Headers**.
:::image type="content" source="media/setup-postman-oauth-request-headers.png" alt-text="setup-postman-oauth-request-headers.png":::
1. In the **Configure New Token** pane, set the following values: 
   
   | Name | Value | Action |
   |----|---|---|
   |Grant Type| implicit| Choose implicit from the drop-down |
   |Callback URL| `{{callback}}`| Copy the value |
   |Auth URL|`{{authurl}}`| Copy the value |  
   |Client ID|`{{clientid}}`| Copy the value |  

1. Your settings should appear something like below: 
    :::image type="content" source="media/setup-postman-configuration-new-token.png" alt-text="media/setup-postman-configuration-new-token.png ":::
1. Click **Get New Access Token**. When you do this, an Azure Active Directory sign-in dialog box appears. Enter your username and password, and then click **Sign In**. Once authentication completes, the following dialogue appears.
:::image type="content" source="media/setup-postman-authentication-completes.png" alt-text="media/setup-postman-authentication-completes.png":::
1. After the authentication dialogue automatically closes in a few seconds, the **Manage Access Tokens** page appears. Click **Use Token**. 
:::image type="content" source="media/setup-postman-manage-access-tokenpage.png" alt-text="setup-postman-manage-access-tokenpage.png":::
1. The newly generated token will automatically appear in the text box below the **Available Tokens** drop-down.
:::image type="content" source="media/setup-postman-access-token-autopopulate.png" alt-text="media/setup-postman-access-token-autopopulate.png":::

   > [!NOTE]
   > If you are configuring environments in Postman for multiple Dataverse instances using different user credentials, you might need to delete the cookies cached by Postman. Click the **Clear cookies**, which can be found right above the **Get New Access Token** button to  remove the saved cookies.
:::image type="content" source="media/setup-postman-clear-cookies.PNG" alt-text="media/setup-postman-clear-cookies.png":::


## Test your connection

Create a new Web API request to test the connection with your Dataverse instance. Use the [WhoAmI](xref:Microsoft.Dynamics.CRM.WhoAmI):
1. Select `GET` as the HTTP method and add `{{webapiurl}}WhoAmI` in the editing space.
:::image type="content" source="media/setup-postman-whoami.png" alt-text="media/setup-postman-whoami.png":::
2. Click **Send** to send this request.
3. If your request is successful, you see the data from the `WhoAmI`.

## See also

[Use Postman to perform operations](use-postman-perform-operations.md)<br/>
[Walkthrough: Register a Dataverse app with Azure Active Directory](../walkthrough-register-app-azure-active-directory.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
