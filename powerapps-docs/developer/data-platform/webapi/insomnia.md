---
title: "Use Insomnia with Dataverse Web API"
description: "Learn how to set up and configure Insomnia with environments that connect with Microsoft Dataverse environments."
ms.date: 03/11/2024
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

# Use Insomnia with Dataverse Web API

There are many third-party tools you can use to authenticate to Microsoft Dataverse environments to compose and send Web API requests. This article describes a strategy to authenticate and connect to Dataverse using a Microsoft Entra application (client) ID for an application registered by Microsoft that is pre-approved for all Dataverse environments. This means you don't need to register an application to get started using the Dataverse Web API. This article describes how to use this client ID with the popular [Insomnia API client](https://insomnia.rest/).

One of the benefits that Insomnia provides is that it doesn't require that you create an account and doesn't store information about requests you send.

> [!NOTE]
> You can also use PowerShell with Visual Studio Code to authenticate with Dataverse Web API as an alternative to Insomnia or other API clients. [Get started using Web API with PowerShell and Visual Studio Code](quick-start-ps.md). This method:
>
> - Uses the Azure AD app registration so you don't need to provide an application (client) ID.
> - Refreshes your access token automatically so you don't need to keep requesting a new one when they expire.
>
> The instructions in this article represent the experience provided by Insomnia when this article was written. The user experience will probably change over time and this article might not represent the current experience. This article will be updated only when changes occur that fundamentally break the authentication procedure described here.


## Install Insomnia

