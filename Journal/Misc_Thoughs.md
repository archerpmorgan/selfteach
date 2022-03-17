# Misc Thoughts

This is a place to put miscellaneous thoughts about the project, things to add or change, more features, things to do differently, etc. 


Since I'm a dummy I left changes on my other machine without pushing. So I will make progress on day2 here today.

[x] Define git branching strategy, environment topology
[x] Basic routing and navigation header for react app, sends everything to the about page
[x] Data modeling and cosmosdb connection
[x] Be able to see my books on the landing page


# Basic Versioning and Environment Structure

Environments:

PROD
DEV

Changes: 

One feature per PR, from a feature branch. Gated PR build, with unit tests and linting. Dev environment for test deployment, integration tests. Then to prod.

# Set Up React Routing 


Helpful links

- <https://reactrouter.com/docs/en/v6/getting-started/tutorial>
