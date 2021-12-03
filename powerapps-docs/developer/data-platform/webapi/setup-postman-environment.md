---
title: "Set up a Postman environment (Microsoft Dataverse for Apps)| MicrosoftDocs"
description: "Learn how to set up and configure a Postman environment that connects with Microsoft Dataverse environments."
ms.custom: 
ms.date: 04/09/2019
ms.reviewer: "pehecke"
ms.service: powerapps
ms.suite: 
ms.tgt_pltfrm: 
ms.topic: article
ms.assetid: 955BA444-A53D-4843-9429-833B1636E2B4
caps.latest.revision: 7
author: JimDaly
ms.author: jdaly
manager: ryjones
search.audienceType: 
  - developer
search.app: 
  - D365CE
---

# Set up a Postman environment

You can use Postman to connect to your Microsoft Dataverse instance and to compose Web API requests, send them, and view responses. Managing authentication challenges many people. This topic describes how to configure a Postman environment to work for your Dataverse environments.

You can use a Postman environment to save a set of variables that you use to connect. These values can be accessed within Postman by using this syntax: `{{name}}`. For more information with Postman variables, see [Postman Documentation > Variables](https://www.getpostman.com/docs/v6/postman/environments_and_globals/variables).

## Prerequisites

* Have a Power Apps Dataverse environment that you can connect to. 
* Download and install the [Postman desktop application](https://www.getpostman.com/apps).

<a name="bkmk_connectcds"></a> 

## Connect with your Dataverse environment

This environment uses a client ID for an application that is registered for all Dataverse environments. 

You can use the `clientid` and `callback` values supplied in these instructions.  However, when building your own application, you should register your own Azure Active Directory (Azure AD) application.

To register your own Azure AD application, see the steps described in [Walkthrough: Register a Dataverse app with Azure Active Directory](../walkthrough-register-app-azure-active-directory.md).

Use these steps to create a Postman environment that you can use to connect with your Dataverse instance:

1. Launch the Postman desktop application.
1. Select the **Environment Options** gear icon in the top-right corner. 
1. In the **Manage Environments** dialog box, select the **Add** button to add a new environment.
  
  ![Click on Add button to add a new Postman environment.](media/postman-manage-env.png "Click on Add button to add a new Postman environment")<br>
  
1. In the dialog box that opens, type a name for the environment. Then add the following key-value pairs into the editing space.<br>

    | Variable name | Value |
    |----|---|
    |`url`|`https://<add your environment name, like 'myorg.crm'>.dynamics.com`|
    |`clientid`|`51f81489-12ee-4a9e-aaae-a2591f45987d`|
    |`version`|`9.0`|
    |`webapiurl`|`{{url}}/api/data/v{{version}}/`|
    |`callback`|`https://callbackurl`|
    |`authurl`|`https://login.microsoftonline.com/common/oauth2/authorize?resource={{url}}`|
    > [!NOTE]
    > For [Dataverse search](relevance-search.md), specify a version of 1.0 and a webapiurl of {{url}}/api/search/v{{version}}/.

    ![Create a new Postman environment to connect with Online instance.](media/postman-add-online-env.png "Create a new Postman environment to connect with Online instance")

2. Replace the instance URL placeholder value with the URL of your Dataverse environment, and select **Add** to save the environment.

3. Close the **Manage environments** dialog box.  

### Generate an access token to use with your environment

To connect using **OAuth 2.0**, you must have an access token. Use the following steps to get a new access token:

1. Make sure the new environment you created is selected.
1. Select the **Authorization** tab.
1. Set the **Type** to **OAuth 2.0**.
1. Verify that you have selected the environment that you created.
1. Select **Get New Access Token**

    ![In Authorization tab, set Type to OAuth 2.0.](media/postman-set-type.png)<br>
1. Set the following values in the dialog box. Select `Implicit` from the **Grant Type** drop-down menu. You can set the **Token Name** to whatever you like, and leave other keys set to default values.<br>

    ![Get new Access Token.](media/postman-access-token.png "Get new Access Token")<br>

    > [!NOTE]
    > If you are configuring environments in Postman for multiple Dataverse instances using different user credentials, you might need to delete the cookies cached by Postman. Select the **Cookies** link, which can be found under the **Send** button, and remove the saved cookies from the **Manage Cookies** dialog box.<br>![Remove Cookies.](media/postman-cookies.png "Remove Cookies")<br>
    > Some of these cookies are very persistent. You can delete some of them in groups, but you might have to delete others individually.   You might need to do this twice to ensure that no cookies remain.

1. Select **Request Token**. When you do this, an Azure Active Directory sign-in page appears. Enter your username and password.
1. After the token is generated, scroll to the bottom and select **Use Token**. This closes the **Manage Access Tokens** dialog box. 
1. After you have added a token, you can select which token to apply to requests. On the **Available Tokens** drop-down list, select the token you have just created. The Authorization header gets added to the Web API request.

See [Test your connection](#test-your-connection) for steps to verify your connection.

## Test your connection

Create a new Web API request to test the connection with your Dataverse instance. Use the <xref href="Microsoft.Dynamics.CRM.WhoAmI?text=WhoAmI function" />:
1. Select `GET` as the HTTP method and add `{{webapiurl}}WhoAmI` in the editing space.
  ![WhoAmI function request.](media/postman-whoami-request.png "WhoAmI function request")
2. Select **Send** to send this request.
3. If your request is successful, you see the data from the <xref href="Microsoft.Dynamics.CRM.WhoAmIResponse?text=WhoAmIResponse ComplexType" /> that is returned by the <xref href="Microsoft.Dynamics.CRM.WhoAmI?text=WhoAmI Function" />.

## See also

[Use Postman to perform operations](use-postman-perform-operations.md)<br>
[Walkthrough: Register a Dataverse app with Azure Active Directory](../walkthrough-register-app-azure-active-directory.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]