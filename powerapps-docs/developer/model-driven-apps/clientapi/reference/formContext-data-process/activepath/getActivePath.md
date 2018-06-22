---
title: "getActivePath (Client API reference) in Dynamics 365 Customer Engagement| MicrosoftDocs"
ms.date: 11/20/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 4916df68-b2d4-4a0b-b341-eb9f7032bc20
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# getActivePath (Client API reference)



[!INCLUDE[./includes/getActivePath-description.md](./includes/getActivePath-description.md)]

The active path represents stages currently rendered in the process control based on the branching rules and current data in the record.

## Syntax

`var stageCollection = formContext.data.process.getActivePath();`

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
            Sdk.writeToConsole("Entity: " + stage.getEntityName());
            Sdk.writeToConsole("StageId: " + stage.getId());
            Sdk.writeToConsole("Status: " + stage.getStatus());
            var stageSteps = stage.getSteps();
            stageSteps.forEach(function (step, i) {
                Sdk.writeToConsole("    Step Name: " + step.getName());
                Sdk.writeToConsole("    Step Attribute: " + step.getAttribute());
                Sdk.writeToConsole("    Step Required: " + step.isRequired());
                Sdk.writeToConsole("    ---------------------------------------")
            })
            Sdk.writeToConsole("---------------------------------------")
        });
    };
}).call(Sdk);
```

When the sample runs in the browser, you can use the developer tools of the browser to view the text written to the console. For example, when this sample is run in the Opportunity entity form with the Opportunity Sales Process, the following is written to the console:

```
Stage Index: 0
Entity: opportunity
StageId: 6b9ce798-221a-4260-90b2-2a95ed51a5bc
Status: active
    Step Name: Identify Contact
    Step Attribute: parentcontactid
    Step Required: false
    ---------------------------------------
    Step Name: Identify Account
    Step Attribute: parentaccountid
    Step Required: false
    ---------------------------------------
    Step Name: Purchase Timeframe
    Step Attribute: purchasetimeframe
    Step Required: false
    ---------------------------------------
    Step Name: Estimated Budget
    Step Attribute: budgetamount
    Step Required: false
    ---------------------------------------
    Step Name: Purchase Process
    Step Attribute: purchaseprocess
    Step Required: false
    ---------------------------------------
    Step Name: Identify Decision Maker
    Step Attribute: decisionmaker
    Step Required: false
    ---------------------------------------
    Step Name: Capture Summary
    Step Attribute: description
    Step Required: false
    ---------------------------------------
---------------------------------------
Stage Index: 1
Entity: opportunity
StageId: 650e06b4-789b-46c1-822b-0da76bedb1ed
Status: inactive
    Step Name: Customer Need
    Step Attribute: customerneed
    Step Required: false
    ---------------------------------------
    Step Name: Proposed Solution
    Step Attribute: proposedsolution
    Step Required: false
    ---------------------------------------
    Step Name: Identify Stakeholders
    Step Attribute: identifycustomercontacts
    Step Required: false
    ---------------------------------------
    Step Name: Identify Competitors
    Step Attribute: identifycompetitors
    Step Required: false
    ---------------------------------------
---------------------------------------
Stage Index: 2
Entity: opportunity
StageId: d3ca8878-8d7b-47b9-852d-fcd838790cfd
Status: inactive
    Step Name: Identify Sales Team
    Step Attribute: identifypursuitteam
    Step Required: false
    ---------------------------------------
    Step Name: Develop Proposal
    Step Attribute: developproposal
    Step Required: false
    ---------------------------------------
    Step Name: Complete Internal Review
    Step Attribute: completeinternalreview
    Step Required: false
    ---------------------------------------
    Step Name: Present Proposal
    Step Attribute: presentproposal
    Step Required: false
    ---------------------------------------
---------------------------------------
Stage Index: 3
Entity: opportunity
StageId: bb7e830a-61bd-441b-b1fd-6bb104ffa027
Status: inactive
    Step Name: Complete Final Proposal
    Step Attribute: completefinalproposal
    Step Required: false
    ---------------------------------------
    Step Name: Present Final Proposal
    Step Attribute: presentfinalproposal
    Step Required: false
    ---------------------------------------
    Step Name: Confirm Decision Date
    Step Attribute: finaldecisiondate
    Step Required: false
    ---------------------------------------
    Step Name: Send Thank You
    Step Attribute: sendthankyounote
    Step Required: false
    ---------------------------------------
    Step Name: File De-brief
    Step Attribute: filedebrief
    Step Required: false
    ---------------------------------------
---------------------------------------
```

### Related topics

[formContext.data.process](../../formContext-data-process.md)
 


