<properties
	pageTitle="Register custom APIs | Microsoft PowerApps"
	description="Register custom APIs in PowerApps using Swagger and OAuth."
	services=""
    suite="powerapps"
	documentationCenter=""
	authors="archnair"
	manager="anneta"
	editor=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="04/28/2017"
   ms.author="archanan"/>

# Register custom APIs in PowerApps

PowerApps can leverage any RESTful APIs hosted anywhere.  This tutorial demonstrates registering and using a custom API.

## Prerequisites

- A [PowerApps account](https://powerapps.microsoft.com).
- A Swagger file (JSON), URL to a Swagger definition OR a Postman collection for your API. If you don't have one, we'll show you several options to create the Swagger file or the Postman collection.
- An image to use as an icon for your custom API (optional).

## Authentication

Custom APIs in PowerApps can use any of several authentication mechanisms

- API Key
- Basic Authentication
- Generic OAuth 2.0
- OAuth 2.0. The specific implementations below are currently supported, with more coming soon.

	- Azure Active Directory
	- Box
	- Dropbox
	- Facebook
	- Google
	- Instagram
	- OneDrive
	- SalesForce
	- Slack
	- Yammer


The [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#securityDefinitionsObject) describes how to specify authentication within a Swagger.

If your API endpoint allows unauthenticated access, you should remove the ```securityDefintions``` object from the OpenAPI (Swagger) file. In the following example, remove all of the following ```securityDefintions``` object:

```
  "securityDefinitions": {
    "AAD": {
      "type": "oauth2",
      "flow": "implicit",
      "authorizationUrl": "https://login.windows.net/common/oauth2/authorize",
      "scopes": {}
    }
  },
```

### Examples
* [Azure Resource Manager](customapi-azure-resource-manager-tutorial.md) with AAD authentication.
* [Azure WebApp](customapi-web-api-tutorial.md) with AAD authentication.

## Register a custom API

### Step 1a: Create a Swagger file

You can create a Swagger file from *any* API endpoint, including:

- Publicly available APIs. Some examples include [Spotify](https://developer.spotify.com/), [Uber](https://developer.uber.com/), [Slack](https://api.slack.com/), [Rackspace](http://docs.rackspace.com/), and more.
- An API that you create and deploy to any cloud hosting provider, including Amazon Web Services (AWS), Heroku, Azure Web Apps, Google Cloud, and more.  
- A custom line-of-business API deployed on your network as long as the API is exposed on the public internet.

When you create the Swagger file, a JSON file is created.  You'll need this is Step 2.

#### Connecting to Azure App Service or Azure Functions

If your API is built with Azure App Service or Azure Functions, see [Exporting an Azure hosted API to PowerApps](https://docs.microsoft.com/en-us/azure/app-service/app-service-export-api-to-powerapps-and-flow) to learn more.

#### Getting help with Swagger files

- If you're new to Swagger, you should visit the [Getting Started pages on Swagger.io](http://swagger.io/getting-started/).

-  There's a Swagger [Hello World example](https://github.com/OAI/OpenAPI-Specification/wiki/Hello-World-Sample) on GitHub.

- To create your own API, deploy it to Azure, create a Swagger file based off this new API, and then register it in PowerApps, see the [Web API tutorial](customapi-web-api-tutorial.md).

- To validate your Swagger files, use the [Swagger editor](http://editor.swagger.io/#/). You can paste your JSON data, and validation automatically occurs.

- To customize your Swagger document to work with PowerApps, see [Customize your Swagger definition](customapi-how-to-swagger.md).

### Step 1b: Create a Postman collection

If you don't already have or want to create a Swagger file for your API, you can still easily create a custom API by using a [Postman](https://www.getpostman.com/) collection.

- To get started, install the [Postman app](https://www.getpostman.com/apps)
- See [how to create Postman Collection](postman-collection.md) to learn more details

### Step 2: Register the custom API

Use the Swagger file (JSON file) or the Postman collection to register the custom API in PowerApps.

1. In [powerapps.com](https://web.powerapps.com), in the menu on the left, click **Connections**. Then click **...** and select **Manage custom APIs** in the upper-right corner.

	 >[AZURE.TIP] If you can't find the menu, it may be under a hamburger button in the upper-left corner in mobile browsers.

	![Create custom API](./media/register-custom-api/managecustomapi.png)  

1. Select **Create custom API**:  

	![Custom API properties](./media/register-custom-api/newcustomapi.png)

1. In the **General** tab, choose how you want to create the custom API
	- Upload Swagger
	- Paste Swagger URL
	- [Upload Postman collection V1](postman-collection.md)

	 Note: The Postman collection will be parsed and translated into a Swagger definition file.

	![How to create custom API](./media/register-custom-api/choosehowtocreate.png)

	Upload an icon for your custom API. Description, Host and Base URL fields will be auto populated with the information from the Swagger file. If not, you can add information to those fields. Select **Continue**.

1. In the **Security** tab, enter any authentication properties. The Authentication type will be auto selected based on what is defined in your Swagger ```securityDefintions``` object.

  ![Authentication types](./media/register-custom-api/authenticationtypes.png)

	Refer to [Azure Resource Manager](customapi-azure-resource-manager-tutorial.md) and [Azure WebApp](customapi-web-api-tutorial.md) examples to learn how to configure AAD authentication values.

	If the JSON file does not use the ```securityDefintions``` object, then no additional values may be needed.

	Note: When using a Postman collection, Authentication type will be auto populated only when using supported authentication types such as OAuth 2.0 or Basic.

1. In the **Definitions** tab, all the operations defined in your Swagger file or Postman collection, along with the Request and Response, will be auto populated. At this stage, if you have all your required operations defined, you can proceed to the next step.

	![Definition tab](./media/register-custom-api/definitiontab.png)

  If you want to edit existing actions or add new actions to your custom API, continue reading below.

	If you want to add a new action that was not already in your Swagger file or Postman collection, select **New action** in the left pane and fill in the General section with the name, description and visibility of your operation.

	In the Request section, select **Import from sample** on the top right. You will see a form where you can paste in a sample request. These sample requests are usually available on the API documentation.

	For example, for the [Cognitive Services Text Analytics API](https://www.microsoft.com/cognitive-services/en-us/text-analytics-api), you can get information about the HTTP Verb, Request URL, Headers, Body [here](https://westus.dev.cognitive.microsoft.com/docs/services/TextAnalytics.V2.0/operations/56f30ceeeda5650db055a3c6).

	![Import from sample](./media/register-custom-api/importfromsample.png)

	Select **Import** to complete the Request definition. You can similarly define the Response too.

1. Once you have all your operations defined, select **Create** to create your custom API.

1. You must create a connection to the custom API so it can be used in your apps. Click on the **+** next to the custom API in the list then complete any necessary steps to sign in to your API. If you're using **OAuth** authentication with your API, you might be presented a sign-in screen. For API Key authentication, you might be prompted for a key value.

### Step 3: Test the custom API

1. Once you have created your custom API, you can go to the **Test** tab, to test the operations defined in the custom API.

	Choose a connection and provide input parameters to test the operation.

	![Test custom API](./media/register-custom-api/testcustomapi.png)

	If the call was successful, you will see a valid response.

	![Test API Response](./media/register-custom-api/testapiresponse.png)

### Step 4: Add the custom API to an app
[Add the custom API to an app](add-data-connection.md) as you would any other data source, and then use the API within the function bar, a text box, and more. For example, in the function bar, you can start typing **MySampleWebAPI** to see the available functions. [Office 365 Outlook](connection-office365-outlook.md) is an example of using the Office 365 API.

## Share a custom API
Users can also share custom APIs with each other.

1. In [powerapps.com](https://web.powerapps.com), in the menu on the left, click **Connections**. Then click **...** and select **Manage custom APIs** in the upper-right corner.

	![New connection](./media/register-custom-api/managecustomapi.png)

2. Select your API, select **Share**, and then enter the users or groups to whom you want to grant access to your API.  

	![Share custom API](./media/register-custom-api/sharecustomapi.png)

3. Select **Save**.

> [AZURE.NOTE] You may only share custom APIs with other users in your organization.

## Quota and throttling

- See the [PowerApps Pricing](https://powerapps.microsoft.com/pricing/) page for details about custom API creation quotas. Custom APIs that are shared with you don't count against this quota.
- For each connection created on a custom API, users can make up to 500 requests per minute.
- Keep in mind that deleting a custom API deletes all the connections created to the API.
- The size of your Swagger file should be under 1MB.

## Next steps

[Learn how to create a Postman collection](postman-collection.md)

[Learn about custom Swagger extensions](customapi-how-to-swagger.md).

[Use an ASP.NET Web API](customapi-web-api-tutorial.md).

[Register an Azure Resource Manager API](customapi-azure-resource-manager-tutorial.md).
