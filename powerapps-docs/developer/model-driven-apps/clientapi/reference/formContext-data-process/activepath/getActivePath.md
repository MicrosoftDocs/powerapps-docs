---
title: "getActivePath (Client API reference) in model-driven apps| MicrosoftDocs"
description: Gets a collection of stages currently in the active path with methods to interact with the stages displayed in the business process flow control.
ms.date: 04/15/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 4916df68-b2d4-4a0b-b341-eb9f7032bc20
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getActivePath (Client API reference)

[!INCLUDE[./includes/getActivePath-description.md](./includes/getActivePath-description.md)]

The active path represents stages currently rendered in the process control based on the branching rules and current data in the record.

## Syntax

`var stageCollection = formContext.data.process.getActivePath();`

[!INCLUDE[cc-terminology](../../../../../data-platform/includes/cc-terminology.md)]

## Return Value

**Type**: Collection. 

**Description**: A collection of all completed stages, the currently active stage, and the predicted set of future stages based on satisfied conditions in the branching rule. This may be a subset of the stages returned with **formContext.data.process**.[getActiveProcess](../activeprocess/getActiveProcess.md) because it will only include those stages which represent a valid transition from the current stage based on branching that has occurred in the process.

## Example

The Sdk.formOnLoad function uses the **formContext.data.process.getActivePath** method to retrieve a collection of stages. Then, the sample code uses the [forEach](../../collections/forEach.md) method of the collection to loop through each stage. The code then writes key properties of the stage to the console using the **Sdk.writeToConsole** function defined in this library. The code then accesses a collection of steps for each stage using the [getSteps](../stage/getSteps.md) method. Finally, the sample uses the [forEach](../../collections/forEach.md) method of the steps collection to access each step and write key properties of the step to the console.

>[!NOTE]
>The **Sdk.formOnLoad** function in the sample JavaScript library must be set as the **OnLoad** event handler for a form, and the **Pass execution context as the first parameter** check box must be selected in the **Handler Properties** dialog.<br/>Also, this sample just illustrates the use of some of the methods in the **formContext.data.process** API. It doesn’t represent using this API to meet a business requirement; it’s only intended to demonstrate how the key property values can be accessed in code.

```JavaScript
// A namespace defined for SDK sample code
// You should define a unique namespace for your libraries
var Sdk = window.Sdk || {};
(function () {

    // A function to log messages while debugging only
    this.writeToConsole = function (message) {
        if (typeof console != 'undefined')
        { console.log(message); }
    };

    // Code to run in the OnLoad event 
    this.formOnLoad = function (executionContext) {
        // Retrieve the formContext
        var formContext = executionContext.getFormContext();

        // Enumerate the stages and steps in the active path
        var activePathCollection = formContext.data.process.getActivePath();
        activePathCollection.forEach(function (stage, n) {
            Sdk.writeToConsole("Stage Index: " + n);
            Sdk.writeToConsole("Table: " + stage.getEntityName());
            Sdk.writeToConsole("StageId: " + stage.getId());
            Sdk.writeToConsole("Status: " + stage.getStatus());
            var stageSteps = stage.getSteps();
            stageSteps.forEach(function (step, i) {
                Sdk.writeToConsole("    Step Name: " + step.getName());
                Sdk.writeToConsole("    Step Column: " + step.getAttribute());
                Sdk.writeToConsole("    Step Required: " + step.isRequired());
                Sdk.writeToConsole("    ---------------------------------------")
            })
            Sdk.writeToConsole("---------------------------------------")
        });
    };
}).call(Sdk);
```

When the sample runs in the browser, you can use the developer tools of the browser to view the text written to the console. For example, when this sample is run in the Opportunity  form with the Opportunity Sales Process, the following is written to the console:

```
Stage Index: 0
Table: opportunity
StageId: 6b9ce798-221a-4260-90b2-2a95ed51a5bc
Status: active
    Step Name: Identify Contact
    Step Column: parentcontactid
    Step Required: false
    ---------------------------------------
    Step Name: Identify Account
    Step Column: parentaccountid
    Step Required: false
    ---------------------------------------
    Step Name: Purchase Timeframe
    Step Column: purchasetimeframe
    Step Required: false
    ---------------------------------------
    Step Name: Estimated Budget
    Step Column: budgetamount
    Step Required: false
    ---------------------------------------
    Step Name: Purchase Process
    Step Column: purchaseprocess
    Step Required: false
    ---------------------------------------
    Step Name: Identify Decision Maker
    Step Column: decisionmaker
    Step Required: false
    ---------------------------------------
    Step Name: Capture Summary
    Step Column: description
    Step Required: false
    ---------------------------------------
---------------------------------------
Stage Index: 1
Table: opportunity
StageId: 650e06b4-789b-46c1-822b-0da76bedb1ed
Status: inactive
    Step Name: Customer Need
    Step Column: customerneed
    Step Required: false
    ---------------------------------------
    Step Name: Proposed Solution
    Step Column: proposedsolution
    Step Required: false
    ---------------------------------------
    Step Name: Identify Stakeholders
    Step Column: identifycustomercontacts
    Step Required: false
    ---------------------------------------
    Step Name: Identify Competitors
    Step Column: identifycompetitors
    Step Required: false
    ---------------------------------------
---------------------------------------
Stage Index: 2
Table: opportunity
StageId: d3ca8878-8d7b-47b9-852d-fcd838790cfd
Status: inactive
    Step Name: Identify Sales Team
    Step Column: identifypursuitteam
    Step Required: false
    ---------------------------------------
    Step Name: Develop Proposal
    Step Column: developproposal
    Step Required: false
    ---------------------------------------
    Step Name: Complete Internal Review
    Step Column: completeinternalreview
    Step Required: false
    ---------------------------------------
    Step Name: Present Proposal
    Step Column: presentproposal
    Step Required: false
    ---------------------------------------
---------------------------------------
Stage Index: 3
Table: opportunity
StageId: bb7e830a-61bd-441b-b1fd-6bb104ffa027
Status: inactive
    Step Name: Complete Final Proposal
    Step Column: completefinalproposal
    Step Required: false
    ---------------------------------------
    Step Name: Present Final Proposal
    Step Column: presentfinalproposal
    Step Required: false
    ---------------------------------------
    Step Name: Confirm Decision Date
    Step Column: finaldecisiondate
    Step Required: false
    ---------------------------------------
    Step Name: Send Thank You
    Step Column: sendthankyounote
    Step Required: false
    ---------------------------------------
    Step Name: File De-brief
    Step Column: filedebrief
    Step Required: false
    ---------------------------------------
---------------------------------------
```

### Related topics

[formContext.data.process](../../formContext-data-process.md)
 




[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]