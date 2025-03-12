---
title: Quick Start Web API with client-side JavaScript and Visual Studio Code
description: Describes how to interactively authenticate and use the Dataverse Web API with client-side JavaScript and Visual Studio Code
ms.date: 03/20/2025
author: JimDaly
ms.author: jdaly
ms.reviewer: jdaly
search.audienceType:
  - developer
---
# Quick Start Web API with client-side JavaScript and Visual Studio Code

This quickstart demonstrates how you can connect to Dataverse and use the Web API with the following technologies:

|Technology|Description|
|---|---|
|JavaScript|JavaScript is a programming language for web development, enabling interactive content. It runs in browsers for client-side scripting and can be used server-side with Node.js.|
|Visual Studio Code|Visual Studio Code is a lightweight, open-source code editor with debugging, syntax highlighting, and plugin support.|
|Single Page Applications|Single Page Applications (SPAs) are web applications that load a single HTML page and dynamically update content as the user interacts with the app. This approach provides a smoother, faster user experience by reducing page reloads and enhancing performance.|
|Microsoft Authentication Library|[Microsoft Authentication Library for JavaScript (MSAL.js)](/javascript/api/overview/msal-overview) is a library that enables authentication and authorization for web applications using Microsoft identity platforms. It simplifies integrating secure sign-in and token acquisition for accessing protected resources.|


This quickstart focuses on connecting to the Dataverse Web API with JavaScript using a SPA client application with a minimum of number of steps.

