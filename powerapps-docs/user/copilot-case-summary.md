---
title: Use Copilot case summary in model-driven apps
description: Learn how to view copilot case summary in model-driven apps.
author: gandhamm
ms.author: mgandham
ms.reviewer: gandhamm
ms.topic: conceptual 
ms.collection: 
ms.date: 04/08/2025
ms.custom: bap-template 
---

# Use Copilot case summary in model-driven apps

Copilot case summaries help users quickly understand the context of a case and resolve customer issues more efficiently. The case summary includes key information such as the case title, customer, subject, product, priority, case type, and description.

## View case summary card

Copilot case summary is enabled by default for all users of model-driven apps that use the **incident** table. 
When you open a case record, the case summary card is collapsed by default so that your screen isn't cluttered with information. Select the card to expand the summary.

Based on the case form configured, users see the enhanced case summary card or the current case summary card.

> [!NOTE]
> Organizations that opted out of automatic Copilot features won't have  case summary cards displayed on the case forms by default.

 ### [Enhanced case summary card](#tab/enhancedcasesummarycard)

 The enhanced case summary card is enabled by default on all case forms except **Case for Interactive experience**, **Enhanced full case form**, **Case**, and **Case for Multisession experience** forms.

 If the case summary is already [enabled for case forms in your model-driven app](/dynamics365/customer-service/administer/copilot-powerapps-settings), you might see both the enhanced and current case summary cards on the form. We recommend that your app administrator do one of the following actions to avoid duplication:
   - To remove the current case summary card, navigate to the required form in Power Apps and then remove the Copilot case summary card on the form.
   - To use the current experience, add your form to the exception list by running the following script in the Copilot Service admin center console.

        ```
          Xrm.WebApi.updateRecord("msdyn_copilotsummarizationsetting", "7fa56176-c226-45e5-b8fa-25d56e0dcc21", {"msdyn_excludeformslist": "4a63c8d1-6c1e-48ec-9db4-3e6c7155334c,915f6055-2e07-4276-ae08-2b96c8d02c57,b05c1e9c-94d0-46c1-8968-df49b8f33ec7,cd0d48a0-10c6-ec11-a7b5-000d3a58b83a"}).then(
          function success(result) {
          console.log("summary config updated");
          },
           function (error) {
           console.log(error.message);
              }
             );   
        ```  

   You can copy the summary, refresh it, regenerate the summary, and provide feedback on the enhanced case summary card.

   :::image type="content" source="media/copilot-case-summary.png" alt-text="Screenshot that shows the Copilot case summary on a model driven app.":::
    
  ### [Current case summary card](#tab/casesummarycard)

   This card is available only on the following out-of-the-box case forms:

   - Case for Interactive experience
   - Enhanced full case form
   - Case
   - Case for Multisession experience
 
   Users will see the current case summary card on these forms irrespective of the administrator configuration.
 
  User can copy the summary, translate the summary into multiple languages, refresh it, regenerate the summary, and provide feedback on the current case summary card.

   :::image type="content" source="media/copilot-case-summary-default.png" alt-text="Screenshot that shows the default Copilot case summary on a model driven app.":::

---

If Custom Record Summary is enabled, users will see the custom record summary in the enhanced summary card by default. We recommend that you remove the current summary card from the form to avoid duplication. Learn more in [Configure custom record summaries for service representatives](/dynamics365/customer-service/administer/copilot-enable-custom-record-summaries).

