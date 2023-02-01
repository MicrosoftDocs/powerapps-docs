---
title: "Use the XRM tooling common login control in your client apps (Microsoft Dataverse)| Microsoft Docs"
description: "The Microsoft Dataverse SDK provides you with a template for Visual Studio that enables you to use the common login control in your client applications. The code for Dataverse authentication, credential storage and retrieval, and diagnostic logging is built into the template so that you can quickly leverage these capabilities in your Windows client applications for Dataverse"
ms.date: 01/30/2023
author: MattB-msft
ms.author: mbarbour
ms.reviewer: pehecke
manager: jstrauss
ms.topic: article
applies_to: 
  - "Dynamics 365 (online)"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors: 
  - JimDaly
  - phecke 
---
# Use the XRM tooling common login control in your client applications

The common login control UI is provided by XAML and C# code files. The logic for Microsoft Dataverse authentication, credential storage and retrieval, and diagnostic logging is built into the control so that you can quickly leverage these capabilities in your Windows (WPF) client applications for Dataverse. The common login control is an implementation of the <xref:Microsoft.Xrm.Tooling.CrmConnectControl>, and the control resembles the following image.  
  
![XRM Tooling common login control.](../media/crm-sdk-v6-commonlogincontrol.png "XRM Tooling common login control")

## Prerequisites
  
- .NET Framework 4.8 or later
- Visual Studio 2019 or later
- Internet access so that you can download/restore the required NuGet packages
- Network access to a Dataverse test environment, and valid logon credentials
   
## Create a WPF application that uses the common login control
  
Here is a quick way to create a **Windows Presentation Foundation (WPF)** application that leverages the common login control and the underlying code for authentication, credential storage and reuse, and default tracing or logging.

The complete application can be found here: [Desktop-app-using-login-control](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/Xrm%20Tooling/Desktop-app-using-login-control).

### Create a project with the login control

Let's start by creating a new Visual Studio solution and WPF project, then add the login control XAML code to it.

1. Start Visual Studio and create a new project using the _WPF App (.NET Framework)_ template for a Windows C# Desktop app.

    :::image type="content" source="../media/xrm-new-project.png" alt-text="New project from template":::

1. Configure the project and target the .NET 4.8 framework.

    :::image type="content" source="../media/xrm-project-config.png" alt-text="Project configuration":::

1. Select **Project > Manage NuGet Packages**. Browse or search for the following packages and install them (in the order shown below) into the project.

    - Microsoft.CrmSdk.XrmTooling.CoreAssembly
    - Microsoft.CrmSdk.XrmTooling.WpfControls

1. In **Solution Explorer**, right-click the project name and select **Add > New Folder**.
1. Name the folder "LoginUX" and then copy the [login control XAML code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/LoginUX) into that folder. You can just drag and drop the ExampleLoginForm.xaml file from File Explorer into the Visual Studio project folder and the C# file will magically show up also.
1. Test build the solution (F6). It should build with no errors or warnings.

### Connect the login control to the app

Now we are going to wire up the login control to the application.

1. Double click the _ExampleLoginForm.xaml_ file in **Solution Explorer**. You should see an image of the control in the designer.
1. Switch to the MainWindow.xaml designer tab. Add a Button control in the designer and set the name and content to _btnSignIn_ and _Sign in to Dataverse_ respectively.
1. Double-click the button to add code for the click event of the button. A code editing window for the MainWindow class file is shown.
1. Replace the empty Button_Click event handler method with this code (below) to call the login control, and create an instance of the Dataverse connection object.

```csharp
private void Button_Click(object sender, RoutedEventArgs e)
{
    // Instantiate the login control.  
    ExampleLoginForm ctrl = new ExampleLoginForm();

    // Wire the button click event to the login response.   
    ctrl.ConnectionToCrmCompleted += ctrl_ConnectionToCrmCompleted;

    // Show the login control.   
    ctrl.ShowDialog();

    // Check that a web service connection is returned and the service is ready.     
    if (ctrl.CrmConnectionMgr != null && ctrl.CrmConnectionMgr.CrmSvc != null && ctrl.CrmConnectionMgr.CrmSvc.IsReady)
    {
        // Display the Dataverse version and connected environment name  
        MessageBox.Show("Connected to Dataverse version: " + ctrl.CrmConnectionMgr.CrmSvc.ConnectedOrgVersion.ToString() +
            " Organization: " + ctrl.CrmConnectionMgr.CrmSvc.ConnectedOrgUniqueName, "Connection Status");
        // TODO Additional web service operations can be performed here
    }
    else
    {
        MessageBox.Show("Cannot connect; try again!", "Connection Status");
    }
}
```

1. Add a using statement at the beginning of the C# file so that the ExampleLoginForm class is resolved.

```csharp
using PowerApps.Samples.LoginUX;
```

1. Add the definition of the ctrl_ConnectionToCrmCompleted event handler method into the MainWindow class below the Button_Click event handler method.

```csharp
private void ctrl_ConnectionToCrmCompleted(object sender, EventArgs e)
{
    if (sender is ExampleLoginForm)
    {
        this.Dispatcher.Invoke(() =>
        {
            ((ExampleLoginForm)sender).Close();
        });
    }
}
```

1. Build the program (F6). It should build with no errors or warnings.

### Test the program

Now we will run the program and test its operation.

1. Run the program (F5).
1. Select the button **Sign in to Dataverse**. The login control will be displayed.
1. The figure below shows selecting the **Office 365** online environment and checking **Display list of available organizations** to see a list of environments that the user is a member of.
1. Select **Login**.
1. When prompted for login information, enter it. The entered account is in the form someone@my-env.onmicrosoft.com.
1. A list of environments is shown. Choose one and select **Login** a second time.
1. A connection status dialog is shown containing the Dataverse version and organization name.
1. Click **OK**.
1. If you click **Sign in to Dataverse** again, the application prompts you to either choose the saved credentials from the last sign-in activity, or to re-enter credentials.
1. When you are done testing, close the program window.
  
### See also  

[Sample: Quick start for XRM Tooling API](sample-quick-start-xrm-tooling-api.md)  
[Build windows client applications using the XRM tools](build-windows-client-applications-xrm-tools.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]