<properties
	pageTitle="PowerApps: UpdateContext function"
	description="Reference information for the UpdateContext function in PowerApps, including syntax and examples"
	services="powerapps"
	documentationCenter="na"
	authors="gregli-msft"
	manager="dwrede"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="10/21/2015"
   ms.author="gregli"/>

# UpdateContext function in PowerApps #

Updates the [context variables](file-name.md) of the current [screen](file-name.md).

## Overview ##

Sometimes you need to temporarily hold a piece of information.  For example, to keep track of how many times a button has been clicked, or the result of a data operation.  Context variables fill this need and **UpdateContext** is the primary way to create them and update their values.

Context variables are scoped to a screen - formulas on one screen cannot access context variables on another screen.  In this way, context variables are similar to local variables in other programming tools.  If the equivalent of a global variable is required, you can use a [collection](file-name.md) and the **[Collect](function-collect.md)** or **[ClearCollect](function-clearcollect.md)** functions. 

PowerApps is not a traditional programming tool.  At its core, PowerApps has a [data flow model](file-name.md) that is automatically kept up to date, similar to how Excel automatically recalculates when a cell changes value.  Context variables do not benefit from the data flow model, are not automatically updated, and their state must be managed explicitly by the author.  This can be tedious and error prone.  Before using a context variable, you should consider carefully if your needs could be accomplished by using a formula based on control, screen, or system state instead. For more information see [working with state](file-name.md). 
  
## Description ##

The **UpdateContext** function takes a single [record](file-name.md) argument, containing column name and value pairs. Each column name refers to a separate context variable. More than one context variable can be created and set with a single **UpdateContext** call. 

Each context variable is set to its new value.  If the context variable did not previously exit, it is created.  If an existing context variable is not referenced in the **UpdateContext** call, it is not modified.  There is no way to remove a context variable once created. 

Context variables are referenced in formulas using their column name.  For example, **UpdateContext( { Counter: 1 } )** creates a context variable named **Counter** that can be referenced in formulas simply as **Counter**.

Context variables can hold single values, records, collections, object references, or any result from a formula.  See the examples for more details.

Context variables hold their values throughout the lifetime of the app.  Even when switching screens, context variables for a screen will remain intact for return to that screen. Context variables are scoped to a screen and cannot be referenced or modified from outside that screen.  There is one exception: the **[Navigate](function-navigate.md)** function can be used to create and set context variables when switching between screens. 

The **UpdateContext** function has no return value.  

This function can only be used within a [behavior formula](file-name.md).

## Syntax ##

**UpdateContext**( *UpdateRecord* )

- *UpdateRecord* – Required. Record containing column name and value pairs.  A context variable is created or updated for each column name and value provided.

**UpdateContext**( { *ContextVariable1*: *Value1* [, *ContextVariable2*: *Value2* [, ... ] ] } )

- *ContextVariable(s)* - Required.  Name of the context variable to create or update.

- *Value(s)* - Required.  Value to assign to the context variable.

## Examples ##

| Formula | Description | Result |
|---------|-------------|--------|
| **UpdateContext( {&nbsp;Counter:&nbsp;1&nbsp;} )** | Creates the context variable **Counter** if it did not already exist and sets its value to 1.  | **Counter** has the value 1. It can be referenced in formulas by the name **Counter**. |
| **UpdateContext( {&nbsp;Counter:&nbsp;2&nbsp;} )** | Updates the **Counter** context variable from the last example to a new value of 2. | **Counter** has the value 2.  |
| **UpdateContext( {&nbsp;Name:&nbsp;"James",&nbsp;Score:&nbsp;10&nbsp;} )** | Creates the context variables **Name** and **Score** if they did not already exist, and set their values to "James" and 10 respectively.| **Name** has the value "James" and **Score** has the value 10. | 
| **UpdateContext( {&nbsp;Person:&nbsp;{&nbsp;Name:&nbsp;"Milton", Address:&nbsp;"1&nbsp;Main&nbsp;St"&nbsp;}&nbsp;} )** | Creates the context variable **Person** if it did not already exist, and sets its value to a record. |**Person** has the value of record **{&nbsp;Name:&nbsp;"Milton", Address:&nbsp;"1&nbsp;Main&nbsp;St"&nbsp;}&nbsp;}**.  This record can be referenced as a whole with the name **Person**, or individual columns of this record can be referenced through **Person!Name** and **Person!Address**. |
| **UpdateContext( {&nbsp;Person: Patch(&nbsp;Person,&nbsp;{Address:&nbsp;"2&nbsp;Main&nbsp;St"&nbsp;}&nbsp;) }&nbsp;)** | Updates the **Address** column in the context variable **Person** with a new value.  | **Person** now has the value of record **{&nbsp;Name:&nbsp;"Milton", Address:&nbsp;"2&nbsp;Main&nbsp;St"&nbsp;}&nbsp;}**.  |

## Step-by-Step Example ##

<ol><li>Name the default screen **Source**, add another screen, and name it **Target**.</li><br><li>On the **Source** screen, add two buttons, and set their **Text** properties so that one says **English** and the other says **Spanish**.</li><br><li>Set the **OnSelect** property of the **English** button to this expression:<br>	**Navigate(Target, ScreenTransition!Fade, {Language:"English"})**</li><br><li>Set the **OnSelect** property of the **Spanish** button to this expression:<br>**Navigate(Target, ScreenTransition!Fade, {Language:"Spanish"})**</li><br><li>On the **Target** screen, add a label, and set its **Text** property to this expression:<br>**If(Language="English", "Hello!", "Hola!")**</li><br><li>On the **Target** screen, click **Shapes** on the **Insert** tab, and then click the Back arrow.</li><br><li>Set the Back arrow's **OnSelect** property to this formula:<br>**Navigate(Source, ScreenTransition!Fade)**</li><br><li>From the **Source** screen, press F5, and then click the button for either language.<br>On the **Target** screen, the label appears in the language that corresponds to the button that you clicked.</li><br><li>Click the Back arrow to return to the **Source** screen, and then click the button for the other language.<br>On the **Target** screen, the label appears in the language that corresponds to the button that you clicked.</li><br><li>Press Esc to return to the default workspace.</li></ol>[Another example](add-screen-context-variable.md)


