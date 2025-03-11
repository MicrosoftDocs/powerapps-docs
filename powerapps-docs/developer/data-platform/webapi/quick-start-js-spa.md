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

:::row:::
   :::column:::
   JavaScript
   :::column-end:::
   :::column:::
   Visual Studio Code
   :::column-end:::
   :::column:::
   Single Page Applications
   :::column-end:::
   :::column:::
   Microsoft Authentication Library for JavaScript (MSAL.js)
   :::column-end:::
:::row-end:::
:::row:::
   :::column:::
   JavaScript is a programming language for web development, enabling interactive content. It runs in browsers for client-side scripting and can be used server-side with Node.js.
   :::column-end:::
   :::column:::
   Visual Studio Code is a lightweight, open-source code editor with debugging, syntax highlighting, and plugin support.
   :::column-end:::
   :::column:::
   Single Page Applications (SPAs) are web applications that load a single HTML page and dynamically update content as the user interacts with the app. This approach provides a smoother, faster user experience by reducing page reloads and enhancing performance.
   :::column-end:::
   :::column:::
   [Microsoft Authentication Library for JavaScript (MSAL.js)](/javascript/api/overview/msal-overview) is a library that enables authentication and authorization for web applications using Microsoft identity platforms. It simplifies integrating secure sign-in and token acquisition for accessing protected resources.
   :::column-end:::
:::row-end:::

This quickstart is focused on using the Dataverse Web API with JavaScript using a SPA client application. For information about how to use Web API in model-driven applications and Power Apps components, see [Xrm.WebApi (Client API reference)](/power-apps/developer/model-driven-apps/clientapi/reference/xrm-webapi) and [Code components WebAPI](/power-apps/developer/component-framework/reference/webapi). Both of these provide methods to work with Dataverse data from within Power Apps applications. Because both of these run in the context of an application that is already authenticated, it isn't necessary to authenticate.

A SPA application can use client-side JavaScript because Cross-Origin Resource Sharing (CORS) is enabled. CORS is a security feature in web browsers that allows controlled access to resources on a web server from a different origin. It enables web applications to bypass the [same-origin policy](https://developer.mozilla.org/docs/Web/Security/Same-origin_policy), facilitating safe and secure data sharing across different domains.

## Prerequisites

- **A working knowledge of modern JavaScript**. Especially [making network requests with JavaScript](https://developer.mozilla.org/docs/Learn_web_development/Core/Scripting/Network_requests).
- **Privileges to create an Entra App registration**. By default all users can register applications, but it is common for Entra administrators to limit who in the tenant can register apps. 

If you aren't sure if you can, try to [Register a SPA application](#register-an-application) and find out. Learn more about how [app registration permissions are delegated in Microsoft Entra ID](/entra/identity/role-based-access-control/delegate-app-roles)
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
   1. For the Redirect URIs enter http://localhost:5500.
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
