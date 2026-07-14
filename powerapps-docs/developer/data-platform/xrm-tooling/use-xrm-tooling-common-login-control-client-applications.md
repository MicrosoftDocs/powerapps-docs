---
title: "Use the XRM tooling common login control in your client apps (Microsoft Dataverse)| Microsoft Docs"
description: "The Microsoft Dataverse SDK provides you with a template for Visual Studio that enables you to use the common login control in your client applications. The code for Dataverse authentication, credential storage and retrieval, and diagnostic logging is built into the template so that you can quickly leverage these capabilities in your Windows client applications for Dataverse"
ms.date: 02/01/2023
author: MattB-msft
ms.author: mbarbour
ms.reviewer: pehecke
ms.topic: how-to
applies_to: 
  - "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - phecke 
---
# Use the XRM tooling common login control in your client applications

 The logic for Microsoft Dataverse authentication, credential storage and retrieval, and diagnostic logging is built into the common login control control so that you can quickly leverage these capabilities in your Windows (WPF) client applications for Dataverse. The common login control is an implementation of the <xref:Microsoft.Xrm.Tooling.CrmConnectControl>. Below is an image of the control.  
  
:::image type="content" source="../media/crm-sdk-v6-commonlogincontrol.png" alt-text="XRM tooling common login control":::

## Prerequisites
  
- .NET Framework 4.8 or later
- Visual Studio 2019 or later
- Internet access so that you can download the required NuGet packages
- Network access to a Dataverse test environment, and valid logon credentials
   
## Create a WPF application that uses the common login control
  
Let's walk through the process of creating a **Windows Presentation Foundation (WPF)** application that leverages the common login control including the underlying code for authentication, credential storage and reuse, and default tracing or logging.

The completed application can be found here: [AppWithLoginControl](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/Xrm%20Tooling/App-with-login-control).

### Create a project with the login control

Start by creating a new Visual Studio solution and WPF project, then add the login control XAML code to it.

1. Start Visual Studio and create a new project using the _WPF App (.NET Framework)_ template for a Windows C# Desktop app.

    :::image type="content" source="../media/xrm-new-project.png" alt-text="New project from template":::

1. Configure the project and target the .NET 4.8 framework.

    :::image type="content" source="../media/xrm-project-config.png" alt-text="Project configuration":::

1. Select **Project > Manage NuGet Packages**. Browse or search for the following packages and install them (in the order shown below) into the project.

    - Microsoft.CrmSdk.XrmTooling.CoreAssembly
    - Microsoft.CrmSdk.XrmTooling.WpfControls

    :::image type="content" source="../media/xrm-nuget-packages.png" alt-text="NuGet package install":::

1. In **Solution Explorer**, right-click the project name and select **Add > New Folder**.

1. Name the folder "LoginUX" and then copy the [login control XAML code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/LoginUX) into that folder. You can just drag and drop the ExampleLoginForm.xaml file from File Explorer into the Visual Studio project folder and the associated C# file will magically also show up in the project.

    :::image type="content" source="../media/xrm-new-folder.png" alt-text="LoginUX folder":::

1. Test build the solution (F6). It should build with no errors or warnings.

### Connect the login control to the app

Now we are going to wire up the login control to the application.

1. Double click the _ExampleLoginForm.xaml_ file in **Solution Explorer**. You should see an image of the control in the designer.

    :::image type="content" source="../media/xrm-designer-control.png" alt-text="Login control in UI designer":::

2. Switch to the MainWindow.xaml designer tab. Add a Button control in the designer and set the Name and Common Content property values to _btnSignIn_ and _Sign in to Dataverse_ respectively.

    :::image type="content" source="../media/xrm-add-button.png" alt-text="Add a button":::

3. Double-click the button to add code for the click event of the button. A code editing window for the MainWindow class file is shown.

4. Replace the empty Button_Click event handler method with this code (below) to call the login control, and create an instance of the Dataverse connection object.

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

5. Add the definition of the ctrl_ConnectionToCrmCompleted event handler method into the MainWindow class below the Button_Click event handler method and at the same indent level.

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

6. Add a using statement at the beginning of the C# file so that the ExampleLoginForm class is resolved.

```csharp
using PowerApps.Samples.LoginUX;
```

7. Build the program (F6). It should build with no errors or warnings.

### Test the program

Now we will run the program and test its operation.

1. Run the program (F5).

1. Select the button **Sign in to Dataverse**. The login control will be displayed.

1. The figure below shows selecting the **Office 365** online environment and then checking **Display list of available organizations** to see a list of environments that the user is a member of.

    :::image type="content" source="../media/xrm-online-logon.png" alt-text="Office 365 logon":::

1. Select **Login**.

1. When prompted for login information, enter it. The entered account is in the form someone@my-env.onmicrosoft.com.

1. A list of environments is displayed in the control. Choose one and select **Login** a second time.

1. A connection status dialog is shown containing the Dataverse version and organization name.

    :::image type="content" source="../media/xrm-connection-status.png" alt-text="Connection status":::

1. Click **OK**.

1. If you click **Sign in to Dataverse** again, the application prompts you to either choose the saved credentials from the last sign-in activity, or to re-enter credentials.
1. When you are done testing, close the program window.
  
### See also  
  
[Build windows client applications using the XRM tools](build-windows-client-applications-xrm-tools.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
