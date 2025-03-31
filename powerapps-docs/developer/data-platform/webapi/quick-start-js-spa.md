---
title: "Quickstart: Web API with client-side JavaScript and Visual Studio Code"
description: Describes how to interactively authenticate and use the Dataverse Web API with client-side JavaScript and Visual Studio Code with a Single Page Application.
ms.topic: quickstart
ms.date: 03/22/2025
author: JimDaly
ms.author: jdaly
ms.reviewer: jdaly
search.audienceType:
  - developer
---
# Quickstart: Web API with client-side JavaScript and Visual Studio Code

This quickstart demonstrates how you can connect to Dataverse and use the Web API with the following technologies:

|Technology|Description|
|---|---|
|**[JavaScript](https://developer.mozilla.org/docs/Web/JavaScript)**| A programming language for web development, enabling interactive content. It runs in browsers for client-side scripting and can be used server-side with Node.js.|
|**[Visual Studio Code](https://code.visualstudio.com/)**|A lightweight, open-source code editor with debugging, syntax highlighting, and plugin support.|
|**[Single Page Applications (SPAs)](https://developer.mozilla.org/docs/Glossary/SPA)**| Web applications that load a single HTML page and dynamically update content as the user interacts with the app. This approach provides a smoother, faster user experience by reducing page reloads and enhancing performance.|
|**[Microsoft Authentication Library for JavaScript (MSAL.js)](/javascript/api/overview/msal-overview?view=msal-js-latest&preserve-view=true)**| A library that enables authentication and authorization for web applications using Microsoft identity platforms. It simplifies integrating secure sign-in and token acquisition for accessing protected resources.|
|**[Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/docs/Web/HTTP/CORS)**|A SPA application can use client-side JavaScript with the Dataverse Web API because CORS is enabled. CORS is a security feature in web browsers that allows controlled access to resources on a web server from a different origin. It enables web applications to bypass the [same-origin policy](https://developer.mozilla.org/docs/Web/Security/Same-origin_policy), facilitating safe and secure data sharing across different domains.|

## Goal

This quickstart focuses on connecting to the Dataverse Web API with JavaScript using a SPA client application with a minimum of number of steps. When you complete this quickstart, you're able to:

- Sign in and connect to Dataverse
- Invoke the [WhoAmI function](/power-apps/developer/data-platform/webapi/reference/whoami) and display your `UserID` value.

:::image type="content" source="media/quickstart-web-api-js-spa.png" alt-text="Completed running quickstart":::

Completing this quickstart enables you to try the [Web API Data operations Samples (Client-side JavaScript)](web-api-samples-client-side-javascript.md) which demonstrate more advanced capabilities.

> [!NOTE]
> This quickstart doesn't apply to the following client-side JavaScript scenarios:
>
> |Scenario|Learn more|
> |---|---|
> |**Model-driven application scripts**|- [Apply business logic using client scripting in model-driven apps using JavaScript](../../model-driven-apps/client-scripting.md)<br />- [Xrm.WebApi (Client API reference)](/power-apps/developer/model-driven-apps/clientapi/reference/xrm-webapi)|
> |**Power Apps component framework**|- [Code components WebAPI](/power-apps/developer/component-framework/reference/webapi)<br />- [Implementing Web API component](../../component-framework/sample-controls/webapi-control.md)|
> |**Power Pages Portals**|[Power Pages Portals Web API](/power-pages/configure/web-api-overview)|
>
> In these scenarios, the respective application type provides a capability for you to send requests rather than use the JavaScript native [Fetch API](https://developer.mozilla.org/docs/Web/API/Fetch_API) directly as shown in this quickstart. Client-side scripts within model-driven apps run in the context of an authenticated application, so each request doesn't require an access token.

## Prerequisites

The following table describes the prerequisites needed to complete this quickstart and [Web API Data operations Samples (Client-side JavaScript)](web-api-samples-client-side-javascript.md).

|Prerequisite|Description|
|---|---|
|**Privileges to create an Entra App registration**|You can't complete this quickstart without the ability create a Microsoft Entra app registration to enable it.<br /><br />If you aren't sure if you can, try the first step to [Register a SPA application](#register-a-spa-application) and find out. |
|**Visual Studio Code**| If Visual Studio Code isn't installed on your computer, you must [Download and install Visual Studio Code](https://code.visualstudio.com/download) to run this quickstart. |
|**Node.js**|Node.js is a runtime environment that allows you to run JavaScript on the server side. This quickstart creates a SPA application that runs JavaScript on the client side in a browser rather than the Node.js runtime. But [Node Package Manager (npm)](https://www.npmjs.com/) is installed with Node.js, and you need npm to install Parcel and the MSAL.js library.|
|**Parcel**|Modern web applications typically have many dependencies on open source libraries distributed using npm and scripts that need to be managed and optimized during the build process. These tools are called 'bundlers'. The most common one is [webpack](https://webpack.js.org/). This quick start uses [Parcel](https://parceljs.org/) because it offers a simplified experience.<br /><br />For quickstarts and samples that show SPA applications using different frameworks and bundlers, see [Microsoft Entra Single-page applications samples](/entra/identity-platform/sample-v2-code?tabs=apptype#single-page-applications). You can adapt these samples to use Dataverse Web API with the information shown in this quickstart.|
|**Web Technologies**|Knowledge of HTML, JavaScript, and CSS are required to understand how this quickstart works. Understanding how to [make network requests with JavaScript](https://developer.mozilla.org/docs/Learn_web_development/Core/Scripting/Network_requests) is essential.|

## Register a SPA application

This step is first because if you can't register an app, you can't complete this quick start.

Any of the following [privileged Microsoft Entra roles](/entra/identity/role-based-access-control/privileged-roles-permissions) include the required permissions:

- [Application Administrator](/entra/identity/role-based-access-control/permissions-reference#application-administrator)
- [Application Developer](/entra/identity/role-based-access-control/permissions-reference#application-developer)
- [Cloud Application Administrator](/entra/identity/role-based-access-control/permissions-reference#cloud-application-administrator)

When you configure the application, you need an application (client) ID, and the ID of your Microsoft Entra tenant. You should also choose a descriptive name for the application so people know what the application was created for.

### Register your app

You can register your application using either the:

- Microsoft Entra web application UI
- Azure PowerShell [New-AzADApplication](/powershell/module/az.resources/new-azadapplication) cmdlet.

### [Microsoft Entra web application](#tab/web)

#### Create the application registration

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/).
1. If you have access to multiple tenants, use the **Settings** :::image type="icon" source="media/settings-icon.png" border="false"::: icon in the top menu to switch to the tenant in which you want to register the application from the **Directories + subscriptions** menu.
1. Browse to **Identity** > **Applications** > **App registrations** and select **New registration**.
1. Enter a **Name** for the application, such as `Dataverse Web API Quickstart SPA`.
1. For **Supported account types**, under **Who can use this application or access this API**, select **Accounts in this organizational directory only (&lt;Your tenant name&gt; - Single tenant)**.
1. For  **Redirect URI (optional)**

   1. For **Select a platform**, choose **Single-page application (SPA)**.
   1. Enter `http://localhost:1234` as the value.

1. Select **Register** to save your changes.
1. In the window for the app registration you created, in the **Overview** tab, below **Essentials**, you can find these values:

   - Application (client) ID
   - Directory (tenant) ID

1. Copy these values because you need them when you [create the .env file](#create-the-env-file) to use environment variables.

#### Add Dataverse `user_impersonation` privilege

1. In the **Manage** area, select **API permissions**.
1. Select **Add a permission**.
1. In the **Request API permissions** flyout, select the **APIs my organization uses** tab.
1. Type 'Dataverse' to find application (client) ID `00000007-0000-0000-c000-000000000000`.
1. Select the Dataverse application.
1. In **Select permissions**, `user_impersonation` is the only available delegated permission. Select it.
1. Select **Add permissions**.

### [PowerShell Script](#tab/ps)

Using these instructions for PowerShell with Visual Studio Code has the following requirements:

- Install the PowerShell extension for Visual Studio Code. [Learn to install PowerShell for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode.PowerShell)
- Install the Az PowerShell module.  [Learn how to install Azure PowerShell](/powershell/azure/install-azure-powershell)

You need your tenant ID to run this script.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/).
1. If you have access to multiple tenants, use the **Settings** :::image type="icon" source="media/settings-icon.png" border="false"::: icon in the top menu to switch to the tenant in which you want to register the application from the **Directories + subscriptions** menu.
1. Select **Overview** in the navigation pane.
1. In the **Overview** tab, in the **Basic information** section you find **Tenant ID**.
1. Select the **Copy to Clipboard** icon.

When you have your tenant ID, you can create the app registration using the Azure PowerShell [New-AzADApplication](/powershell/module/az.resources/new-azadapplication) cmdlet.

1. In Visual Studio Code, select **File** > **New Text File**, or <kbd>Ctrl</kbd>+<kbd>N</kbd> to open a new text file.

   You don't need to save the file.

1. Copy and paste the following script into the new file.

   ```powershell
   # Values to pass to the New-AzADApplication command
   $tenantId = "<your-tenant-id>" # Replace with your tenant ID
   $appName = "Dataverse Web API SPA Quickstart"
   $redirectUri = "http://localhost:1234"


   # Connect to Azure
   try {
      Connect-AzAccount -Tenant $tenantId -UseDeviceAuthentication | Out-Null
   }
   catch {

      Write-Host "An error occurred while connecting: $_" -ForegroundColor Red
      exit 1
   }

   try {
      $appResponse = New-AzADApplication `
         -DisplayName $appName `
         -SPARedirectUri @($redirectUri) `
         -AvailableToOtherTenants $false `
         -RequiredResourceAccess @(
         @{
            ResourceAppId  = "00000007-0000-0000-c000-000000000000"; # Dynamics CRM API
            ResourceAccess = @(
               @{
                  Id   = "a42657d6-7f20-40e3-b6f0-cee03008a62a"; # user_impersonation
                  Type = "Scope" 
               }
            ) 
         }
      )

      if ($appResponse -eq $null) {
         Write-Host "Failed to create the application." -ForegroundColor Red
         return $null
      }
      else {

         Write-Host "Copy the following to paste into an .env file at the root of your project:`n"
         Write-Host "# The environment this application will connect to."
         Write-Host "BASE_URL=https://<yourorg>.api.crm.dynamics.com"
         Write-Host "# The registered Entra application id"
         Write-Host "CLIENT_ID=$($appResponse.appId)"
         Write-Host "# The Entra tenant id"
         Write-Host "TENANT_ID=$($tenantId)"
         Write-Host "# The SPA redirect URI included in the Entra application registration"
         Write-Host "REDIRECT_URI=$($redirectUri)"
      }
   }
   catch {
      Write-Host "An error occurred while creating the application: $_" -ForegroundColor Red
      return $null
   }
   ```

1. Edit this line to replace `<your-tenant-id>` with your tenant id value:

   `$tenantId = "<your-tenant-id>" # Replace with your tenant ID`

1. Press <kbd>F5</kbd> to execute the script.
1. When the script runs, the device authorization flow begins. Find a message like the following in the terminal window:

   ```
   [Login to Azure] To sign in, use a web browser to open the page <https://microsoft.com/devicelogin> and enter the code A1BC2DE3F to authenticate.
   ```

   Where `A1BC2DE3F` is a generated code value.

1. Copy the code and use <kbd>Ctrl</kbd>+Click to open the [https://microsoft.com/devicelogin](https://microsoft.com/devicelogin) link. This link opens a series of dialogs in your browser.

   1. In the **Enter code to allow access** dialog, enter the code you copied and select **Next**.
   1. In the **Pick an account** dialog, select the account you want to use.
   1. In the **Enter password** dialog, enter your password and select the **Sign in** button.
   1. In the **Are you trying to sign in to Microsoft Azure PowerShell?** dialog, select **Continue**.

1. You can close the browser tab and return to Visual Studio Code.
1. In the terminal window, you should see output like the following text:

   ```
   Copy the following to paste into an .env file at the root of your project:

   # The environment this application will connect to.
   BASE_URL=https://<yourorg>.api.crm.dynamics.com
   # The registered Entra application id
   CLIENT_ID=11112222-bbbb-3333-cccc-4444dddd5555
   # The Entra tenant id
   TENANT_ID=aaaabbbb-0000-cccc-1111-dddd2222eeee
   # The SPA redirect URI included in the Entra application registration
   REDIRECT_URI=http://localhost:1234
   ```

Copy this data. You use it when you [create the .env file](#create-the-env-file) to use environment variables.

---

> [!NOTE]
> If you don't have the privileges to create an app registration for your company, get a tenant of your own through via the [Power Apps Developer Plan](/power-platform/developer/plan).

## Install Node.js

1. Go to [Download Node.js](https://nodejs.org/en/download).
1. Choose the appropriate installer for your operating system (Windows, macOS, or Linux) and download it.
1. Run the installer. Make sure you accept the default option to: **Install npm, the recommended package manager for Node.js.**
1. Verify the installation by opening a terminal or command prompt, typing these commands and pressing <kbd>Enter</kbd>.

   - `node -v`
   - `npm -v`

   You should see something like this:

   ```powershell
   PS C:\Users\you> node -v
   v22.14.0
   PS C:\Users\you> npm -v
   9.5.0
   PS C:\Users\you>
   ```

## Create a project

> [!NOTE]
> You can skip these steps by cloning or downloading the [PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples) repository. The  completed application for these steps is available at [/dataverse/webapi/JS/quickspa](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/JS/quickspa). Follow the instructions in the README.

The instructions in this section guide you to install dependencies from npm, create the folder structure, open Visual Studio Code.

1. Open a terminal window to a place where you want to create a project. For these instructions, we use `C:\projects`.
1. Type the following commands and press <kbd>Enter</kbd> to achieve the following actions:

   |Command  |Action  |
   |---------|---------|
   |`mkdir quickspa`|Create a new folder named `quickspa`.|
   |`cd quickspa`|Move into the new `quickspa` folder.|
   |`npm install --save-dev parcel`|Install Parcel and initialize the project.|
   |`npm install @azure/msal-browser`|Install the MSAL.js library.|
   |`npm install dotenv`|Install [dotenv](https://www.npmjs.com/package/dotenv) to access environment variables that store potentially sensitive configuration data.|
   |`mkdir src`|Create a `src` folder where you add HTML, JS, and CSS files for your app in the following steps.|
   |`code .`|Open Visual Studio Code in the context of the `quickspa` folder.|

Your project should look like this in Visual Studio Code Explorer:

:::image type="content" source="media/quickspa-project.png" alt-text="Shows the newly created quickspa project before any files are added.":::

### Create the .env file

Storing configuration data in the environment separate from code is a security best practice.

1. Create a new file named `.env` in the root of your `quickspa` folder.
1. Paste in the values from [Register your app](#register-your-app) to replace the `CLIENT_ID` and `TENANT_ID` values below.

   :::code language="text" source="~/../PowerApps-Samples/dataverse/webapi/JS/quickspa/.env.example":::

1. Set the `BASE_URL` value to the URL of the [Web API URL](compose-http-requests-handle-errors.md#web-api-url-and-versions) for the environment you want to connect to.

> [!NOTE]
> You won't check-in the `.env` file. In [Create `.gitignore` file](#create-gitignore-file), you will exclude it. But you might want to create a `.env.example` file using the placeholder values so that people know what data it should contain.

### Create an HTML page

The instructions in this section describe how to create the HTML file that provides the user interface for the SPA application.

1. Create a new file in the `src` folder named `index.html`.
1. Copy and paste this content to the `index.html` page:

   :::code language="html" source="~/../PowerApps-Samples/dataverse/webapi/JS/quickspa/src/index.html":::


This HTML provides the following elements:

|Element ID|Element type|Description|
|---------|---------|---------|
|`loginButton`|[button](https://developer.mozilla.org/docs/Web/HTML/Element/button)|To open the login dialog.|
|`logoutButton`|[button](https://developer.mozilla.org/docs/Web/HTML/Element/button)|To open the logout dialog. Hidden by default.|
|`buttonContainer`|[nav](https://developer.mozilla.org/docs/Web/HTML/Element/nav)|Contains buttons that require user to be logged in to use. Disabled by default.|
|`whoAmIButton`|[button](https://developer.mozilla.org/docs/Web/HTML/Element/button)|Executes the [WhoAmI function](/power-apps/developer/data-platform/webapi/reference/whoami) to display the user's ID.|
|`container`|[main](https://developer.mozilla.org/docs/Web/HTML/Element/main)|Area where information can be displayed to the user.|
||[script](https://developer.mozilla.org/docs/Web/HTML/Element/script)|Loads the `index.js` file after the rests of the elements of the page loads.|

### Create a JavaScript script

This file contains all the logic that makes the `index.html` page dynamic.

1. Create a new folder in the `src` folder named `scripts`.
1. Create a new file in `scripts` folder named `index.js`.
1. Copy and paste this content into the `index.js` page:

   :::code language="javascript" source="~/../PowerApps-Samples/dataverse/webapi/JS/quickspa/src/scripts/index.js":::


The `index.js` script contains the following constants and functions:

|Item|Description  |
|---------|---------|
|`config` |Contains the data used by the Microsoft Authentication Library (MSAL) configuration.|
|`msalConfig` |Microsoft Authentication Library (MSAL) configuration.|
|`msalInstance`|The MSAL [PublicClientApplication](/javascript/api/%40azure/msal-browser/publicclientapplication) instance. |
|`container`|The element where messages are displayed.|
|`getToken`|Retrieves an access token using MSAL.|
|`logIn`|Event listener function for the login button. Opens a choose account dialog.|
|`logOut`|Event listener function for the logout button. Opens a choose account dialog.|
|`whoAmI`|Asynchronous function that calls the [WhoAmI function](/power-apps/developer/data-platform/webapi/reference/whoami) to retrieve data from Dataverse. |
| `whoAmIButton` event listener|The function that calls the `whoAmI` function and manages the UI changes to show the message.|

### Create a CSS page

The Cascading Style Sheet (CSS) file makes the HTML page more attractive and has a role in controlling when controls are disabled or hidden.

1. Create a new folder named `styles` in the `src` folder.
1. Create a new file named `style.css` in the `styles` folder.
1. Copy and paste this text into the `style.css` file:

   :::code language="css" source="~/../PowerApps-Samples/dataverse/webapi/JS/quickspa/src/styles/style.css":::


### Create `.gitignore` file

When your app is checked in with source control, adding a `.gitignore` file prevents checking in files the specified files and folders.

1. Create a file named `.gitignore`.
1. Add the following content:

   ```
   .parcel-cache
   dist
   node_modules
   .env
   ```

The `.parcel-cache` and `dist` folders appear when you run the app for the first time.

Not checking in the `.env` file is a security best practice. You might want to check in a placeholder `.env.sample` file with placeholder values.

Your project should look like this in Visual Studio Code Explorer:

:::image type="content" source="media/quickspa-project-with-files.png" alt-text="Shows the quickspa project after files are added.":::

### Configure your package.json file

Your `package.json` file should look something like this:

```json
{
  "devDependencies": {
    "parcel": "^2.14.1",
  },
  "dependencies": {
    "@azure/msal-browser": "^4.7.0",
    "dotenv": "^16.4.7"
  }
}
```

Add this `scripts` item underneath `dependencies`:

```json
  "dependencies": {
    "@azure/msal-browser": "^4.7.0",
    "dotenv": "^16.4.7"
  },
  "scripts": {
    "start": "parcel src/index.html"
  }
```

This configuration allows you to start the application using `npm start` in the next step.

## Try it

1. In Visual Studio Code, open a terminal window
1. Type `npm start` and press <kbd>Enter</kbd>.

   > [!NOTE]
   > You might see some output written to the terminal while the project initializes for the first time.
   > This is parcel installing some more node modules to mitigate issues when using [dotenv](https://www.npmjs.com/package/dotenv). 
   > Look at the `package.json` and you should some new items added to the `devDependencies`.


   You should expect output to the terminal that looks like this:

   ```
   Server running at http://localhost:1234
   Built in 1.08s
   ```

1. Press <kbd>Ctrl</kbd> + click the [http://localhost:1234](http://localhost:1234) link to open your browser.
1. In your browser, select the **Login** button.

   The **Sign in to your account** dialog opens.

1. In the **Sign in to your account** dialog, select the account that has access to Dataverse.

   The first time you access using a new application (client) ID value, you see this **Permissions requested** dialog:

   :::image type="content" source="media/dataverse-web-api-quickstart-spa-permissions-requested.png" alt-text="Permissions requested dialog":::

1. Select **Accept** on the **Permissions requested** dialog.
1. Select the **WhoAmI** button.

   The message **Congratulations! You connected to Dataverse using the Web API.** is displayed with your `UserId` value from the [WhoAmIResponse complex type](/power-apps/developer/data-platform/webapi/reference/whoamiresponse).

## Trouble shooting

This section contains errors that you might encounter running this quick start.

> [!NOTE]
> If you experience issues completing the steps in this quick start, try cloning or downloading the [PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples) repository. The completed application for these steps is available at [/dataverse/webapi/JS/quickspa](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/JS/quickspa). Follow the instructions in the README. If that doesn't work, create an GitHub issue referencing this `quickspa` sample application.

### Selected user account doesn't exist in tenant

When the account you select doesn't belong to the same Microsoft Entra tenant as the registered application, you get this error in the **Pick an account** dialog:

`Selected user account does not exist in tenant '{Your tenant name}' and cannot access the application '{Your application ID}' in that tenant. The account needs to be added as an external user in the tenant first. Please use a different account.`

**Resolution**: Make sure you choose the correct user.

## Next steps

Try other samples that use client-side JavaScript.

> [!div class="nextstepaction"]
> [Web API Data operations Samples (Client-side JavaScript)](web-api-samples-client-side-javascript.md)

Learn more about Dataverse Web API capabilities by understanding the service documents.

> [!div class="nextstepaction"]
> [Web API types and operations](web-api-types-operations.md)
