If you have followed along with the course so far, you've spent some time working in web.powerapps.com. Whether you knew it or not, you have been working in a specific *environment* the whole time. An environment is simply a grouping of apps and other resources (more on this in a minute). Look at the upper right of the screen in web.powerapps.com, and you see a drop-down menu that shows your current environment.

![Environment picker](./media/learning-manage-environments/environment-picker.png)

If you are new to PowerApps, you might have only the default environment at this point. Click or tap the menu to see if there are other environments available.

## Why use environments?
An environment is a container for apps and other resources, like data connections and flows from Microsoft Flow. It's a way to group things based on business requirements. There are several reasons to create additional environments beyond the default one:

* **Separate app development by department**: in a large organization, each department could work in a different environment.
* **Support application lifecycle management (ALM)**: you could have separate environments for apps in development and apps that you have already finished and shared.
* **Manage data access**: each environment can have its own Common Data Service for Apps database, and other data connections are specific to the environment (i.e. they're not shared across environments).

One thing to keep in mind is that environments are relevant only to app creators and PowerApps admins. When you share an app to a user, that user just runs the app as long as they have the right permissions. They don't have to worry about what environment it came from.

## Create an environment
So far in this course, we have focused on app creators, but environments are created and maintained by admins. If you're not an admin, this information can still be helpful when you talk to your admin about setting up environments. In the PowerApps admin center, click or tap **Environments** then **New environment**. On the **New environment** screen, enter a name for the environment, select a region, select whether to create a Common Data Service for Apps database for the environment, and click or tap **Create an environment**.

![Create an environment](./media/learning-manage-environments/create-environment.png)

That's it, you now have a new environment to work in. If you go back to web.powerapps.com, you will see it in the environments drop-down menu.

## Manage access to an environment
You have access to an environment if you are:

* An **Environment Admin**: you have full permissions in the environment.
* An **Environment Maker**: you can see all apps, create apps, and work with the Common Data Service for Apps (other permissions apply).

As an admin, you grant access to an environment from the **Environments** tab. First, click or tap an environment. To add someone (an **Environment Maker** in this example), click or tap **Environment roles** then **Environment Maker**. From there, add users or groups to the role and click **Save**.

![Manage environment access](./media/learning-manage-environments/environment-access.png)

You now understand the benefits of environments, and how to create them and grant access to them. Even if you're not in an admin role, it's helpful to know how this works. 

This brings us to the end of the Managing apps section, and also the end of this Guided Learning course. We hope you've enjoyed it and learned a lot - let us know if you have any feedback, and check back because we plan to add content over time. For more in-depth content right now, check out the [PowerApps documentation](https://docs.microsoft.com/powerapps/). 

