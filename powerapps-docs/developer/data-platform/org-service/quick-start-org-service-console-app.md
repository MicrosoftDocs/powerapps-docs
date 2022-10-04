---
title: "Quickstart: Organization service sample (C#) (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This quick start will show you how to connect to the Organization service of Microsoft Dataverse." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 09/30/2022
author: JimDaly
ms.author: jdaly
manager: kvivek
ms.reviewer: pehecke
ms.topic: "article"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
 - JimDaly
 - phecke
---
# Quickstart: Organization service sample (C#)

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

This topic shows you how to begin using classes in the SDK for .NET assemblies to work with Microsoft Dataverse business data. You will create a minimal console application to connect to your environment's Organization service using the <xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient> class and execute a web service operation.

Your application will call the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*> method passing an instance of the <xref:Microsoft.Crm.Sdk.Messages.WhoAmIRequest> class. The result returned from the web service is a populated <xref:Microsoft.Crm.Sdk.Messages.WhoAmIResponse>.<xref:Microsoft.Crm.Sdk.Messages.WhoAmIResponse.UserId> value which is the identifier of your Dataverse user account.

> [!NOTE]
> This quick start example does not include error handling for brevity. This is a minimum code example of what you need to connect to and use the Organization service.

## Prerequisites

 - Visual Studio (2019 or later)
 - Internet connection
 - Logon credentials of a Dataverse system user account for the target environment
 - URL address of the Dataverse environment you want to connect with
 - Basic understanding of the Visual C# language

## Create Visual Studio project

1. Create a new .NET console app project. For this project we are demonstrating .NET 6, but .NET Framework will also work.

    ![Start a console app project.](../media/quick-start-org-service-console-app-1.png)

    > [!NOTE]
    > This screenshot shows the name `OrgServiceQuickStart`, but you can choose to name the project and solution whatever you want. 

1. In **Solution Explorer**, right-click the project you created and select **Manage NuGet Packages...** in the context menu.

    ![Add NuGet package.](../media/quick-start-org-service-console-app-2.png)

1. Browse for the latest version of the  `Microsoft.CrmSdk.XrmTooling.CoreAssembly` NuGet package and install it.

    ![Install Microsoft.CrmSdk.XrmTooling.CoreAssembly NuGet package.](../media/quick-start-org-service-console-app-3.png)

> [!NOTE]
> You must select **I Accept** in the **Licence Acceptance** dialog.

## Edit Program.cs

1. Add these using statements to the top of `Program.cs`

    ```csharp
    using Microsoft.Crm.Sdk.Messages;
    using Microsoft.Xrm.Tooling.Connector;
    ```

1. Replace the `Main` method with the following code. The supported values for *AuthType* are listed in [Connection string parameters](../xrm-tooling/use-connection-strings-xrm-tooling-connect.md).

    ```csharp
    static void Main(string[] args)
    {            
        // e.g. https://yourorg.crm.dynamics.com
        string url = "<your environment url>";
        // e.g. you@yourorg.onmicrosoft.com
        string userName = "<your user name>";
        // e.g. y0urp455w0rd 
        string password = "<your password>";

        string conn = $@"
        Url = {url};
        AuthType = OAuth;
        UserName = {userName};
        Password = {password};
        AppId = 51f81489-12ee-4a9e-aaae-a2591f45987d;
        RedirectUri = app://58145B91-0C36-4500-8554-080854F2AC97;
        LoginPrompt=Auto;
        RequireNewInstance = True";

        using (var svc = new CrmServiceClient(conn))
        {

            WhoAmIRequest request = new WhoAmIRequest();

            WhoAmIResponse response = (WhoAmIResponse)svc.Execute(request);

            Console.WriteLine("Your UserId is {0}", response.UserId);

            Console.WriteLine("Press any key to exit.");
            Console.ReadLine();
        }
    }
    ```

1. Edit the following values to add information for your environment. You can find your environment URL in the Web application under **Settings > Customization > Developer Resources**.

    ```csharp
    // e.g. https://yourorg.crm.dynamics.com
    string url = "<your environment url>";
    // e.g. you@yourorg.onmicrosoft.com
    string userName = "<your user name>";
    // e.g. y0urp455w0rd
    string password = "<your password>";
    ```

## Run the program

1. Press F5 to run the program. The output should look like this:

    ```bash
    Your UserId is 969effb0-98ae-478c-b547-53a2968c2e75
    Press any key to exit.
    ```

### Congratulations!

You have successfully connected to the organization service.

## Next Steps

These articles will explain how to work with Dataverse tables:

[Entity class operations using the Organization service](entity-operations.md)<br />
[Create table rows using the Organization Service](entity-operations-create.md)<br />
[Retrieve a table row using the Organization Service](entity-operations-retrieve.md)<br />
[Update and delete table rows using the Organization Service](entity-operations-update-delete.md)<br />
[Associate and disassociate table rows using the Organization Service](entity-operations-associate-disassociate.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]