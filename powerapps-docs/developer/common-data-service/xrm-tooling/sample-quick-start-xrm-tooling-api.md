---
title: "Sample: Quick start for XRM Tooling API (Common Data Service for Apps)| Microsoft Docs"
description: ""
ms.custom: ""
ms.date: 06/16/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "samples"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 060d45bb-b7fd-48bd-ab8f-629c1b8bc1dc
caps.latest.revision: 20
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# Sample: Quick start for XRM Tooling API

The QuickStart sample is a .NET Framework managed code sample that shows how to connect to a Common Data Service for Apps instance by using the XRM Tooling APIs, and perform basic create, update, retrieve, and delete operations on an entity. For more information about XRM Tooling, see [Build windows client applications using the XRM tools](../build-windows-client-applications-xrm-tools.md).

Download the sample: [Work with XRM Tooling API](https://code.msdn.microsoft.com/XRM-Tooling-Sample-24a5c55c)

## Prerequisites

[!INCLUDE [sdk-prerequisite](../../../includes/sdk-prerequisite.md)]
  
## Requirements

You must have access to a CDS for Apps environment.

## Demonstrates

- The sample code is built using the **WPF Application for CRM** SDK template that provides a common login control with built-in support for authentication and credential caching and reuse. For more information about the common login control and how to use the SDK template in Visual Studio, see [Use the XRM Tooling common login control](use-xrm-tooling-common-login-control-client-applications.md).  
- No helper code is used to establish a connection to CDS for Apps.  
- After connecting to CDS for Apps, the sample performs basic create, update, retrieve, and delete operations on an account entity.  
- Stores user credentials in a configuration file (`Default_QuickStartXRMToolingWPFClient.exe.config`) in the `c:\Users\`*`<username>`*`\AppData\Roaming\Microsoft\QuickStartXRMToolingWPFClient` folder when the sample is run for the first time, and thereafter prompts the user to either use the stored or specify new credentials at runtime to sign in to CDS for Apps.  
- Generates the following log files, if any issue occurs, to aid troubleshooting:  
- Login_ErrorLog.log: To report sign-in errors. This file is available at `C:\Users\`*`<username>`*`\AppData\Roaming\Microsoft\QuickStartXRMToolingWPFClient`.  
- QuickStartXRMToolingWPFClient.log: To report operational errors. This file is available at the same location as the executable, that is in the debug folder of your Visual Studio project.  

## To run the sample

1. Download and extract the sample.  
1. Open the `Quick start for XRM Tooling\C#\QuickStartXRMToolingWPFClient.sln`  file in Visual Studio.  
2. Press **F5** to compile and run the program.  

## Example

```csharp  
using System;  
using System.Collections.Generic;  
using System.Linq;  
using System.Text;  
using System.Threading.Tasks;  
using System.Windows;  
using System.Windows.Controls;  
using System.Windows.Data;  
using System.Windows.Documents;  
using System.Windows.Input;  
using System.Windows.Media;  
using System.Windows.Media.Imaging;  
using System.Windows.Navigation;  
using System.Windows.Shapes;  
  
// This namespace is automatically added for using   
// components in LoginWindow\CrmLogin.xaml (common login control).  
using QuickStartXRMToolingWPFClient.LoginWindow;  
  
// Add this namespace for performing   
// various operations in CRM.  
using Microsoft.Xrm.Tooling.Connector;  
  
namespace QuickStartXRMToolingWPFClient  
{  
    /// <summary>  
    /// Demonstrates how to do basic entity operations like create, retrieve,  
    /// update, and delete using the XRM Tooling APIs and the common login  
    /// control.</summary>  
    /// <remarks>  
    /// At run-time, you will be given the option to delete all the  
    /// database records created by this program.</remarks>  
    public partial class MainWindow : Window  
    {  
        public MainWindow()  
        {  
            InitializeComponent();  
            btnDelete.Visibility = Visibility.Hidden;  
        }  
  
        #region Class Level Members  
  
        private CrmLogin _ctrl = null;  
        private Guid _accountId;  
  
        #endregion Class Level Members  
  
        #region How To Sample Code  
  
        /// <summary>  
        /// Connect to Microsoft CRM, and get an instance of CRMServiceClient   
        /// </summary>  
  
        private void LoginButton_Click(object sender, RoutedEventArgs e)  
        {  
            // Create an instance of the XRM Tooling common login control  
            _ctrl = new CrmLogin();  
  
            /// Wire event to the CRM sign-in response.   
            _ctrl.ConnectionToCrmCompleted += ctrl_ConnectionToCrmCompleted;  
            UpdateStatus("Initiating connection to CRM...");  
  
            /// Show the XRM Tooling common login control.   
            _ctrl.ShowDialog();  
  
            /// Validate if you are connected to CRM   
            if (_ctrl.CrmConnectionMgr != null && _ctrl.CrmConnectionMgr.CrmSvc != null && _ctrl.CrmConnectionMgr.CrmSvc.IsReady)  
            {  
                UpdateStatus("Connected to CRM! (Version: " + _ctrl.CrmConnectionMgr.CrmSvc.ConnectedOrgVersion.ToString() +   
                    "; Org: " + _ctrl.CrmConnectionMgr.CrmSvc.ConnectedOrgUniqueName.ToString() + ")");  
                UpdateStatus("***************************************");  
                UpdateStatus("Click Start to create, retrieve, update, and delete (optional) an account record.");  
                btnSignIn.IsEnabled = false;  
                btnCRUD.IsEnabled = true;  
            }  
            // If you are not connected to CRM; display the last error and last CRM excption  
            else  
            {  
                UpdateStatus("The connection to CRM failed or was cancelled by the user.");              
            }              
        }  
  
        private void btnCRUD_Click(object sender, RoutedEventArgs e)  
        {  
            // Create an account record  
            Dictionary<string, CrmDataTypeWrapper> inData = new Dictionary<string, CrmDataTypeWrapper>();  
            inData.Add("name", new CrmDataTypeWrapper("Sample Account Name", CrmFieldType.String));  
            inData.Add("address1_city", new CrmDataTypeWrapper("Redmond", CrmFieldType.String));  
            inData.Add("telephone1", new CrmDataTypeWrapper("555-0160", CrmFieldType.String));  
            _accountId = _ctrl.CrmConnectionMgr.CrmSvc.CreateNewRecord("account", inData);  
  
            // Validate if the account is created, and then retrieve it  
            if (_accountId != Guid.Empty)  
            {  
                UpdateStatus("***************************************");  
                UpdateStatus(DateTime.Now.ToString() + ": Created an account with the following" + "\n" + "details, and retrieved it:");  
                Dictionary<string, object> data = _ctrl.CrmConnectionMgr.CrmSvc.GetEntityDataById("account", _accountId, null);  
                foreach (var pair in data)  
                {  
                    if ((pair.Key == "name") || (pair.Key == "address1_city") || (pair.Key == "telephone1"))  
                    {  
                        UpdateStatus(pair.Key.ToUpper() + ": " + pair.Value);  
                    }  
                }  
                btnCRUD.IsEnabled = false;  
            }  
            else  
            {  
                UpdateStatus("***************************************");  
                UpdateStatus("Could not create the account.");  
            }  
  
            // Update the account record  
            Dictionary<string, CrmDataTypeWrapper> updateData = new Dictionary<string, CrmDataTypeWrapper>();  
            updateData.Add("name", new CrmDataTypeWrapper("Updated Sample Account Name", CrmFieldType.String));  
            updateData.Add("address1_city", new CrmDataTypeWrapper("Boston", CrmFieldType.String));  
            updateData.Add("telephone1", new CrmDataTypeWrapper("555-0161", CrmFieldType.String));   
            bool updateAccountStatus = _ctrl.CrmConnectionMgr.CrmSvc.UpdateEntity("account","accountid",_accountId,updateData);  
  
            // Validate if the the account record was updated successfully, and then display the updated information  
            if (updateAccountStatus == true)  
            {  
                UpdateStatus("***************************************");  
                UpdateStatus(DateTime.Now.ToString() + ": Updated the account details as follows:");  
                Dictionary<string, object> data = _ctrl.CrmConnectionMgr.CrmSvc.GetEntityDataById("account", _accountId, null);  
                foreach (var pair in data)  
                {  
                    if ((pair.Key == "name") || (pair.Key == "address1_city") || (pair.Key == "telephone1"))  
                    {  
                        UpdateStatus(pair.Key.ToUpper() + ": " + pair.Value);  
                    }  
                }  
            }  
            else  
            {  
                UpdateStatus("***************************************");  
                UpdateStatus("Could not update the account.");  
            }  
  
            // Prompt the user to delete the account record created in the sample  
            UpdateStatus("***************************************");  
            UpdateStatus("To delete the account record created by the sample, click Delete Record.");  
            UpdateStatus("Otherwise, click Exit to close the sample application.");  
            btnDelete.Visibility = Visibility.Visible;          
        }  
  
        // Delete the account record created in this sample.  
        private void btnDelete_Click(object sender, RoutedEventArgs e)  
        {  
            btnDelete.IsEnabled = false;  
            _ctrl.CrmConnectionMgr.CrmSvc.DeleteEntity("account", _accountId);  
            UpdateStatus("***************************************");  
            UpdateStatus(DateTime.Now.ToString() + ": Deleted the account record.");  
            UpdateStatus("Click Exit to close the sample application.");  
        }  
  
        // Exit the sample application  
        private void btnExit_Click(object sender, RoutedEventArgs e)  
        {  
            this.Close();  
        }  
  
        /// <summary>  
        /// Progressively displays the status messages about the actions  
        /// performed during the running of the sample.  
        /// <param name="updateText">Indicates the status string that needs to be   
        /// displayed to the user.</param>  
        /// </summary>  
        public void UpdateStatus(string updateText)  
        {  
            if (lblStatus.Content.ToString() != String.Empty)  
            {  
                lblStatus.Content = lblStatus.Content + "\n" + updateText;  
            }  
            else  
            {  
                lblStatus.Content = updateText;  
            }  
        }  
  
        /// <summary>  
        /// Raised when the login process is completed.  
        /// </summary>  
        private void ctrl_ConnectionToCrmCompleted(object sender, EventArgs e)  
        {  
            if (sender is CrmLogin)  
            {  
                this.Dispatcher.Invoke(() =>  
                {  
                    ((CrmLogin)sender).Close();  
                });  
            }  
        }  
    }  
    #endregion How To Sample Code  
  
}  
```

### See also

[Use the XRM Tooling common login control](use-xrm-tooling-common-login-control-client-applications.md)<br />
[Build Windows client applications using the XRM tools](../build-windows-client-applications-xrm-tools.md)<br />
<!-- TODO:
[Tutorials for Learning About CDS for Apps Development](../tutorials-resources-sdk.md)<br /> -->
