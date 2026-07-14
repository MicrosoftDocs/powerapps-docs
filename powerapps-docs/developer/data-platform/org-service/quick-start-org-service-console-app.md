---
title: "Quickstart: Execute an SDK for .NET request (C#) (Microsoft Dataverse) | Microsoft Docs"
description: "Demonstrates how to connect to the SDK for .NET of Microsoft Dataverse and execute a request."
ms.date: 06/20/2025
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
ms.topic: quickstart
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - phecke
---

# Quickstart: Execute an SDK for .NET request (C#)

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

This article shows you how to begin using classes in the SDK for .NET assemblies to work with Microsoft Dataverse business data. You'll create a minimal console application to connect to your environment's Organization service using the <xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient> class and execute a web service operation.

Your application calls the [IOrganizationService.Execute method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A) passing an instance of the <xref:Microsoft.Crm.Sdk.Messages.WhoAmIRequest> class. The result returned from the web service is a populated [WhoAmIResponse.UserId](xref:Microsoft.Crm.Sdk.Messages.WhoAmIResponse.UserId) value that is the unique identifier of your Dataverse system user account.

> [!NOTE]
> This quick start example doesn't include exception handling for brevity. This quick start is a minimum code example of what you need to connect to and use the SDK for .NET.

You can obtain the complete code sample from GitHub [GetStarted](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp-NETCore/GetStarted/ConsoleApp%20(public)/Program.cs). Consult the program's [README](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp-NETCore/GetStarted/README.md) for more details.

## Prerequisites

- Visual Studio (2022 or later)
- Internet connection
- Logon credentials of a Dataverse system user account for the target environment
- URL address of the Dataverse environment you want to connect with
- Basic understanding of the Visual C# language

Read the following important information about using a connection string or username/password authentication in application code.
[!INCLUDE [cc-connection-string](../includes/cc-connection-string.md)]

## Create Visual Studio project

1. Create a new .NET console app project. For this project, we're using Visual Studio 2022 and targeting .NET 6.

    ![Start a console app project.](../media/quick-start-org-service-console-app-1.png)

1. In **Solution Explorer**, right-click the project you created and select **Manage NuGet Packages...** in the context menu.

    ![Add NuGet package.](../media/quick-start-org-service-console-app-2.png)

1. **Browse** for the latest version of the  `Microsoft.PowerPlatform.Dataverse.Client` NuGet package and install it.

    ![Install Microsoft.PowerPlatform.Dataverse.Client NuGet package.](../media/quick-start-org-service-console-app-3.png)

> [!NOTE]
> You are prompted to OK the preview changes, and then select **I Accept** in the **Licence Acceptance** dialog.

## Add application code

1. In **Solution Explorer**, double-click Program.cs to edit that file. Replace the file's contents with the code shown below.

   ```csharp
   using Microsoft.Crm.Sdk.Messages;
   using Microsoft.PowerPlatform.Dataverse.Client;
   using Microsoft.Xrm.Sdk;
   
   class Program
   {
      // TODO Enter your Dataverse environment's URL and logon info.
      static string url = "https://yourorg.crm.dynamics.com";
      static string userName = "you@yourorg.onmicrosoft.com";
      static string password = "yourPassword";
   
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
   
      static void Main()
      {
         //ServiceClient implements IOrganizationService interface
         IOrganizationService service = new ServiceClient(connectionString);
   
         var response = (WhoAmIResponse)service.Execute(new WhoAmIRequest());
   
         Console.WriteLine($"User ID is {response.UserId}.");
   
   
         // Pause the console so it does not close.
         Console.WriteLine("Press the <Enter> key to exit.");
         Console.ReadLine();
      }
   }
   ```