See the [Insomnia documentation for steps to install Insomnia](https://docs.insomnia.rest/insomnia/install). The instructions are different for MacOS, Windows, and Linux.

For Windows, the installer is an executable (exe) that you download and run. When the installation completes, you might be offered different options. These options shouldn't interfere with the instructions in this article, but not all were tested. At the time this article was written, these option were presented:

- For the option to enable features to sync data with the cloud, choose **Keep storing locally in Local Vault**.
- For the option to create an account, choose **Use the local Scratch Pad**. This limits some of the capabilities of Insomnia. [Learn more about Insomnia Scratch Pad](https://docs.insomnia.rest/insomnia/scratchpad)

   :::image type="content" source="media/welcome-to-insomnia.png" alt-text="The welcome to insomnia dialog including the Use the local Scratch Pad option.":::

## Create an environment

Use Insomnia environments to store environment variables that you will use to connect to Dataverse environments. An Insomnia environment is a JSON object containing key-value pairs of data that you can reference for many purposes.

The *[base environment](https://docs.insomnia.rest/insomnia/environment-variables#base-environment)* is assigned to every workspace and the variables within it can be accessed throughout the workspace. If you only ever need to connect to a single environment, you could use the instructions below with the base environment. However, since you will probably need to connect to more than one environment, we recommend creating a *[sub environment](https://docs.insomnia.rest/insomnia/environment-variables#sub-environments)* for each environment you need to connect to. For example, you can create a sub environment for your development, test, and production environments.

1. After you have opened Insomnia, select the gear icon :::image type="icon" source="media/insomnia-gear-icon.png" border="false"::: next to the base environment to open the **Manage Environments** dialog.
1. Select the :::image type="icon" source="media/insomnia-plus-icon.png" border="false"::: icon to create a new environment. Environments can be *shared* or *private*. Choose **Private environment**.
1. Double click the name of the **New Environment** you just created and rename it as you like, you can give it the name of the Dataverse environment you want to connect to, or something like **Dev environment.**
1. Copy the following JSON:

   ```json
   {
      "url": "https://yourorg.api.crm.dynamics.com",
      "version": "9.2",
      "webapiurl": "{{ _.url }}/api/data/v{{ _.version }}/",
      "redirecturl": "https://localhost",
      "authurl": "https://login.microsoftonline.com/common/oauth2/authorize?resource={{ _.url }}",
      "clientid": "51f81489-12ee-4a9e-aaae-a2591f45987d"
   }
   ```

1. Paste the JSON into the environment you created.
1. Edit the `url` and replace the `https://yourorg.api.crm.dynamics.com` value  match the URL for your environment.

   You can find the Web API endpoint for your environment using the instructions in [View developer resources](../view-download-developer-resources.md). Remove `/api/data/v9.2` from the Web API endpoint URL. This URL must end in `dynamics.com`.

   You should expect that the references to the `_.url` and `_.version` variables will not resolve immediately, so you will see warnings like this:

   :::image type="content" source="media/insomnia-unresolved-environment-variables.png" alt-text="Unresolved environment variables":::

   However, after you close the window and re-open it, you can see that the variables are now known and resolved.

   :::image type="content" source="media/insomnia-resolved-environment-variables.png" alt-text="Resolved environment variables":::





<!-- OLD -->

To save you time and get you started right away, this article describes how to configure and use a Postman environment to work for your Dataverse environments without registering your own Microsoft Entra ID application. For information on Postman environment and variables, see [Postman Documentation > Variables](https://learning.postman.com/docs/sending-requests/managing-environments).

> [!NOTE]
> You can also use PowerShell with Visual Studio Code to authenticate with Dataverse Web API as an alternative to Postman. [Get started using Web API with PowerShell and Visual Studio Code](quick-start-ps.md). This method: 
>
> - Uses the Azure AD app registration so you don't need to provide an application (client) ID.
> - Refreshes your access token automatically so you don't need to keep requesting a new one.

## Prerequisites

* Have a Power Apps Dataverse environment that you can connect to. 
* Download and install the [Postman desktop application](https://www.getpostman.com/apps).
* Have a Postman account [Postman Sign up](https://identity.getpostman.com/signup).

<a name="bkmk_connectcds"></a> 

## Connect with your Dataverse environment

> [!IMPORTANT]
> To save you time and get you started right away, we have provided a Client ID for an application that is registered for all Dataverse environments, so you don't have to register your own Microsoft Entra ID application to connect with Dataverse API.

1. Launch the Postman desktop application. 
1. To create a new environment, select **Environments** on the left and select <b>+</b>.
  
   :::image type="content" source="media/setup-postman-create-new-environment.png" alt-text="Create a new environment":::
   
1. Enter a name for your environment, for example, <b>MyNewEnvironment</b>. 
1. Sign into [Power Apps](https://make.powerapps.com/) to get the base url of the Web API endpoint. 
1. Select your Power Apps environment and then select the <b>Settings</b> button in the top-right corner. Then select <b>Developer resources</b>.

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

1. Your settings should appear something like the following:

    :::image type="content" source="media/setup-postman-create-new-environment-with-values.png" alt-text="New environment with values":::     
   
1. Select **Save** to save your newly created environment named <b>MyNewEnvironment</b>.

1. With your newly created environment selected, set it as the *active* one by either:
  - Clicking the ellipses menu near the top-right and selecting **Set as active environment**, or
  - Clicking the environment dropdown in the top-right and selecting **MyNewEnvironment**".

### Generate an access token to use with your environment

To connect using **OAuth 2.0**, you must have an access token. Use the following steps to get a new access token:

1. Make sure the newly created environment <b>MyNewEnvironment</b> is selected. Select <b>+</b> right next to <b>MyNewEnvironment</b>. 

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

1. Your settings should appear something like the following: 
    
    :::image type="content" source="media/setup-postman-configuration-new-token.png" alt-text="Set up Postman configuration":::

   > [!NOTE]
   > If you are configuring environments in Postman for multiple Dataverse instances using different user credentials, click **Clear cookies** to delete the cookies cached by Postman. 
    
1. Select **Get New Access Token**. 
   
   Once you select **Get New Access Token**, a Microsoft Entra ID sign-in dialog box appears. Enter your username and password, and then select **Sign In**. Once authentication completes, the following dialogue appears.

    :::image type="content" source="media/setup-postman-authentication-completes.png" alt-text="Authentication completes":::

1. After the authentication dialogue automatically closes in a few seconds, the **Manage Access Tokens** pane appears. Select **Use Token**. 

    :::image type="content" source="media/setup-postman-manage-access-tokenpage.png" alt-text="Access token page":::

1. The newly generated token automatically appears in the text box below the **Available Tokens** drop-down.

    :::image type="content" source="media/setup-postman-access-token-autopopulate.png" alt-text="Token autopopulate":::

## Test your connection 

Use these steps to test your connection using [WhoAmI](xref:Microsoft.Dynamics.CRM.WhoAmI):

1. Select `GET` as the HTTP method and add `{{webapiurl}}WhoAmI` in the editing space.

    :::image type="content" source="media/setup-postman-whoami-url.png" alt-text="Calling WhoAmI endpoint":::
   
1. Select **Send** to send this request.
1. If your request is successful, see the <xref:Microsoft.Dynamics.CRM.WhoAmIResponse> data returned from the `WhoAmI` function:

    :::image type="content" source="media/setup-postman-whoami.png" alt-text="Response from WhoAmI":::

## Next steps

Learn about using Postman to perform operations with the Web API.

> [!div class="nextstepaction"]
> [Service Documents](use-postman-perform-operations.md)<br/>

## See also

[Use Postman to perform operations](use-postman-perform-operations.md)<br/>
[Walkthrough: Register a Dataverse app with Microsoft Entra ID](../walkthrough-register-app-azure-active-directory.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
