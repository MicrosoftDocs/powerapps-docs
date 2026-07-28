Sensitivity labels help classify and protect business data. When you send or receive emails in apps such as Dynamics 365 Customer Service or Dynamics 365 Contact Center, these labels help enforce your organization's security and compliance policies. They protect sensitive information, help prevent accidental sharing, and ensure that attachments and replies retain the appropriate level of protection.

## How sensitivity labels work in your emails

You can apply a sensitivity label to an email in the following ways:

- From the **Inbox** in **Copilot Service workspace**, select an email. In the preview pane, select the **Sensitivity label** dropdown in the **Command** bar to choose a label.
- From the email editor, when composing a new email or replying to an existing one. To choose a label, select the **Sensitivity label** dropdown in the command bar.

For an incoming email, the sensitivity label applied by the sender is displayed in the email header. 

When you compose or respond to emails, the following actions apply:

- If you apply labels such as **Do Not Forward** or **Do Not Reply** to an email, the corresponding actions are automatically restricted for email recipients within the organization.
- When you reply to or forward an email that has a sensitivity label, the system automatically applies the same label to your email. You can’t change the current label to a less restrictive label. For example, if the original email is labeled **Confidential**, you can’t change it to **General**.
- Your organization can have a default sensitivity label configured. The default label is automatically applied when you start composing a new email in the email editor. 
- Based on your organization's configurations, you can't send or save an email until you apply the required sensitivity label.
- When you add an attachment to an email, the attachment retains its existing sensitivity label. If there's a conflict between the attachment and email labels, the email displays a message indicating which label takes precedence. Displaying this message helps ensure that the entire message is classified consistently.

## Work with encrypted emails

Some sensitivity labels apply encryption to emails, which means only authorized recipients can read them.

When a customer sends an encrypted email, users can see that the email exists in the case timeline. The application doesn't display the encrypted message content.

To view the message, users are redirected to Outlook on the web, where the email can be decrypted and opened securely.

> [!NOTE]  
> Dataverse doesn't decrypt or store encrypted email content.

Encrypted emails:

- Appear in the timeline
- Must be viewed through Outlook on the web

The following features don't support encrypted emails:

- Case summaries
- Case enrichment
- Intent detection
- Other AI-driven workflows

> [!NOTE]
> Copilot features that rely on email content for AI-generated insights aren't available for encrypted email content unless the content is decrypted outside the application.


### Related information

[Configure sensitivity label support for emails](/dynamics365/customer-service/administer/configure-email-sensitivity)
