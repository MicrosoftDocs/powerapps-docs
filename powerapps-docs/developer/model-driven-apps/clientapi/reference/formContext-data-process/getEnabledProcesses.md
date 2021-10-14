---
title: "getEnabledProcesses (Client API reference) in model-driven apps| MicrosoftDocs"
description: Asynchronously retrieves the business process flows enables for a table that the current user can switch to.
ms.date: 04/15/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 52f79803-2ce0-4ca7-8200-aec544545d62
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getEnabledProcesses (Client API reference)

[!INCLUDE[./includes/getEnabledProcesses-description.md](./includes/getEnabledProcesses-description.md)]

## Syntax

`formContext.data.process.getEnabledProcesses(callbackFunction(enabledProcesses));`

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|callbackFunction|Function|Yes|The callback function must accept a parameter that contains an object with dictionary properties where the name of the property is the Id of the business process flow and the value of the property is the name of the business process flow.<br/><br/>The enabled processes are filtered according to the user’s privileges. The list of enabled processes is the same ones a user can see in the UI if they want to change the process manually.|

## Example

The **Sdk.formOnLoad** function in the example uses the **formContext.data.process.getEnabledProcesses** method to asynchronously retrieve information about business process flows that are enabled for the table. The sample passes an anonymous function as the first parameter. This function is executed asynchronously when the data is returned and the data is passed as the parameter to the anonymous function.

The information about enabled business process flow is provided as a dictionary object where the Id of the process is the name of the property and the name of the business process flow is the value of the property. The sample code processes this information and sets the values in a global **Sdk.enabledProcesses** array to be accessed by logic that executes later. The sample also loops through the values in the **Sdk.enabledProcesses** array, and uses the **Sdk.writeToConsole** function to write information about the retrieved business process flows to the console.

>[!NOTE]
>The **Sdk.formOnLoad** function in the sample JavaScript library must be set as the **OnLoad** event handler for a form, and the **Pass execution context as the first parameter** check box must be selected in the **Handler Properties** dialog.<br/>Also, this sample just illustrates the use of some of the methods in the **formContext.data.process** API. It doesn’t represent using this API to meet a business requirement; it’s only intended to demonstrate how the key property values can be accessed in code.

```JavaScript
//A namespace defined for SDK sample code
//You should define a unique namespace for your libraries
var Sdk = window.Sdk || {};
(function () {
    //A global variable to store information about enabled business processes after they are retrieved asynchronously
    this.enabledProcesses = [];

    // A function to log messages while debugging only
    this.writeToConsole = function (message) {
        if (typeof console != 'undefined')
        { console.log(message); }
    };

    // Code to run in the OnLoad event 
    this.formOnLoad = function (executionContext) {
        // Retrieve the formContext
        var formContext = executionContext.getFormContext();

        // Retrieve Enabled processes
        formContext.data.process.getEnabledProcesses(function (processes) {
            //Move processes to the global Sdk.enabledProcesses array;
            for (var processId in processes) {
                Sdk.enabledProcesses.push({ id: processId, name: processes[processId] })
            }
            Sdk.writeToConsole("Enabled business processes flows retrieved and added to Sdk.enabledProcesses array.");

            //Write the values of the Sdk.enabledProcesses array to the console
            if (Sdk.enabledProcesses.length < 0) {
                Sdk.writeToConsole("There are no enabled business process flows for this table.");
            }
            else {
                Sdk.writeToConsole("These are the enabled business process flows for this table:");
                for (var i = 0; i < Sdk.enabledProcesses.length; i++) {
                    var enabledProcess = Sdk.enabledProcesses[i];
                    Sdk.writeToConsole("id: " + enabledProcess.id + " name: " + enabledProcess.name)
                }
            }

            //Any code that depends on the Sdk.enabledProcesses array needs to be initiated here

        });
    };

}).call(Sdk);
```

When you run this sample with the browser developer tools open, the following is an example of the output written to the console for a table with multiple business process flows enabled.

```
Enabled business processes flows retrieved and added to Sdk.enabledProcesses array.
These are the enabled business process flows for this table:
id: 7994be68-899e-4a40-8d18-f5c3b6940188 name: Sample Lead Process
id: 919e14d1-6489-4852-abd0-a63a6ecaac5d name: Lead to Opportunity Sales Process
```

### Related topics

[setActiveProcessInstance](setActiveProcessInstance.md)

[formContext.data.process](../formContext-data-process.md)
 




[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]