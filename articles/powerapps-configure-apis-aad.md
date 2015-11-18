<properties
	pageTitle="Configure an API to Connect to AAD Protected Backend | Microsoft Azure"
	description="Configure an API to Connect to AAD Protected Backend"
	services="powerapps"
	documentationCenter="" 
	authors="MandiOhlinger"
	manager="dwrede"
	editor=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na" 
   ms.date="11/17/2015"
   ms.author="guayan"/>

# Configure an API to Connect to AAD Protected Backend

Sometimes your existing backend is protected by Azure Active Directory (AAD). You can configure the API you register in PowerApps to connect to such backend.

#### Prerequisites to get started

- Sign up for PowerApps Enterprise
- Create an App Service Environment
- [Install Azure PowerShell][11]  1.0 Preview or above
- Registered an API in your App Service Environment

## Create an AAD application

The first thing you need to do is to create an AAD application and give it the proper permissions to your existing backend (which is also an AAD application). Following are the steps:

1. In [Azure portal][13], go to your Azure Active Directory and select **applications** tab.  
	![][14]
2. Click the **Add** button at the bottom, then:  
	a. Choose **Add an application my organization is developing**.  
	b. Give it a name and then keep type as **Web application and/or web API**.  
	c. Give it a unqiue **Sign-on URL** and **App ID URI**.  
3. In the newly created AAD application page, go to the **Configure** tab:  
	![][15]
4. In **keys** section, use the dropdown list to create a key. The key shows up after you select **Save**:  
	![][16]
5. In **single sign-on** section, add ``https://<your App Service Environment name>.azure-apim.net:456/redirect`` as a **reply URL**.
6. In **permissions to other applications** section:  
	a. Click **Add application**, then in the pop up dialog, choose the AAD application protecting your existing backend:  
	![][17]
	b. Use the dropdown list to add proper permissions:  
	![][18]
7. Select **Save** at the bottom. After this, please copy the **client ID** and **key** and keep them in some place temporarily. Especially the key, since it won't show again after you close Azure portal.

For more information, please refer to [Integrating Applications with Azure Active Directory][12].

## Configure your API using Azure PowerShell

At this point, there is no Azure portal support for you to initialize the configuration needed for the API. Following is a script for how to configure it using Azure PowerShell.

> [AZURE.TIP] To learn about how to install and configure Azure PowerShell, please refer to [How to install and configure Azure PowerShell][11]. The following script works with Azure PowerShell 1.0 preview or above.

```powershell
# get the API resource
$api = Get-AzureRmResource -ResourceType Microsoft.Web/apiManagementAccounts/apis -ResourceName <App Service Environment name>/<API name> -ResourceGroupName <resource group name>

# configure the API resource for AAD authentication
$connectionParameters = @{
    token = @{
        type = "oauthSetting";
        oAuthSettings = @{
            identityProvider = "aad";
            clientId = "<your AAD app client id>";
            clientSecret = "<your AAD app key>";
            customParameters = @{
                tenantId = @{
                    value = "<your AAD tenant ID>"
                };
                resourceUri = @{
                    value = "<the app ID URI of the AAD app protecting your backend>"
                }
            }
        }
    }
}
Add-Member -InputObject $api.Properties -MemberType NoteProperty -Name ConnectionParameters -Value $connectionParameters

# update the API resource
New-AzureRmResource -Location $api.Location -ResourceId $api.ResourceId -Properties $api.Properties
```

**Notice** that the connection parameter name **token** is important. You can pick your own name for it as long as it's camel case. You'll use it later in your backend code or API policy.

After this, go to [Azure portal][19] and navigate to the **General** settings blade of your API, you should be able to see the following additional configuration is enabled.

## Try it out

To try it out, open PowerApps clients and find this API in **Available connections". When click "Connect", it should pop up an AAD login window. Enter your organization's AAD account and your connection will be created.

Now when a runtime call is made from PowerApps clients to this API using this connection, your backend will receive the user's AAD token in HTTP header **x-ms-apim-tokens** in the following format in [Base64 encoding][20]:

```json
{
  "token": {
    "AccessToken": ""
    // ...
  }
}
```

**Notice** that the property name **token** matches the connection parameter name you use when configuring the setting.

Your backend code can then get the AAD token from the **AccessToken** property and use it if needed. The App Service Environment will take care of token refresh automatically.

## Configure API policy

Optionally, you can also use API policy to set the AAD token into the standard HTTP **Authorization** header. This way, if your backend code needs to use the AAD token, you can get it in a standard way rather than looking into a custom HTTP header and perform Base64 decoding. To do so, go to the **Policy** blade of your API and set the following policy.

```xml
<policies>
	<inbound>
		<base/>
		<choose>
			<when condition="@(context.Variables.ContainsKey(&quot;tokens&quot;) &amp;&amp; ((JObject)context.Variables[&quot;tokens&quot;])[&quot;token&quot;] != null &amp;&amp; !String.IsNullOrEmpty((string)((JObject)context.Variables[&quot;tokens&quot;])[&quot;token&quot;][&quot;AccessToken&quot;]))">
				<set-header exists-action="override" name="Authorization">
					<value>@("Bearer " + (string)((JObject)context.Variables["tokens"])[&quot;token&quot;]["AccessToken"])</value>
				</set-header>
			</when>
		</choose>
	</inbound>
	<backend>
		<base/>
	</backend>
	<outbound>
		<base/>
	</outbound>
</policies>
```

To understand the policy, it basically let you references the values in the **x-ms-apim-tokens** header as a decoded JObject via a **tokens** variable. Then you can use the **set-header** policy to get the actual AAD token and set it to the **Authorization** header. This is the same policy used by [Azure API Management][22]. To learn more, please refer to [Policies in Azure API Management][23].

**Notice** that the property name **token** matches the connection parameter name you use when configuring the setting.

## Summary and next steps

In this topic, you've seen how to configure an API to connect to backend protected by AAD. Here are some related topics and resources for learning more about PowerApps.

- [Develop an API for PowerApps][21]


<!--References-->
[11]: https://azure.microsoft.com/documentation/articles/powershell-install-configure/
[12]: https://azure.microsoft.com/documentation/articles/active-directory-integrating-applications/
[13]: https://manage.windowsazure.com
[14]: ./media/powerapps-configure-apis-aad/aad-applications-tab.png
[15]: ./media/powerapps-configure-apis-aad/aad-application-configure-tab.png
[16]: ./media/powerapps-configure-apis-aad/aad-application-configure-keys.png
[17]: ./media/powerapps-configure-apis-aad/aad-application-add-other-application.png
[18]: ./media/powerapps-configure-apis-aad/aad-application-add-permissions.png
[19]: https://portal.azure.com
[20]: https://tools.ietf.org/html/rfc4648
[21]: powerapps-develop-api.md
[22]: https://azure.microsoft.com/services/api-management/
[23]: https://azure.microsoft.com/documentation/articles/api-management-howto-policies
