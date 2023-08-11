---
title: "Set up a Postman environment (Microsoft Dataverse for Apps)| MicrosoftDocs"
description: "Learn how to set up and configure a Postman environment that connects with Microsoft Dataverse environments."
ms.date: 05/04/2022
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
ms.topic: article
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - phecke
---

# Set up a Postman environment

 To save you time and get you started right away, this article describes how to configure and use a Postman environment to work for your Dataverse environments without you having to register your own Azure Active Directory (Azure AD) application. For information on Postman environment and variables, see [Postman Documentation > Variables](https://learning.postman.com/docs/sending-requests/managing-environments).

## Prerequisites

* Have a Power Apps Dataverse environment that you can connect to. 
* Download and install the [Postman desktop application](https://www.getpostman.com/apps).
* Have a Postman account [Postman Sign up](https://identity.getpostman.com/signup).

<a name="bkmk_connectcds"></a> 

## Connect with your Dataverse environment

> [!IMPORTANT]
> To save you time and get you started right away, we have provided a Client ID for an application that is registered for all Dataverse environments, so you don't have to register your own Azure Active Directory (Azure AD) application to connect with Dataverse API.

1. Launch the Postman desktop application. 
1. To create a new environment, select **Environments** on the left and click <b>+</b>.
  
   :::image type="content" source="media/setup-postman-create-new-environment.png" alt-text="Create a new environment":::
   
1. Enter a name for your environment, for example, <b>MyNewEnvironment</b>. 
1. Sign into [Power Apps](https://make.powerapps.com/) to get the base url of the Web API endpoint. 
1. Select your Power Apps environment and then click the <b>Settings</b> button in the top-right corner. Then click <b>Developer resources</b>.

    :::image type="content" source="media/setup-postman-powerapps-environment.png" alt-text="PowerApps environment":::
    
1. In the **Developer resources** pane, retrieve the base url of the Web API endpoint.

    :::image type="content" source="media/setup-postman-developerresource.png" alt-text="Postman developer resources":::
    
1. In Postman, add the following key-value pairs into the editing space and use initial value for current value.

   | VARIABLE | INITIAL VALUE | ACTION |
   |----|---|---|
   |`url`| `https://<your org name>.api.crm.dynamics.com` | Use the base url of the Web API endpoint|
   |`clientid`|`51f81489-12ee-4a9e-aaae-a2591f45987d`| Copy the value|
   |`version`|`9.2`| Copy the value | 
   |`webapiurl`|`{{url}}/api/data/v{{version}}/`| Copy the value |
   |`callback`|`https://localhost`| Copy the value |
   |`authurl`|`https://login.microsoftonline.com/common/oauth2/authorize?resource={{url}}`| Copy the value |

1. Your settings should appear something like below:

    :::image type="content" source="media/setup-postman-create-new-environment-with-values.png" alt-text="New environment with values":::     
   
1. Click **Save** to save your newly created environment named <b>MyNewEnvironment</b>.

1. With your newly created environment selected, set it as the *active* one by either:
  - Clicking the ellipses menu near the top-right and selecting **Set as active environment**, or
  - Clicking the environment dropdown in the top-right and selecting **MyNewEnvironment**".

### Generate an access token to use with your environment

To connect using **OAuth 2.0**, you must have an access token. Use the following steps to get a new access token:

1. Make sure the newly created environment <b>MyNewEnvironment</b> is selected. Click <b>+</b> right next to <b>MyNewEnvironment</b>. 

    :::image type="content" source="media/setup-postman-preuathorization.png" alt-text="Preauthorization":::
    
1. The following pane appears. Select the **Authorization** tab. 

    :::image type="content" source="media/setup-postman-untitledrequest.PNG" alt-text="Untitled request":::
    
1. Set the **Type** to **OAuth 2.0** and set **Add authorization data to** to **Request Headers**.

    :::image type="content" source="media/setup-postman-oauth-request-headers.png" alt-text="Auth request headers":::
    
1. In the **Configure New Token** pane, set the following values: 
   
   | Name | Value | Action |
   |----|---|---|
   |Grant Type| implicit| Choose implicit from the drop-down |
   |Callback URL| `{{callback}}`| Copy the value |
   |Auth URL|`{{authurl}}`| Copy the value |  
   |Client ID|`{{clientid}}`| Copy the value |  

1. Your settings should appear something like below: 
    
    :::image type="content" source="media/setup-postman-configuration-new-token.png" alt-text="Set up Postman configuration":::

   > [!NOTE]
   > If you are configuring environments in Postman for multiple Dataverse instances using different user credentials, click **Clear cookies** to delete the cookies cached by Postman. 
    
1. Click **Get New Access Token**. 
   
   Once you click **Get New Access Token**, an Azure Active Directory sign-in dialog box appears. Enter your username and password, and then click **Sign In**. Once authentication completes, the following dialogue appears.

    :::image type="content" source="media/setup-postman-authentication-completes.png" alt-text="Authentication completes":::

1. After the authentication dialogue automatically closes in a few seconds, the **Manage Access Tokens** pane appears. Click **Use Token**. 

    :::image type="content" source="media/setup-postman-manage-access-tokenpage.png" alt-text="Access token page":::

1. The newly generated token will automatically appear in the text box below the **Available Tokens** drop-down.

    :::image type="content" source="media/setup-postman-access-token-autopopulate.png" alt-text="Token autopopulate":::

## Test your connection 

The following shows how to test your connection using [WhoAmI](xref:Microsoft.Dynamics.CRM.WhoAmI):

1. Select `GET` as the HTTP method and add `{{webapiurl}}WhoAmI` in the editing space.

    :::image type="content" source="media/setup-postman-whoami-url.png" alt-text="Calling WhoAmI endpoint":::
   
1. Click **Send** to send this request.
1. If your request is successful, you will see the data returning from the `WhoAmI` endpoint, like below:

    :::image type="content" source="media/setup-postman-whoami.png" alt-text="Response from WhoAmI":::

## Next steps

Learn about using Postman to perform operations with the Web API.

> [!div class="nextstepaction"]
> [Service Documents](use-postman-perform-operations.md)<br/>

## See also

[Use Postman to perform operations](use-postman-perform-operations.md)<br/>
[Walkthrough: Register a Dataverse app with Azure Active Directory](../walkthrough-register-app-azure-active-directory.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
