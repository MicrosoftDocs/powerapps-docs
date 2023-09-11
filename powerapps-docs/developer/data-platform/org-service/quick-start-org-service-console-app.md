---
title: "Quickstart: Execute an SDK for .NET request (C#) (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Demonstrates how to connect to the SDK for .NET of Microsoft Dataverse and execute a request." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 10/05/2022
author: phecke
ms.author: pehecke
ms.reviewer: jdaly
ms.topic: "article"
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - phecke
---

# Quickstart: Execute an SDK for .NET request (C#)

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

This topic shows you how to begin using classes in the SDK for .NET assemblies to work with Microsoft Dataverse business data. You will create a minimal console application to connect to your environment's Organization service using the <xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient> class and execute a web service operation.

Your application will call the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*> method passing an instance of the <xref:Microsoft.Crm.Sdk.Messages.WhoAmIRequest> class. The result returned from the web service is a populated <xref:Microsoft.Crm.Sdk.Messages.WhoAmIResponse>.<xref:Microsoft.Crm.Sdk.Messages.WhoAmIResponse.UserId> value which is the unique identifier of your Dataverse system user account.

> [!NOTE]
> This quick start example does not include exception handling for brevity. This is a minimum code example of what you need to connect to and use the SDK for .NET.

You can download the complete code sample from GitHub [quickstart-execute-request](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/orgsvc/C%23-NETCore/GetStarted/quickstart-execute-request/).

## Prerequisites

 - Visual Studio (2019 or later)
 - Internet connection
 - Logon credentials of a Dataverse system user account for the target environment
 - URL address of the Dataverse environment you want to connect with
 - Basic understanding of the Visual C# language

## Create Visual Studio project

1. Create a new .NET console app project. For this project we are using Visual Studio 2022 and targeting .NET 6, but .NET Framework will also work.

    ![Start a console app project.](../media/quick-start-org-service-console-app-1.png)

1. In **Solution Explorer**, right-click the project you created and select **Manage NuGet Packages...** in the context menu.

    ![Add NuGet package.](../media/quick-start-org-service-console-app-2.png)

1. Browse for the latest version of the  `Microsoft.PowerPlatform.Dataverse.Client` NuGet package and install it.

    ![Install Microsoft.PowerPlatform.Dataverse.Client NuGet package.](../media/quick-start-org-service-console-app-3.png)

> [!NOTE]
> Your will be prompted to OK the preview changes, and then select **I Accept** in the **Licence Acceptance** dialog.

## Add application code

1. In **Solution Explorer**, double-click Program.cs to edit that file. Replace the file's contents with the code shown below.

    ```csharp
    using Microsoft.Crm.Sdk.Messages;
    using Microsoft.PowerPlatform.Dataverse.Client;

    class Program
    {
        // TODO Enter your Dataverse environment's URL and logon info.
        static string url = "https://yourorg.crm.dynamics.com";
        static string userName = "someone@myorg.onmicrosoft.com";
        static string password = "password";

        // This service connection string uses the info provided above.
        // The AppId and RedirectUri are provided for sample code testing.
        static string connectionString = $@"
        AuthType = OAuth;
        Url = {url};
        UserName = {userName};
        Password = {password};
        AppId = 51f81489-12ee-4a9e-aaae-a2591f45987d;
        RedirectUri = app://58145B91-0C36-4500-8554-080854F2AC97;
        LoginPrompt=Auto;
        RequireNewInstance = True";

        static void Main(string[] args)
        {
            using (ServiceClient serviceClient = new(connectionString))
            {
                if (serviceClient.IsReady)
                {
                    WhoAmIResponse response = 
                        (WhoAmIResponse)serviceClient.Execute(new WhoAmIRequest());

                    Console.WriteLine("User ID is {0}.", response.UserId);
                }
                else
                {
                    Console.WriteLine(
                        "A web service connection was not established.");
                }
            }

            // Pause the console so it does not close.
            Console.WriteLine("Press any key to exit.");
            Console.ReadLine();
        }
    }
    ```

1. Change the values for the environment URL, username, and password as indicated by the TODO code comment.

    > [!NOTE]
    > You can find supported values for *AuthType* listed in [Connection string parameters](../xrm-tooling/use-connection-strings-xrm-tooling-connect.md#connection-string-parameters). You can find your environment URL in the legacy web application under **Settings > Customization > Developer Resources** or in Power Apps **Settings** (gear icon) > **Developer Resources**.
    >
    > While this code sample places the username/password information in the code for simplicity, other code samples will use the more recommended approach of prompting for that information or storing it in a separate App.config or appsettings.json file.

## Run the program

1. Press F5 to run the program. The output should look something like this:

    ```bash
    User ID is 969effb0-98ae-478c-b547-53a2968c2e75
    Press any key to exit.
    ```

## Next Steps

The console app demonstrates how to connect to the Organization web service using a connection string, execute a web service message request, and access some data in the response. Next, you may want to look at common web service data operations like create, retrieve, update, and delete.

The following articles will explain how to work with business data in Dataverse tables.  
[Entity class operations using the SDK for .NET](entity-operations.md)  
[Create table rows using the SDK for .NET](entity-operations-create.md)  
[Retrieve a table row using the SDK for .NET](entity-operations-retrieve.md)  
[Update and delete table rows using the SDK for .NET](entity-operations-update-delete.md)<br />
[Associate and disassociate table rows using the SDK for .NET](entity-operations-associate-disassociate.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
