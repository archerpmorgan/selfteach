# Day 1

Agenda

- [x] Create repository
- [x] Create README and a 'getting started' file with project description and feature itemization
- [] Create shell project with all the starter files, and be able to run locally and see something
- [] My .gitignore is up and running and is appropriate for my tech stack
- [] I have the Azure resources I need to host the started app
- [] The app is hosted
- [] I have some starter CI/CD pipelines

## creating shell project

The broad tech stack for the service will be Azure Storage (CosmosDB + Azure Blob) and React+Express+Node, so essentially the "ERN" of MERN but with CosmosDB instead of MongoDB. 

### Express API with Node.js

The backed.

> npm init -y

Creates `package.json` file with project metadata

> npm install --save express

Creates `package-lock.json` which keeps track of dependencies, names and versions, and the `node modules` directory, which stores the module code.

Added some boilerplate startup code to index.js, and now it runs.

### React App

The frontend/SPA that utilizes the Express app


Resources I used for the day:

- What exactly is Node? See <https://www.freecodecamp.org/news/what-exactly-is-node-js-ae36e97449f5/>
- What is the JS event loop for? <https://www.freecodecamp.org/news/what-exactly-is-node-js-ae36e97449f5/>

### .gitignore

The basic node template does the trick for node. We DO NOT version the node modules directory or other runtime stuff.