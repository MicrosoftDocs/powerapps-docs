---
title: "Quickstart: Execute a Dataverse SDK for .NET Request in C#"
description: "Learn how to connect a C# console app to Microsoft Dataverse and execute a Dataverse SDK for .NET request. Follow this quickstart to verify your connection."
ms.date: 08/04/2026
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

# Quickstart: Execute a Dataverse SDK for .NET request in C#

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

This quickstart shows how to use the Microsoft Dataverse SDK for .NET in a minimal C# console application. Connect to the Organization service by using the <xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient> class and execute a web service request to verify access to your environment's business data.

Your application calls the [IOrganizationService.Execute method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A) and passes an instance of the <xref:Microsoft.Crm.Sdk.Messages.WhoAmIRequest> class. The result returned from the web service is a populated [WhoAmIResponse.UserId](xref:Microsoft.Crm.Sdk.Messages.WhoAmIResponse.UserId) value that is the unique identifier of your Dataverse system user account.

> [!NOTE]
> This quickstart example doesn't include exception handling for brevity. This quickstart is a minimum code example of what you need to connect to and use the SDK for .NET.

You can get the complete code sample from GitHub [GetStarted](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp-NETCore/GetStarted/ConsoleApp%20(public)/Program.cs). Consult the program's [README](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp-NETCore/GetStarted/README.md) for more details.

## Prerequisites

- Visual Studio (2026 or later)
- Internet connection
- Sign-in credentials for a Dataverse system user account for the target environment
- URL address of the Dataverse environment you want to connect with
- Basic understanding of the Visual C# language

Read the following important information about using a connection string or username/password authentication in application code.
[!INCLUDE [cc-connection-string](../includes/cc-connection-string.md)]

## Create a .NET console app project in Visual Studio

1. Create a new project. For this project, use Visual Studio 2026.
   
   :::image type="content" source="media/quick-start-org-service-console-app/create-new-project.png" alt-text="Screenshot of Visual Studio showing the option to start a new project":::

1. Choose the .NET console app project template.

   :::image type="content" source="media/quick-start-org-service-console-app/template.png" alt-text="Screenshot of Visual Studio showing the .NET console app project template.":::

   Select **Next**.

1. Set the name of the project and the location.

   :::image type="content" source="media/quick-start-org-service-console-app/name-location.png" alt-text="Screenshot of Visual Studio showing the .NET name and location dialog.":::

   Select **Next**.

1. Select **.NET 10.0 (Long Term Support)** as the **Framework**.

   :::image type="content" source="media/quick-start-org-service-console-app/framework.png" alt-text="Screenshot of Visual Studio showing the .NET frameworks support configuration.":::

   Select **Create**.

1. In **Solution Explorer**, right-click the project you created and select **Manage NuGet Packages...** in the context menu.

    :::image type="content" source="../media/visual-studio-manage-nuget-packages.png" alt-text="Screenshot of Solution Explorer with Manage NuGet Packages selected for the project.":::

1. **Browse** for the latest version of the  `Microsoft.PowerPlatform.Dataverse.Client` NuGet package and install it.

   :::image type="content" source="media/quick-start-org-service-console-app/nuget-package.png" alt-text="Screenshot of NuGet Package Manager showing the Microsoft.PowerPlatform.Dataverse.Client package ready to install.":::

> [!NOTE]
> You're prompted to select **Apply** to preview changes, and then select **I Accept** in the **Licence Acceptance** dialog.

## Add code for the Dataverse SDK for .NET request

1. In **Solution Explorer**, double-click `Program.cs` to edit the file. Replace the file's contents with the following code.

   :::code language="csharp" source="~/../PowerApps-Samples/dataverse/orgsvc/CSharp-NETCore/GetStarted/ConsoleApp (public)/Program.cs":::
   

1. Change the values for the `url`, `userName`, and `password` as indicated by the `// TODO` code comment.

    > [!NOTE]
    > You can find your environment URL in the legacy web application under **Settings > Customization > Developer Resources** or in Power Apps **Settings** (gear icon) > **Developer Resources**.
    >
    > While this code sample places the username and password information in the code for simplicity, other code samples use the more recommended approach of prompting for that information or storing it in a separate `App.config` or `appsettings.json` file.
    >
    > You can find supported values for *AuthType* listed in [Connection string parameters](../xrm-tooling/use-connection-strings-xrm-tooling-connect.md#connection-string-parameters).

## Run the program

Press **F5** to run the program. The output should look similar to the following example:

```console
User ID is 00aa00aa-bb11-cc22-dd33-44ee44ee44ee
Press any key to exit.
```

## Use the IOrganizationService interface methods

The [Dataverse.Client.ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient) that this program uses implements the [IOrganizationService Interface](iorganizationservice-interface.md), which includes the [Execute method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A).

To better understand the `IOrganizationService` interface, try the following steps:

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

1. Paste this `WhoAmIExample` method below the `Main` method in your program.
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

1. Run the sample again. You should see something like:

   ```console
   OrganizationId:00aa00aa-bb11-cc22-dd33-44ee44ee44ee
   BusinessUnitId:11bb11bb-cc22-dd33-ee44-55ff55ff55ff
   UserId:22cc22cc-dd33-ee44-ff55-66aa66aa66aa
   Press the <Enter> key to exit.
   ```

## Next steps

Now that you have a simple console program that connects to Dataverse, use this project to try other methods and messages. You can use this Quick Start console application project to do ad-hoc testing.

### Try other IOrganizationService interface methods

> [!TIP]
> In the documentation, you can find many example methods like this `WhoAmIExample` that accept an `IOrganizationService service` parameter.

Try the examples for these [IOrganizationService methods](xref:Microsoft.Xrm.Sdk.IOrganizationService):

- [Create](xref:Microsoft.Xrm.Sdk.IOrganizationService.Create%2A)
- [Retrieve](xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve%2A)
- [Update](xref:Microsoft.Xrm.Sdk.IOrganizationService.Update%2A)
- [Delete](xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete%2A)
- [RetrieveMultiple](xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple%2A)
- [Associate](xref:Microsoft.Xrm.Sdk.IOrganizationService.Associate%2A)
- [Disassociate](xref:Microsoft.Xrm.Sdk.IOrganizationService.Disassociate%2A)

### Try other messages

You can find other messages that you can invoke by using the [Execute method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A) in these namespaces:

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
