## Automatic query optimization

<!-- Dataverse is designed to deliver reliable performance at scale, even as it handles complex operations behind the scenes. Many customer interactions with Dataverse result in SQL queries being executed internally. While these operations are abstracted away from the user, they are continuously optimized by intelligent systems built into the platform. While customers may occasionally experience brief periods of slowness, these are typically transient and self-resolving.

This doesn't require any manual tuning, configurations, settings changes from customers. It is enabled by default for all customers. -->

Don't be surprised when the performance of a slow query improves without any change on your part. Dataverse actively monitors data retrieval operations to improve performance. When a specific query using standard tables performs poorly, Dataverse might automatically make changes that improve the performance of the query. This behavior might make certain performance issues appear transient because they can't be reproduced later.  

Automatic query optimization doesn't require any configuration. It's enabled by default for everyone.