> [!NOTE]
> This sample isn't about the following scenarios:
>
> |Scenario|More information|
> |---|---|
> |Model-driven application scripts|- [Apply business logic using client scripting in model-driven apps using JavaScript](../../model-driven-apps/client-scripting.md)<br />- [Xrm.WebApi (Client API reference)](/power-apps/developer/model-driven-apps/clientapi/reference/xrm-webapi)|
> |Power Apps code component framework|- [Code components WebAPI](/power-apps/developer/component-framework/reference/webapi)<br />- [Implementing Web API component](../../component-framework/sample-controls/webapi-control.md)|
> |Power Pages Portals|[Power Pages Portals Web API](/power-pages/configure/web-api-overview)|
>
> For each of these scenarios, the respective application type provides a capability for you to send requests rather than use the JavaScript native [Fetch API](https://developer.mozilla.org/docs/Web/API/Fetch_API) directly as shown in these samples. Client-side scripts within model-driven apps run in the context of an authenticated application, so each request doesn't require an access token.

A SPA application can use client-side JavaScript because Cross-Origin Resource Sharing (CORS) is enabled. CORS is a security feature in web browsers that allows controlled access to resources on a web server from a different origin. It enables web applications to bypass the [same-origin policy](https://developer.mozilla.org/docs/Web/Security/Same-origin_policy), facilitating safe and secure data sharing across different domains.

## Prerequisites

- **A working knowledge of modern JavaScript**. Especially [making network requests with JavaScript](https://developer.mozilla.org/docs/Learn_web_development/Core/Scripting/Network_requests).
- **Privileges to create an Entra App registration**. By default all users can register applications, but it is common for Entra administrators to limit who in the tenant can register apps.

If you aren't sure if you can, try to [Register a SPA application](#register-a-spa-application) and find out. Learn more about how [app registration permissions are delegated in Microsoft Entra ID](/entra/identity/role-based-access-control/delegate-app-roles)

- **Visual Studio Code**. [Download and install Visual Studio Code](https://code.visualstudio.com/download).
- **Live Server Visual Studio Code extension**. Modern JavaScript development practices are highly dependent on technologies like [npm](https://www.npmjs.com/), [webpack](https://webpack.js.org/), and whatever frameworks you have chosen. These extensions allow for managing all the libraries that modern web applications depend on. This quick start will avoid taking dependencies on anything other than the MSAL.js library. The [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) makes it easy to serve an HTML page on your local computer with a minimum of complexity. You can install this extension by searching for Live Server in the [Visual Studio Code marketplace](https://code.visualstudio.com/docs/editor/extension-marketplace).

   There are quickstart tutorials that

- **Node.js**. Node.js is a runtime environment that allows you to run JavaScript on the server side. This quickstart uses a SPA application that runs JavaScript on the client side, so we aren't going to use the node runtime. But npm (Node Package Manager) is installed with node, and you need npm to get the latest version of MSAL.js.

## Register a SPA application

This is the first step because if you can't register an app, there is no point in going further.

Usually your Azure account must have permissions to manage applications. Any of the following Microsoft Entra roles include the required permissions:

- Application Administrator
- Application Developer
- Cloud Application Administrator.

To configure the application you need an application ID (also called a Client ID), and the ID of your Entra tenant.

There are two ways you can do this:

:::row:::
   :::column:::
   Using the Entra web application
   :::column-end:::
   :::column:::
   Using PowerShell Script
   :::column-end:::
:::row-end:::
:::row:::
   :::column:::
   These instructions describe how to [Register the application and copy IDs](/entra/identity-platform/quickstart-single-page-app-sign-in?pivots=workforce&tabs=javascript-workforce%2Cjavascript-external#register-the-application-and-record-identifiers).

   After this, to specify your app type to your app registration, follow these steps:

   1. Under Manage, select Authentication.
   1. On the Platform configurations page, select Add a platform, and then select SPA option.
   1. For the Redirect URIs enter <http://localhost:5500>.
   1. Select Configure to save your changes.
   :::column-end:::
   :::column:::

   :::column-end:::
:::row-end:::

These instructions describe how to [Register the application and copy IDs](/entra/identity-platform/quickstart-single-page-app-sign-in?pivots=workforce&tabs=javascript-workforce%2Cjavascript-external#register-the-application-and-record-identifiers).

## Install Node.js

1. Go to [Download Node.js](https://nodejs.org/en/download).
1. Choose the appropriate installer for your operating system (Windows, macOS, or Linux).
1. Run the installer. Make sure you select the option to install NPM along with node.
1. Verify the installation by opening a terminal or command prompt and typing these commands: `node -v` and `npm -v`

   You should see something like this:

   ```powershell
   PS C:\Users\you> node -v
   v22.14.0
   PS C:\Users\you> npm -v
   9.5.0
   PS C:\Users\you>
   ```

## Create a project

1. Create a folder somewhere on your computer. The name isn't important, but for these instructions call it `quickspa`.
1. Open this folder using Visual Studio Code.

### Get the msal-browser.min.js library

We need a copy of the latest version of the `msal-browser.min.js` library, but we don't want to take a dependency on using npm to build and run our code.

1. Open a terminal window and type  `npm init -y`.

   This creates a `package.json` file in your folder.

1. In the terminal window type `npm install @azure/msal-browser`.

   This creates a `node_modules` folder and a `package-lock.json` file in the `quickspa` folder.

1. Go to `node_modules\@azure\msal-browser\lib\` and copy the `msal-browser.min.js` file.
1. Paste the `msal-browser.min.js` file into the `quickspa` folder.
1. Delete the `node_modules` folder and the `package-lock.json` and `package.json` files.

   The `msal-browser.min.js` file should be the only file left in the `quickspa` folder.

### Create HTML page

1. Create a new file named `index.html`.
1. Copy and paste this content to the `index.html` page:

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>QuickSPA</title>
      <link rel="stylesheet" href="styles.css" />
   </head>
   <body>
      <header>
         <h1>Welcome to QuickSPA</h1>
         <button id="loginButton">Login</button>
         <button id="logoutButton" class="hidden">Logout</button>
      </header>
      <nav class="disabled">
         <button id="whoAmIButton">WhoAmI</button>
      </nav>
      <main id="container"></main>
      <script type="module" src="index.js"></script>
   </body>
   </html>
   ```

### Create JavaScript page

1. Create a new file named `index.js`.
Copy and paste this content into the `index.js` page:

   ```javascript
   // Import the MSAL library in the same folder as this file
   import "/msal-browser.min.js";

   const config = {
   // Change these values in the next step:
   baseUrl: "https://<your org>.api.crm.dynamics.com", //<= Change this
   clientId: "00001111-aaaa-2222-bbbb-3333cccc4444", //<= Change this
   tenantId: "aaaabbbb-0000-cccc-1111-dddd2222eeee", //<= Change this
   redirectUri: "http://localhost:5500/index.html",
   };

   // Microsoft Authentication Library (MSAL) configuration
   const msalConfig = {
   auth: {
      clientId: config.clientId,
      authority: "https://login.microsoftonline.com/" + config.tenantId,
      redirectUri: config.redirectUri,
      postLogoutRedirectUri: config.redirectUri,
      },
   cache: {
      cacheLocation: "sessionStorage", // This configures where your cache will be stored
      storeAuthStateInCookie: true,
      },
   };

   // Create an instance of MSAL
   const msalInstance = new msal.PublicClientApplication(msalConfig);
   await msalInstance.initialize();

   // body/main element where messages are displayed
   const container = document.getElementById("container");

   /**
   * Retrieves an access token using MSAL (Microsoft Authentication Library).
   *
   * @async
   * @function getToken
   * @returns {Promise<string>} The access token.
   * @throws {Error} If token acquisition fails and is not an interaction required error.
   */
   async function getToken() {
   const request = {
      scopes: [config.baseUrl + "/.default"],
   };

   try {
      const response = await msalInstance.acquireTokenSilent(request);
      return response.accessToken;
   } catch (error) {
      if (error instanceof msal.InteractionRequiredAuthError) {
            const response = await msalInstance.acquireTokenPopup(request);
            return response.accessToken;
         } else {
            console.error(error);
            throw error;
         }
      }
   }

   // Event handler for login button
   async function logIn() {
   // When there is no active account.
   if (!msalInstance.getActiveAccount()) {
      const request = {
         scopes: ["User.Read", config.baseUrl + "/user_impersonation"],
      };
      try {
         const response = await msalInstance.loginPopup(request);
         msalInstance.setActiveAccount(response.account);

         // Hide the login button so no one can click it again.
         this.style.display = "none";

         // Show the logout button
         const logoutButton = document.getElementById("logoutButton");
         logoutButton.innerHTML = "Logout " + response.account.name;
         logoutButton.style.display = "block";
         document.getElementsByTagName("nav")[0].classList.remove("disabled");
      } catch (error) {
         let p = document.createElement("p");
         p.textContent = "Error logging in: " + error;
         p.className = "error";
         container.append(p);
      }
      } else {
      // Remove the active account and try again
      msalInstance.setActiveAccount(null);
      this.click();
      }
   }

   // Event handler for logout button
   async function logOut() {
   const activeAccount = await msalInstance.getActiveAccount();
   const logoutRequest = {
         account: activeAccount,
         mainWindowRedirectUri: config.redirectUri,
   };

   try {
      await msalInstance.logoutPopup(logoutRequest);

      // return the button to the starting state
      document.getElementById("loginButton").style.display = "block";
      this.innerHTML = "Logout";
      this.style.display = "none";

      document.getElementsByTagName("nav")[0].classList.add("disabled");
      } 
   catch (error) {
         console.error("Error logging out: ", error);
      }
   }

   // Add event listener to the login button
   document.getElementById("loginButton").onclick = logIn;

   // Add event listener to the logout button
   document.getElementById("logoutButton").onclick = logOut;

   /// Function to get the current user's information
   /// using the WhoAmI endpoint of the Dataverse Web API.
   async function whoAmI() {
   const token = await getToken();
   const request = new Request(config.baseUrl + "/api/data/v9.2/WhoAmI", 
   {
      method: "GET",
      headers: {
         Authorization: `Bearer ${token}`,
         "Content-Type": "application/json",
         Accept: "application/json",
         "OData-Version": "4.0",
         "OData-MaxVersion": "4.0",
      },
   });
   // Send the request to the API
   const response = await fetch(request);
   // Handle the response
   if (!response.ok) {
      throw new Error("Network response was not ok: " + response.statusText);
   }
   // Successfully received response
   return await response.json();
   }

   // Add event listener to the whoAmI button
   document.getElementById("whoAmIButton").onclick = async function () {
   // Clear any previous messages
   container.replaceChildren();
   try {
      const response = await whoAmI();
      let p1 = document.createElement("p");
      p1.textContent =
         "Congratulations! You connected to Dataverse using the Web API.";
      container.append(p1);
      let p2 = document.createElement("p");
      p2.textContent = "User ID: " + response.UserId;
      container.append(p2);
      } 
   catch (error) {
         let p = document.createElement("p");
         p.textContent = "Error fetching user info: " + error;
         p.className = "error";
         container.append(p);
      }
   };
   ```

1. Update the `index.js` file to replace lines 5-7 below with the values from [Register a SPA application](#register-a-spa-application).

   ```JavaScript
      baseUrl: "https://<your org>.api.crm.dynamics.com", //<= Change this
      clientId: "00001111-aaaa-2222-bbbb-3333cccc4444", //<= Change this
      tenantId: "aaaabbbb-0000-cccc-1111-dddd2222eeee", //<= Change this
   ```

### Create CSS page

1. Create a new file named `styles.css`.
1. Copy and paste this into the `styles.css` page:

   ```css
   .disabled {
      pointer-events: none;
      opacity: 0.5;
      /* Optional: to visually indicate the element is disabled */
   }

   .hidden {
      display: none;
   }

   .error {
      color: red;
   }

   body {
      font-family: 'Roboto', sans-serif;
      font-size: 16px;
      line-height: 1.6;
      color: #333;
      background-color: #f9f9f9;
   }

   h1 {
      color: #2c3e50;
   }

   button {
      background-color: #3498db;
      color: #fff;
      border: none;
      padding: 10px 20px;
      border-radius: 5px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      transition: background-color 0.3s ease;
      margin: 5px;
      /* Adjust the value as needed */
   }

   button:hover {
      background-color: #2980b9;
   }

   header {
      padding-bottom: 10px;
      /* Adjust the value as needed */
   }
   ```

## Try it

1. In Visual Studio Code, click the **Go Live** button.
1. Click the **Login** button.

   The **Sign in to your account** dialog opens.

1. Select the account that has access to Dataverse.
1. Click the **WhoAmI** button.

   The message **Congratulations! You connected to Dataverse using the Web API.** is displayed with your `UserId` value from the [WhoAmIResponse complex type](/power-apps/developer/data-platform/webapi/reference/whoamiresponse).

## Trouble shooting
