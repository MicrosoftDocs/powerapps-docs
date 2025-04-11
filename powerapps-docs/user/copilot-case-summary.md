---
title: Use Copilot case summary in model-driven apps
description: Learn how to view copilot case summary in model-driven apps.
author: gandhamm
ms.author: mgandham
ms.reviewer: gandhamm
ms.topic: how-to
ms.collection: 
ms.date: 04/11/2025
ms.custom: bap-template 
---

# Use Copilot case summary in model-driven apps

Copilot case summaries help users quickly understand the context of a case and resolve customer issues more efficiently. The case summary includes key information such as the case title, customer, subject, product, priority, case type, and description.

## View case summary card

Copilot case summary is enabled by default for all model-driven apps that use the **incident** table. When you open a case record, the case summary card appears. The card is collapsed by default. When you expand the card, Copilot generates and displays the case summary.

Based on the case form configured, users see the enhanced case summary card or the current version of the case summary card.

> [!NOTE]
> Users won't see case summary cards on case forms by default if their organization has opted out of the automatic enablement of Copilot feature.

 ### [Enhanced case summary card](#tab/enhancedcasesummarycard)

 The enhanced Copilot case summary card is enabled by default on all case forms except **Case for Interactive experience**, **Enhanced full case form**, **Case**, and **Case for Multisession experience** forms.

 - If case summary isn't enabled for case forms in your model-driven app, users see the enhanced case summary card on the form. 
-  If the case summary is already [enabled for case forms in your model-driven app](/dynamics365/customer-service/administer/copilot-powerapps-settings), users see both the enhanced and current case summary cards on the form. To avoid duplication, we recommend that your app administrator do one of the following actions:
   - To retain the enhanced case summary card, navigate to the required case form in Power Apps and then remove the custom summarization control.
   -  To retain the current case summary card, add the case form to the exception list. Run the following script in the Copilot Service admin center console to add the form to the exception list.

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

 On the enhanced case summary card, users can copy the summary, refresh it, regenerate the summary, and provide feedback.

   :::image type="content" source="media/copilot-case-summary.png" alt-text="Screenshot that shows the Copilot case summary on a model driven app.":::
    
  ### [Current case summary card](#tab/casesummarycard)

   This card is available on the following out-of-the-box case forms only:

   - Case for Interactive experience
   - Enhanced full case form
   - Case
   - Case for Multisession experience
 
   - If case summary is enabled or disabled, users will seer the current case summary card on these forms.

  Users can copy the summary, translate the summary into multiple languages, refresh it, regenerate the summary, and provide feedback on the current case summary card.

   :::image type="content" source="media/copilot-case-summary-default.png" alt-text="Screenshot that shows the default Copilot case summary on a model driven app.":::

---

If [Custom Record Summary](/dynamics365/customer-service/administer/copilot-enable-custom-record-summaries) is enabled, users see the custom record summary displayed in the enhanced summary card by default. We recommend that you perform the steps in the [enhanced case summary card](#enhanced-case-summary-card) section to avoid duplication.
