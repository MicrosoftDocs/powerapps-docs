---
title: Define advanced form steps for portals
description: Learn how to create a advanced form step for a advanced form on a portal.
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 06/17/2020
ms.author: sandhan
ms.reviewer: tapanm
contributors:
    - tapanm-msft
    - sandhangitmsft
---

# Define advanced form steps for portals

The Advanced Form Step provides the flow logic of the form's user experience such as steps and conditional branching. It also provided details regarding the rendering of a form and additional behavior.

> [!NOTE]
> Advanced Forms persists the history of the steps a user has visited in an object on a Advanced Form Session table. If a Advanced Form's steps have been modified, previously created history data could now be stale. Anytime steps are changed, it is recommended that you delete all Advanced Form Session records to eliminate miss match between sequence of steps logged in history and the current sequence.

Each Advanced Form will be presented on the portal has one or more steps. These steps share some common properties, outlined below. Each Step contains a pointer (a lookup) to the next step, with the exception of terminal steps. Terminal steps do not have a next time, and are thus the last step of the Advanced Form (due to conditional branching, there can be multiple terminal steps).

![Steps to create a advanced form](../media/web-form-creation-steps.png "Steps to create a advanced form")  

| Name     | Description                                    |
|----------|------------------------------------------------|
| Name     | A title used for reference.                    |
| Advanced Form | The Advanced Form associated with the current step. |
|Type|One of the following:<br>[Load Form/Load Tab step type](load-form-step.md): displays properties of forms. <ul><li>[Load Form/Load Tab step type](load-form-step.md): displays properties of tabs.</li><li>[Conditional step type](add-conditional-step.md): displays properties for specifying expressions to be evaluated for conditional branching. </li><li>[Redirect step type](add-redirect-step.md): displays the settings appropriate for configuring a website redirection.</li></ul><br>For further details on the settings for these advanced form step types, please refer to their corresponding sections below.<br>**Note**: The first step cannot be of type "Condition".|
| Next Step                 | The step that will follow the current step. This will be blank for single step single form.                                                                                                            |
| Target Table Logical Name | The logical name of the table associated with the form.                                                                                                                                               |
| Move Previous Permitted    | Indicates whether the user is given an option to navigate to the previous step in a multiple step advanced form. Default is true. Uncheck to prevent the user from being able to move to the previous step. |
||

After an advanced form step is used within a form, it can't be added to the Advanced Form again. If you try to reuse advanced form steps, the following message appears:

"The step \<advanced form step name\> has already been used earlier in this form. Update the Advanced Form to use each step only once, and try again."

When that happens, ensure you use don't reuse advanced form steps within the Advanced Form.

### See also

[Configure a portal](configure-portal.md)  
[Define table](entity-forms.md)  
[Load Form/Load Tab step type](load-form-step.md)  
[Redirect step type](add-redirect-step.md)  
[Conditional step type](add-conditional-step.md)  
[Add custom JavaScript](add-custom-javascript.md)  



[!INCLUDE[footer-include](../../../includes/footer-banner.md)]