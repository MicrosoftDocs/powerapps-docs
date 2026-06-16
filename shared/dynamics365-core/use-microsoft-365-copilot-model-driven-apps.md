[Microsoft 365 Copilot](/copilot/overview) for apps is your next-generation AI assistant. It helps you explore and understand data in your apps through natural language conversations. Use Microsoft 365 Copilot to boost productivity with AI-powered insights and navigation.

## Prerequisites

An administrator must enable Microsoft 365 Copilot in your application before it becomes visible in your app. For more information, see [Add Microsoft 365 Copilot for app users](/power-apps/maker/model-driven-apps/add-microsoft-365-copilot).

> [!NOTE]
>
> - To use the Microsoft 365 Copilot feature in a Power Apps app, users must have both a Power Apps premium license and a Microsoft 365 Copilot license. For more information about licensing, see [Power Platform licensing guide](https://go.microsoft.com/fwlink/?linkid=2085130).
> - To use the Microsoft 365 Copilot feature in a Dynamics 365 app, users must have a Dynamics 365 Enterprise or Premium license. However, to get the full capabilities of Work IQ, beyond Dataverse grounding, a Microsoft 365 Copilot license is required. For more information about licensing, see [Dynamics 365 licensing guide](https://go.microsoft.com/fwlink/?LinkId=866544).


## Copilot pane

After Microsoft 365 Copilot is enabled, you can access it through the Copilot button near the upper-right corner of the page.

:::image type="content" source="/power-apps/user/media/microsoft-365-copilot-button.png" alt-text="Screenshot that shows the Copilot button on a page.":::

If both Microsoft 365 Copilot and [Copilot chat in apps](/power-apps/user/use-copilot-model-driven-apps) are enabled, you can switch between them:
 - **Chat** option opens Microsoft 365 Copilot.
 - **App Skills** option opens [Copilot chat in apps](/power-apps/user/use-copilot-model-driven-apps). 
These terms align with Microsoft 365 apps for consistency.

:::image type="content" source="/power-apps/user/media/copilot-chat-switcher.png" alt-text="Screenshot that shows the Copilot split button showcasing Chat and App Skills options on a page.":::

You can expand or collapse the Microsoft 365 Copilot pane as needed.

## Ask questions with Microsoft 365 Copilot

Microsoft 365 Copilot in apps answers questions about the Dataverse table data in the app.

:::image type="content" source="/power-apps/user/media/microsoft-365-copilot-question-answer.png" alt-text="Screenshot that shows a question and response in Microsoft 365 Copilot." lightbox="/power-apps/user/media/microsoft-365-copilot-question-answer.png":::

## Share your feedback

Help us improve Copilot responses by using the feedback controls on each response. Provide feedback for every response:

- If a response is high quality and helpful, select the thumbs up button.
- If a response is incorrect, incomplete, or not helpful, select the thumbs down button.

When you provide feedback, share as much information as possible. For example, include what you expected to see, what was missing or incorrect, and any relevant context. The more detail you share, the better we can understand your feedback and continuously improve responses.

:::image type="content" source="/power-apps/user/media/microsoft-365-copilot-feedback.png" alt-text="Screenshot of Microsoft 365 Copilot in a model-driven app, highlighting the thumbs up and thumbs down feedback buttons for a response." lightbox="/power-apps/user/media/microsoft-365-copilot-feedback.png":::

## Microsoft 365 Copilot suggested questions

To help you get started, Microsoft 365 Copilot suggests questions. Many include placeholders you can replace with appropriate text.

:::image type="content" source="/power-apps/user/media/microsoft-365-copilot-prompts.png" alt-text="Screenshot that shows suggested prompts that have placeholders." lightbox="/power-apps/user/media/microsoft-365-copilot-prompts.png":::

## Use agents in Microsoft 365 Copilot

> [!IMPORTANT]
>
> If you select an agent in Microsoft 365 Copilot in apps, it stops answering questions about Dataverse table data unless you configure it to do so. However, the agent can still use chat history. To get the side chat to answer questions about the Dataverse table data in the app again, you need to remove the explicit agent selection.

You can use any agent available in Microsoft 365 Copilot directly from the side pane. When an agent is available within Microsoft 365 Copilot, you can interact by either choosing it from the navigation panel or @ mentioning it.

:::image type="content" source="/power-apps/user/media/microsoft-365-copilot-opened-navigation.png" alt-text="Screenshot that shows how to open the Microsoft 365 Copilot navigation panel with different agents displayed." lightbox="/power-apps/user/media/microsoft-365-copilot-opened-navigation.png":::

One of the benefits of @ mentioning an agent is that you can add or remove it from an ongoing conversation, which lets you have several agents collaborating in one conversation. When you select an agent from the navigation panel, you have a direct conversation only with the agent you selected.

:::image type="content" source="/power-apps/user/media/microsoft-365-copilot-at-mention.png" alt-text="Screenshot that shows how to @ mention agents in Microsoft 365 Copilot.":::

## Navigate to model-driven form using citations

When results have citations, select the citation result in the side pane to navigate to the model-driven form.

:::image type="content" source="/power-apps/user/media/microsoft-365-copilot-citation-nav.png" alt-text="Screenshot that shows a model-driven form that was navigated to after clicking a citation link.":::

## Limitations

- Microsoft 365 Copilot for model-driven apps allows users to view data by using read-only operations. This capability means that users can only view data that matches their queries and can't make any changes. To make changes, customization with an agent is required.
- Microsoft 365 Copilot for model-driven apps isn't available in the Power Apps mobile app.