1. Change the values for the `url`, `userName`, and `password` as indicated by the `// TODO` code comment.

    > [!NOTE]
    > You can find your environment URL in the legacy web application under **Settings > Customization > Developer Resources** or in Power Apps **Settings** (gear icon) > **Developer Resources**.
    >
    > While this code sample places the username/password information in the code for simplicity, other code samples use the more recommended approach of prompting for that information or storing it in a separate App.config or appsettings.json file.
    >
    > You can find supported values for *AuthType* listed in [Connection string parameters](../xrm-tooling/use-connection-strings-xrm-tooling-connect.md#connection-string-parameters).

## Run the program

Press **F5** to run the program. The output should look something like this:

```console
User ID is 00aa00aa-bb11-cc22-dd33-44ee44ee44ee
Press any key to exit.
```

## Use the IOrganizationService interface methods

Notice that the [Dataverse.Client.ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient) this program uses implements the [IOrganizationService Interface](iorganizationservice-interface.md) which includes the [Execute method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A).

To see and understand the `IOrganizationService` interface a little better, try this:

1. Go to the reference article for the [WhoAmIRequest class](xref:Microsoft.Crm.Sdk.Messages.WhoAmIRequest).
1. Copy the example method from that article. It looks like this:

   ```csharp
   /// <summary>
   /// Outputs the data returned from the WhoAmI message
   /// </summary>
   /// <param name="service">Authenticated client implementing the IOrganizationService interface</param>
   static void WhoAmIExample(IOrganizationService service) {

      var response = (WhoAmIResponse)service.Execute(new WhoAmIRequest());

      Console.WriteLine($"OrganizationId:{response.OrganizationId}");
      Console.WriteLine($"BusinessUnitId:{response.BusinessUnitId}");
      Console.WriteLine($"UserId:{response.UserId}");

   }
   ```

   Notice that it accepts an `IOrganizationService` service instance as the parameter.

1. Paste this `WhoAmIExample` method below the `Main` method in your program
1. Replace the `Main` method in your program with this:

   ```csharp
       static void Main()
    {
        //ServiceClient implements IOrganizationService interface
        IOrganizationService service = new ServiceClient(connectionString);

        WhoAmIExample(service: service);

        // Pause the console so it does not close.
        Console.WriteLine("Press the <Enter> key to exit.");
        Console.ReadLine();
    }
   ```

1. Run the sample again and you should see something like:

   ```console
   OrganizationId:00aa00aa-bb11-cc22-dd33-44ee44ee44ee
   BusinessUnitId:11bb11bb-cc22-dd33-ee44-55ff55ff55ff
   UserId:22cc22cc-dd33-ee44-ff55-66aa66aa66aa
   Press the <Enter> key to exit.
   ```

## Next Steps

Now that you have a simple console program that connects to Dataverse, use this project to try other methods and messages. You can use this Quick Start console application project to do ad-hoc testing.

### Try other IOrganizationService interface methods

> [!TIP]
> In our documentation, you can find many example methods like this `WhoAmIExample` that accept an `IOrganizationService service` parameter.

Try the examples for these [IOrganizationService methods](xref:Microsoft.Xrm.Sdk.IOrganizationService) methods:

- [Create](xref:Microsoft.Xrm.Sdk.IOrganizationService.Create%2A)
- [Retrieve](xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve%2A)
- [Update](xref:Microsoft.Xrm.Sdk.IOrganizationService.Update%2A)
- [Delete](xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete%2A)
- [RetrieveMultiple](xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple%2A)
- [Associate](xref:Microsoft.Xrm.Sdk.IOrganizationService.Associate%2A)
- [Disassociate](xref:Microsoft.Xrm.Sdk.IOrganizationService.Disassociate%2A)

### Try other messages

You can find other messages that you can invoke using the [Execute method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A) in these name spaces:

- [Microsoft.Xrm.Sdk.Messages Namespace](xref:Microsoft.Xrm.Sdk.Messages)
- [Microsoft.Crm.Sdk.Messages Namespace](xref:Microsoft.Crm.Sdk.Messages)

### Learn to work with record data

The following articles explain how to work with business data in Dataverse tables:
  
- [Entity class operations using the SDK for .NET](entity-operations.md)
- [Create table rows using the SDK for .NET](entity-operations-create.md)
- [Retrieve a table row using the SDK for .NET](entity-operations-retrieve.md)
- [Update and delete table rows using the SDK for .NET](entity-operations-update-delete.md)
- [Associate and disassociate table rows using the SDK for .NET](entity-operations-associate-disassociate.md)

### Explore our code samples

You can find SDK for .NET sample code in our GitHub repository at [PowerApps-Samples/dataverse/orgsvc](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc).

### Use ServiceClient extensions

In addition to implementing the [IOrganizationService interface](xref:Microsoft.Xrm.Sdk.IOrganizationService), [ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient) offers extension methods beyond the core methods defined by `IOrganizationService` and the capability to enable logging with [ILogger](xref:Microsoft.Extensions.Logging.ILogger). [Learn more about using ServiceClient](../sdk-client-transition.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
