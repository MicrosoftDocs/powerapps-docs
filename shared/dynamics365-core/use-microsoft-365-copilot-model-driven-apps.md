[Microsoft 365 Copilot](/copilot/overview) for apps is a next-generation AI assistant that helps you gain insights into the data in your apps through conversations in natural language. Microsoft 365 Copilot boosts your productivity through AI-powered insights and navigation assistance.

> [!IMPORTANT]
>
> - This feature is in preview.  
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2189520), and are available before an official release so that customers can get early access and provide feedback.

## Prerequisites

An administrator must enable Microsoft 365 Copilot in your application before it becomes visible in your app. For more information, see [Add Microsoft 365 Copilot for app users](/power-apps/maker/model-driven-apps/add-microsoft-365-copilot).

## Copilot pane

After Microsoft 365 Copilot is enabled, access it through the Copilot button near the upper-right corner of the page.

:::image type="content" source="/power-apps/user/media/microsoft-365-copilot-button.png" alt-text="Screenshot that shows the Copilot button on a page.":::

If both Microsoft 365 Copilot and [Copilot chat in apps](/power-apps/user/use-copilot-model-driven-apps) are enabled, you can access and try each option. The **Chat** option opens Microsoft 365 Copilot, and the **App Skills** option opens [Copilot chat in apps](/power-apps/user/use-copilot-model-driven-apps). These terms align with Microsoft 365 apps for consistency.

:::image type="content" source="/power-apps/user/media/copilot-chat-switcher.png" alt-text="Screenshot that shows the Copilot split button showcasing Chat and App Skills options on a page.":::

Expand or collapse the Microsoft 365 Copilot pane as needed.

## Use Microsoft 365 Copilot to ask questions

Microsoft 365 Copilot in apps answers questions about the Dataverse table data in the app.

:::image type="content" source="/power-apps/user/media/microsoft-365-copilot-question-answer.png" alt-text="Screenshot that shows a question and response in Microsoft 365 Copilot." lightbox="/power-apps/user/media/microsoft-365-copilot-question-answer.png":::

## Share your feedback

Help us improve Copilot responses by using the feedback controls on each response. Provide feedback for every response:

- If a response is high quality and helpful, select the thumbs up button.
- If a response is incorrect, incomplete, or not helpful, select the thumbs down button.

When you provide feedback, share as much information as possible. For example, include what you expected to see, what was missing or incorrect, and any relevant context. The more detail you share, the better we can understand your feedback and continuously improve responses.

:::image type="content" source="/power-apps/user/media/microsoft-365-copilot-feedback.png" alt-text="Screenshot of Microsoft 365 Copilot in a model-driven app, highlighting the thumbs up and thumbs down feedback buttons for a response." lightbox="/power-apps/user/media/microsoft-365-copilot-feedback.png":::

## Microsoft 365 Copilot suggested questions

To help you get started, Microsoft 365 Copilot suggests questions to ask. Many suggested questions have placeholders you replace with appropriate text.

:::image type="content" source="/power-apps/user/media/microsoft-365-copilot-prompts.png" alt-text="Screenshot that shows suggested prompts that have placeholders." lightbox="/power-apps/user/media/microsoft-365-copilot-prompts.png":::

## Use agents in Microsoft 365 Copilot

> [!IMPORTANT]
>
> When you explicitly select an agent in Microsoft 365 Copilot in apps, the agent no longer answers questions about the Dataverse table data in the app unless you explicitly configure your agent to do so. However, the agent uses information from the chat history. To get the side chat to answer questions about the Dataverse table data in the app again, you need to remove the explicit agent selection.

Microsoft 365 Copilot in apps lets you use any agent available in Microsoft 365 Copilot right from the side pane. Once an agent is available within Microsoft 365 Copilot, you can interact with your agent by either choosing it from the navigation panel or @ mentioning it.

:::image type="content" source="/power-apps/user/media/microsoft-365-copilot-opened-navigation.png" alt-text="Screenshot that shows how to open the Microsoft 365 Copilot navigation panel with different agents displayed." lightbox="/power-apps/user/media/microsoft-365-copilot-opened-navigation.png":::

One of the benefits of @ mentioning an agent is that you can add or remove it from an ongoing conversation, which lets you have several agents collaborating in one conversation. When you select an agent from the navigation panel, you have a direct conversation only with the agent you selected.

:::image type="content" source="/power-apps/user/media/microsoft-365-copilot-at-mention.png" alt-text="Screenshot that shows how to @ mention agents in Microsoft 365 Copilot.":::

## Limitations

- The model chooser option, which allows users to select different AI models or configurations in the standalone version, is not available.
- Microsoft Copilot Studio agents published to Microsoft 365 Copilot through Copilot Studio channels don't have context passed from the app through Microsoft 365 Copilot to the agent.

