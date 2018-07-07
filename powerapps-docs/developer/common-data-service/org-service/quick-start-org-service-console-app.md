---
title: "Quick Start: Organization service sample (C#) (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This quick start will show you how to connect to the organization service of the Common Data Service for Apps" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Quick Start: Organization service sample (C#)

In this quick start you will create a minimum console application to connect to the Organization service using the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> class. You will pass  your connection information using a connection string passed to the constructor.

You will use the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*> method passing an instance of the <xref:Microsoft.Crm.Sdk.Messages.WhoAmIRequest> class, and you will display the <xref:Microsoft.Crm.Sdk.Messages.WhoAmIResponse>.<xref:Microsoft.Crm.Sdk.Messages.WhoAmIResponse.UserId> value.

> [!NOTE]
> This quick start example does not include error handling. This is a minimum example of what you need to connect to and use the Organization service.


## Prerequisites

 - Visual Studio (2017 recommended)
 - Internet connection
 - Valid user account for a Common Data Service for Apps instance
    - Your username
    - Your password
 - Url to the CDS for Apps environment you want to connect with
 - Basic understanding of the Visual C# language

## Create Visual Studio project

1. Create a new Console App (.NET Framework) project using .NET Framework 4.6.2

    ![Start a console app project](../media/quick-start-org-service-console-app-1.png)

    > [!NOTE]
    > This screenshot shows the name `OrgServiceQuickStart`, but you can choose to name the project and solution whatever you want. 

1. In **Solution Explorer**, right-click the project you created and select **Manage NuGet Packages...** in the context menu.

    ![Add NuGet package](../media/quick-start-org-service-console-app-2.png)

1. Browse for the latest version of the  `Microsoft.CrmSdk.XrmTooling.CoreAssembly` NuGet package and install it.

    ![Install Microsoft.CrmSdk.XrmTooling.CoreAssembly NuGet package](../media/quick-start-org-service-console-app-3.png)

> [!NOTE]
> You must select **I Accept** in the **Licence Acceptance** dialog.

## Edit Program.cs

1. Add these using statements to the top of `Program.cs`

    ```csharp
    using Microsoft.Crm.Sdk.Messages;
    using Microsoft.Xrm.Tooling.Connector;
    ```

1. Replace the `Main` method with the following code:

    ```csharp
    static void Main(string[] args)
    {            
        // i.e. https://yourorg.crm.dynamics.com
        string url = "<your environment url>";
        // i.e. you@yourorg.onmicrosoft.com
        string userName = "<your user name>";
        // i.e. y0urp455w0rd
        string password = "<your password>";

        string conn = $@"
        Url = {url};
        AuthType = Office365;
        UserName = {userName};
        Password = {password};
        RequireNewInstance = True";

        using (var crmSvc = new CrmServiceClient(conn))
        {

            WhoAmIRequest request = new WhoAmIRequest();

            WhoAmIResponse response = (WhoAmIResponse)crmSvc.Execute(request);

            Console.WriteLine("Your UserId is {0}", response.UserId);

            Console.WriteLine("Press any key to exit.");
            Console.ReadLine();
        }
    }
    ```

1. Edit the following values to add information for your environment:

    ```csharp
    // i.e. https://yourorg.crm.dynamics.com
    string url = "<your environment url>";
    // i.e. you@yourorg.onmicrosoft.com
    string userName = "<your user name>";
    // i.e. y0urp455w0rd
    string password = "<your password>";
    ```

## Run the program

1. Press F5 to run the program. The output should look like this:

    ```
    Your UserId is 969effb0-98ae-478c-b547-53a2968c2e75
    Press any key to exit.
    ```

### Congratulations!

You have successfully connected to the organization service.


<!-- TODO: Include link to next steps topics -->