---
title: "Quickstart: Register and configure a SPA application for Dataverse using msal.js (Microsoft Dataverse) | Microsoft Docs"
description: "Describes the process of registering and configuring the simplest Single-Page Application (SPA) to access data in Microsoft Dataverse using msal.js and Cross-origin Resource Sharing (CORS)."
ms.date: 09/09/2022
ms.topic: quickstart
author: ritesp # GitHub ID
ms.subservice: dataverse-developer
ms.author: ritesp # MSFT alias of Microsoft employees only
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors:
 - JimDaly
---

# Quickstart: Register and configure a SPA application for Dataverse using msal.js

This topic describes the process of registering and configuring the simplest Single-Page Application (SPA) to access data in Microsoft Dataverse using msal.js and Cross-origin Resource Sharing (CORS). More information: [Use OAuth with Cross-Origin Resource Sharing  to connect a Single-Page Application to Dataverse ](oauth-cross-origin-resource-sharing-connect-single-page-application.md).
  
## Prerequisites
  
- Access to a Dataverse environment.
- An Azure account with an active subscription.
- The Azure account must have permission to manage applications in Microsoft Entra ID. Any of the following Microsoft Entra ID roles include the required permissions:

   - [Application administrator](/azure/active-directory/roles/permissions-reference#application-administrator)
   - [Application developer](/azure/active-directory/roles/permissions-reference#application-developer)
   - [Cloud application administrator](/azure/active-directory/roles/permissions-reference#cloud-application-administrator)

- Visual Studio Code (VS Code) [Download](https://code.visualstudio.com/download)
  
<a name="bkmk_goal"></a>

## Goal of this quick start

When you complete this quick start you will be able to run a simple SPA application that will provide the ability for a user to authenticate and retrieve data from Dataverse.  

When you debug the application initially there will only be a **Login** button.  

- Click **Login** and a pop-up will open to enter your credentials.  
- After you enter your credentials you will find the **Login** button is hidden and a **Logout** button and a **Get Accounts** button are visible. You will also see a greeting using information from your user account.
- Click the **Get Accounts** button to retrieve 10 account records from your Dataverse organization. The result is shown in the following screenshot:  
  
   ![The SimpleSPA page.](media/simple-spa.png "The SimpleSPA page")

- Finally, you can click on **Logout** button to logout. 

> [!NOTE]
> This SPA application is not intended to represent a pattern for developing robust SPA applications. It is simplified to focus on the process of registering and configuring the application.

## Get your Dataverse Web API endpoint

Use the instructions in [View developer resources](view-download-developer-resources.md) to identify a Web API endpoint for an environment you can access. It should look something like this: `https://yourorg.api.crm.dynamics.com/api/data/v9.2`. 

## Register your application

1. From [Power Platform admin center](https://admin.powerplatform.microsoft.com) in the left navigation expand **Admin centers** and select **Microsoft Entra ID**.

   :::image type="content" source="media/azure-active-directory-from-ppac.png" alt-text="Microsoft Entra ID from Power Platform Admin Center":::

   This will open the **Microsoft Entra admin center**

1. Expand **Applications** and select **App registrations**.

   :::image type="content" source="media/aad-app-registrations-from-entra-admin-center.png" alt-text="Azure App registrations from Microsoft Entra admin center":::

1. Click **New registration**. This will open the **Register an application** form.

   :::image type="content" source="media/aad-app-registration-form.png" alt-text="Register and application form":::

1. In the **Register an application** form, type a **Name**. For the purpose of this quickstart, use the name *Simple SPA*.
1. For **Supported account types**, the default selection should be:<br />**Accounts in this organizational directory only (&lt;tenant name&gt; only – Single tenant)**. Don't change this.
1. For **Redirect URI (optional)**, use these options:

   - **Select a platform**: Single-page application (SPA)
   - `e.g. https://example.com/auth`: `http://localhost:5500/index.html`

1. Click **Register**.
1. In the **Overview** area, copy the following values because you will need them in the final step of [Create a web application project](#create-a-web-application-project).

   - **Application (client) ID**
   - **Directory (tenant) ID**

1. Select **API permissions**.
1. Click **Add a permission**.
1. In the **Request API permissions** fly-out, select **Dynamics CRM**.

   - If you don't see **Dynamics CRM**, look for **Dataverse**. Or select the **APIs my organization uses** tab and search for *Dataverse*.

1. Select the **user_impersonation** delegated permission.
1. Click **Add permissions**.

The configured permissions should look like this when you are done:

:::image type="content" source="media/configured-permissions-for-simple-spa-app.png" alt-text="Configured permissions for Simple SPA app":::

## Install Live Server Visual Studio Code extension

[Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) is a Visual Studio Code extension that allows you to easily launch a local development server for web pages.

1. Use these instructions to find and install the Live Server extension for VS Code in the VS Code marketplace:

   - [Browse for extensions](https://code.visualstudio.com/docs/editor/extension-marketplace#_browse-for-extensions)
   - [Install an extension](https://code.visualstudio.com/docs/editor/extension-marketplace#_install-an-extension)

1. After you have installed the Live Server extension, make these changes to the default settings.
1. Click the gear icon :::image type="icon" source="media/vscode-gear-icon.png" border="false"::: in VS Code and select **Settings** , or use the `Ctrl+,` keyboard shortcut.
1. In the search window type `liveServer.settings.host` and change the default value from `127.0.0.1` to `localhost`.

## Create a web application project  
  
1. Create a folder on your computer. The name is not important but for the purpose of these instructions name it `simplespa`.
1. Open VS Code and select **File** > **Open Folder** in the menu. Select the `simplespa` folder.
1. Create a new HTML file in the folder named `index.html`. (Not `index.htm`)
1. Copy the contents below into the index.html file:

   ```html
   <html>
    <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <script>
         const baseUrl = "https://org.api.crm.dynamics.com";      //<= Change this
         const clientId = "11111111-1111-1111-1111-111111111111"; //<= Change this
         const tenantId = "22222222-2222-2222-2222-222222222222"; //<= Change this
         const redirectUrl = "http://localhost:5500/index.html";
         const webAPIEndpoint = baseUrl +"/api/data/v9.2";

         
         // Configuration object to be passed to MSAL instance on creation. 
         
         const msalConfig = {
            auth: {       
               clientId: clientId,
               // Full directory URL, in the form of https://login.microsoftonline.com/<tenant-id>
               authority: "https://login.microsoftonline.com/"+tenantId,       
               redirectUri: redirectUrl,
            },
            cache: {
               cacheLocation: "sessionStorage" // This configures where your cache will be stored
            },
            system: {   
               loggerOptions: {   
                  loggerCallback: (level, message, containsPii) => {   
                        if (containsPii) {      
                           return;      
                        }      
                        switch (level) {      
                           case msal.LogLevel.Error:      
                              console.error(message);      
                              return;      
                           case msal.LogLevel.Info:      
                              console.info(message);      
                              return;      
                           case msal.LogLevel.Verbose:      
                              console.debug(message);      
                              return;      
                           case msal.LogLevel.Warning:      
                              console.warn(message);      
                              return;      
                        }   
                  }   
               }   
            }
         };

      </script>
         <!-- Latest version of msal-browser.js from CDN as of 2022/09 -->
      <script
            type="text/javascript" 
            src="https://alcdn.msauth.net/browser/2.28.1/js/msal-browser.min.js">
      </script>
      <style>
         body {  
            font-family: 'Segoe UI';  
         }  

         table {  
            border-collapse: collapse;  
         }  

         td, th {  
            border: 1px solid black;  
         }

         #message {  
            color: green;  
         }
   </style>
   </head>
   <body>
   <div>
      <button id="loginButton" onclick="signIn()">Login</button>
      <button id="logoutButton" onclick="signOut()" style="display:none;">Logout</button>
      <button id="getAccountsButton" onclick="getAccounts(writeTable)" style="display:none;">Get Accounts</button>  
      <div id="message"></div>
      <table id="accountsTable" style="display:none;">  
       <thead><tr><th>Name</th><th>City</th></tr></thead>  
       <tbody id="accountsTableBody"></tbody>  
      </table>
   </div>
   <script>
      const loginButton = document.getElementById("loginButton");
      const logoutButton = document.getElementById("logoutButton");
      const getAccountsButton = document.getElementById("getAccountsButton");
      const accountsTable = document.getElementById("accountsTable");
      const accountsTableBody = document.getElementById("accountsTableBody");
      const message = document.getElementById("message");
      // Create the main myMSALObj instance
      const myMSALObj = new msal.PublicClientApplication(msalConfig);

      let username = "";

      // Sets the username. Called at the end of this script.
      function selectAccount() {

         const currentAccounts = myMSALObj.getAllAccounts();
         if (currentAccounts.length === 0) {
            return;
         } else if (currentAccounts.length > 1) {
            // Add choose account code here
            console.warn("Multiple accounts detected.");
         } else if (currentAccounts.length === 1) {
            username = currentAccounts[0].username;
            showWelcomeMessage(username);
         }
      }

      // Called by the loginButton
      function signIn() {
         myMSALObj.loginPopup({
            scopes: ["User.Read",baseUrl+"/user_impersonation"] //<= Includes Dataverse scope
            })
            .then(response =>{
               if (response !== null) {
               username = response.account.username;
               showWelcomeMessage(username);
                  } else {
                     selectAccount();
                  }
            })
            .catch(error => {
                  console.error(error);
            });
      }

      // Shows greeting and enables logoutButton and getAccountsButton
      // Called from signIn or selectAccount functions
      function showWelcomeMessage(username) {
       message.innerHTML = `Welcome ${username}`;
       loginButton.style.display = "none";
       logoutButton.style.display = "block";
       getAccountsButton.style.display = "block";
      }

      // Called by the logoutButton
      function signOut() {

         const logoutRequest = {
            account: myMSALObj.getAccountByUsername(username),
            postLogoutRedirectUri: msalConfig.auth.redirectUri,
            mainWindowRedirectUri: msalConfig.auth.redirectUri
         };

         myMSALObj.logoutPopup(logoutRequest);
      }

      // Provides the access token for a request, opening pop-up if necessary.
      // Used by GetAccounts function
      function getTokenPopup(request) {

         request.account = myMSALObj.getAccountByUsername(username);
         
         return myMSALObj.acquireTokenSilent(request)
            .catch(error => {
                  console.warn("Silent token acquisition fails. Acquiring token using popup");
                  if (error instanceof msal.InteractionRequiredAuthError) {
                     // fallback to interaction when silent call fails
                     return myMSALObj.acquireTokenPopup(request)
                        .then(tokenResponse => {
                              console.log(tokenResponse);
                              return tokenResponse;
                        }).catch(error => {
                              console.error(error);
                        });
                  } else {
                     console.warn(error);   
                  }
         });
      }

      // Retrieves top 10 account records from Dataverse
      function getAccounts(callback) {
         // Gets the access token
         getTokenPopup({
               scopes: [baseUrl+"/.default"]
            })
            .then(response => {
               getDataverse("accounts?$select=name,address1_city&$top=10", response.accessToken, callback);
            }).catch(error => {
               console.error(error);
            });
      }

      /** 
       * Helper function to get data from Dataverse
      * using the authorization bearer token scheme
      * callback is the writeTable function below
      */
      function getDataverse(url, token, callback) {
          const headers = new Headers();
          const bearer = `Bearer ${token}`;
          headers.append("Authorization", bearer);
          // Other Dataverse headers
          headers.append("Accept", "application/json"); 
          headers.append("OData-MaxVersion", "4.0");  
          headers.append("OData-Version", "4.0");  

          const options = {
             method: "GET",
             headers: headers
          };

        console.log('GET Request made to Dataverse at: ' + new Date().toString());

        fetch(webAPIEndpoint+"/"+url, options)
             .then(response => response.json())
             .then(response => callback(response))
             .catch(error => console.log(error));
       }

       // Renders the table with data from GetAccounts
       function writeTable(data) {

          data.value.forEach(function (account) {

              var name = account.name;
              var city = account.address1_city;

              var nameCell = document.createElement("td");
              nameCell.textContent = name;
               
              var cityCell = document.createElement("td");
              cityCell.textContent = city;

              var row = document.createElement("tr");

              row.appendChild(nameCell);
              row.appendChild(cityCell);
            
              accountsTableBody.appendChild(row); 
        
          });
      
          accountsTable.style.display = "block";
          getAccountsButton.style.display = "none";
       }
       
       selectAccount();
     </script>
    </body>
   </html>
   ```

   > [!NOTE]
   > The JavaScript code in the HTML page was adapted from the sample code published here: [https://github.com/Azure-Samples/ms-identity-javascript-v2](https://github.com/Azure-Samples/ms-identity-javascript-v2) which connects to Microsoft Graph.
   >
   > The key difference is the scopes used when getting the access token.
   >
   > Use these scopes for the login button:
   > ```javascript
   >   // Called by the loginButton
   >   function signIn() {
   >      myMSALObj.loginPopup({
   >         scopes: ["User.Read",baseUrl+"/user_impersonation"]  //<= Includes Dataverse scope
   >         })
   > ```
   > These scopes include both the Microsoft Graph `User.Read` scope, but also the Dataverse `user_impersonation` scope.
   > By including both of these scopes when signing in, the inital consent dialog will include all the necessary scopes used in the applicaiton.
   >
   > Then, when specifying the scope used for the call to Dataverse you can use either `/.default` or `/user_impersonation`.
   >
   > ```javascript
   >       // Retrieves top 10 account records from Dataverse
   >       function getAccounts(callback) {
   >          // Gets the access token
   >          getTokenPopup({
   >                scopes: [baseUrl+"/.default"]
   >             })
   >    ```
   >
   > `/user_impersonation` scope only works for delegated permissions, which is the case here, so it could be used. `/.default` works for both delegated and application permissions.
   >
   > If you don't include the `baseUrl+"/user_impersonation"` scope when logging in, the user will have to consent a second time when they click the **Get Accounts** button for the first time.
   >
   >
   > You can find other SPA examples and tutorials here: [Single-page application (SPA) documentation](/azure/active-directory/develop/index-spa).

1. Within the index.html page, locate the following configuration variables and set them using the information you gathered in earlier steps: [Get your Dataverse Web API endpoint](#get-your-dataverse-web-api-endpoint) and [Register your application](#register-your-application).

   ```javascript
   const baseUrl = "https://org.api.crm.dynamics.com";      //<= Change this
   const clientId = "11111111-1111-1111-1111-111111111111"; //<= Change this
   const tenantId = "22222222-2222-2222-2222-222222222222"; //<= Change this
   ```
  
## Debug the app

Because you installed the Live Server extension in [Install Live Server Visual Studio Code extension](#install-live-server-visual-studio-code-extension), in the VS Code tool bar you should find this button: :::image type="icon" source="media/vscode-live-server-go-live-button.png" border="false":::.

1. Click the **Go Live** button and a new browser window will open to `http://localhost:5500/index.html` rendering the index.html page.

   The first time you run the app and click the **Login** button, you will get a consent dialog like this:

   :::image type="content" source="media/permissions-requested-dialog.png" alt-text="Permissions requested dialog":::

   If you are an administrator, you can select the **Consent on behalf of your organization** checkbox which will enable others to also run the app without having to use the **Permissions requested** dialog.

1. Click **Accept** to continue testing to verify that the app works as described in [Goal of this quick start](#goal-of-this-quick-start).

## Troubleshooting

The experience in this quick start depends on the Live Server port setting to be the default value: `5500`. If you already have Live Server installed and have modified the port setting, you will need to change the default setting or the URL set in the app registration.

Please note that the `liveServer.settings.port` may also be set for the **Workspace** and will override the **User** setting.

If you open multiple Live Server instances, the port setting may increment to 5501 or higher. This will break the callback used for authentication because the port is 'hard-coded' into the application registration as `http://localhost:5500/index.html`.

### See also

[Single-page application (SPA) documentation](/azure/active-directory/develop/index-spa)<br />
[Use OAuth with Cross-Origin Resource Sharing to connect a Single-Page Application to Dataverse](oauth-cross-origin-resource-sharing-connect-single-page-application.md)<br />
[Create client applications](connect-dataverse.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
