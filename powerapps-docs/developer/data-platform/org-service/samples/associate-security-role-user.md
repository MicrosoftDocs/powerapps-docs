---
title: "Sample: Associate security role to a user"
description: "This sample showcases how to assign a security role to a user "
ms.date: 04/01/2025
author: paulliew
ms.author: paulliew
ms.reviewer: jdaly
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Sample: Associate security role to a user

Learn how to associate a system user with a security role by using the `Associate` message or method.

Related articles:

- [Query data using QueryExpression](../queryexpression/overview.md)
- [Role-based security roles](/power-platform/admin/database-security)
- [IOrganizationService.Associate Method](/dotnet/api/microsoft.xrm.sdk.iorganizationservice.associate)

## About the sample code

|Sample|Description|Build target|
|---|---|---|
|AssociateSecurityRoleToUser|Demonstrates associating a user with a role.|.NET 9|

> [!div class="nextstepaction"]
> [SDK for .NET: Associate security role to a user sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp-NETCore/Security/AssociateSecurityRoleToUser)

The code sample demonstrates how to associate a system user with a security role. Specifically, the samples demonstrate how to:

1. Connect to Dataverse using a [connection string](../../xrm-tooling/use-connection-strings-xrm-tooling-connect.md) that defines required connection information
1. Query for a security role using its name attribute.
1. Associate the logged on user with that security role.

Additional information can be found in [README-code-design](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp-NETCore/README-code-design.md) file.

## How to build and run the code sample

1. Clone the [PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples) repository.
1. Locate the sample folder.
1. Open the solution file (*.sln) in Visual Studio.
1. Edit the project's appsettings.json file and set the `Url`value as appropriate for your Dataverse test environment.
1. Build and run the project [F5].
1. You'll be prompted in a browser window for account sign-in credentials to the target environment.

## Expected program output

For a successful run, the program's console output should look similar to the following example.
Otherwise, any errors or exceptions are displayed.

```console
Discovering who you are...done.
Associating your system user record with role 'Basic User'..done.

Use the Power Platform admin center to see that you now have
the 'Basic User' role. Afterwards, remove the role if desired.
Press any key to undo environment data changes.
```

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
