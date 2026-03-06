[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

Business skills are natural-language instructions that capture how your organization gets work done. They represent your business processes, policies, and domain knowledge in a format that agents can understand and follow. Each skill describes how to complete a specific type of work, the steps involved, the information required, and the business rules that apply. 

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2216214), and are available before an official release so that customers can get early access and provide feedback.
> - This feature is being gradually rolled out across regions and might not be available yet in your region.

Agents discover and use business skills as needed at runtime to complete tasks according to your organization's processes. When multiple agents use the same skill, they follow the same process, ensuring consistent behavior across your organization. 

> [!Important]
> Business skills aren't executable code. They contain natural-language instructions that guide agent behavior, similar to how you might document a process for a new employee.

## Key capabilities 

Key capabilities include: 

- **Reusability**: Define a process once and use it across multiple agents and surfaces 
- **Consistency**: Agents follow the same process definition, reducing variation in outcomes 
- **Maintainability**: Update a skill in one place to change behavior across all agents that use it 
- **Governance**: Use Dataverse security to control who can create, modify, and share business skills. Each skill has an owner, and sharing follows Dataverse RBAC patterns. 
- **Solution-aware**: A solution-aware object that appears in **Solution explorer** and can be moved across environments 

## Using business skills 

After you create business skills in your environment, AI agents can use them to understand and run business processes. Access skills through the Dataverse MCP server preview.

- To start using business skills, connect to the Dataverse MCP server preview in Microsoft Copilot Studio or from agent mode in Visual Studio Code or non-Microsoft clients.    
- Try asking your agent, "Show me all business skills in this environment." The agent retrieves a list of all the skills in your connected environment by using the Dataverse MCP server.  
- Start testing by asking your agent a relevant scenario that matches your skill’s intended use case. For example, if you created a skill for logging call transcripts into Dataverse, provide a sample transcript to your agent and ask it to log the transcript information in Dataverse.
  > [!NOTE]
  > If your agent doesn't automatically fetch skill details, try adding "Using business skills" before your actual prompt. For example, "Using business skills log this transcript in Dataverse."  
- Remember to add any other relevant tools, including MCP servers and connectors, that the agent needs access to for successfully executing your business processes defined in skills. 
- Confirm your intended actions were successful and continue to iterate on the skill instructions based on results. 

## Share a business skill 

Skills are user-owned by default. To allow others to interact with the skills do the following: 

- Make skills viewable to everyone in your organization by granting permissions to view business skills. 
  - Go to the app you built earlier.  
  - Select a skill.  
  - Change the **Viewable by** property to organization to allow other users in your environment with at least basic user privileges to see the skill.  
  - The **Viewable by** property is **individual by default**, so if you create a skill, only you can view it.

- Share skills with other users or teams in the environment.
  - Go to the Skill Management app you built earlier.  
  - Select a skill and select **Share** in the top command bar. (If you don’t see **Share**, select the three dots for more capabilities and select **Share**.) 
  - Search for a user or team to share the skill with and select that user.
  - Choose the relevant permissions and select **Share**.
